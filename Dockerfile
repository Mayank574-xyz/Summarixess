# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 8080

# Run the app
CMD ["python", "main.py"]
