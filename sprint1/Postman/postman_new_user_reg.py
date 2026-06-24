import json
import csv
import random
from faker import Faker
import requests

# Inicializáljuk a Fakert magyar nyelvű adatokhoz
fake = Faker("hu_HU")

url = "http://localhost:8080/api/users/registration"
headers = {"Content-Type": "application/json"}

# A CSV fájl neve, amibe menteni fogunk
csv_filename = "new_users.csv"

# Megnyitjuk a CSV fájlt írásra (newline='' kell, hogy ne hagyjon ki üres sorokat)
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    # Létrehozzuk a CSV író objektumot
    csv_writer = csv.writer(csv_file)

    # Beírjuk a fejlécet a CSV-be
    csv_writer.writerow(["Email", "Password", "LastName", "FirstName", "PhoneNumber"])

    print(f"--> Regisztrációk indítása, adatok mentése ide: {csv_filename}\n")

    # 20-szoros ismétlés
    for i in range(20):
        # Véletlenszerű adatok generálása
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.ascii_free_email()
        password = (
            "1234_Abcd"  # Ha ezt is randomizálni akarod, használhatod a fake.password()-öt
        )

        # Magyar mobiltelefonszám generálása
        provider_code = random.choice(["20", "30", "70", "50"])
        phone_number = f"+36{provider_code}{fake.msisdn()[5:]}"

        # A JSON payload összeállítása
        payload = json.dumps(
            {
                "email": email,
                "password": password,
                "lastName": last_name,
                "firstName": first_name,
                "phoneNumber": phone_number
            }
        )

        # Kérés elküldése
        try:
            response = requests.post(url, headers=headers, data=payload)

            # Ha a szerver sikeresen fogadta (200 vagy 201-es státuszkód)
            if response.status_code in [200, 201]:
                print(
                    f"[{i+1}/20] SIKER: {last_name} {first_name} ({email}) regisztrálva."
                )

                # Mentés a CSV fájlba
                csv_writer.writerow([email, password, last_name, first_name, phone_number])
            else:
                print(
                    f"[{i+1}/20] HIBA: A szerver {response.status_code} kódot küldött. (Nem mentve a CSV-be)"
                )

        except requests.exceptions.ConnectionError:
            print(
                f"\n[{i+1}/20] KRITIKUS HIBA: A szerver nem érhető el! Leállás..."
            )
            break

print(f"\nFolyamat kész! A fájlt megtalálod a PyCharmban: {csv_filename}")