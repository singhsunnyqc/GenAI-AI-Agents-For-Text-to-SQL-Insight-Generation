FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 80

HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health

ENTRYPOINT ["streamlit", "run", "./src/app.py", "--server.port=80", "--server.address=0.0.0.0"]