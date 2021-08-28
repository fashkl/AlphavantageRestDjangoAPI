# Alpha Vantage Stock Prices API - Django Backend


- API using Django that fetches the price of BTC/USD from the alphavantage API
every hour, and stores it on postgres database.
- API has two endpoints
  - GET `/api/v1/quotes` - returns exchange rate
  - POST `/api/v1/quotes` which triggers force requesting of the price from [alphavantage.co](https://www.alphavantage.co/)
- API is secured with API Key

## Requirements
- Python > 3.7
- Docker (optional)

## Running Locally
- create a `.env` using `.env.example` as an example and fill variables with values
- Define your api security header and access token by filling variables in `constants.py` file with values that will be validated with those provided through `.env` file  
- Run `pip install -r requirements.txt`
- Run `python manage.py migrate`
- Run `python manage.py runserver --noreload`
- open http://localhost:8000

## Running locally with Docker
- create a `.env` using `.env.example` as an example and fill variables with values
- Define your api security header and access token by filling variables in `constants.py` file with values that will be validated with those provided through `.env` file  
- Run application using docker-compose by running `docker-compose up --build`
- open http://localhost:8000

## Calling API
- ### Postman
  - Set Headers of request with `CUSTOM-TOKEN-HEADER:token_value_in_env`
- ### CURL
  - to get the latest quote using curl run `curl -H 'CUSTOM-TOKEN-HEADER:{token_value_in_env}' http://localhost:8000/api/vi/quotes`
  - to update the latest quote using curl run `curl -H 'CUSTOM-TOKEN-HEADER:{token_value_in_env}' -X POST http://localhost:8000/api/vi/quotes`