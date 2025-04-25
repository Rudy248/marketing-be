# Marketing Campaign Analytics Dashboard - Backend

A FastAPI-based backend application for managing marketing campaign data.

## Demo
https://marketing-fe-seven.vercel.app/ (Frontend)
https://web-production-1aa0d.up.railway.app/docs (Backend)

## Features

- RESTful API for campaign management
- SQLite database with SQLAlchemy ORM
- CORS support for frontend integration
- Mock data generation for testing

## Tech Stack

- FastAPI
- SQLite database
- SQLAlchemy ORM
- Pydantic for data validation

## Prerequisites

- Python (v3.8 or higher)
- pip

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Rudy248/marketing-be.git
   cd fastapi
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be available at `http://localhost:8000`

## API Endpoints

- `GET /campaigns` - Get all campaigns




## Deployment (Railway)

1. Push your code to GitHub
2. Create a new project on Railway
3. Connect your GitHub repository
4. Add environment variables:
   - `FRONTEND_URL`: Your Vercel frontend URL
5. Deploy

## License

This project is licensed under the MIT License - see the LICENSE file for details.
