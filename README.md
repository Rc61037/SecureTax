# SecureTax

SecureTax is a full-stack web app that simplifies federal income tax calculation. Its modern React/Next.js frontend guides users through an intuitive 4-step form. Under the hood, a robust Python/FastAPI backend precisely computes taxes and deductions using 2025 brackets, bridging sleek design with accurate financial tools.

## Getting Started

Follow these instructions to run the application locally on your machine. The app consists of a FastApi Python backend and a React/Next.js frontend. You will need to start both servers.

### 1. Start the Backend API
The backend requires Python and hosts the endpoint for the tax calculations. 

Open a terminal and run the following commands:

```bash
# Navigate to the backend directory
cd backend

# Activate the virtual environment
venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app.main:app --reload
```
The API will start running at **http://localhost:8000**.

### 2. Start the Frontend Website
The frontend uses Next.js and requires Node.js.

Open a **new, separate** terminal and run the following commands:

```bash
# Navigate to the frontend directory
cd frontend

# Install the node dependencies
npm install

# Start the development server
npm run dev
```

### 3. Open the Website
Once both the backend and frontend servers are visibly running in their respective terminals, open your web browser and navigate to:

**[http://localhost:3000](http://localhost:3000)**

You can now interact with the SecureTax application!
