-- MySQL dump 10.13  Distrib 5.5.47, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: guynesher123
-- ------------------------------------------------------
-- Server version	5.5.47-0ubuntu0.14.04.1-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gb_follows`
--

DROP TABLE IF EXISTS `gb_follows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gb_follows` (
  `author_id` int(11) unsigned NOT NULL DEFAULT '0',
  `last_tweet_follow` datetime DEFAULT NULL,
  PRIMARY KEY (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gb_retweets`
--

DROP TABLE IF EXISTS `gb_retweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gb_retweets` (
  `tweet_id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `tweet_text` text COLLATE utf8mb4_unicode_ci,
  `tweet_time` datetime DEFAULT NULL,
  `author_id` bigint(20) unsigned DEFAULT NULL,
  `status` int(1) DEFAULT '0',
  `time_zone` text CHARACTER SET utf8,
  `error` text CHARACTER SET utf8,
  `location` text CHARACTER SET utf8,
  `url` text CHARACTER SET utf8,
  PRIMARY KEY (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gn_follows`
--

DROP TABLE IF EXISTS `gn_follows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gn_follows` (
  `author_id` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `last_tweet_follow` datetime DEFAULT NULL,
  PRIMARY KEY (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gn_retweets`
--

DROP TABLE IF EXISTS `gn_retweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gn_retweets` (
  `tweet_id` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `tweet_text` text COLLATE utf8mb4_unicode_ci,
  `tweet_time` datetime DEFAULT NULL,
  `author_id` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` int(1) DEFAULT '0',
  `time_zone` text CHARACTER SET utf8,
  `error` text CHARACTER SET utf8,
  `location` text CHARACTER SET utf8,
  `url` text CHARACTER SET utf8,
  `poller` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vd_follows`
--

DROP TABLE IF EXISTS `vd_follows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vd_follows` (
  `author_id` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `last_tweet_follow` datetime DEFAULT NULL,
  PRIMARY KEY (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vd_retweets`
--

DROP TABLE IF EXISTS `vd_retweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vd_retweets` (
  `tweet_id` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `tweet_text` text COLLATE utf8mb4_unicode_ci,
  `tweet_time` datetime DEFAULT NULL,
  `author_id` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` int(1) DEFAULT '0',
  `time_zone` text CHARACTER SET utf8,
  `error` text CHARACTER SET utf8,
  `location` text CHARACTER SET utf8,
  `url` text CHARACTER SET utf8,
  `poller` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-25 10:37:30
