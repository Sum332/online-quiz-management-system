-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: defaultdb
-- ------------------------------------------------------
-- Server version	8.0.46

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

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL,
  `option_a` varchar(255) NOT NULL,
  `option_b` varchar(255) NOT NULL,
  `option_c` varchar(255) NOT NULL,
  `option_d` varchar(255) NOT NULL,
  `correct_answer` varchar(1) NOT NULL,
  `quiz_time` int DEFAULT '10',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (2,'Which language is used to create web pages?','python','java','mysql','html','D',10),(3,'Which language is mainly used for styling web pages?','css','java','sql','html','A',10),(4,'Which database are we using in this project?','SQlite','MongoDB','MYsql','Oracle','C',10),(5,'Which framework are we using for the Python backend?','Dinjago','Flask','React','Angular','B',10),(6,'what is the capital of india ?','mumbai','delhi','kolkata','chennai','B',5),(7,'father of nation ?\r\n','gandhi','nehru','bhagt','lokmany','A',5);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz_answers`
--

DROP TABLE IF EXISTS `quiz_answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quiz_answers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `question_id` int NOT NULL,
  `answer` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_answer` (`user_id`,`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz_answers`
--

LOCK TABLES `quiz_answers` WRITE;
/*!40000 ALTER TABLE `quiz_answers` DISABLE KEYS */;
INSERT INTO `quiz_answers` VALUES (1,2,1,'A'),(2,2,2,'D'),(3,2,3,'A'),(4,2,4,'C'),(5,2,5,'B');
/*!40000 ALTER TABLE `quiz_answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz_settings`
--

DROP TABLE IF EXISTS `quiz_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quiz_settings` (
  `id` int NOT NULL,
  `quiz_time` int NOT NULL DEFAULT '10',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz_settings`
--

