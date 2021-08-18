-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-08-2021 a las 07:28:21
-- Versión del servidor: 10.4.20-MariaDB
-- Versión de PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `conciertos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `artistas`
--

CREATE TABLE `artistas` (
  `id_artista` int(11) NOT NULL,
  `nombre_artista` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `artistas`
--

INSERT INTO `artistas` (`id_artista`, `nombre_artista`) VALUES
(1, 'Queen'),
(2, 'Metallica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletos`
--

CREATE TABLE `boletos` (
  `id_boleto` int(11) NOT NULL,
  `fecha_hora_compra_boleto` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `verificado_boleto` tinyint(1) NOT NULL DEFAULT 0,
  `aceptado_boleto` tinyint(1) NOT NULL DEFAULT 0,
  `id_usuario` int(11) NOT NULL,
  `id_puerta_acceso` int(11) NOT NULL,
  `id_concierto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `boletos`
--

INSERT INTO `boletos` (`id_boleto`, `fecha_hora_compra_boleto`, `verificado_boleto`, `aceptado_boleto`, `id_usuario`, `id_puerta_acceso`, `id_concierto`) VALUES
(1, '2021-08-18 05:18:00', 0, 0, 1, 1, 1),
(2, '2021-08-18 05:18:00', 0, 0, 2, 2, 1),
(3, '2021-08-18 05:22:01', 1, 0, 3, 3, 1),
(32, '2021-08-18 05:22:02', 1, 0, 4, 3, 1),
(33, '2021-08-18 05:21:47', 1, 0, 5, 1, 1),
(34, '2021-08-18 05:18:00', 0, 0, 6, 2, 1),
(35, '2021-08-18 05:21:56', 1, 0, 7, 2, 1),
(36, '2021-08-18 05:18:00', 0, 0, 8, 2, 1),
(37, '2021-08-18 05:18:00', 0, 0, 9, 2, 1),
(38, '2021-08-18 05:18:00', 0, 0, 10, 1, 1),
(39, '2021-08-18 05:18:00', 0, 0, 11, 1, 1),
(40, '2021-08-18 05:18:00', 0, 0, 12, 2, 1),
(41, '2021-08-18 05:18:00', 0, 0, 13, 3, 1),
(42, '2021-08-18 05:22:03', 1, 0, 14, 3, 1),
(43, '2021-08-18 05:18:00', 0, 0, 15, 3, 1),
(44, '2021-08-18 05:21:59', 1, 0, 16, 3, 1),
(45, '2021-08-18 05:22:20', 1, 0, 17, 3, 1),
(46, '2021-08-18 05:21:55', 1, 0, 18, 2, 1),
(47, '2021-08-18 05:21:49', 1, 0, 19, 1, 1),
(48, '2021-08-18 05:18:00', 0, 0, 20, 2, 1),
(49, '2021-08-18 05:21:55', 1, 0, 21, 2, 1),
(50, '2021-08-18 05:21:51', 1, 0, 22, 1, 1),
(51, '2021-08-18 05:22:00', 1, 0, 23, 3, 1),
(52, '2021-08-18 05:21:54', 1, 0, 24, 2, 1),
(53, '2021-08-18 05:21:52', 1, 0, 25, 1, 1),
(54, '2021-08-18 05:18:00', 0, 0, 26, 1, 1),
(55, '2021-08-18 05:18:00', 0, 0, 27, 3, 1),
(56, '2021-08-18 05:18:00', 0, 0, 28, 2, 1),
(57, '2021-08-18 05:18:00', 0, 0, 29, 3, 1),
(58, '2021-08-18 05:21:53', 1, 0, 30, 1, 1),
(59, '2021-08-18 05:21:46', 1, 0, 31, 1, 1),
(60, '2021-08-18 05:18:00', 0, 0, 35, 2, 1),
(61, '2021-08-18 05:22:01', 1, 0, 36, 3, 1),
(62, '2021-08-18 05:21:49', 1, 0, 37, 1, 1),
(63, '2021-08-18 05:22:03', 1, 0, 38, 3, 1),
(64, '2021-08-18 05:18:00', 0, 0, 39, 1, 1),
(65, '2021-08-18 05:21:57', 1, 0, 40, 2, 1),
(66, '2021-08-18 05:18:00', 0, 0, 41, 3, 1),
(67, '2021-08-18 05:21:50', 1, 0, 42, 1, 1),
(68, '2021-08-18 05:18:00', 0, 0, 43, 3, 1),
(69, '2021-08-18 05:21:56', 1, 0, 44, 2, 1),
(70, '2021-08-18 05:18:00', 0, 0, 45, 1, 1),
(71, '2021-08-18 05:21:55', 1, 0, 46, 2, 1),
(72, '2021-08-18 05:21:54', 1, 0, 47, 2, 1),
(73, '2021-08-18 05:18:00', 0, 0, 48, 2, 1),
(74, '2021-08-18 05:18:00', 0, 0, 49, 3, 1),
(75, '2021-08-18 05:18:00', 0, 0, 50, 1, 1),
(76, '2021-08-18 05:22:05', 1, 0, 51, 3, 1),
(77, '2021-08-18 05:21:58', 1, 0, 52, 2, 1),
(78, '2021-08-18 05:21:53', 1, 0, 53, 1, 1),
(79, '2021-08-18 05:18:00', 0, 0, 54, 1, 1),
(80, '2021-08-18 05:22:06', 1, 0, 55, 3, 1),
(81, '2021-08-18 05:18:00', 0, 0, 57, 3, 1),
(82, '2021-08-18 05:18:00', 0, 0, 58, 1, 1),
(83, '2021-08-18 05:22:04', 1, 0, 59, 3, 1),
(84, '2021-08-18 05:18:00', 0, 0, 60, 1, 1),
(85, '2021-08-18 05:18:00', 0, 0, 61, 3, 1),
(86, '2021-08-18 05:18:00', 0, 0, 62, 1, 1),
(87, '2021-08-18 05:18:00', 0, 0, 63, 3, 1),
(88, '2021-08-18 05:21:51', 1, 0, 64, 1, 1),
(89, '2021-08-18 05:21:58', 1, 0, 65, 2, 1),
(90, '2021-08-18 05:22:00', 1, 0, 66, 3, 1),
(91, '2021-08-18 05:18:00', 0, 0, 67, 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `conciertos`
--

CREATE TABLE `conciertos` (
  `id_concierto` int(11) NOT NULL,
  `fecha_hora_concierto` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `id_artista` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `conciertos`
--

INSERT INTO `conciertos` (`id_concierto`, `fecha_hora_concierto`, `id_artista`) VALUES
(1, '2021-08-26 00:30:00', 1),
(2, '2021-08-27 00:30:00', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_concierto`
--

CREATE TABLE `datos_concierto` (
  `id_concierto` int(11) NOT NULL,
  `n_aceptados_p1` int(11) NOT NULL,
  `n_aceptados_p2` int(11) NOT NULL,
  `n_aceptados_p3` int(11) NOT NULL,
  `n_total` int(11) NOT NULL,
  `n_rechazados` int(11) NOT NULL,
  `n_duplicados` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id_empleado` int(11) NOT NULL,
  `nombre_empleado` varchar(50) NOT NULL,
  `apellido_p_empleado` varchar(50) NOT NULL,
  `apellido_m_empleado` varchar(50) NOT NULL,
  `fecha_nac_empleado` varchar(50) NOT NULL,
  `correo_elec_empleado` varchar(50) NOT NULL,
  `password_empleado` varchar(50) NOT NULL,
  `disponible_empleado` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id_empleado`, `nombre_empleado`, `apellido_p_empleado`, `apellido_m_empleado`, `fecha_nac_empleado`, `correo_elec_empleado`, `password_empleado`, `disponible_empleado`) VALUES
(1, 'Samuel', 'Martinez', 'Arenas', '01/01/2000', 'samuel@gmail.com', 'samuel123', 1),
(2, 'Alejandro', 'Rodriguez', 'Velez', '01/01/2000', 'alejandro@gmail.com', 'alejandro123', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puertas_acceso`
--

CREATE TABLE `puertas_acceso` (
  `id_puerta_acceso` int(11) NOT NULL,
  `nombre_puerta_acceso` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `puertas_acceso`
--

INSERT INTO `puertas_acceso` (`id_puerta_acceso`, `nombre_puerta_acceso`) VALUES
(1, 'PUERTA 1'),
(2, 'PUERTA 2'),
(3, 'PUERTA 3');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_clientes`
--

CREATE TABLE `tipos_clientes` (
  `id_tipo_cliente` int(11) NOT NULL,
  `nombre_tipo_cliente` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipos_clientes`
--

INSERT INTO `tipos_clientes` (`id_tipo_cliente`, `nombre_tipo_cliente`) VALUES
(1, 'NORMAL'),
(2, 'PREMIUM');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(50) NOT NULL,
  `apellido_p_usuario` varchar(50) NOT NULL,
  `apellido_m_usuario` varchar(50) NOT NULL,
  `fecha_nac_usuario` varchar(50) NOT NULL,
  `accesso_permitido_usuario` tinyint(1) NOT NULL DEFAULT 1,
  `id_tipo_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre_usuario`, `apellido_p_usuario`, `apellido_m_usuario`, `fecha_nac_usuario`, `accesso_permitido_usuario`, `id_tipo_cliente`) VALUES
(1, 'Samuel', 'Martinez', 'Arenas', '01/01/2000', 1, 1),
(2, 'Alejandro', 'Rodriguez', 'Velez', '01/01/2000', 1, 1),
(3, 'Alberto', 'Tepale', 'Diagas', '01/01/2000', 1, 2),
(4, 'Ramiro', 'Lechuga', 'Ascension', '01/01/2000', 1, 2),
(5, 'Jesus', 'Toxqui', 'Ortega', '01/01/2000', 1, 2),
(6, 'Kevin', 'Paez', 'Gallardo', '01/01/2000', 1, 1),
(7, 'Javier', 'Maldonado', 'Martinez', '01/01/2000', 1, 2),
(8, 'Angela', 'Corona', 'Gonzalez', '01/01/2000', 1, 1),
(9, 'Gudelia Pilar', 'Perez', 'Conde', '01/01/2000', 1, 1),
(10, 'Juan', 'Texca', 'Coto', '01/01/2000', 1, 1),
(11, 'Mariana', 'Baez', 'Perez', '01/01/2000', 1, 1),
(12, 'Martin', 'Rivera', 'Martinez', '01/01/2000', 1, 1),
(13, 'Adrian', 'Rodriguez', 'Flores', '01/01/2000', 1, 1),
(14, 'Ivonne', 'Salazar', 'Rosas', '01/01/2000', 1, 2),
(15, 'Antonio', 'Jimenez', 'Lopez', '01/01/2000', 1, 1),
(16, 'Ximena', 'Ramirez', 'Pardo', '01/01/2000', 1, 2),
(17, 'Areli', 'Hernandez', 'Mendoza', '01/01/2000', 1, 1),
(18, 'Gerardo', 'Lopez', 'Garcia', '01/01/2000', 1, 2),
(19, 'Santiago', 'Mendoza', 'Rodriguez', '01/01/2000', 1, 2),
(20, 'Gabriela', 'Blanca', 'Tome', '01/01/2000', 1, 1),
(21, 'Daniel ', 'Villegas', 'Cruz', '01/01/2000', 1, 2),
(22, 'Joselin', 'Martinez', 'Juarez', '01/01/2000', 1, 2),
(23, 'Andrea', 'Solis', 'Velazquez', '01/01/2000', 1, 2),
(24, 'Mauricio', 'Netza', 'Dominguez', '01/01/2000', 1, 2),
(25, 'Arturo', 'Torres', 'Salinas', '01/01/2000', 1, 2),
(26, 'Lorena', 'Leon', 'Jimenez', '01/01/2000', 1, 1),
(27, 'Azucena', 'Martinez', 'Perez', '01/01/2000', 1, 1),
(28, 'Carolina', 'Rodriguez', 'Flores', '01/01/2000', 1, 1),
(29, 'Lucia', 'Diaz', 'Garcia', '01/01/2000', 1, 1),
(30, 'Fernando', 'Barrera', 'Gutierrez', '01/01/2000', 1, 1),
(31, 'Maria', 'Hernandez', 'Suarez', '01/01/2000', 1, 2),
(32, 'Carlos', 'Suarez', 'Benitez', '01/01/2000', 1, 1),
(33, 'Karina', 'Tellez', 'Vazquez', '01/01/2000', 1, 1),
(34, 'Pedro', 'Hernandez', 'Martinez', '01/01/2000', 1, 1),
(35, 'Marco', 'Perez', 'Juarez', '01/01/2000', 1, 1),
(36, 'Sofia', 'Cardenas', 'Torres', '01/01/2000', 1, 2),
(37, 'Camila', 'Vazquez', 'Garcia', '01/01/2000', 1, 2),
(38, 'Juliana', 'Herrera', 'Soria', '01/01/2000', 1, 2),
(39, 'Laura', 'Escalona', 'Linares', '01/01/2000', 1, 1),
(40, 'Karla', 'Moreno', 'Zamora', '01/01/2000', 1, 2),
(41, 'Sara', 'Olvera', 'Corrales', '01/01/2000', 1, 1),
(42, 'Belen', 'Solano', 'Castro', '01/01/2000', 1, 2),
(43, 'Samantha', 'Baez', 'Baez', '01/01/2000', 1, 1),
(44, 'Miranda', 'Rosales', 'Alarcon', '01/01/2000', 1, 2),
(45, 'Luis', 'Martinez', 'Sanchez', '01/01/2000', 1, 1),
(46, 'Andres', 'Peralta', 'Ochoa', '01/01/2000', 1, 2),
(47, 'Emiliano', 'Fraga', 'Perez', '01/01/2000', 1, 2),
(48, 'Ana', 'Rubio', 'Valencia', '01/01/2000', 1, 1),
(49, 'Fabricio', 'Fuentes', 'Rodriguez', '01/01/2000', 1, 1),
(50, 'Eduardo', 'Arenas', 'Montiel', '01/01/2000', 1, 1),
(51, 'Raquel', 'Sanchez', 'Juarez', '01/01/2000', 1, 1),
(52, 'Francisco', 'Torres', 'Bautista', '01/01/2000', 1, 2),
(53, 'Maribel', 'Dominguez', 'Flores', '01/01/2000', 1, 1),
(54, 'Javier', 'Suarez', 'Diagas', '01/01/2000', 1, 1),
(55, 'Ricardo', 'Tepale', 'Sanchez', '01/01/2000', 1, 1),
(57, 'Melissa', 'Gonzalez', 'Ramos', '01/01/2000', 1, 1),
(58, 'Pedro', 'Paez', 'Santos', '01/01/2000', 1, 1),
(59, 'Pablo', 'Fernandez', 'Flores', '01/01/2000', 1, 2),
(60, 'Juana', 'Mendoza', 'Alcantara', '01/01/2000', 1, 1),
(61, 'Adrian', 'Rosas', 'Perez', '01/01/2000', 1, 1),
(62, 'Rosalia', 'Suarez', 'Tome', '01/01/2000', 1, 1),
(63, 'Guadalupe', 'Torres', 'Aguila', '01/01/2000', 1, 1),
(64, 'Erick', 'Rodriguez', 'Diaz', '01/01/2000', 1, 2),
(65, 'Karen', 'Flores', 'Martinez', '01/01/2000', 1, 2),
(66, 'Teresa', 'Paez', 'Juarez', '01/01/2000', 1, 2),
(67, 'Juan', 'Martinez', 'Perez', '01/01/2000', 1, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `artistas`
--
ALTER TABLE `artistas`
  ADD PRIMARY KEY (`id_artista`);

--
-- Indices de la tabla `boletos`
--
ALTER TABLE `boletos`
  ADD PRIMARY KEY (`id_boleto`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_puerta_acceso` (`id_puerta_acceso`),
  ADD KEY `id_concierto` (`id_concierto`);

--
-- Indices de la tabla `conciertos`
--
ALTER TABLE `conciertos`
  ADD PRIMARY KEY (`id_concierto`),
  ADD KEY `id_artista` (`id_artista`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id_empleado`);

--
-- Indices de la tabla `puertas_acceso`
--
ALTER TABLE `puertas_acceso`
  ADD PRIMARY KEY (`id_puerta_acceso`);

--
-- Indices de la tabla `tipos_clientes`
--
ALTER TABLE `tipos_clientes`
  ADD PRIMARY KEY (`id_tipo_cliente`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `id_tipo_cliente` (`id_tipo_cliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `artistas`
--
ALTER TABLE `artistas`
  MODIFY `id_artista` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `boletos`
--
ALTER TABLE `boletos`
  MODIFY `id_boleto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=92;

--
-- AUTO_INCREMENT de la tabla `conciertos`
--
ALTER TABLE `conciertos`
  MODIFY `id_concierto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `puertas_acceso`
--
ALTER TABLE `puertas_acceso`
  MODIFY `id_puerta_acceso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tipos_clientes`
--
ALTER TABLE `tipos_clientes`
  MODIFY `id_tipo_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `boletos`
--
ALTER TABLE `boletos`
  ADD CONSTRAINT `boletos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `boletos_ibfk_2` FOREIGN KEY (`id_puerta_acceso`) REFERENCES `puertas_acceso` (`id_puerta_acceso`),
  ADD CONSTRAINT `boletos_ibfk_3` FOREIGN KEY (`id_concierto`) REFERENCES `conciertos` (`id_concierto`);

--
-- Filtros para la tabla `conciertos`
--
ALTER TABLE `conciertos`
  ADD CONSTRAINT `conciertos_ibfk_1` FOREIGN KEY (`id_artista`) REFERENCES `artistas` (`id_artista`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_tipo_cliente`) REFERENCES `tipos_clientes` (`id_tipo_cliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
