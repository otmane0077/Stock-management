-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 02, 2023 at 02:03 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fmpdf`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `name` varchar(10) DEFAULT NULL,
  `passwd` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `passwd`) VALUES
('a', 'a'),
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `equipement`
--

CREATE TABLE `equipement` (
  `Equipement_ID` int(11) NOT NULL,
  `Nom` varchar(255) DEFAULT NULL,
  `Type_ID` int(11) DEFAULT NULL,
  `Fournisseur_ID` int(11) DEFAULT NULL,
  `QuantiteEntree` int(11) DEFAULT NULL,
  `DateEntree` date DEFAULT NULL,
  `QuantiteSortie` int(11) DEFAULT NULL,
  `QuantiteDispo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `equipement`
--

INSERT INTO `equipement` (`Equipement_ID`, `Nom`, `Type_ID`, `Fournisseur_ID`, `QuantiteEntree`, `DateEntree`, `QuantiteSortie`, `QuantiteDispo`) VALUES
(6, 'Clavier', 32, 211, 100, '0007-11-23', 5, 95),
(7, 'PC_Dell', 1, 4, 50, '0007-11-23', 5, 45),
(8, 'pompes a perfusion', 123, 32, 16, '0008-08-23', 10, 6),
(9, 'Amalgamateur', 142, 32, 3, '0000-00-00', 1, 2),
(10, 'clavier2', 1, 4, 3, '0000-00-00', 0, 3),
(11, 'clavier2', 1, 4, 3, '0000-00-00', 0, 3);

-- --------------------------------------------------------

--
-- Table structure for table `fournisseur`
--

CREATE TABLE `fournisseur` (
  `Fournisseur_ID` int(11) NOT NULL,
  `Nom` varchar(255) DEFAULT NULL,
  `Societe` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fournisseur`
--

INSERT INTO `fournisseur` (`Fournisseur_ID`, `Nom`, `Societe`) VALUES
(4, 'hajar', 'fhajarx'),
(32, 'Zakaria', 'Medica'),
(211, 'Otmane', 'Zhomax');

-- --------------------------------------------------------

--
-- Table structure for table `lieuaffectation`
--

CREATE TABLE `lieuaffectation` (
  `LieuAffectation_ID` int(11) NOT NULL,
  `Nom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lieuaffectation`
--

INSERT INTO `lieuaffectation` (`LieuAffectation_ID`, `Nom`) VALUES
(1, 'FMPDF'),
(2, 'CHU');

-- --------------------------------------------------------

--
-- Table structure for table `service`
--

CREATE TABLE `service` (
  `Service_ID` int(11) NOT NULL,
  `Nom` varchar(255) DEFAULT NULL,
  `ChefService` varchar(255) DEFAULT NULL,
  `LieuAffectation_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service`
--

INSERT INTO `service` (`Service_ID`, `Nom`, `ChefService`, `LieuAffectation_ID`) VALUES
(1, 'Informatique', 'Kamal Berrada', 1),
(2, 'RH', 'ahmad', 1),
(12, 'Chirurgie dentaire', 'Mr.mohammed', 2);

-- --------------------------------------------------------

--
-- Table structure for table `sortie`
--

CREATE TABLE `sortie` (
  `Sortie_ID` int(11) NOT NULL,
  `Equipement_ID` int(11) DEFAULT NULL,
  `QuantiteDonnee` int(11) DEFAULT NULL,
  `LieuAffectation_ID` int(11) DEFAULT NULL,
  `Service_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sortie`
--

INSERT INTO `sortie` (`Sortie_ID`, `Equipement_ID`, `QuantiteDonnee`, `LieuAffectation_ID`, `Service_ID`) VALUES
(5, 7, 5, 1, 1),
(6, 6, 5, 1, 2),
(7, 9, 1, 2, 12),
(8, 8, 10, 2, 12);

-- --------------------------------------------------------

--
-- Table structure for table `type`
--

CREATE TABLE `type` (
  `Type_ID` int(11) NOT NULL,
  `Nom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `type`
--

INSERT INTO `type` (`Type_ID`, `Nom`) VALUES
(1, 'Bureautique'),
(32, 'Technique'),
(123, 'Therapeutique'),
(142, 'Chirurgie_dentaire'),
(332, 'Enseignement');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `equipement`
--
ALTER TABLE `equipement`
  ADD PRIMARY KEY (`Equipement_ID`),
  ADD KEY `Type_ID` (`Type_ID`),
  ADD KEY `Fournisseur_ID` (`Fournisseur_ID`);

--
-- Indexes for table `fournisseur`
--
ALTER TABLE `fournisseur`
  ADD PRIMARY KEY (`Fournisseur_ID`);

--
-- Indexes for table `lieuaffectation`
--
ALTER TABLE `lieuaffectation`
  ADD PRIMARY KEY (`LieuAffectation_ID`);

--
-- Indexes for table `service`
--
ALTER TABLE `service`
  ADD PRIMARY KEY (`Service_ID`),
  ADD KEY `LieuAffectation_ID` (`LieuAffectation_ID`);

--
-- Indexes for table `sortie`
--
ALTER TABLE `sortie`
  ADD PRIMARY KEY (`Sortie_ID`),
  ADD KEY `Equipement_ID` (`Equipement_ID`),
  ADD KEY `LieuAffectation_ID` (`LieuAffectation_ID`),
  ADD KEY `Service_ID` (`Service_ID`);

--
-- Indexes for table `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`Type_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `equipement`
--
ALTER TABLE `equipement`
  MODIFY `Equipement_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `sortie`
--
ALTER TABLE `sortie`
  MODIFY `Sortie_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `equipement`
--
ALTER TABLE `equipement`
  ADD CONSTRAINT `equipement_ibfk_1` FOREIGN KEY (`Type_ID`) REFERENCES `type` (`Type_ID`),
  ADD CONSTRAINT `equipement_ibfk_2` FOREIGN KEY (`Fournisseur_ID`) REFERENCES `fournisseur` (`Fournisseur_ID`);

--
-- Constraints for table `service`
--
ALTER TABLE `service`
  ADD CONSTRAINT `service_ibfk_1` FOREIGN KEY (`LieuAffectation_ID`) REFERENCES `lieuaffectation` (`LieuAffectation_ID`);

--
-- Constraints for table `sortie`
--
ALTER TABLE `sortie`
  ADD CONSTRAINT `sortie_ibfk_1` FOREIGN KEY (`Equipement_ID`) REFERENCES `equipement` (`Equipement_ID`),
  ADD CONSTRAINT `sortie_ibfk_2` FOREIGN KEY (`LieuAffectation_ID`) REFERENCES `lieuaffectation` (`LieuAffectation_ID`),
  ADD CONSTRAINT `sortie_ibfk_3` FOREIGN KEY (`Service_ID`) REFERENCES `service` (`Service_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
