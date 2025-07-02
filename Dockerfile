FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY server.py .
COPY pyproject.toml .
COPY README.md .

# Install the package
RUN pip install -e .

# Create non-root user
RUN useradd --create-home --shell /bin/bash jaqpot
USER jaqpot

# Expose port (though MCP typically uses stdio)
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command to run the MCP server
CMD ["python", "server.py"]