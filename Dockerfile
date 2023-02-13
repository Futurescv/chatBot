FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

RUN pip install openai

ENV API_KEY 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