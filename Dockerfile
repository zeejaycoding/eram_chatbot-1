FROM rasa/rasa:3.6.20

USER root

# minimal Linux deps
RUN apt-get update && apt-get install -y gcc

# copy project
COPY . /app

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

# validate spaCy model
RUN python -m spacy validate || true

EXPOSE 8080

USER 1001

CMD ["rasa", "run", "--enable-api", "--port", "8080"]
