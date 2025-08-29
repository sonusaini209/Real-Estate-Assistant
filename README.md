# AI-Powered Real Estate Chatbot

A Flask-based chatbot that answers property questions, handles FAQs, and automates visit bookings using OpenAI and LangChain.

## Features
- 🏠 Property information lookup by ID or name
- ❓ FAQ responses for common questions
- 📅 Automated visit booking system
- 🤖 AI-enhanced natural language responses
- 💬 Modern web chat interface

## Quick Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set environment variable**
```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

4. **Run the application**
```bash
python app.py
```

5. **Open your browser**
Navigate to `http://localhost:5000`

## Deployment on Render

1. Connect your GitHub repository to Render
2. Set environment variable: `OPENAI_API_KEY`
3. Use build command: `pip install -r requirements.txt`
4. Use start command: `gunicorn app:app`

## Usage Examples

**FAQ Questions:**
- "What are your working hours?"
- "Where is your office?"

**Property Queries:**
- "What is the price of Property P001?"
- "Show details for Marina Heights"
- "Is Ocean Breeze available?"

**Book a Visit:**
- "I want to book a visit"
- "Schedule a property visit"

## File Structure
```
├── app.py              # Main Flask application
├── helpers.py          # Helper functions
├── templates/
│   └── index.html      # Chat interface
├── data/
│   ├── properties.csv  # Property database
│   └── visits.csv      # Visit bookings (auto-created)
└── requirements.txt    # Dependencies
```
