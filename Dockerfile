FROM ubuntu

# Set working directory
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt .

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv build-essential pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment and activate it
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install dependencies using pip in the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the image
COPY myproject /app

# Set entrypoint
ENTRYPOINT ["python3"]

# Set default command to run Django server
CMD ["manage.py", "runserver", "0.0.0.0:8000"]