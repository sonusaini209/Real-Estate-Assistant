from flask import Flask, render_template, request, jsonify, session
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
import pandas as pd
from helper import (
    load_properties, get_faq_response, find_property_by_id, 
    find_property_by_name, format_property_response, 
    detect_booking_intent, detect_property_query, save_visit_booking
)

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here-change-in-production')

# Initialize OpenAI LLM (using GPT-3.5-turbo which is free tier)
llm = None
openai_key = os.getenv('OPENAI_API_KEY')
if openai_key:
    try:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo", 
            temperature=0.7,
            openai_api_key=openai_key
        )
    except Exception as e:
        print(f"Warning: Could not initialize OpenAI LLM: {e}")
        llm = None

# Load properties data on startup
properties_df = load_properties()

@app.route('/')
def home():
    """Main chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages."""
    data = request.json or {}
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'response': 'Please type a message.'})
    
    # Initialize session data for booking flow
    if 'booking_flow' not in session:
        session['booking_flow'] = {}
    
    # Handle booking flow states
    booking_flow = session['booking_flow']
    
    if booking_flow.get('state') == 'waiting_name':
        booking_flow['name'] = user_message
        booking_flow['state'] = 'waiting_phone'
        session['booking_flow'] = booking_flow
        return jsonify({'response': 'Great! Please share your phone number:'})
    
    elif booking_flow.get('state') == 'waiting_phone':
        booking_flow['phone'] = user_message
        booking_flow['state'] = 'waiting_property'
        session['booking_flow'] = booking_flow
        return jsonify({'response': 'Perfect! Which property are you interested in? (You can provide the listing ID like P001 or property name, or type "any" if no specific property):'})
    
    elif booking_flow.get('state') == 'waiting_property':
        property_info = user_message if user_message.lower() != 'any' else ''
        
        # Save the booking
        save_visit_booking(
            name=booking_flow['name'],
            phone=booking_flow['phone'],
            property_id=property_info if property_info.startswith('P') else '',
            property_name=property_info if not property_info.startswith('P') else '',
            user_message=f"Original request: {booking_flow.get('original_message', '')}"
        )
        
        # Clear booking flow
        session['booking_flow'] = {}
        
        response = f"Thank you {booking_flow['name']}! Your visit booking has been saved successfully. We will contact you at {booking_flow['phone']} to confirm the appointment."
        
        # Polish response with LLM if available
        if llm:
            try:
                polished_response = llm.invoke([HumanMessage(content=f"Make this booking confirmation message more professional and friendly: {response}")]).content
                response = polished_response
            except:
                pass  # Use original response if LLM fails
        
        return jsonify({'response': response})
    
    # Check for booking intent
    if detect_booking_intent(user_message):
        session['booking_flow'] = {
            'state': 'waiting_name',
            'original_message': user_message
        }
        return jsonify({'response': 'I\'d be happy to help you book a property visit! Please share your full name:'})
    
    # Check for FAQ
    faq_response = get_faq_response(user_message)
    if faq_response:
        # Polish FAQ response with LLM if available
        if llm:
            try:
                polished_response = llm.invoke([HumanMessage(content=f"Make this FAQ response more conversational and helpful: {faq_response}")]).content
                return jsonify({'response': polished_response})
            except:
                pass
        return jsonify({'response': faq_response})
    
    # Check for property queries
    query_type, query_value = detect_property_query(user_message)
    if query_type and query_value:
        if query_type == 'listing_id':
            property_data = find_property_by_id(properties_df, query_value)
        else:  # property_name
            property_data = find_property_by_name(properties_df, query_value)
        
        if property_data:
            response = format_property_response(property_data)
            
            # Polish with LLM if available
            if llm:
                try:
                    polished_response = llm.invoke([HumanMessage(content=f"Make this property information more engaging and natural: {response}")]).content
                    return jsonify({'response': polished_response})
                except:
                    pass
            return jsonify({'response': response})
        else:
            return jsonify({'response': f'Sorry, I couldn\'t find any property matching "{query_value}". Please check the listing ID or property name and try again.'})
    
    # Default response with LLM enhancement
    default_response = """I'm a real estate chatbot that can help you with:
    
• General information about our office and services
• Property details from our listings (try asking about a specific property like "P001" or "Sunrise Apartments")
• Booking property visits (just say "I want to book a visit")

What would you like to know?"""
    
    if llm:
        try:
            polished_response = llm.invoke([HumanMessage(content=f"User asked: '{user_message}'. Respond helpfully as a real estate chatbot and suggest they can ask about: office info, property details, or booking visits. Keep it brief and friendly.")]).content
            return jsonify({'response': polished_response})
        except:
            pass
    
    return jsonify({'response': default_response})

@app.route('/properties')
def list_properties():
    """API endpoint to list all properties."""
    return jsonify(properties_df.to_dict('records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

