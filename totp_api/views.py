from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PhoneModel
import base64

# This class returns the string needed to generate the key


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "randomhashedsecretKey"


class retriveAndVerifyTOTP(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            # if Mobile already exists the take this else create New One
            mobile = PhoneModel.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            PhoneModel.objects.create(
                mobile=phone,
            )
            mobile = PhoneModel.objects.get(
                mobile=phone)  # user Newly created Model
        mobile.isVerified = False
        mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(
            phone).encode())  # Key is generated
        # HOTP Model for OTP is created
        OTP = pyotp.TOTP(key, interval=60, digits=6)
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        # Just for demonstration
        return Response({"OTP": OTP.now(), "message": "OTP is valid only for 60 seconds"}, status=200)

    # OTP Verification
    @staticmethod
    def post(request, phone):
        try:
            mobile = PhoneModel.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(
            phone).encode())  # Generating Key
        OTP = pyotp.TOTP(key, interval=60, digits=6)  # HOTP Model
        if OTP.verify(request.data["OTP"]):  # Verifying the OTP
            mobile.isVerified = True
            mobile.save()
            return Response({'message': 'You are authorised', 'isVerified': True}, status=200)
        return Response({'message': 'OTP is wrong'}, status=400)
