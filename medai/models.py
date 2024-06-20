from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.utils import timezone

day_choices = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri']

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    class Meta:
        abstract = True


class Doctor(Person, TimeStampMixin):
    specialization = JSONField()
    registration_body = models.CharField(max_length=100, null=True, blank=True)
    registration_number = models.CharField(max_length=100, null=True, blank=True)
    registration_year = models.IntegerField(null=True, blank=True)


class Availability(TimeStampMixin):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, related_name='availabilities')
    booking_date = models.DateField(null=True, blank=True)
    booking_time = models.TimeField(null=True, blank=True)


class Patient(Person, TimeStampMixin):
    diseases = JSONField()


class Appointment(TimeStampMixin):
    status_choices = ['scheduled', 'cancelled', 'ongoing', 'closed']
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, related_name='my_appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, default='scheduled', choices=[(x, x) for x in status_choices])

class Consultation(TimeStampMixin):
    appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING, related_name='consultations')
    type = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
