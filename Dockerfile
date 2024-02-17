# streamlit demo dockerfile
# docker build -f Dockerfile -t streamlit --progress=plain .
# docker run -p 8501:8501 streamlit

FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/Laz4rz/streamlit_demo_app.git .

# app files are stored with dockerfile
COPY . .

# --progress=plain for output to be visible
RUN ls -la 

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_demo.py", "--server.port=8080", "--server.adress=0.0.0.0"]
