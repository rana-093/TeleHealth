from rest_framework import serializers
from .models import Person, Doctor, Patient, Appointment, Consultation, Availability
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        doctor = validated_data['doctor']
        availability_flag = False
        availabilities = Availability.objects.filter(doctor=doctor)
        for availability in availabilities:
            if availability.booking_date == validated_data['appointment_date'] and availability.booking_time == validated_data['appointment_time']:
                availability_flag = True
        if not availability_flag:
            raise ValidationError('Doctor is not available in your chosen date time!')
        return validated_data

    class Meta:
        model = Appointment
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    appointment_details = AppointmentSerializer(source='appointment', read_only=True)

    class Meta:
        model = Consultation
        fields = '__all__'


class AvailabilityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class AvailabilitySerializer(serializers.Serializer):
    doctor_id = serializers.IntegerField()
    booking_dates = serializers.ListField(child=serializers.DateField())
    booking_times = serializers.ListField(child=serializers.TimeField())

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if len(list(validated_data['booking_dates'])) != len(list(validated_data['booking_times'])):
            raise ValidationError('Booking dates and times need to be in sync')
        return validated_data

    def save(self, **kwargs):
        doctor = get_object_or_404(Doctor, id=int(self.validated_data['doctor_id']))
        dates = list(self.validated_data['booking_dates'])
        times = list(self.validated_data['booking_times'])
        availabilities = []

        for i in range(len(dates)):
            availability, created = Availability.objects.get_or_create(
                doctor = doctor,
                booking_date=dates[i],
                booking_time=times[i]
            )
            availabilities.append(availability)
        return availabilities