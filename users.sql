CREATE DATABASE IF NOT EXISTS myhealth;
CREATE DATABASE IF NOT EXISTS myhealth_test;
CREATE USER IF NOT EXISTS `healthadmin`@`localhost` IDENTIFIED BY 'health#123H';
GRANT ALL PRIVILEGES ON myhealth.* TO `healthadmin`@`localhost`;
GRANT ALL PRIVILEGES ON myhealth_test.* TO `healthadmin`@`localhost`;
FLUSH PRIVILEGES;
