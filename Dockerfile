# Use an official Python base image
FROM python:3.11-slim


# Set work directory
WORKDIR /app

# Install system dependencies (for audio, ffmpeg, etc. as required by dependencies)
RUN pip install --no-cache-dir -r requirements.txt


# Copy project files
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 8000

# Default command (update this if your app has a different entrypoint)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
