# Run `docker-compose up --build` for quick deployment

# APIS:

# Patient API:

1. POST - http://localhost:8000/api/v1/patients/
   body: {
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1980-01-01",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "diseases": {
        "Major": "Cough"
    }
   }
2. GET - http://localhost:8000/api/v1/patients/
3. DELETE - http://localhost:8000/api/v1/patients/{id}
4. PATCH - http://localhost:8000/api/v1/patients/{id}
   body: {
   "first_name": "Johnny",
   "last_name": "Doeee",  
   }

# Doctor's API

1. GET - http://localhost:8000/api/v1/doctors/
2. POST - http://localhost:8000/api/v1/doctors/
   body: {
   "first_name": "John",
   "last_name": "Doe",
   "date_of_birth": "1980-01-01",
   "email": "john.doe@example.com",
   "phone": "123-456-7890",
   "specialization": {
   "primary": "Cardiology",
   "secondary": ["Pediatrics", "General Medicine"]
   },
   "registration_body": "Medical Board",
   "registration_number": "MB123456",
   "registration_year": 2005
   }
3. DELETE - http://localhost:8000/api/v1/doctors/{id}
4. PATCH - http://localhost:8000/api/v1/doctors/{id}
   body: {
    "first_name": "Johnn",
    "last_name": "Cena",
   }
