# API GOOGLE TOKEN

## Configuration

* Create file .env and put credentials on credentials folder p.e:

`NAME=credentials/my-credentials.json`

* Create folder `credentials/` and put into json file credentials

* Adjust CORS domain on `main.py` file

## Install

* Setup project

``` bash
pip install virtualenv
python -m venv env
source env/Scripts/activate
pip install -r requirements.txt
```

* Run App

`uvicorn main:app`

* Document API

`http://127.0.0.1:8000/docs`

## Uses

P.e:

```curl
curl -X 'POST' \
  'host/google-token/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "CONFLU"
}'
```
