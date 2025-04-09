-- Create sample users
USE flaskdb;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL
);

-- Insert some sample data
INSERT INTO user (username, email) VALUES ('admin', 'admin@example.com');
INSERT INTO user (username, email) VALUES ('user1', 'user1@example.com');
INSERT INTO user (username, email) VALUES ('user2', 'user2@example.com');
