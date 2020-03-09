# Employee Registration API

An employee registration API.

## Features

With this API:
- Can consult address by zip code number.
- Can consult address by query params: "federated_state", "city" and "street"
- Can list, create, update and delete employees

### Requirements
```
- Python 3
- Django 3.0.4
- Django Rest Framework 3.11.0
- Postgres latest
```

### Clone the repository
```
git clone https://github.com/marlonleite/employee_registration.git
```

### Installation

Virtualenv:
```
python3 --version
python3 -m venv venv
source venv/bin/activate
 
pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic
python manage.py migrate
python manage.py runserver
```

Docker:
```
Create:
docker-compose up -d

Drop:
docker-compose down

```

## How it works:

Consulting address:

```
GET /api/address/<int:zip_code>/
```
or
```
GET /api/address/?federated_state=<string>&city=<string>&street=<string>/
```

```
Response:
{
    "zip_code": "string",
    "federated_state": "string",
    "city": "string",
    "street": "string",
    "neighborhood": "string"
}
```

List employees:
```
GET /api/employees/
```
```
Response 200:

[
    {
        "id": <int>,
        "name": <string>,
        "document": <string>,
        "email": <string>,
        "address": {
            "id": <int>,
            "street": <string>,
            "number": <int>,
            "neighborhood": <string>,
            "city": <string>,
            "federated_state": <string>,
            "zip_code": <string>
        }
    }
]
```

Create employee:
```
POST /api/employees/
```
```
data json:
{
    "name": <string>,
    "document": <string>,
    "email": <string>,
    "address": {
        "zip_code": <string>,
        "federated_state": <string>,
        "city": <string>,
        "street": <string>,
        "neighborhood": <string>,
        "number": <int>
    }
}
```
```
Response 201:
{
    "id": <int>,
    "name": <string>,
    "document": <string>,
    "email": <string>,
    "address": {
        "id": <int>,
        "street": <string>,
        "number": <int>,
        "neighborhood": <string>,
        "city": <string>,
        "federated_state": <string>,
        "zip_code": <string>
    }
}
```

Update employee:
```
PATCH /api/employees/<id>/
```
```
data json:
{
    ...
    "name": <string>
    ...
}

or

{
    "address": {
        ...
        "number": <int>
        ...
    }
}

```
```
Response 200:
{
    "id": <int>,
    "name": <string>,
    "document": <string>,
    "email": <string>,
    "address": {
        "id": <int>,
        "street": <string>,
        "number": <int>,
        "neighborhood": <string>,
        "city": <string>,
        "federated_state": <string>,
        "zip_code": <string>
    }
}
```

Delete employee:
```
DELETE /api/employees/<id>/
```
```
Response 204 No Content
```

## Running the tests

Some tests were done in the application. 
Test address by zip code. 
Test address by street address, city and federation state. 
Test Employee create, list, update and delete. 
Expected returns status of the application.

Go there:
```
./manage.py test
```

## Authors

* **Marlon Leite** - [GitHub](https://github.com/marlonleite)

