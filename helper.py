import pandas as pd
import csv
import os
from datetime import datetime
from typing import Dict, Optional, List

# Load properties data
def load_properties() -> pd.DataFrame:
    """Load properties from CSV file."""
    try:
        df = pd.read_csv('data/properties.csv')
        return df
    except FileNotFoundError:
        print("Error: properties.csv file not found in data directory")
        return pd.DataFrame()

# FAQ responses
FAQ_RESPONSES = {
    "office location": "Our main office is located at 123 Business District, Dubai, UAE.",
    "working hours": "Our working hours are Monday to Friday, 9:00 AM to 6:00 PM UAE time.",
    "contact": "You can contact us at info@zorever.com or call +971-4-123-4567.",
    "services": "We provide real estate services including property sales, rentals, and property management.",
    "about": "Zorever is a leading real estate company in Dubai specializing in residential and commercial properties."
}

def get_faq_response(query: str) -> Optional[str]:
    """Check if query matches any FAQ and return response."""
    query_lower = query.lower()
    
    for keyword, response in FAQ_RESPONSES.items():
        if keyword in query_lower:
            return response
    return None

def find_property_by_id(df: pd.DataFrame, listing_id: str) -> Optional[Dict]:
    """Find property by exact listing_id match."""
    result = df[df['listing_id'].str.upper() == listing_id.upper()]
    if not result.empty:
        return result.iloc[0].to_dict()
    return None

def find_property_by_name(df: pd.DataFrame, property_name: str) -> Optional[Dict]:
    """Find property by fuzzy name matching (case-insensitive substring)."""
    # Try exact match first
    exact_match = df[df['property_name'].str.lower() == property_name.lower()]
    if not exact_match.empty:
        return exact_match.iloc[0].to_dict()
    
    # Try substring match
    substring_match = df[df['property_name'].str.lower().str.contains(property_name.lower(), na=False)]
    if not substring_match.empty:
        return substring_match.iloc[0].to_dict()
    
    return None

def format_property_response(property_data: Dict) -> str:
    """Format property data into a readable response."""
    template = f"""{property_data['property_name']} — {property_data['bedrooms']} BHK ({property_data['area_sqft']} sqft) in {property_data['city']}.
Price: {property_data['price']:,} {property_data['price_currency']}. Status: {property_data['availability']}.
Short: {property_data['short_description']}. Contact: {property_data['agent_email']}"""
    
    return template

def detect_booking_intent(query: str) -> bool:
    """Detect if user wants to book a visit."""
    booking_keywords = ['book visit', 'schedule visit', 'visit booking', 'book a visit', 'schedule a visit', 'arrange visit']
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in booking_keywords)

def detect_property_query(query: str) -> tuple:
    """Detect property queries and extract listing_id or property name."""
    query_lower = query.lower()
    
    # Check for listing_id pattern (P followed by numbers)
    words = query.split()
    for word in words:
        if word.upper().startswith('P') and word[1:].isdigit():
            return 'listing_id', word.upper()
    
    # Check for property name queries
    property_indicators = ['property', 'apartment', 'villa', 'house', 'details', 'price', 'available', 'show']
    if any(indicator in query_lower for indicator in property_indicators):
        # Extract potential property names
        common_property_words = ['sunrise', 'desert', 'marina', 'golden', 'palm', 'sky', 'ocean']
        for word in common_property_words:
            if word in query_lower:
                return 'property_name', word
    
    return None, None

def save_visit_booking(name: str, phone: str, property_id: str = "", property_name: str = "", user_message: str = ""):
    """Save visit booking to CSV file."""
    file_path = 'data/visits.csv'
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Create file with header if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['timestamp', 'listing_id', 'property_name', 'name', 'phone', 'user_message'])
    
    # Append the booking
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([timestamp, property_id, property_name, name, phone, user_message])
