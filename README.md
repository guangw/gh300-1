# Mergington High School Activities System

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

A web application that allows students at Mergington High School to view and sign up for extracurricular activities. Built with **FastAPI** for the backend and vanilla **HTML/CSS/JavaScript** for the frontend.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/guangw/gh300-1.git
   cd gh300-1
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the application**
   - **Web Interface**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs
   - **Alternative API Docs**: http://localhost:8000/redoc

## 🏗️ Project Structure

```
├── src/
│   ├── app.py              # FastAPI application and API routes
│   ├── static/
│   │   ├── index.html      # Main web interface
│   │   ├── app.js          # Frontend JavaScript logic
│   │   └── styles.css      # Styling and layout
│   └── README.md           # Additional project documentation
├── tests/
│   ├── __init__.py
│   └── test_cities.py      # Test cases for the cities API
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🎯 Features

- **Activity Management**: View all available extracurricular activities
- **Student Registration**: Sign up for activities with email validation
- **Duplicate Prevention**: Prevents students from registering twice for the same activity
- **Cities API**: Query cities by country (includes USA, Canada, UK, Spain)
- **Responsive Design**: Modern, mobile-friendly web interface
- **Real-time Updates**: Dynamic participant count and availability

## 🛠️ Development

### Running in Development Mode

For development with auto-reload:
```bash
uvicorn src.app:app --reload
```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_cities.py
```

### VS Code Development

This project includes VS Code configuration:

1. **Launch Configuration**: Use F5 to start debugging
2. **Recommended Extensions**: 
   - Python
   - GitHub Copilot (if available)

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Redirects to the web interface |
| `GET` | `/activities` | Get all activities with details |
| `POST` | `/activities/{activity_name}/signup?email={email}` | Sign up for an activity |
| `GET` | `/cities/{country}` | Get cities by country code |

### Example API Usage

**Get all activities:**
```bash
curl http://localhost:8000/activities
```

**Sign up for an activity:**
```bash
curl -X POST "http://localhost:8000/activities/Chess%20Club/signup?email=student@mergington.edu"
```

**Get cities by country:**
```bash
curl http://localhost:8000/cities/Spain
```

## 🔧 Configuration

### Supported Countries for Cities API
- **USA**: New York, Los Angeles, Chicago
- **Canada**: Toronto, Vancouver, Montreal
- **UK**: London, Manchester, Birmingham
- **Spain**: Seville

### Activity Data Structure
```json
{
  "activity_name": {
    "description": "Activity description",
    "schedule": "When it meets",
    "max_participants": 20,
    "participants": ["email@mergington.edu"]
  }
}
```

## 🚀 Deployment

### Using Docker (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Deployment
For production, consider using:
- **Gunicorn** with Uvicorn workers
- **Nginx** as a reverse proxy
- **Environment variables** for configuration
- **Proper database** (PostgreSQL, MySQL) instead of in-memory storage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Testing

This project includes test coverage for:
- Cities API endpoint functionality
- Activity registration validation
- Error handling for non-existent resources

Run tests before submitting pull requests to ensure code quality.

## 📄 License

&copy; 2025 GitHub &bull; [MIT License](https://gh.io/mit)

---

**Getting Started with GitHub Copilot Exercise** - Part of GitHub Skills

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/guangw/gh300-1/issues/1)
