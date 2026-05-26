 
-	Klónozd a repót
-	Indítsd el a Docker Desktop-ot (vagy az Engine-t, ha linux-ról vagy és nincs Desktop)
-	Nyiss egy terminált abban a mappában, ahol a compose.yaml file van

Konténerek indítása:  
`docker compose up`  
(letölti a szükséges image-eket, a docker ebből létrehozza a megfelelő konténereket és el is indítja őket)  
Az adatbázis feltöltéséhez a gyökérmappában található sql fájlt használja fel automatikusan.

A frontend a http://localhost:4200 címen lesz elérhető (böngésző)  

A backend a http://localhost:8080 címen lesz elérhető (Postman)  

Az adatbázishoz a localhost 3306-os porton lehet kapcsolódni, csatlakozási adatok:  
`username: root `  
`password: test1234`  

  

További információk:  
`docker compose start`: elindítja a konténereket  
`docker compose stop`: leállítja a konténereket  
`docker compose down`: **_törli_** a konténereket  

**Ha töröljük a database konténert, elvesznek a benne lévő adatok!**