LOCK TABLES `quiz_settings` WRITE;
/*!40000 ALTER TABLE `quiz_settings` DISABLE KEYS */;
INSERT INTO `quiz_settings` VALUES (1,5);
/*!40000 ALTER TABLE `quiz_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `score` int NOT NULL,
  `total_questions` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `results_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (1,1,1,1),(2,1,5,5),(3,1,5,5),(4,1,5,5),(5,1,5,5),(6,1,5,5),(7,1,0,5),(8,1,0,5),(9,1,0,5),(10,1,0,5),(11,1,5,5),(12,1,5,5),(13,1,5,5),(14,1,4,5),(15,1,5,5),(16,1,4,4),(17,1,4,4),(18,1,4,4),(19,1,4,4),(20,1,4,4),(21,1,4,4),(22,1,2,4),(23,1,4,4),(24,1,4,4),(25,1,6,6),(26,1,6,6);
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(20) DEFAULT 'student',
  `admin_status` varchar(20) DEFAULT 'approved',
  `bio` text,
  `profile_pic` varchar(255) DEFAULT NULL,
  `approval_token` varchar(255) DEFAULT NULL,
  `reset_token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Sumit Jogi','sumit@gmail.com','7028434919','scrypt:32768:8:1$xfhXpZLuYMfgxFnE$a9477bd98bd0a5d7e39790daf51324d987a4148879f884c2a901b279402bd49f62ec7e296ec18e39f1e94107ec85c64e42b0f6d91fc30f2296a1633134ab3c17','student','approved','Computer Science Student','WhatsApp_Image_2026-09-04_at_10.10.54_PM.jpeg',NULL,NULL),(2,'Admin','admin@gmail.com',NULL,'scrypt:32768:8:1$0KMB3epMEclgLAFk$87f88cbc03a7be35ecf9f01ab253ea62afbf73be3f90863c13453136a46429ab6a284169e0b76bc62a50181c1f85fa8b7bef806ece4586e9ee06ce0245c83be3','admin','approved',NULL,NULL,NULL,NULL),(3,'Sumit Balbhim Jogi','sumitjogi330@gmail.com','7028434919','scrypt:32768:8:1$IWl8CIFpvt55p6B2$a6f967913f493b17afc0b73c2698bd9e2262863f47fd5f5e4e72768c447ff2046b13240c81fb797b9bf2ca8fd46be4fcb180d0011636f857b30f8a66b5c469bd','admin','pending',NULL,NULL,NULL,'hfjO5aUfCfYGIolrfmAnzGHugABrJKD6d9TElhNvQS0'),(4,'Sumit Jogi','sumitjogi641+test@gmail.com','1234567890','scrypt:32768:8:1$N1JOrytGWhKK8oEj$f2260de47db7b8d96b1da239861fdce6103cacf1d4e84ad0175d9fc0de8a2b5addac4a9fe94e3469a40aa3c3c304feb4e417a5d9eddbf3e09100fcf870a31adc','admin','rejected',NULL,NULL,NULL,'HQb_vnszj43dD8mYnm1j0iuvWh5BONYVkKMt2lb1iHE'),(6,'Sumit Jogi','sumitjogi641++test@gmail.com','7028434919','scrypt:32768:8:1$3AbxXLjlxfSAebhO$8b2f6baca130d12c3fddc371224ddb9bd79f93421542d9b3b74622228808f3f73d9a293229b5b9f5c91a144157ece27d51740a256941c507dc53bcd0eb5c1f9e','admin','pending',NULL,NULL,NULL,NULL),(8,'Sumit Jogi','sumitjogi641test@gmail.com','7028434919','scrypt:32768:8:1$LDStZfOit4VvCTWE$73e9af55514405da2b40733d836980f02994d4abc73f0130240a860b0466b18528b61814479cf646c1ad922a369ab794a37b8418cf91598f5a8332a6f9bee2d0','admin','rejected',NULL,NULL,NULL,NULL),(10,'Sumit Jogi','sumitjogi330+test@gmail.com','7028434919','scrypt:32768:8:1$AFM5oef1y7vmJIOm$7f577fdc6fb7a30584f3992e8531bd9f88c098eac77b03c04a97847a101d6950be8de2bba2ede69de8d27b1b62d4eebdd7e1883caeac7a184b3fd9fe5df3378f','admin','pending',NULL,NULL,NULL,NULL),(11,'Ayan Maniyar','ayan@gmail.com','1234567880','scrypt:32768:8:1$W6GFoHivmGOJgucP$6ad2d454797890e9f67b2b53ef0fe2a8b843e08d500e0c4186e9c4f19d06f2f2ad167323f8d3d45ade5aac11e9d5eeb0e04e218ff979f08c993552fa0b923d5a','admin','rejected',NULL,NULL,NULL,NULL),(13,'Ayan Maniyar','maniyar@gmail.com','1234567880','scrypt:32768:8:1$t0uEqMhG9ci4T5MZ$691eff8f4baa049ca7419d5fc42bb1cdbdb4770f72e50598b82267fc4e5083ed2784d189c31581edc1c3794a3da9ccfff71e76b3a5e2e994522b012cb61b716d','admin','pending',NULL,NULL,NULL,NULL),(14,'Ayan Maniyar','sumitjogi671@gmial.com','3241516898','scrypt:32768:8:1$s4rwxi9G8m3k4vwi$85ffed107a2078ca4bf95d4264a60e77aa62a9ec120740f843f7b2fd115da5ac95a0f348dde2c3b0c5b948b2d2a19df5691377d473b308cef1440f8469ca0bc6','admin','rejected',NULL,NULL,NULL,NULL),(15,'Rahul Mule','rahul@gmail.com','123456787','scrypt:32768:8:1$8NXQeKgZzvBGPiYV$883da6651b9801e0b7e14f9cee48a12738a210b6d7f51a33e100b26afb08817bfeaf4192fb1f16363c000bfd55ae2e8b8cd21b329f3003848ac40756b8a6abe4','admin','pending',NULL,NULL,NULL,NULL),(16,'Rahul ','rahulm@gmailcom','234567891','scrypt:32768:8:1$dv4HiaCNk6ghbjve$42e8b3e72c8787ad7c9b6c4004dcd632d21c7f2b4dcc1266bd32920951b3ee9f4382855b06697724f8e77eb2f70d55eb52aedb1b54db6c4225da1e43c46614d0','admin','pending',NULL,NULL,NULL,NULL),(17,'Shree','shree@gmail.com','345678912','scrypt:32768:8:1$bIYylV6zMtAeSu14$6fa6a7c0e360da15f7cbf36b20c77cb843d18d879523851c2a8108eebb3b93fcb4d42b1670fce803fba85a3360b00c085f9a3e32bf4af44f2ab4ea27d7f61176','admin','pending',NULL,NULL,NULL,NULL),(19,'Shree','shreedhar@gmail.com','3456782747','scrypt:32768:8:1$GQ5Qkz9G6KJLuS76$0473346ce9702d0b765d5f69040671d0a3ae0aa0dd6119db41db2236e33f7b57fd1c4e7c9f047cccac6c4d4c7f4c22d24acda79bfd64d902533a8fe997ad456a','admin','pending',NULL,NULL,NULL,NULL),(20,'Shree','shreed@gamil.com','1234567899','scrypt:32768:8:1$xzsIBq1bQVSNJODC$f63a591f4f2922a50a6028760a47e30e68e4943d12296d9dd69bcff9216e11265688df84d1cbfe2950840859b4efd59451c04516f9ca18d6449854b3bbeaa767','admin','pending',NULL,NULL,NULL,NULL),(21,'Akshay','ak@gmail.com','1234512345','scrypt:32768:8:1$mTZjHRwmTvF644tA$fa314b9073be4df4d0eda4b7a82a6712cc18a9946047e65d239f27a2dda8c65632814389bad3570047b23f1cddc806209be80150530e3ce464c4bbeefe0b687c','admin','pending',NULL,NULL,NULL,NULL),(22,'Sumit Test','sumitjogi641@gmail.com','1234554321','scrypt:32768:8:1$qKaWNmYztwfVPqZT$a4a7bcb6110cc6df900a7f3d704911870d60cdc8e6ef299ee08abf1f33b7fb6913ad052822c6cd067ab67ce654137775ce1deab7151a261d76b35eaf02509c46','student','approved',NULL,NULL,NULL,NULL),(23,'Om Dangat','omd@gmail.com','1234567890','scrypt:32768:8:1$UauuKjOIjsceXagq$b939958c4eb4e22d7af31c1ab58de263e8ece2c0fee0b753a967c33cf1ca2ed5f809c813dcae2fde2e8828badd0cf78619989d71ac04a92f40d810f8b3be8b16','student','approved',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-18 10:15:59

