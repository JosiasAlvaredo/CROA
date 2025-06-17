CREATE DATABASE IF NOT EXISTS `app_renault`;
USE `app_renault`;
CREATE TABLE IF NOT EXISTS `invitados`(
    `dni` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_equipo` BIGINT,
    `nombre_apellido` VARCHAR(255) NOT NULL,
    `dieta` VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS `equipos`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(255) NOT NULL,
    `categoria` VARCHAR(255) NOT NULL,
    `responsable_1_id` BIGINT,
    `responsable_2_id` BIGINT,
    `deporte` VARCHAR(255) NOT NULL,
    `puntaje` BIGINT NOT NULL
);
ALTER TABLE `invitados`
ADD FOREIGN KEY (`id_equipo`) REFERENCES `equipos` (`id`);
CREATE TABLE IF NOT EXISTS `opciones_cantina`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(255) NOT NULL,
    `precio` BIGINT NOT NULL
);
CREATE TABLE IF NOT EXISTS `organizadores`(
    `dni` BIGINT NOT NULL PRIMARY KEY,
    `nombre_apellido` VARCHAR(255) NOT NULL,
    `rol` VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS `partido`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `equipo_1_id` BIGINT NOT NULL,
    `equipo_2_id` BIGINT NOT NULL,
    `arbitro_id` BIGINT NOT NULL,
    `numero_de_cancha` BIGINT NOT NULL,
    `deporte` VARCHAR(255) NOT NULL,
    `ganador_id` BIGINT,
    `hora` DATE NOT NULL,
    FOREIGN KEY (`equipo_1_id`) REFERENCES `equipos` (`id`),
    FOREIGN KEY (`equipo_2_id`) REFERENCES `equipos` (`id`),
    FOREIGN KEY (`arbitro_id`) REFERENCES `organizadores` (`dni`)
);
CREATE TABLE IF NOT EXISTS `fixture`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS `horarios`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS `eventos_de_escenario`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS `puntos_del_mapa`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS `sponsors`(
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

DESC `equipos`;