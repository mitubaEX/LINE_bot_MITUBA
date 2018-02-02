CREATE TABLE users(
  id int primary key AUTO_INCREMENT,
  display_name varchar(128) NOT NULL,
  user_id varchar(128) NOT NULL,
  picture_url varchar(128) NOT NULL,
  status_message varchar(128) NOT NULL
) CHARACTER SET utf8mb4;
