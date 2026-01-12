# Use the full Rasa image that includes both core + SDK (actions support)
FROM rasa/rasa:3.4.0-full

WORKDIR /app

# Copy ALL project files
COPY . /app

# Install any extra Python deps for actions FIRST
RUN pip install --no-cache-dir -r actions_server/actions/requirements.txt || true

# Ensure models directory exists
RUN mkdir -p models

# Copy and extract the pre-trained model
COPY rasa_server/models/20260110-010725-silver-bark.tar.gz /tmp/model.tar.gz
RUN cd /tmp && tar -xzf model.tar.gz -C /app/models && rm model.tar.gz

# Switch user back to non-root for security
USER 1001

# Expose ports
EXPOSE 8080 5055

# Run BOTH servers
CMD ["sh", "-c", "\
  rasa run actions --actions actions_server.actions --port 5055 & \
  rasa run --model models --enable-api --cors '*' --port 8080 \
"]