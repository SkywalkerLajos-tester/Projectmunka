TESTUSER = [
########## 0-1 valid registration + with same email
    {
    "lastname": "Elek",
    "firstname": "Teszt",
    "phone_number": "+91123456789",
    "email": "test@elek.hu",
    "email_confirm": "test@elek.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
########## 2 registration without last name
    {
    "lastname": "",
    "firstname": "Teszt",
    "phone_number": "+91123456789",
    "email": "test_l@elek.hu",
    "email_confirm": "test_l@elek.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
########## 3 registration without first name
    {
    "lastname": "Elek",
    "firstname": "",
    "phone_number": "+91123456789",
    "email": "test_f@elek.hu",
    "email_confirm": "test_f@elek.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
########## 4 registration without phone number
    {
    "lastname": "Elek",
    "firstname": "Teszt",
    "phone_number": "",
    "email": "test_p@elek.hu",
    "email_confirm": "test_p@elek.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
########## 5 registration with invalid names and phone numbers
    {
    "lastname": "5678",
    "firstname": "1234",
    "phone_number": "abcdefghij",
    "email": "test_invalid@elek.hu",
    "email_confirm": "test_invalid@elek.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
########## 6 registration with invalid email
    {
    "lastname": "Elek",
    "firstname": "Teszt",
    "phone_number": "+91123456789",
    "email": "test",
    "email_confirm": "test",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
########## 7 registration with wrong email confirmation
    {
    "lastname": "Elek",
    "firstname": "Teszt",
    "phone_number": "+91123456789",
    "email": "test_c@test.hu",
    "email_confirm": "test__c@test.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcd"
},
########## 8 registration with wrong password
    {
    "lastname": "Elek",
    "firstname": "Teszt",
    "phone_number": "+91123456789",
    "email": "test_p@test.hu",
    "email_confirm": "test_p@test.hu",
    "password": "1234",
    "password_confirm": "1234"
},
########## 9 registration with wrong password confirmation
    {
    "lastname": "Elek",
    "firstname": "Teszt",
    "phone_number": "+91123456789",
    "email": "test_pc@test.hu",
    "email_confirm": "test_pc@test.hu",
    "password": "1234_Abcd",
    "password_confirm": "1234_Abcdd"
},
    ]