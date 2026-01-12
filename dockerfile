FROM rasa/rasa:3.4.0-full

WORKDIR /app

COPY . /app

# Install deps if any
RUN pip install --no-cache-dir -r actions/requirements.txt || true   # adjust path if needed

# Model fix: rename to latest.tar.gz
RUN mkdir -p models && \
    cp rasa_server/models/20260110-010725-silver-bark.tar.gz models/latest.tar.gz  # adjust original path

USER 1001

EXPOSE 8080 5055

CMD ["sh", "-c", "\
  rasa run actions --actions actions --port 5055 & \
  rasa run --model models/latest.tar.gz --enable-api --cors '*' --port $PORT \
"]