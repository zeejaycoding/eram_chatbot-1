# Use the full Rasa image that includes both core + SDK (actions support)
FROM rasa/rasa:3.4.0-full

WORKDIR /app

# Copy ALL project files
COPY . /app

# Copy your pre-trained model from rasa_server
RUN mkdir -p models
COPY rasa_server/models/20260110-010725-silver-bark.tar.gz models/latest.tar.gz

# Install any extra Python deps for actions
RUN pip install --no-cache-dir -r actions/requirements.txt || true

# Switch user back to non-root for security
USER 1001

# Expose ports
EXPOSE 5005 5055

# Run BOTH servers in the same container
CMD ["sh", "-c", "\
  rasa run actions --actions actions.actions --port 5055 & \
  rasa run --model models/latest.tar.gz --enable-api --cors '*' --port ${PORT:-5005} \
"]