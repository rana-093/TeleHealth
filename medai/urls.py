from django.urls import path
from rest_framework import routers
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'v1/doctors', DoctorViewSet, base_name='doctors')
router.register(r'v1/patients', PatientViewSet, base_name='patients')
router.register(r'v1/appointments', AppointmentViewSet, base_name='appointments')
router.register(r'v1/availabilities', AvailabilityViewSet, base_name='availabilities')
router.register(r'v1/consultations', ConsultationViewSet, base_name='consultations')


urlpatterns = []
urlpatterns += router.urls
