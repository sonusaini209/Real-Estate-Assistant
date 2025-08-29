<h1 align="center">AI-Powered Real Estate Chatbot</h1>

<p align="center">
  &nbsp;
  <a href="https://github.com/sonusaini209/Real-Estate-Assistant">
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

##  Overview

This project demonstrates a complete AI-powered chatbot solution for real estate businesses, featuring:

**Smart Property Search:** Find properties by listing ID (P001-P0012) or name matching  
**Natural Language FAQs:** Answers common questions about office hours, location, and services  
**Automated Visit Booking:** Multi-step booking flow with data persistence to CSV  
**AI Enhancement:** Uses OpenAI GPT-3.5-turbo to polish all responses for natural conversation  

##  Features

| Feature                 | Description                                              |
|-------------------------|----------------------------------------------------------|
| Property Lookup         | Search by listing ID (P001) or property name (Marina Heights) |
| FAQ System             | Handles office location, working hours, contact info, services |
| Visit Booking          | Complete booking flow: name → phone → property selection |
| AI Enhancement         | OpenAI integration for natural, conversational responses |
| Modern Web UI          | Responsive chat interface with typing indicators |
| Data Persistence       | CSV storage for properties and visit bookings |



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

```bash

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


```
zorever-assessment/
├── app.py              # Main Flask application with routes
├── helpers.py          # Data processing and intent detection
├── templates/
│   └── index.html      # Modern responsive chat interface
├── data/
│   ├── properties.csv  # Property database (12 sample properties)
│   └── visits.csv      # Visit bookings (auto-created)
├── requirements.txt    # Python dependencies
└── runtime.txt         # Python version for deployment
```

## 🔧 Tech Stack

### Backend
- **Python 3.11+** - Core programming language
- **Flask 3.1+** - Lightweight web framework
- **pandas** - Data manipulation and CSV processing
- **python-dotenv** - Environment variable management

### AI & Machine Learning
- **OpenAI GPT-3.5-turbo** - Natural language processing
- **LangChain** - LLM framework for structured interactions

### Frontend
- **HTML5** - Semantic markup structure
- **CSS3** - Modern styling with gradients and animations
- **JavaScript (ES6+)** - Interactive chat functionality

### Data Storage
- **CSV Files** - Simple, portable data storage
- **Session Management** - Flask sessions for booking flow
- **File I/O** - Python standard library operations

### Deployment & DevOps
- **Gunicorn** - WSGI HTTP server for production
- **Render** - Cloud hosting platform
- **Git** - Version control system
