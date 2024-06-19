Run `docker-compose up --build` for quick deployment

Base URL: **http://localhost:8080/**

## Patient Endpoints
**POST** `/api/v1/patients/`
Create a new patient record.
#### Request Body
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1980-01-01",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "diseases": {
        "Major": "Cough"
    }
}
```
**GET** `/api/v1/patients/`
Get all patient records.

**PATCH** `/api/v1/patients/{id}`
Update a patient record.
#### Request Body
```json
{
    "first_name": "Honey",
    "last_name": "Doee",
}
```

**DELETE** `/api/v1/patients/{id}`
Delete a patient record.


# Doctor's API

1. GET - http://localhost:8000/api/v1/doctors/
2. POST - http://localhost:8000/api/v1/doctors/ <br />
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

# Availability Setting for a doctor:
1. POST - http://localhost:8000/api/v1/availabilities/
body : {
    "doctor_id": 1,
    "booking_dates": ["2024-06-19", "2024-06-19"],
    "booking_times": ["16:00", "18:00"]
}

# Appointment for doctor:
1. GET - http://localhost:8000/api/v1/appointments/upcoming_appointments/?doctor_id={id} -> For Upcoming appointments for a doctor
2. GET - http://localhost:8000/api/v1/appointments/ -> Get all appointments
3. POST - http://localhost:8000/api/v1/appointments/
body: {
    "doctor": 1,
    "patient": 2, 
    "appointment_date": "2024-06-19",
    "appointment_time": "17:00"
}
