-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 26/10/2023 às 15:39
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `estoque_db`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `acesso`
--

CREATE TABLE `acesso` (
  `id` int(11) NOT NULL,
  `ip` varchar(255) NOT NULL,
  `data_acesso` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `acesso`
--

INSERT INTO `acesso` (`id`, `ip`, `data_acesso`) VALUES
(2, '127.0.0.1', '2023-10-03 22:32:55'),
(3, '127.0.0.1', '2023-10-03 22:33:23'),
(4, '127.0.0.1', '2023-10-03 22:34:36'),
(5, '127.0.0.1', '2023-10-04 03:00:00'),
(6, '', '2023-10-01 03:00:00'),
(7, '', '2023-10-02 03:00:00'),
(8, '', '2023-10-05 03:00:00'),
(9, '', '2023-10-04 03:00:00'),
(10, '127.0.0.1', '2023-10-04 11:23:24'),
(11, '127.0.0.1', '2023-10-06 22:22:41'),
(12, '127.0.0.1', '2023-10-10 13:23:31');

-- --------------------------------------------------------

--
-- Estrutura para tabela `produtos`
--

CREATE TABLE `produtos` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `marca` varchar(255) NOT NULL,
  `preco_compra` decimal(10,2) NOT NULL,
  `preco_venda` decimal(10,2) NOT NULL,
  `data_compra` date NOT NULL,
  `quantidade_estoque` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `produtos`
--

INSERT INTO `produtos` (`id`, `nome`, `marca`, `preco_compra`, `preco_venda`, `data_compra`, `quantidade_estoque`) VALUES
(11, 'mermoria RAM 8 GB', 'Kingston', 150.00, 190.00, '2023-09-15', 10),
(12, 'processador i7 11° geração', 'Intel', 650.00, 800.00, '2023-09-27', 5),
(13, 'SSD 1 TB', 'Star Disk', 359.00, 410.00, '2023-08-16', 8),
(14, 'SSD 512 GB ', 'Kingston', 410.00, 450.00, '2023-07-11', 8),
(15, 'Gabinete', 'giga byte', 245.00, 345.00, '2023-10-01', 3),
(16, 'Gabinete v2', 'giga byte', 260.00, 350.00, '2023-10-01', 3),
(19, 'notbook', 'positivo', 2300.00, 3200.00, '2023-09-01', 0),
(33, 'lampada', 'led', 4.00, 8.00, '2023-10-02', 100),
(34, 'shampoo', 'dove', 18.00, 25.00, '2023-08-22', 10),
(35, 'Secador de cabelo', 'Taiff', 200.00, 400.00, '2023-10-02', 6),
(36, 'horst', 'dell', 3500.00, 5500.00, '2023-10-19', 4),
(37, 'teclado', 'seila', 125.00, 158.00, '2023-06-01', 12),
(38, 'Modem ', 'D-link', 100.00, 145.00, '2023-10-03', 5);

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `usuario` varchar(55) NOT NULL,
  `senha` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `senha`) VALUES
(1, 'horst', 'horst');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `acesso`
--
ALTER TABLE `acesso`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `acesso`
--
ALTER TABLE `acesso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
