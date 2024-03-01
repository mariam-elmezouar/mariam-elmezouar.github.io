
--
-- CREATE THE DATABASE
--
Drop DATABASE if exists StudentDB;
CREATE DATABASE StudentDB;
USE StudentDB;

--
-- CREATE TABLES
--

create table Student(ID int, 
name varchar(20), 
GPA real Not Null, 
sizeHS int,
Primary key(ID))engine = innodb;

create table Campus(location varchar(20), 
enrollment int, 
camprank int,
primary key(location))engine = innodb;

create table Apply(ID int, 
location varchar(20), 
major varchar(20), 
decision varchar(20), 
primary key(ID,location,major),
foreign key(location) references Campus(location) on Update CASCADE,
foreign key(ID) references Student(Id) on Delete CASCADE)engine = innodb;

--
-- POPULATE TABLES
--

insert into Student values (123, 'Amy', 3.9, 1000);
insert into Student values (234, 'Bob', 3.8, 1500);
insert into Student values (345, 'Craig', 3.7, 500);
insert into Student values (456, 'Doris', 3.7, 1000);
insert into Student values (567, 'Edward', 3.6, 2000);
insert into Student values (678, 'Fay', 3.5, 200);
insert into Student values (789, 'Gary', 3.5, 800);
insert into Student values (987, 'Helen', 3.5, 800);
insert into Student values (876, 'Irene', 3.9, 400);
insert into Student values (765, 'Jay', 2.9, 1500);
insert into Student values (654, 'Amy', 3.9, 1000);
insert into Student values (543, 'Craig', 3.8, 2000);

insert into Campus values ('Berkeley', 35000, 1);
insert into Campus values ('Los Angeles', 38000, 2);
insert into Campus values ('San Diego', 27500, 3);
insert into Campus values ('Santa Cruz', 15000, 4);

insert into Apply values (123, 'Berkeley', 'CS', 'Y');
insert into Apply values (123, 'Santa Cruz', 'EE', 'Y');
insert into Apply values (234, 'Los Angeles', 'biology', 'N');
insert into Apply values (345, 'San Diego', 'bioengineering', 'Y');
insert into Apply values (345, 'Santa Cruz', 'bioengineering', 'N');
insert into Apply values (345, 'Santa Cruz', 'CS', 'Y');
insert into Apply values (345, 'Santa Cruz', 'EE', 'N');
insert into Apply values (678, 'Berkeley', 'history', 'Y');
insert into Apply values (987, 'Berkeley', 'CS', 'N');
insert into Apply values (987, 'Los Angeles', 'CS', 'Y');
insert into Apply values (876, 'Berkeley', 'CS', 'N');
insert into Apply values (876, 'San Diego', 'biology', 'Y');
insert into Apply values (876, 'San Diego', 'marine biology', 'N');
insert into Apply values (765, 'Berkeley', 'history', 'Y');
insert into Apply values (765, 'Santa Cruz', 'history', 'N');
insert into Apply values (765, 'Santa Cruz', 'psychology', 'Y');
insert into Apply values (543, 'San Diego', 'CS', 'N');
