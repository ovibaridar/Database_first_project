-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2023 at 05:45 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 5.6.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbms_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `Name` varchar(20) NOT NULL,
  `Batch` int(11) NOT NULL,
  `student_id` varchar(11) NOT NULL,
  `semister` varchar(5) NOT NULL,
  `gender` varchar(7) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `address` varchar(30) NOT NULL,
  `photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`Name`, `Batch`, `student_id`, `semister`, `gender`, `email`, `password`, `address`, `photo`) VALUES
('Toufic Ahammed', 18, '01821106001', '4th', 'Male', 'touficahmed007@gmail.com', '314121214131', 'shibganj,Bogura,Rajshahi', '01821106001toufic.jpg'),
('Abdullah  Al Muksit', 18, '01821106008', '4th', 'Male', 'almuksitsazid@gmail.com', 'almuksitsazid1', 'Gabtoli , Bogura ,Rajshahi', '01821106008muksit.jpg'),
('nayeem islam ', 18, '01821106011', '4th', 'Male', 'povibaridar06@gmail.com', '314121214131', 'Gabtoli , Bogura ,Rajshahi', '01821106011nayeem.jpg'),
('shesheir', 19, '01921206022', '4th', 'Male', 'shesheir@gmail.com', '123456789', 'bogura', '01921206022download.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
