FROM rasa/rasa:3.6.20

# Switch to root to install system dependencies
USER root

RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev python3-dev supervisor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy project and models
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy model
RUN python -m spacy download en_core_web_sm

# Copy supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Switch back to non-root
USER 1001

# Expose ports
EXPOSE 5005 5055

# Start supervisor to run both Rasa and actions
CMD ["/usr/bin/supervisord"]
