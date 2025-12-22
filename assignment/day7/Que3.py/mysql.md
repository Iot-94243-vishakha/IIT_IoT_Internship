* USE iot_application;
* CREATE TABLE smart_home_status(
    * id INT PRIMARY KEY AUTO_INCREMENT,
    * light_status VARCHAR(5),
    * fan_status VARCHAR(5),
    * temperature FLOAT,
    * date_time DATETIME
);