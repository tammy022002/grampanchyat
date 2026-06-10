#!/bin/bash

# Define cleanup function to kill both servers on exit
cleanup() {
    echo "Stopping servers..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
    exit
}

# Trap SIGINT (Ctrl+C) and SIGTERM to run cleanup
trap cleanup SIGINT SIGTERM

echo "==========================================="
echo "   Starting Gram Panchayat ERP Servers     "
echo "==========================================="

echo "--> Cleaning up old processes..."
lsof -ti:8000 | xargs kill -9 2>/dev/null || true
lsof -ti:4200 | xargs kill -9 2>/dev/null || true

# Start Backend
echo "--> Initializing Backend (FastAPI)..."
cd backend

# Setup Python Virtual Environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv and install dependencies
source venv/bin/activate
pip install -r requirements.txt

# Start FastAPI on port 8000 in the background
echo "--> Starting Uvicorn Server..."
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload &
BACKEND_PID=$!
cd ..

# Start Frontend
echo "--> Initializing Frontend (Angular)..."
cd frontend

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

# Start Angular on port 4200 in the background
echo "--> Starting Angular Development Server..."
NG_CLI_ANALYTICS=false npm start &
FRONTEND_PID=$!
cd ..

echo "==========================================="
echo "Backend running at: http://127.0.0.1:8000"
echo "Frontend running at: http://localhost:4200"
echo "Press Ctrl+C to stop both servers."
echo "==========================================="

# Wait for background processes to prevent script from exiting
wait $BACKEND_PID $FRONTEND_PID
