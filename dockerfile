FROM rasa/rasa:3.4.0-full

WORKDIR /app

COPY . /app

# Install deps (if any)
RUN pip install --no-cache-dir -r actions/requirements.txt || true

# Switch user
USER 1001

EXPOSE 8080 5055

# Correct CMD: Use exec form or proper sh -c with full command
CMD ["sh", "-c", "rasa run actions --actions actions --port 5055 & rasa run --model models/extracted --enable-api --cors '*' --port $PORT"]