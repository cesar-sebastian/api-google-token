# API GOOGLE TOKEN

## Configuration

* Set file .env and put credentials on credentials folder
* Adjust CORS domain on `main.py` file

## Install

* Activate environment

`. activate`

* Generate App

`pip install -r requirements.txt`

* Run App

`uvicorn main:app`

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
