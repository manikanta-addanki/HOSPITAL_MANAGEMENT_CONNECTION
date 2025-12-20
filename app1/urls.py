from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # AUTH
    path("", views.user_register, name="home"),          # first page = register
    path("register/", views.user_register, name="user_register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),

    # DASHBOARD
    path("dashboard/", views.dashboard, name="dashboard"),

    # PATIENTS
    path("patients/", views.patient_list, name="patient_list"),
    path("patients/create/", views.patient_create, name="patient_create"),
    path("patients/<int:id>/", views.patient_detail, name="patient_detail"),
    path("patients/<int:id>/update/", views.patient_update, name="patient_update"),
    path("patients/<int:id>/delete-auth/", views.patient_delete_auth, name="patient_delete_auth"),

    # DOCTORS
    path("doctors/", views.doctor_list, name="doctor_list"),
    path("doctors/create/", views.doctor_create, name="doctor_create"),
    path("doctors/<int:id>/update/", views.doctor_update, name="doctor_update"),
    path("doctors/<int:id>/delete-auth/", views.doctor_delete_auth, name="doctor_delete_auth"),

    # APPOINTMENTS
    path("appointments/", views.appointment_list, name="appointment_list"),
    path("appointments/create/", views.appointment_create, name="appointment_create"),
    path("appointments/<int:id>/update/", views.appointment_update, name="appointment_update"),
    path("appointments/<int:id>/delete-auth/", views.appointment_delete_auth, name="appointment_delete_auth"),

    # BILLING
    path("billing/", views.billing_list, name="billing_list"),
    path("billing/create/", views.billing_create, name="billing_create"),

    # LAB REPORTS
    path("labreports/", views.labreport_list, name="labreport_list"),
    path("labreports/create/", views.labreport_create, name="labreport_create"),

    # STAFF
    path("staff/", views.staff_list, name="staff_list"),
    path("staff/create/", views.staff_create, name="staff_create"),

    # BEDS
    path("beds/", views.bed_list, name="bed_list"),
    path("beds/create/", views.bed_create, name="bed_create"),

    # MEDICINES
    path("medicines/", views.medicine_list, name="medicine_list"),
    path("medicines/create/", views.medicine_create, name="medicine_create"),

    # PRESCRIPTIONS
    path("prescriptions/", views.prescription_list, name="prescription_list"),
    path("prescriptions/create/", views.prescription_create, name="prescription_create"),
]

# For serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
