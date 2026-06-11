import csv
import requests

url = "http://localhost:8080/api/users/login"

# Ide gyűjtjük össze a sikeresen bejelentkezett felhasználókat és a tokenjeiket
successful_logins = []

# 1. CSV beolvasása és kérések elküldése
with open("users.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        email = row["email"]
        password = row["password"]

        print(f"Bejelentkezés: {email}...")
        response = requests.get(url, auth=(email, password))

        if response.status_code == 200:
            # Átalakítjuk a választ JSON-ná
            response_data = response.json()

            # Kinyerjük a tokent (ha a kulcs pontos neve 'accessToken')
            token = response_data.get("tokenModel", {}).get("accessToken")

            if token:
                print("-> Sikeres! Token elmentve.")
                # Elmentjük az adatokat a listánkba
                successful_logins.append({
                    "email": email,
                    "password": password,
                    "accessToken": token
                })
            else:
                print("-> Sikeres login, de nem található 'accessToken' a válaszban!")
        else:
            print(f"-> Sikertelen login! Státusz: {response.status_code}")

        print("-" * 40)

# 2. A kinyert tokenek kimentése egy ÚJ CSV fájlba
if successful_logins:
    with open("logged_in_users.csv", mode="w", newline="", encoding="utf-8") as output_file:
        fieldnames = ["email", "password", "accessToken"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        # Írjuk ki a fejlécet
        writer.writeheader()
        # Írjuk be az összes sikeresen összegyűjtött sort
        writer.writerows(successful_logins)

    print(f"Szuper! Összesen {len(successful_logins)} token elmentve a 'logged_in_users.csv' fájlba.")
else:
    print("Egyetlen sikeres bejelentkezés sem történt, nem készült új CSV.")