CREATE DATABASE  IF NOT EXISTS `dojos_and_ninjas_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dojos_and_ninjas_schema`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: dojos_and_ninjas_schema
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `ninjas`
--

DROP TABLE IF EXISTS `ninjas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ninjas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dojo_id` int NOT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ninjas_dojos_idx` (`dojo_id`),
  CONSTRAINT `fk_ninjas_dojos` FOREIGN KEY (`dojo_id`) REFERENCES `dojos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ninjas`
--

LOCK TABLES `ninjas` WRITE;
/*!40000 ALTER TABLE `ninjas` DISABLE KEYS */;
INSERT INTO `ninjas` VALUES (2,1,'Bob','Evans',45,'2024-03-13 10:40:17','2024-03-13 10:40:17'),(3,2,'Bob','Dudeman',40,'2024-03-13 10:40:17','2024-03-13 10:40:17'),(4,2,'Rod','Johnson',28,'2024-03-13 10:40:17','2024-03-13 10:40:17'),(5,3,'Mark','Butler',34,'2024-03-13 10:40:17','2024-03-13 10:40:17'),(6,1,'Cletus','Butkus',52,'2024-03-13 10:40:17','2024-03-13 10:40:17'),(7,3,'Roman','Reigns',39,'2024-03-13 10:42:45','2024-03-13 10:42:45'),(8,1,'Dick','Butkus',78,'2024-03-14 15:55:22','2024-03-14 15:55:22'),(9,6,'Testing','Testing',46,'2024-03-14 16:38:42','2024-03-14 16:38:42'),(10,5,'Narciso','Lobo',28,'2024-03-14 16:39:37','2024-03-14 16:39:37'),(11,6,'Wow','It Works',25,'2024-03-14 16:47:02','2024-03-14 16:47:02'),(12,4,'YAAASSSSS','QUEEENNNN',46,'2024-03-14 16:47:26','2024-03-14 16:47:26'),(13,5,'Dojo','Master',70,'2024-03-15 11:28:51','2024-03-15 11:28:51'),(15,2,'Request','Form',77,'2024-03-15 11:31:58','2024-03-15 11:31:58');
/*!40000 ALTER TABLE `ninjas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-15 12:44:29
