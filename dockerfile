# Use an official Python runtime as a base image
FROM python:3.10.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container at /app
COPY requirements.txt /app

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container at /app
COPY . /app

# Expose the port that FastAPI runs on
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
