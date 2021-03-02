-- Creates a user in localhost server username: user_0d_1.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
