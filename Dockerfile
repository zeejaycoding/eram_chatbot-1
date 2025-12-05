FROM rasa/rasa:3.4.0-spacy-en

USER root
RUN apt-get update && apt-get install -y --no-install-recommends supervisor \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy ONLY the model first
COPY models/*.tar.gz ./models/

# Then the full project
COPY . .

RUN pip install --no-cache-dir rasa-sdk==3.4.0 onnxruntime==1.17.0

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

USER 1001
EXPOSE 5005 5055
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
