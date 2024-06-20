from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import  viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.timezone import now
from .models import Person, Doctor, Patient, Appointment, Availability, Consultation
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, ConsultationSerializer, AvailabilityModelSerializer, AvailabilitySerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=False, methods=['get'])
    def upcoming_appointments(self, request):
        doctor_id = request.query_params.get('doctor_id')
        appointments = Appointment.objects.filter(doctor_id=doctor_id, appointment_date__gte=now(), status='scheduled')
        return Response(AppointmentSerializer(appointments, many=True).data)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilityModelSerializer
    http_method_names = ['post', 'get']

    def create(self, request, *args, **kwargs):
        serializer = AvailabilitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        availabilities = serializer.save()
        availability_serializer = AvailabilityModelSerializer(availabilities, many=True)
        return Response(data=availability_serializer.data, status=status.HTTP_201_CREATED)


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

    def list(self, request, *args, **kwargs):
        appointment_id = request.query_params.get('appointment_id', None)
        consulations = self.queryset
        print("consultaions: ", consulations)
        if appointment_id:
            consulations = consulations.filter(appointment_id=appointment_id)
        serializer = ConsultationSerializer(consulations, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



