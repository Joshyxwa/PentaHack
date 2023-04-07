-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: speechedtech
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `Passage` text,
  `Level` text,
  `Difficulty` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES ('Once upon a time, a little mouse named Max found a shiny red apple. He nibbled and nibbled until he had eaten the whole thing. But then he realized he was lost! Max looked around and saw a friendly owl who helped him find his way home. The end.','Kindergarten','Easy'),('Once upon a time, in a far-off land, there was a magical tree. The tree could talk and it would grant wishes to anyone who asked. One day, a brave little girl named Lily came to the tree and wished for a special adventure. The tree granted her wish, and Lily went on a wonderful journey full of fun and excitement. The end.','Kindergarten','Medium'),('Once upon a time, there was a little rabbit named Benny. One day, while playing in the forest, Benny got lost. But then he met a wise owl who showed him the way home. Benny was grateful and never forgot the owl\'s kindness. The end.','Kindergarten','Hard'),('Lily the lamb lost her way, But found her family the very next day, They hugged her tight and showed her love, And Lily knew she was home, safe and snug, Happily bleating, in the meadow she\'d roam.','Kindergarten','Easy'),('Tommy the turtle was very slow, But he won the race, you know, By taking one step at a time, He reached the finish line just fine, Proving that slow and steady wins the race every time.','Kindergarten','Hard'),('In the small town of Millfield, there was a young boy named Alex who loved to explore the nearby woods. One day, while wandering through the woods, he stumbled upon an old, abandoned cabin. Curiosity getting the best of him, Alex ventured inside and discovered a mysterious book hidden in a dusty old chest. As he began to read the book, he realized that it contained powerful magic spells that he could use to change the world. But he also learned that with great power comes great responsibility, and he had to be careful with how he used it. From that day on, Alex worked hard to become a skilled wizard, using his powers to help those in need and make the world a better place. The end.','Secondary','Easy'),('At the age of 16, Sarah had already made a name for herself as a talented computer programmer. But one day, she received a mysterious message on her computer, challenging her to participate in a worldwide hacking competition. Sarah accepted the challenge and soon found herself competing against the best hackers from around the world. Despite facing numerous challenges and setbacks, Sarah refused to give up and continued to work tirelessly on her code. In the end, she emerged as the winner of the competition, earning respect and admiration from the entire hacking community. Sarah realized that sometimes the greatest rewards come from taking risks and pushing beyond your limits. The end.','Secondary','Medium'),('n the bustling city of New York, there was a young girl named Lily who had always dreamed of becoming a famous singer. One day, she stumbled upon a flyer advertising a singing competition, with the grand prize being a record deal and a chance to perform on stage in front of thousands of people. Despite her nerves, Lily decided to audition for the competition, pouring her heart and soul into her performance. Weeks later, she received the news that she had won the competition and would soon be living out her dream. As she took the stage on the big night, Lily looked out at the crowd and smiled, knowing that anything was possible if she believed in herself. The end.','Secondary','Hard'),('In a small town, everyone knew Samantha\'s name, For her passion for music was her claim to fame, But despite her talent, she faced many hurdles, With perseverance and hard work, she overcame these troubles, And now she performs on stages all around the world.','Secondary','Easy'),('In the small town of Maplewood, there lived a girl named Lily, Her love for science was fierce, it made her feel silly, But she never let anyone dim her light, She worked hard every day and studied late into the night, With perseverance and dedication, she became a top scientist, And her inventions changed the world, making it more efficient, Lily proved that passion and hard work can make dreams come true, And that even a small-town girl can change the world, with a breakthrough.','Secondary','Hard'),('Once upon a time, there was a little boy named Max who loved to play outside. One day, while exploring the woods near his home, Max came across a small, injured bird. Feeling sorry for the bird, Max carefully picked it up and brought it home. He made a cozy nest for the bird and fed it until it was strong enough to fly away. From that day on, Max loved taking care of animals and promised to always be kind to them. The end.','Primary','Easy'),('Once upon a time, there was a little bird named Tweetie who had always dreamed of flying to the moon. One night, she noticed a bright, shining star in the sky and decided to follow it all the way to the moon. With each flap of her wings, Tweetie got closer and closer to her goal. Finally, after many long hours of flying, she arrived on the surface of the moon. As she looked out at the stars from her new home, Tweetie felt proud and accomplished, knowing that anything was possible if she believed in herself. The end.','Primary','Medium'),('In the green fields of Buttercup Valley, there lived a curious little lamb named Larry. One day, while playing with his friends, Larry noticed a bright, shiny object in the distance. Curiosity getting the better of him, he trotted over to investigate, and discovered that it was a magical treasure chest. Excited to see what was inside, Larry used all his strength to open the chest and found that it was filled with sparkling jewels and golden coins. Overwhelmed with joy, Larry shared his treasure with all his friends, and together they had a great feast and danced under the stars. From that day on, Larry and his friends knew that even the smallest and most unexpected things could bring great happiness. The end.','Primary','Hard'),('Once upon a time, there was a curious little mouse. One day, the mouse went on an adventure to find some cheese. On the way, the mouse met a friendly cat who showed him the way. Together, they found a big block of cheese and shared it happily. The end.','Primary','Easy '),('2 / 2  Once upon a time, in a land far away, A little rabbit named Benny loved to play, One day he met a friendly little mouse, Together they explored the forest, house to house, And so their adventures began, full of fun and play.','Primary','Hard');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-07 20:38:52
