FROM rasa/rasa:3.4.0

WORKDIR /app

COPY . /app

# Install deps
RUN pip install --no-cache-dir -r actions/requirements.txt || true   # adjust if path different


# Switch user
USER 1001

EXPOSE 8080 5055

CMD ["sh", "-c", "\
  rasa run actions --actions actions --port 5055 & \
  rasa run --model models/extracted --enable-api --cors '*' --port $PORT \
"]
#####