# FastAPI URL Shortener

A URL shortener crafted using FastAPI, SQLAlchemy, Pydantic, and Alembic.

## Create the .env file

The first thing one needs to do is to create an .env file in the root folder of this repo. Copy the keys from .env.dist and fill in the values according to your local database connection arguments.

## Build the Docker Container

Two different containers are composed together using `docker compose`. One for the application itself, and one separately for the PostgreSQL database. To build and run the Docker containers, execute the following command:

```bash
docker compose up --build
```

## Run/Test the Application Locally

Utilize Postman or a similar tool to test the application's endpoints:

### Shortening URLs

Make a POST request to shorten a URL:

```http
POST http://localhost:80/shorten/
Content-Type: application/json

{
    "url": "https://www.example.com"
}
```

### Using a Shortened URL

To navigate using a shortened URL, access:

```
GET http://localhost:80/urls/<shortened_hashcode>
```

### Checking Stats of a Shortened URL

To check the statistics of a shortened URL, use:

```
GET http://localhost:80/urls/<shortened_hashcode>/stats
```
