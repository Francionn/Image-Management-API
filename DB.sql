create database if not exists user;

use user;

create table if not exists db_post(
	id int AUTO_INCREMENT,
	image LONGBLOB not null,
	descrip VARCHAR(50),
	action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	primary key(id)
);

insert into db_post (image, descrip)

VALUE ("arqv.jpeg", "description");