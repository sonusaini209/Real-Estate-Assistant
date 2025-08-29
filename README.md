<h1 align="center">AI-Powered Real Estate Chatbot — Zorever Assessment</h1>

<p align="center">
  <a href="https://your-app-name.onrender.com/">
    <img alt="Live Demo" src="https://img.shields.io/badge/Live-Demo-blue" />
  </a>
  &nbsp;
  <a href="https://github.com/yourusername/zorever-assessment">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/GitHub-Repository-black" />
  </a>
  &nbsp;
  <a href="https://www.python.org/">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.11+-blue" />
  </a>
  &nbsp;
  <a href="https://flask.palletsprojects.com/">
    <img alt="Flask" src="https://img.shields.io/badge/Flask-3.1+-green" />
  </a>
  &nbsp;
  <a href="https://openai.com/">
    <img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-GPT--3.5-orange" />
  </a>
  &nbsp;
  <a href="https://opensource.org/licenses/MIT">
    <img alt="License MIT" src="https://img.shields.io/badge/License-MIT-yellow" />
  </a>
</p>

<p align="center">
  <em>A fully functional AI-powered real estate chatbot with modern web interface.<br />
  Answers property FAQs, provides detailed property information, and automates visit bookings.</em>
</p>

## ✨ Overview

This project demonstrates a complete AI-powered chatbot solution for real estate businesses, featuring:

**Smart Property Search:** Find properties by listing ID (P001-P007) or name matching  
**Natural Language FAQs:** Answers common questions about office hours, location, and services  
**Automated Visit Booking:** Multi-step booking flow with data persistence to CSV  
**AI Enhancement:** Uses OpenAI GPT-3.5-turbo to polish all responses for natural conversation  

## 🛠️ Features

| Feature                 | Description                                              |
|-------------------------|----------------------------------------------------------|
| Property Lookup         | Search by listing ID (P001) or property name (Marina Heights) |
| FAQ System             | Handles office location, working hours, contact info, services |
| Visit Booking          | Complete booking flow: name → phone → property selection |
| AI Enhancement         | OpenAI integration for natural, conversational responses |
| Modern Web UI          | Responsive chat interface with typing indicators |
| Data Persistence       | CSV storage for properties and visit bookings |

### Live Demo

Deploy to Render and update this link: [https://your-app-name.onrender.com/](https://your-app-name.onrender.com/)

### Supported Queries Examples

**FAQ Questions:**
- `What are your working hours?`
- `Where is your office located?`

**Property Searches:**
- `What is the price of Property P001?`
- `Show details for Marina Heights`
- `Is Ocean Breeze available?`

**Visit Booking:**
- `I want to book a visit`
- `Schedule a property visit`

## 💻 Local Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/zorever-assessment
cd zorever-assessment

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variable
export OPENAI_API_KEY=your_openai_api_key_here

# Run the application
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser

## 🚀 Render Deployment

1. **Connect Repository:** Link your GitHub repo to Render
2. **Environment Variables:** Set `OPENAI_API_KEY` in Render dashboard
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `gunicorn app:app`

## 📁 Project Structure

```
zorever-assessment/
├── app.py              # Main Flask application with routes
├── helpers.py          # Data processing and intent detection
├── templates/
│   └── index.html      # Modern responsive chat interface
├── data/
│   ├── properties.csv  # Property database (7 sample properties)
│   └── visits.csv      # Visit bookings (auto-created)
├── requirements.txt    # Python dependencies
└── runtime.txt         # Python version for deployment
```

## 🏠 Sample Properties Available

| ID   | Property Name      | Type      | Price      | Status    |
|------|-------------------|-----------|------------|-----------|
| P001 | Sunrise Apartments | Apartment | $250,000   | Available |
| P002 | Desert View Villa  | Villa     | $1,250,000 | On Request|
| P003 | Marina Heights     | Apartment | $450,000   | Available |
| P004 | Golden Sands Tower | Apartment | $320,000   | Available |
| P005 | Palm Residence     | Villa     | $800,000   | Available |
| P006 | Sky Gardens        | Apartment | $520,000   | On Request|
| P007 | Ocean Breeze       | Apartment | $280,000   | Available |

## 🤖 AI Integration

- **Model:** OpenAI GPT-3.5-turbo
- **Framework:** LangChain for structured LLM interactions  
- **Enhancement:** All responses are polished by AI for natural conversation
- **Fallback:** System works without OpenAI (basic template responses)

## 📝 Technical Requirements Met

✅ **Generic FAQ Handling:** Office location, working hours, services  
✅ **Property-Specific Queries:** Lookup by ID or name with fuzzy matching  
✅ **Visit Booking Automation:** Multi-step flow with CSV persistence  
✅ **Modern Web Interface:** Responsive design with real-time chat  
✅ **AI Enhancement:** Natural language response polishing
