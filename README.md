# django-otp-api-time-based[TOTP]

## API Calls

#### GET [Request OTP]
```http://127.0.0.1:8000/otp/${mobilenumber}/```

##### Response
Data: 
```
   {
    "OTP":040301,
    "isVerified": false,
    "message": "OTP is valid only for 60 seconds"
   }
```

#### POST [Verify OTP]
```http://127.0.0.1:8000/otp/${mobilenumber}/```

##### Response
Data: 
```
   {
    "message": "You are authorized",
    "isVerified": true
   }
```
