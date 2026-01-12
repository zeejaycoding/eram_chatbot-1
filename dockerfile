# Use the full Rasa image that includes both core + SDK (actions support)
FROM rasa/rasa:3.4.0-full

WORKDIR /app

# Copy ALL project files (adjust paths if needed)
COPY . /app

# Install any extra Python deps for actions FIRST
RUN pip install --no-cache-dir -r actions_server/actions/requirements.txt || true

# Ensure models directory exists and copy your model
RUN mkdir -p models
COPY rasa_server/models/20260110-010725-silver-bark.tar.gz models/

# Switch user back to non-root for security
USER 1001

# Expose ports (optional, Railway ignores for public)
EXPOSE 8080 5055

# Run BOTH servers — use $PORT for the core server (Railway sets this!)
CMD ["sh", "-c", "\
  rasa run actions --actions actions_server.actions --port 5055 & \
  rasa run --model models/20260110-010725-silver-bark.tar.gz --enable-api --cors '*' --port $PORT \
"]