FROM python:3.13 AS builder

WORKDIR /app

COPY . .

RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/wheels /wheels

RUN pip install /wheels/*

COPY . .

CMD [ "python","api_collector.py" ]


