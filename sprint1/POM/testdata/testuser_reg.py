TESTUSER = [
    ##### valid registration + with same email
    {
    "lastname": "Elemér",
    "firstname": "Teszt",
    "phone_number": "+91123456789",
    "email": "test@ele.hu",
    "email_confirm": "test@ele.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
##### registration with invalid name and phone number
    {
    "lastname": "456",
    "firstname": "123",
    "phone_number": "abcd",
    "email": "test@belek.hu",
    "email_confirm": "test@belek.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
##### registration with invalid email
    {
    "lastname": "456",
    "firstname": "123",
    "phone_number": "abcd",
    "email": "test",
    "email_confirm": "test",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},

    ]