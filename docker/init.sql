-- Créez la table 'auth'
CREATE TABLE auth (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Créez la table 'user_tasks'
CREATE TABLE user_tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    task VARCHAR(255) NOT NULL,
    completed BOOLEAN NOT NULL
);