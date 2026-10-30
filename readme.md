# MLOps Lab 2

This repository contains the complete implementation and production-ready code for **Lab 2** of the MLOps course. It showcases a modern machine learning operations pipeline featuring a FastAPI web service, containerization using Docker, automated unit testing, and GitHub Actions for CI/CD workflows.

## 📂 Project Structure

```
MLOps-Lab2/
│
├── .github/
│   └── workflows/        # Automated CI/CD pipelines (GitHub Actions)
├── src/                  # Application source code (FastAPI endpoints and logic)
├── tests/                # Automated testing suite (pytest)
├── Dockerfile            # Container configuration instructions
└── requirements.txt      # Python dependencies list

```

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have the following installed on your local environment:

* Python (version 3.9 or higher)

* Docker Desktop or Engine

### 2. Installation & Local Setup

Clone this repository to your machine and install the required dependencies:

```
git clone https://github.com/SAIF5M/MLOps-Lab2.git
cd MLOps-Lab2
pip install -r requirements.txt

```

### 3. Running the API Locally

Start the FastAPI application development server using Uvicorn:

```
uvicorn src.main:app --reload

```

Once active, you can open the interactive API documentation (Swagger UI) directly in your browser at: `http://127.0.0.1:8000/docs`

## 🐳 Docker Containerization

To package and run the application inside an isolated Docker container:

1. **Build the Docker Image:**

   ```
   docker build -t mlops-lab2 .
   
   ```

2. **Run the Docker Container:**

   ```
   docker run -p 8000:8000 mlops-lab2
   
   ```

## 🧪 Testing

To run the automated unit and integration tests using `pytest`:

```
pytest

```