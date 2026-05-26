-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: moovsmart
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS address;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE address (
  address_id bigint NOT NULL AUTO_INCREMENT,
  budapest_district int DEFAULT NULL,
  city varchar(255) DEFAULT NULL,
  door varchar(255) DEFAULT NULL,
  floor int DEFAULT NULL,
  house_number int DEFAULT NULL,
  postal_code int DEFAULT NULL,
  street_name varchar(255) DEFAULT NULL,
  PRIMARY KEY (address_id)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES address WRITE;
/*!40000 ALTER TABLE address DISABLE KEYS */;
INSERT INTO address VALUES (2,5,'Budapest',NULL,NULL,NULL,NULL,NULL),(3,13,'Budapest',NULL,NULL,NULL,NULL,NULL),(4,10,'Budapest',NULL,NULL,NULL,NULL,NULL),(5,5,'Budapest',NULL,NULL,NULL,NULL,NULL),(6,5,'Budapest',NULL,NULL,NULL,NULL,NULL),(7,10,'Budapest',NULL,NULL,NULL,NULL,NULL),(8,NULL,'Győr',NULL,NULL,NULL,NULL,NULL),(9,NULL,'Győr',NULL,NULL,NULL,NULL,NULL),(10,NULL,'Győr',NULL,NULL,NULL,NULL,NULL),(11,NULL,'Győr',NULL,NULL,NULL,NULL,NULL),(12,NULL,'Szeged',NULL,NULL,NULL,NULL,NULL),(13,NULL,'Szeged',NULL,NULL,NULL,NULL,NULL),(14,NULL,'Szeged',NULL,NULL,NULL,NULL,NULL),(15,NULL,'Pécs',NULL,NULL,NULL,NULL,NULL),(16,NULL,'Pécs',NULL,NULL,NULL,NULL,NULL),(17,19,'Budapest',NULL,NULL,42,1195,'Irányi Dániel utca');
/*!40000 ALTER TABLE address ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS booking;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE booking (
  booking_id bigint NOT NULL AUTO_INCREMENT,
  places_to_book int DEFAULT NULL,
  open_house_id bigint DEFAULT NULL,
  user_id bigint DEFAULT NULL,
  PRIMARY KEY (booking_id),
  KEY FKgaeook59gatnixvya3ax99a3c (open_house_id),
  KEY FKkgseyy7t56x7lkjgu3wah5s3t (user_id),
  CONSTRAINT FKgaeook59gatnixvya3ax99a3c FOREIGN KEY (open_house_id) REFERENCES open_house (open_house_id),
  CONSTRAINT FKkgseyy7t56x7lkjgu3wah5s3t FOREIGN KEY (user_id) REFERENCES `user` (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES booking WRITE;
/*!40000 ALTER TABLE booking DISABLE KEYS */;
/*!40000 ALTER TABLE booking ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email_token`
--

DROP TABLE IF EXISTS email_token;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE email_token (
  id bigint NOT NULL AUTO_INCREMENT,
  expiry_date_time datetime(6) DEFAULT NULL,
  token varchar(255) DEFAULT NULL,
  user_id bigint NOT NULL,
  PRIMARY KEY (id),
  KEY FKr09ag0ercq2i63an8pcxmh2bm (user_id),
  CONSTRAINT FKr09ag0ercq2i63an8pcxmh2bm FOREIGN KEY (user_id) REFERENCES `user` (id)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_token`
--

LOCK TABLES email_token WRITE;
/*!40000 ALTER TABLE email_token DISABLE KEYS */;
INSERT INTO email_token VALUES (1,'2023-09-08 08:32:31.967607','af7bb966-fb66-4f0c-b069-a3fba2e68f7d',7),(2,'2023-09-08 08:32:33.421002','101bf16c-5602-4b19-86ee-8f2e48949c98',8),(3,'2023-09-08 10:51:19.581796','45dcfb4e-afb1-48f1-98f5-7c4358c50933',9),(4,'2023-09-09 08:31:11.335174','adea242f-8c12-478c-b5a0-045790ea61da',10),(5,'2023-09-09 08:33:20.474878','4b7c4e66-d9e1-4711-9162-18a434f33705',11);
/*!40000 ALTER TABLE email_token ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hibernate_sequence`
--

DROP TABLE IF EXISTS hibernate_sequence;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE hibernate_sequence (
  next_val bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hibernate_sequence`
--

LOCK TABLES hibernate_sequence WRITE;
/*!40000 ALTER TABLE hibernate_sequence DISABLE KEYS */;
INSERT INTO hibernate_sequence VALUES (6);
/*!40000 ALTER TABLE hibernate_sequence ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `open_house`
--

DROP TABLE IF EXISTS open_house;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE open_house (
  open_house_id bigint NOT NULL AUTO_INCREMENT,
  created_at datetime(6) DEFAULT NULL,
  current_participants int DEFAULT NULL,
  from_time datetime(6) DEFAULT NULL,
  is_active bit(1) DEFAULT NULL,
  max_participants int DEFAULT NULL,
  to_time datetime(6) DEFAULT NULL,
  property_id bigint DEFAULT NULL,
  PRIMARY KEY (open_house_id),
  KEY FKfvm0v3wkr3vqfauq5o9v7ltkr (property_id),
  CONSTRAINT FKfvm0v3wkr3vqfauq5o9v7ltkr FOREIGN KEY (property_id) REFERENCES property (property_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `open_house`
--

LOCK TABLES open_house WRITE;
/*!40000 ALTER TABLE open_house DISABLE KEYS */;
/*!40000 ALTER TABLE open_house ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property`
--

DROP TABLE IF EXISTS property;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE property (
  property_id bigint NOT NULL AUTO_INCREMENT,
  activated_at datetime(6) DEFAULT NULL,
  air_conditioning bit(1) DEFAULT NULL,
  archived_at datetime(6) DEFAULT NULL,
  created_at datetime(6) DEFAULT NULL,
  `description` text,
  floor_area double DEFAULT NULL,
  heating_type varchar(255) DEFAULT NULL,
  latitude double NOT NULL,
  listing_status varchar(255) DEFAULT NULL,
  listing_type varchar(255) DEFAULT NULL,
  longitude double NOT NULL,
  `name` varchar(200) NOT NULL,
  number_of_bathrooms double DEFAULT NULL,
  number_of_bedrooms int DEFAULT NULL,
  price double DEFAULT NULL,
  property_type varchar(255) DEFAULT NULL,
  property_uuid varchar(255) DEFAULT NULL,
  address_id bigint DEFAULT NULL,
  owner_user_id bigint DEFAULT NULL,
  PRIMARY KEY (property_id),
  KEY FKgcduyfiunk1ewg7920pw4l3o9 (address_id),
  KEY FKl5wyfd7jklotrfg5krwx9qfp7 (owner_user_id),
  CONSTRAINT FKgcduyfiunk1ewg7920pw4l3o9 FOREIGN KEY (address_id) REFERENCES address (address_id),
  CONSTRAINT FKl5wyfd7jklotrfg5krwx9qfp7 FOREIGN KEY (owner_user_id) REFERENCES `user` (id)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property`
--

LOCK TABLES property WRITE;
/*!40000 ALTER TABLE property DISABLE KEYS */;
INSERT INTO property VALUES (2,'2023-08-10 18:44:05.000000',_binary '',NULL,NULL,'sdfdfgbfdghgdhfjngfhj',100,'GAS',47.50185428013412,'ACTIVE','SELL',19.047708998806034,'First property',1,3,50,'HOUSE',NULL,2,1),(3,'2023-08-04 18:44:07.000000',_binary '\0',NULL,NULL,'sdfdfgbfdghgdhfjngfhj',60,'ELECTRIC',47.51302870418362,'ACTIVE','SELL',19.055590214146974,'Second property',2,1,60,'HOUSE',NULL,3,1),(4,'2023-07-10 18:44:15.000000',_binary '',NULL,NULL,'valami leírás',150,'GAS',47.52716699701925,'ACTIVE','RENT',19.082918841135964,'Third property',2,4,70,'HOUSE',NULL,4,1),(5,'2023-08-05 18:44:22.000000',_binary '',NULL,NULL,'valami leírás',80,'GAS',47.49498279413341,'ACTIVE','SELL',19.051209225791826,'Fourth property',2,4,50,'HOUSE',NULL,5,1),(6,'2023-08-05 18:44:22.000000',_binary '',NULL,NULL,'valami leírás',70,'GAS',47.50546645505575,'ACTIVE','SELL',19.052224654628017,'Fifth property',2,4,30,'APARTMENT',NULL,6,1),(7,'2023-08-05 18:44:22.000000',_binary '',NULL,NULL,'valami leírás',200,'GAS',47.49070380851649,'ACTIVE','SELL',19.135629879764075,'Sixth property',2,4,40,'CONDO',NULL,7,2),(8,'2023-08-05 18:44:22.000000',_binary '',NULL,NULL,'valami leírás',120,'ELECTRIC',47.68361545058954,'ACTIVE','RENT',17.635408223951885,'Seventh property',2,4,100,'MULTI_FAMILY',NULL,8,3),(9,'2023-08-07 18:44:22.000000',_binary '\0',NULL,NULL,'valami leírás',70,'ELECTRIC',47.669368394632414,'ACTIVE','SELL',17.651262839293718,'8th property',2,3,60,'CONDO',NULL,9,4),(10,'2023-08-15 18:44:22.000000',_binary '\0',NULL,NULL,'valami leírás',70,'GAS',47.68243332513053,'ACTIVE','RENT',17.63458801230814,'9th property',2,5,90,'MULTI_FAMILY',NULL,10,5),(11,'2023-08-02 18:44:22.000000',_binary '\0',NULL,NULL,'valami leírás',70,'GAS',47.69336701271636,'ACTIVE','RENT',17.626386262375863,'10th property',10,10,30,'APARTMENT',NULL,11,6),(12,'2023-05-06 18:44:22.000000',_binary '',NULL,NULL,'valami leírás',70,'GAS',46.24779553754815,'ACTIVE','SELL',20.14061182573053,'11th property',12,2,10,'ROW_HOUSE',NULL,12,7),(13,'2023-08-12 18:44:22.000000',_binary '',NULL,NULL,'valami leírás',70,'GAS',46.24948358997446,'ACTIVE','SELL',20.137612816844065,'12th property',2,2,200,'SUMMER_HOUSE',NULL,13,8),(14,'2023-08-06 18:44:22.000000',_binary '',NULL,NULL,'valami leírás',70,'GAS',46.24443646203349,'ACTIVE','SELL',20.176918066829227,'13th property',2,3,20,'APARTMENT',NULL,14,9),(15,'2023-08-06 18:44:22.000000',_binary '',NULL,NULL,'valami leírás',80,'GAS',46.083112462935816,'ACTIVE','SELL',18.237067527571934,'13th property',2,3,30,'APARTMENT',NULL,15,10),(16,NULL,_binary '\0',NULL,'2023-09-06 15:57:02.000000','nincs aktiválva',100,'GAS',46.083112462935816,'ACTIVE','SELL',18.237067527571934,'13th property',2,3,100,'APARTMENT',NULL,16,11),(17,'2023-09-06 17:34:32.598337',_binary '',NULL,'2023-09-06 17:34:32.598323','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vel quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Lectus magna fringilla urna porttitor rhoncus dolor purus non. Sed vulputate mi sit amet mauris. Quam nulla porttitor massa id neque. Bibendum at varius vel pharetra vel turpis nunc. Phasellus egestas tellus rutrum tellus. Tortor condimentum lacinia quis vel eros donec. Neque gravida in fermentum et sollicitudin ac orci. Velit euismod in pellentesque massa placerat duis ultricies.',230,'ELECTRIC',0,'ACTIVE','SELL',0,'Családi ház',2.5,5,100,'ROW_HOUSE',NULL,17,4);
/*!40000 ALTER TABLE property ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_images`
--

DROP TABLE IF EXISTS property_images;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE property_images (
  property_property_id bigint NOT NULL,
  images varchar(255) DEFAULT NULL,
  KEY FK6kvlamqvp6mxs9qhqx7rbo1uf (property_property_id),
  CONSTRAINT FK6kvlamqvp6mxs9qhqx7rbo1uf FOREIGN KEY (property_property_id) REFERENCES property (property_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_images`
--

LOCK TABLES property_images WRITE;
/*!40000 ALTER TABLE property_images DISABLE KEYS */;
INSERT INTO property_images VALUES (2,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--CZpFWVyS--/v1709049299/category/10_zn79vo.jpg'),(2,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--D2IqaDQJ--/v1709049301/category/1_wnsglh.jpg'),(2,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--td29LGqs--/v1709049320/category/interior_y2ejtu.jpg'),(3,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--ly1mMVII--/v1709049309/category/5_pjbc1k.jpg'),(3,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--MiIDhXt4--/v1709049311/category/6_pqepoi.jpg'),(3,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--_W4EruLs--/v1709049313/category/7_pchjuh.jpg'),(4,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--mDK3hetN--/v1709049315/category/8_bj5d5o.jpg'),(5,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--U7QaErU6--/v1709049317/category/9_yl36lj.jpg'),(6,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--ATKTJ_JB--/v1709049318/category/cameron_vxfygd.jpg'),(7,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--td29LGqs--/v1709049320/category/interior_y2ejtu.jpg'),(8,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--pbe2Q6s8--/v1709049322/category/jason-briscoe_waosad.jpg'),(9,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--pbe2Q6s8--/v1709049322/category/jason-briscoe_waosad.jpg'),(10,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--td29LGqs--/v1709049320/category/interior_y2ejtu.jpg'),(11,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--51mxRid7--/v1709049329/category/r-architecture_xg1buk.jpg'),(12,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--td29LGqs--/v1709049320/category/interior_y2ejtu.jpg'),(13,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--U7QaErU6--/v1709049317/category/9_yl36lj.jpg'),(17,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--pbe2Q6s8--/v1709049322/category/jason-briscoe_waosad.jpg'),(17,'https://res.cloudinary.com/dyacsfxsx/image/authenticated/s--_W4EruLs--/v1709049313/category/7_pchjuh.jpg');
/*!40000 ALTER TABLE property_images ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS user;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  id bigint NOT NULL AUTO_INCREMENT,
  email varchar(255) DEFAULT NULL,
  first_name varchar(255) DEFAULT NULL,
  is_enabled bit(1) NOT NULL,
  last_name varchar(255) DEFAULT NULL,
  password_hash varchar(255) DEFAULT NULL,
  profile_picture varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES user WRITE;
/*!40000 ALTER TABLE user DISABLE KEYS */;
INSERT INTO user VALUES (1,'horse@gmail.com','Hegedus',_binary '','Béla','$2a$10$Ir/ZNjoFCgdwMln0.RHEdObc2qJY7zjBsiUZBaD.7T4/hEPpbZAP.','http://res.cloudinary.com/dyacsfxsx/image/authenticated/s--tRToFmtN--/v1708959737/7_qxlrqy.jpg','ROLE_USER'),(2,'pinterlive@gmail.com','Sandor',_binary '','Pinter','$2a$10$xgNyjk68NU89z/7b7Ie6MO8qthygSwzCESAFB2o7HHv/UWN31C7ru','http://res.cloudinary.com/dyacsfxsx/image/authenticated/s--tRToFmtN--/v1708959737/7_qxlrqy.jpg','ROLE_USER'),(3,'tesztelek@freemail.hu','Levi',_binary '','Lénárt','$2a$10$hYhj/s4QP2FDIlSTAtQxm.HNqr7LxaHh.UPRZn7ydXpLOXm8LeXVy','http://res.cloudinary.com/dyacsfxsx/image/authenticated/s--tRToFmtN--/v1708959737/7_qxlrqy.jpg','ROLE_USER'),(4,'kovesli@gmail.com','Bence',_binary '','Kövesdy','$2a$10$yHxnPxirQrcf/nI6AGj2tO2/GC3eXoFWq7wG.ZwFx736JiAbLlEeu',NULL,'ROLE_USER'),(5,'orsiii@gmail.com','Orsi',_binary '','H','$2a$10$FDGxzZbz960IDH/MlILmUOUQ1GYj4lKO2kEyRy/zsy8iwlVV2Yuue',NULL,'ROLE_USER'),(6,'takacs@gmail.com','Teszt',_binary '','Laci','$2a$10$6ZuxP8/B2g3hBySWm9m3WeDcpw4ooXr1ABPfXdxV3lC3mIz45UxRi',NULL,'ROLE_USER'),(7,'rajmund.ruska@gmail.com','Rajmund',_binary '','Ruska','$2a$10$rLvYF8vc3b/z32NClszP7u4mmrhYFiCSIAWuxBzkA8.7ZqhjDpHHS',NULL,'ROLE_USER'),(8,'rajmund.ru@gmail.com','Raj',_binary '','Ruska','$2a$10$7zcrCUwleXgEWEJdN/cmjekwIx.JBmVKY1EZK.Hf6Dnwa/xu2V7.m',NULL,'ROLE_USER'),(9,'pleasefreeme@gmail.com','Levente',_binary '','Lénárt','$2a$10$VeJGdnfp9F29ArJHNqt3FOlFt8fuYYqKD0lN1rvuAWCwQJ/4r.uuS',NULL,'ROLE_USER'),(10,'alma@gmail.com','alma',_binary '\0','nagy','$2a$10$pbX2tDEyi8GFmUblxskp2e5Vuh8FSkb/8j1ZlDYsNHJxbug9ZLHSm',NULL,'ROLE_USER'),(11,'almafa@gmail.com','a',_binary '\0','a','$2a$10$xS8nX.vyYd.FZouIVHEEGOKX9zvIwRiUuSmGmyoBqoMf5UxcyuFwK',NULL,'ROLE_USER');
/*!40000 ALTER TABLE user ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_like_property`
--

DROP TABLE IF EXISTS user_like_property;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE user_like_property (
  property_id bigint NOT NULL,
  user_id bigint NOT NULL,
  PRIMARY KEY (property_id,user_id),
  KEY FK4dj7xkkp1vm3hn8cm465tujmr (user_id),
  CONSTRAINT FK4dj7xkkp1vm3hn8cm465tujmr FOREIGN KEY (user_id) REFERENCES `user` (id),
  CONSTRAINT FKelmdijmpf3tnj0793cce3y2xm FOREIGN KEY (property_id) REFERENCES property (property_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_like_property`
--

LOCK TABLES user_like_property WRITE;
/*!40000 ALTER TABLE user_like_property DISABLE KEYS */;
/*!40000 ALTER TABLE user_like_property ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-06 21:51:04
