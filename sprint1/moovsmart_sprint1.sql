/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE
DATABASE /*!32312 IF NOT EXISTS*/ `moovsmart` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `moovsmart`;
DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address`
(
    `id`           bigint NOT NULL AUTO_INCREMENT,
    `city`         varchar(255) DEFAULT NULL,
    `county`       varchar(255) DEFAULT NULL,
    `house_number` varchar(255) DEFAULT NULL,
    `latitude` double DEFAULT NULL,
    `longitude` double DEFAULT NULL,
    `street`       varchar(255) DEFAULT NULL,
    `zip_code`     int          DEFAULT NULL,
    `property_id`  bigint       DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `UK_fog6ojr29kwm7hkfbjg81wcny` (`property_id`),
    CONSTRAINT `FKcaqh5qfje1gr350yx6yppp1tl` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK
TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address`
VALUES (2, 'Budapest', 'undefined', '3', 47.4907357, 19.053726659979795, 'Irányi utca', 1056, 2),
       (3, 'Debrecen', 'Hajdú-Bihar', 'undefined', 47.4938324, 21.6650359, 'Szeged utca', 4030, 3),
       (4, 'Szekszárd', 'Tolna', '6', 46.3521127, 18.70133069032609, 'Kossuth Lajos utca', 7100, 4),
       (5, 'Budapest', 'Budapest', '5', 47.4993529, 19.084797337895658, 'Kerepesi út', 1087, 5),
       (6, 'Dunaújváros', 'Fejér', '6', 46.9606997, 18.9270114, 'Radnóti Miklós utca', 2400, 6),
       (7, 'Kecskemét', 'Bács-Kiskun', '6', 46.904000350000004, 19.681144304468035, 'Szent Miklós utca', 6000, 7),
       (8, 'Budapest', 'Budapest', '6', 47.535767, 19.01389791555662, 'Cseppkő utca', 1025, 8),
       (9, 'Tahitótfalu', 'Pest', '6', 47.7532205, 19.0843672, 'Petőfi Sándor utca', 2021, 9),
       (10, 'Budapest', 'undefined', '6', 47.51838255, 19.172539901246928, 'Sándor utca', 1161, 10),
       (11, 'Szombathely', 'Vas', '6', 47.211265600000004, 16.6602671, 'Vadász utca', 9700, 11);
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK
TABLES;
DROP TABLE IF EXISTS `file_registry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `file_registry`
(
    `id`                 bigint NOT NULL AUTO_INCREMENT,
    `category`           varchar(255) DEFAULT NULL,
    `file_path`          varchar(255) DEFAULT NULL,
    `file_size`          bigint       DEFAULT NULL,
    `media_type`         varchar(255) DEFAULT NULL,
    `original_file_name` varchar(255) DEFAULT NULL,
    `title`              varchar(255) DEFAULT NULL,
    `upload_datetime`    datetime(6) DEFAULT NULL,
    `property_id`        bigint       DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY                  `FKlva5ck5pqrdt37qliai3oyi6u` (`property_id`),
    CONSTRAINT `FKlva5ck5pqrdt37qliai3oyi6u` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK
TABLES `file_registry` WRITE;
/*!40000 ALTER TABLE `file_registry` DISABLE KEYS */;
INSERT INTO `file_registry`
VALUES (2, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--VA3LlSJv--/v1779900181/category/1_rafxqc.jpg',
        338794, 'image/jpeg', '1.jpg', 'file', '2024-01-18 11:43:19.450057', 2),
       (3, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--zEZiHewL--/v1779900701/category/cameron_cv76q2.jpg',
        51166, 'image/jpeg', 'cameron-smith-3gMTVySU4rs-unsplash.jpg', 'file', '2024-01-18 11:43:58.718687', 2),
       (4, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--XyVlLWmn--/v1779900734/category/kam-idris_ukjulk.jpg',
        41903, 'image/jpeg', 'kam-idris-Ot2iTXgC6fY-unsplash.jpg', 'file', '2024-01-18 11:44:06.148439', 2),
       (5, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--GIpy9YEA--/v1779900744/category/kitchen_cl2alt.jpg',
        404645, 'image/jpeg', 'kitchen-2400367_1280.jpg', 'file', '2024-01-18 11:44:12.941808', 2),
       (6, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--e7qB1FSi--/v1779900362/category/2_w7spsw.jpg',
        323433, 'image/jpeg', '2.jpg', 'file', '2024-01-18 11:45:44.595415', 3),
       (7, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--PxtAnsHC--/v1779900507/category/3_rwkzqu.jpg',
        232117, 'image/jpeg', '3.jpg', 'file', '2024-01-18 11:46:36.214254', 4),
       (8, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--B3BavI87--/v1779900545/category/4_atapsu.jpg',
        195532, 'image/jpeg', '4.jpg', 'file', '2024-01-18 11:47:23.805843', 5),
       (9, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--wciIsf_U--/v1779900637/category/5_uosgms.jpg',
        110221, 'image/jpeg', '5.jpeg', 'file', '2024-01-18 11:48:31.772197', 6),
       (10, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--Y2b9qCyh--/v1779900758/category/r-architecture_e8rpol.jpg',
        68699, 'image/jpeg', 'r-architecture-T6d96Qrb5MY-unsplash.jpg', 'file', '2024-01-18 11:49:21.917025', 3),
       (11, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--QGNS1n5C--/v1779900751/category/marvin-meyer_expok1.jpg',
        73420, 'image/jpeg', 'marvin-meyer-cjhuXRtRT0Y-unsplash.jpg', 'file', '2024-01-18 11:49:27.867686', 3),
       (12, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--GIpy9YEA--/v1779900744/category/kitchen_cl2alt.jpg',
        404645, 'image/jpeg', 'kitchen-2400367_1280.jpg', 'file', '2024-01-18 11:49:34.137789', 3),
       (13, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--GIpy9YEA--/v1779900744/category/kitchen_cl2alt.jpg',
        404645, 'image/jpeg', 'kitchen-2400367_1280.jpg', 'file', '2024-01-18 11:49:42.317863', 4),
       (14, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--XyVlLWmn--/v1779900734/category/kam-idris_ukjulk.jpg',
        41903, 'image/jpeg', 'kam-idris-Ot2iTXgC6fY-unsplash.jpg', 'file', '2024-01-18 11:49:50.354653', 4),
       (15, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--tsLntK66--/v1779900727/category/jason-briscoe_cf1ybc.jpg',
        98519, 'image/jpeg', 'jason-briscoe-AQl-J19ocWE-unsplash.jpg', 'file', '2024-01-18 11:49:56.108898', 4),
       (16, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--JCoyGO52--/v1779900710/category/interior_dbvlu7.jpg',
        383809, 'image/jpeg', 'interior-4226020_1920.jpg', 'file', '2024-01-18 11:50:03.631472', 5),
       (17, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--tsLntK66--/v1779900727/category/jason-briscoe_cf1ybc.jpg',
        136314, 'image/jpeg', 'jason-briscoe-UV81E0oXXWQ-unsplash.jpg', 'file', '2024-01-18 11:50:09.963493', 5),
       (18, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--QGNS1n5C--/v1779900751/category/marvin-meyer_expok1.jpg',
        73420, 'image/jpeg', 'marvin-meyer-cjhuXRtRT0Y-unsplash.jpg', 'file', '2024-01-18 11:50:16.103475', 5),
       (19, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--GIpy9YEA--/v1779900744/category/kitchen_cl2alt.jpg',
        404645, 'image/jpeg', 'kitchen-2400367_1280.jpg', 'file', '2024-01-18 11:50:22.878112', 6),
       (20, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--tsLntK66--/v1779900727/category/jason-briscoe_cf1ybc.jpg',
        136314, 'image/jpeg', 'jason-briscoe-UV81E0oXXWQ-unsplash.jpg', 'file', '2024-01-18 11:50:30.138927', 6),
       (21, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--Y2b9qCyh--/v1779900758/category/r-architecture_e8rpol.jpg',
        68699, 'image/jpeg', 'r-architecture-T6d96Qrb5MY-unsplash.jpg', 'file', '2024-01-18 11:50:36.769476', 6),
       (22, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--H7lfL1RW--/v1779900644/category/6_w2rmvt.jpg',
        116661, 'image/jpeg', '6.jpg', 'file', '2024-01-18 11:51:41.911251', 7),
       (23, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--qROZ8mGp--/v1779900651/category/7_ukdtbg.jpg',
        437900, 'image/jpeg', '7.jpg', 'file', '2024-01-18 11:52:25.570154', 8),
       (24, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--k6EqxLdt--/v1779900660/category/8_yxvqcz.jpg',
        255897, 'image/jpeg', '8.jpg', 'file', '2024-01-18 11:53:33.110872', 9),
       (25, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--s1A59Ewt--/v1779900685/category/9_vhtkac.jpg',
        126285, 'image/jpeg', '9.jpg', 'file', '2024-01-18 11:54:38.101611', 10),
       (26, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--kYbyahKj--/v1779900692/category/10_don69g.jpg',
        199447, 'image/jpeg', '10.jpg', 'file', '2024-01-18 11:55:28.667336', 11),
       (27, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--zEZiHewL--/v1779900701/category/cameron_cv76q2.jpg',
        51166, 'image/jpeg', 'cameron-smith-3gMTVySU4rs-unsplash.jpg', 'file', '2024-01-18 11:55:42.352325', 11),
       (28, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--JCoyGO52--/v1779900710/category/interior_dbvlu7.jpg',
        383809, 'image/jpeg', 'interior-4226020_1920.jpg', 'file', '2024-01-18 11:55:50.324175', 11),
       (29, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--tsLntK66--/v1779900727/category/jason-briscoe_cf1ybc.jpg',
        98519, 'image/jpeg', 'jason-briscoe-AQl-J19ocWE-unsplash.jpg', 'file', '2024-01-18 11:55:57.369617', 11),
       (30, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--tsLntK66--/v1779900727/category/jason-briscoe_cf1ybc.jpg',
        136314, 'image/jpeg', 'jason-briscoe-UV81E0oXXWQ-unsplash.jpg', 'file', '2024-01-18 11:56:07.498358', 10),
       (31, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--XyVlLWmn--/v1779900734/category/kam-idris_ukjulk.jpg',
        41903, 'image/jpeg', 'kam-idris-Ot2iTXgC6fY-unsplash.jpg', 'file', '2024-01-18 11:56:14.092637', 10),
       (32, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--GIpy9YEA--/v1779900744/category/kitchen_cl2alt.jpg',
        404645, 'image/jpeg', 'kitchen-2400367_1280.jpg', 'file', '2024-01-18 11:56:21.128522', 10),
       (33, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--Y2b9qCyh--/v1779900758/category/r-architecture_e8rpol.jpg',
        68699, 'image/jpeg', 'r-architecture-T6d96Qrb5MY-unsplash.jpg', 'file', '2024-01-18 11:56:29.788420', 9),
       (34, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--QGNS1n5C--/v1779900751/category/marvin-meyer_expok1.jpg',
        73420, 'image/jpeg', 'marvin-meyer-cjhuXRtRT0Y-unsplash.jpg', 'file', '2024-01-18 11:56:36.772649', 9),
       (35, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--GIpy9YEA--/v1779900744/category/kitchen_cl2alt.jpg',
        404645, 'image/jpeg', 'kitchen-2400367_1280.jpg', 'file', '2024-01-18 11:56:43.726443', 9),
       (36, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--tsLntK66--/v1779900727/category/jason-briscoe_cf1ybc.jpg',
        136314, 'image/jpeg', 'jason-briscoe-UV81E0oXXWQ-unsplash.jpg', 'file', '2024-01-18 11:56:52.695448', 8),
       (37, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--JCoyGO52--/v1779900710/category/interior_dbvlu7.jpg',
        383809, 'image/jpeg', 'interior-4226020_1920.jpg', 'file', '2024-01-18 11:56:59.069478', 8),
       (38, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--zEZiHewL--/v1779900701/category/cameron_cv76q2.jpg',
        51166, 'image/jpeg', 'cameron-smith-3gMTVySU4rs-unsplash.jpg', 'file', '2024-01-18 11:57:06.283476', 8),
       (39, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--XyVlLWmn--/v1779900734/category/kam-idris_ukjulk.jpg',
        41903, 'image/jpeg', 'kam-idris-Ot2iTXgC6fY-unsplash.jpg', 'file', '2024-01-18 11:57:14.922517', 7),
       (40, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--zEZiHewL--/v1779900701/category/cameron_cv76q2.jpg',
        51166, 'image/jpeg', 'cameron-smith-3gMTVySU4rs-unsplash.jpg', 'file', '2024-01-18 11:57:21.589526', 7),
       (41, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--GIpy9YEA--/v1779900744/category/kitchen_cl2alt.jpg',
        404645, 'image/jpeg', 'kitchen-2400367_1280.jpg', 'file', '2024-01-18 11:57:28.211796', 7),
       (42, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--VA3LlSJv--/v1779900181/category/1_rafxqc.jpg',
        338794, 'image/jpeg', '1.jpg', 'file', '2024-02-27 15:53:20.907823', 2),
       (43, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--kYbyahKj--/v1779900692/category/10_don69g.jpg',
        199447, 'image/jpeg', '10.jpg', 'file', '2024-02-27 15:55:00.800476', 2),
       (44, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--VA3LlSJv--/v1779900181/category/1_rafxqc.jpg',
        338794, 'image/jpeg', '1.jpg', 'file', '2024-02-27 15:55:02.590882', 2),
       (45, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--e7qB1FSi--/v1779900362/category/2_w7spsw.jpg',
        323433, 'image/jpeg', '2.jpg', 'file', '2024-02-27 15:55:04.335627', 2),
       (46, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--PxtAnsHC--/v1779900507/category/3_rwkzqu.jpg',
        232117, 'image/jpeg', '3.jpg', 'file', '2024-02-27 15:55:06.540454', 2),
       (47, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--B3BavI87--/v1779900545/category/4_atapsu.jpg',
        195532, 'image/jpeg', '4.jpg', 'file', '2024-02-27 15:55:08.476636', 2),
       (48, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--wciIsf_U--/v1779900637/category/5_uosgms.jpg',
        110221, 'image/jpeg', '5.jpg', 'file', '2024-02-27 15:55:09.913547', 2),
       (49, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--H7lfL1RW--/v1779900644/category/6_w2rmvt.jpg',
        116661, 'image/jpeg', '6.jpg', 'file', '2024-02-27 15:55:12.175422', 2),
       (50, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--qROZ8mGp--/v1779900651/category/7_ukdtbg.jpg',
        437900, 'image/jpeg', '7.jpg', 'file', '2024-02-27 15:55:14.213991', 2),
       (51, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--k6EqxLdt--/v1779900660/category/8_yxvqcz.jpg',
        255897, 'image/jpeg', '8.jpg', 'file', '2024-02-27 15:55:16.363556', 2),
       (52, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--s1A59Ewt--/v1779900685/category/9_vhtkac.jpg',
        126285, 'image/jpeg', '9.jpg', 'file', '2024-02-27 15:55:18.104912', 2),
       (53, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--zEZiHewL--/v1779900701/category/cameron_cv76q2.jpg',
        51166, 'image/jpeg', 'cameron.jpg', 'file', '2024-02-27 15:55:19.536363', 2),
       (54, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--JCoyGO52--/v1779900710/category/interior_dbvlu7.jpg',
        383809, 'image/jpeg', 'interior.jpg', 'file', '2024-02-27 15:55:21.178807', 2),
       (55, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--tsLntK66--/v1779900727/category/jason-briscoe_cf1ybc.jpg',
        136314, 'image/jpeg', 'jason-briscoe.jpg', 'file', '2024-02-27 15:55:22.713127', 2),
       (56, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--jalZZJ5n--/v1779900719/category/jason_epvq8w.jpg',
        98519, 'image/jpeg', 'jason.jpg', 'file', '2024-02-27 15:55:24.147048', 2),
       (57, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--XyVlLWmn--/v1779900734/category/kam-idris_ukjulk.jpg',
        41903, 'image/jpeg', 'kam-idris.jpg', 'file', '2024-02-27 15:55:25.483709', 2),
       (58, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--GIpy9YEA--/v1779900744/category/kitchen_cl2alt.jpg',
        404645, 'image/jpeg', 'kitchen.jpg', 'file', '2024-02-27 15:55:27.320153', 2),
       (59, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--QGNS1n5C--/v1779900751/category/marvin-meyer_expok1.jpg',
        73420, 'image/jpeg', 'marvin-meyer.jpg', 'file', '2024-02-27 15:55:28.857712', 2),
       (60, 'proHouse',
        'https://res.cloudinary.com/dsuglujz7/image/authenticated/s--Y2b9qCyh--/v1779900758/category/r-architecture_e8rpol.jpg',
        68699, 'image/jpeg', 'r-architecture.jpg', 'file', '2024-02-27 15:55:30.597622', 2);
/*!40000 ALTER TABLE `file_registry` ENABLE KEYS */;
UNLOCK
TABLES;
DROP TABLE IF EXISTS `property`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `property`
(
    `id`              bigint NOT NULL AUTO_INCREMENT,
    `condition_type`  enum('NEWLY_BUILT','AVERAGE','RENOVATED','NEEDS_RENOVATION') DEFAULT NULL,
    `date_created`    date   DEFAULT NULL,
    `description`     text,
    `heating_type`    enum('FLOOR_HEATING','GAS','CONVECTOR') DEFAULT NULL,
    `is_deleted`      bit(1) DEFAULT NULL,
    `number_of_baths` int    DEFAULT NULL,
    `number_of_rooms` int    DEFAULT NULL,
    `price`           int    DEFAULT NULL,
    `property_type`   enum('HOUSE','FLAT','LOT') DEFAULT NULL,
    `sale_type`       enum('SELL','RENT') DEFAULT NULL,
    `square_meter`    int    DEFAULT NULL,
    `year_built`      int    DEFAULT NULL,
    `user_id`         bigint DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY               `FKo76rpd66l7rdheheo63pmpmy5` (`user_id`),
    CONSTRAINT `FKo76rpd66l7rdheheo63pmpmy5` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK
TABLES `property` WRITE;
/*!40000 ALTER TABLE `property` DISABLE KEYS */;
INSERT INTO `property`
VALUES (2, 'NEWLY_BUILT', '2024-01-18',
        'Eladó Lakás a Belváros Szívében\nModern stílusú, harmadik emeleti lakás eladó a város szívében. A tágas nappali és az ablakokból áradó természetes fény teszik otthonossá ezt az ingatlant. A környék kiváló infrastruktúrával rendelkezik, éttermek és üzletek csak pár perc sétára találhatók. Az ideális választás azoknak, akik kényelmes és vibráló belvárosi életre vágynak.',
        'FLOOR_HEATING', NULL, 3, 5, 65000000, 'HOUSE', 'SELL', 90, 2000, 4),
       (3, 'RENOVATED', '2024-01-18',
        'Eladó Családi Ház Zöldövezeti Környezetben\nEgy varázslatos kertes családi ház várja új tulajdonosát csendes környéken. Az otthon két emeletén összesen négy hálószoba és tágas nappali található. A kertben gyümölcsfák és virágok teszik még hangulatosabbá a környezetet. A közelben iskola és játszótér is könnyedén elérhető, így ideális választás családoknak.',
        'CONVECTOR', NULL, 2, 4, 80000000, 'HOUSE', 'SELL', 80, 1995, 2),
       (4, 'RENOVATED', '2024-01-18',
        'Eladó Családi Ház Frekventált Környéken\nCsaládi ház eladó frekventált helyen a város központjában. A tágas belső tér és a nagy kirakatok lehetőséget teremtenek a kreatív elrendezésre és családi együtt töltött időre. Az ingatlan ideális választás nagycsaládosoknak, akik szeretnék kihasználni a hely adta lehetőségeket.',
        'GAS', NULL, 2, 4, 52000000, 'FLAT', 'SELL', 60, 2005, 3),
       (5, 'RENOVATED', '2024-01-18',
        'Eladó Családi Ház Frekventált Környéken\nCsaládi ház eladó frekventált helyen a város központjában. A tágas belső tér és a nagy kirakatok lehetőséget teremtenek a kreatív elrendezésre és családi együtt töltött időre. Az ingatlan ideális választás nagycsaládosoknak, akik szeretnék kihasználni a hely adta lehetőségeket.',
        'CONVECTOR', NULL, 4, 5, 92000000, 'HOUSE', 'SELL', 110, 1976, 1),
       (6, 'AVERAGE', '2024-01-18',
        'Eladó Lakás a Belváros Szívében\nModern stílusú, harmadik emeleti lakás eladó a város szívében. A tágas nappali és az ablakokból áradó természetes fény teszik otthonossá ezt az ingatlant. A környék kiváló infrastruktúrával rendelkezik, éttermek és üzletek csak pár perc sétára találhatók. Az ideális választás azoknak, akik kényelmes és vibráló belvárosi életre vágynak.',
        'GAS', NULL, 3, 5, 77000000, 'HOUSE', 'SELL', 70, 1998, 2),
       (7, 'RENOVATED', '2024-01-18',
        'Kiadó Stúdiólakás a Trendi Környéken\nFiataloknak és egyedülállóknak ideális stúdiólakás kiadó a város trendi negyedében. A modern konyha és fürdőszoba praktikus és stílusos. Az ingatlan közelében találhatók kávézók, butikok és művészeti galériák, így az itt lakók mindig élénk és inspiráló környezetben lehetnek.',
        'CONVECTOR', NULL, 2, 3, 250000, 'HOUSE', 'RENT', 50, 2006, 3),
       (8, 'NEEDS_RENOVATION', '2024-01-18',
        'Kiadó Panorámás Lakás a Hegyek Lábánál\nGyönyörű kilátással rendelkező, modern berendezésű lakás kiadó a hegyek lábánál. A tágas erkélyről lenyűgöző a kilátás a környező tájra. A lakásban két hálószoba és egy kényelmes nappali található. Ideális otthon azoknak, akik szeretik a természet közelségét, de nem akarnak lemondani a városi kényelemről.',
        'CONVECTOR', NULL, 2, 4, 200000, 'HOUSE', 'RENT', 50, 1990, 1),
       (9, 'RENOVATED', '2024-01-18',
        'Kiadó Stúdiólakás a Trendi Környéken\nFiataloknak és egyedülállóknak ideális stúdiólakás kiadó a város trendi negyedében. A modern konyha és fürdőszoba praktikus és stílusos. Az ingatlan közelében találhatók kávézók, butikok és művészeti galériák, így az itt lakók mindig élénk és inspiráló környezetben lehetnek.',
        'CONVECTOR', NULL, 1, 4, 180000, 'FLAT', 'RENT', 70, 1988, 2),
       (10, 'RENOVATED', '2024-01-18',
        'Kiadó Panorámás Lakás a Hegyek Lábánál\nGyönyörű kilátással rendelkező, modern berendezésű lakás kiadó a hegyek lábánál. A tágas erkélyről lenyűgöző a kilátás a környező tájra. A lakásban két hálószoba és egy kényelmes nappali található. Ideális otthon azoknak, akik szeretik a természet közelségét, de nem akarnak lemondani a városi kényelemről.',
        'FLOOR_HEATING', NULL, 4, 5, 280000, 'HOUSE', 'RENT', 80, 1970, 3),
       (11, 'AVERAGE', '2024-01-18',
        'Kiadó Stúdiólakás a Trendi Környéken\nFiataloknak és egyedülállóknak ideális stúdiólakás kiadó a város trendi negyedében. A modern konyha és fürdőszoba praktikus és stílusos. Az ingatlan közelében találhatók kávézók, butikok és művészeti galériák, így az itt lakók mindig élénk és inspiráló környezetben lehetnek.',
        'CONVECTOR', NULL, 2, 4, 240000, 'HOUSE', 'RENT', 60, 1991, 1);
/*!40000 ALTER TABLE `property` ENABLE KEYS */;
UNLOCK
TABLES;
DROP TABLE IF EXISTS `property_features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `property_features`
(
    `property_id` bigint NOT NULL,
    `features`    enum('GARAGE','GARDEN','BALCONY','BASEMENT','AIR_CONDITIONER') DEFAULT NULL,
    KEY           `FK1fl54bdsb4eiul3516fkmdc4t` (`property_id`),
    CONSTRAINT `FK1fl54bdsb4eiul3516fkmdc4t` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK
TABLES `property_features` WRITE;
/*!40000 ALTER TABLE `property_features` DISABLE KEYS */;
INSERT INTO `property_features`
VALUES (2, 'GARAGE'),
       (2, 'BASEMENT'),
       (3, 'BALCONY'),
       (3, 'BASEMENT'),
       (4, 'BALCONY'),
       (4, 'AIR_CONDITIONER'),
       (5, 'GARDEN'),
       (5, 'BALCONY'),
       (6, 'GARAGE'),
       (6, 'AIR_CONDITIONER'),
       (7, 'BALCONY'),
       (7, 'BASEMENT'),
       (8, 'BALCONY'),
       (9, 'GARDEN'),
       (9, 'BASEMENT'),
       (10, 'GARDEN'),
       (10, 'BALCONY'),
       (10, 'BASEMENT'),
       (10, 'AIR_CONDITIONER'),
       (11, 'BALCONY'),
       (11, 'BASEMENT');
/*!40000 ALTER TABLE `property_features` ENABLE KEYS */;
UNLOCK
TABLES;
DROP TABLE IF EXISTS `user_entity_user_role_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_entity_user_role_list`
(
    `user_entity_id` bigint NOT NULL,
    `role`           enum('ROLE_USER','ROLE_ADMIN') DEFAULT NULL,
    KEY              `FK5rm21xavcdxo243kjgjrb0we7` (`user_entity_id`),
    CONSTRAINT `FK5rm21xavcdxo243kjgjrb0we7` FOREIGN KEY (`user_entity_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK
TABLES `user_entity_user_role_list` WRITE;
/*!40000 ALTER TABLE `user_entity_user_role_list` DISABLE KEYS */;
INSERT INTO `user_entity_user_role_list`
VALUES (1, 'ROLE_USER'),
       (2, 'ROLE_USER'),
       (3, 'ROLE_USER'),
       (4, 'ROLE_USER');
/*!40000 ALTER TABLE `user_entity_user_role_list` ENABLE KEYS */;
UNLOCK
TABLES;
DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users`
(
    `id`           bigint NOT NULL AUTO_INCREMENT,
    `email`        varchar(255) DEFAULT NULL,
    `first_name`   varchar(255) DEFAULT NULL,
    `last_name`    varchar(255) DEFAULT NULL,
    `password`     varchar(255) DEFAULT NULL,
    `phone_number` varchar(255) DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `UK_6dotkott2kjsp8vw4d0m25fb7` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK
TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users`
VALUES (1, 'test1@test.hu', 'Dora', 'Kozics', '$2a$10$M0ilenxACv7UREuBxN6X3.jpptKasU57BJhRTc86xT75sUKO3Ut3i', '+36301112222'),
       (2, 'test2@test.hu', 'Imre', 'Kovács', '$2a$10$OMUjOKaFFfkURK.wpUXuxeURRIp2QPNKHCRSQnB6DvcNVSYFpE2Sq', '+36301122222'),
       (3, 'test3@test.hu', 'Csanád', 'Révész', '$2a$10$B1cGfFQTDUSI2CpQQH6D3OwsuDajPYqbXfUrxNMtYrwpudqUwbRXy', '+36301222222'),
       (4, 'teszt4@test.hu', 'Béla', 'Nagy', '$2a$10$LhLJRj9nCIiBVrUbSFX0nusnPflTUwkcwMjE7n9VlqVtyQKwEX8v6', '+1 (124) 794-9011');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK
TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

