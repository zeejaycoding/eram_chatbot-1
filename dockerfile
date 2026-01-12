FROM rasa/rasa:3.4.0-full

WORKDIR /app

COPY . /app

# Install deps
RUN pip install --no-cache-dir -r actions/requirements.txt || true   # adjust if path different

# Extract the model tar.gz into models/ folder
RUN mkdir -p models/extracted && \
    tar -xzf rasa_server/models/20260110-010725-silver-bark.tar.gz -C models/extracted && \
    # Optional: if extraction creates a subfolder, move contents up (adjust based on your tar structure)
    # mv models/extracted/*/* models/extracted/ 2>/dev/null || true

# Switch user
USER 1001

EXPOSE 8080 5055

CMD ["sh", "-c", "\
  rasa run actions --actions actions --port 5055 & \
  rasa run --model models/extracted --enable-api --cors '*' --port $PORT \
"]