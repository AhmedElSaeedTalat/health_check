-- script to create db and user
CREATE DATABASE IF NOT EXISTS myhealth;
CREATE USER IF NOT EXISTS `healthadmin`@`localhost` IDENTIFIED BY 'health#123H';
GRANT ALL PRIVILEGES ON myhealth.* TO `healthadmin`@`localhost`;
FLUSH PRIVILEGES;
