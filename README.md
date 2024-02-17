# streamlit_demo_app

### test build
```
docker build -f Dockerfile -t eu.gcr.io/streamlitdemo-414616/app:v1 --progress=plain .
docker run -p 8080:8080 eu.gcr.io/streamlitdemo-414616/app:v1
```
### deploy build
```
gcloud builds submit . -t eu.gcr.io/streamlitdemo-414616/app:v1
```
