from django.urls import path, include
from .views import retriveAndVerifyTOTP

urlpatterns = [
    path("<phone>/", retriveAndVerifyTOTP.as_view(), name="OTP"),
]
