SET FOREIGN_KEY_CHECKS=0;
USE entrance_db;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS courses;

CREATE TABLE courses(course_name VARCHAR(50) NOT NULL PRIMARY KEY,
                     cutoff INT DEFAULT 0
                    );

insert into courses values("Data Science", 2);
insert into courses values("EEE", 3);
insert into courses values("IT", 1);
insert into courses values("", 0);

CREATE TABLE students(student_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    email VARCHAR(50) NOT NULL, 
                    password VARCHAR(30) NOT NULL,
                    name VARCHAR(30) NOT NULL,
                    score INT DEFAULT 0,
                    course_name VARCHAR(50), 
                    FOREIGN KEY (course_name) REFERENCES courses(course_name)
                    );

insert into students values(1, "janet@gmail.com", "jmjm", "Janet", 0, "");
insert into students values(2, "guru@gmail.com", "gr", "Guru", 0, "");
insert into students values(3, "rakesh@gmail.com", "rk", "Rakesh", 0, "");

CREATE TABLE questions(question_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    question VARCHAR(1000) NOT NULL,
                    choice1 VARCHAR(100) NOT NULL,
                    choice2 VARCHAR(100) NOT NULL,
                    choice3 VARCHAR(100) NOT NULL,
                    choice4 VARCHAR(100) NOT NULL,
                    answer INT NOT NULL                     
                    );
insert into questions values(1, "A person crosses a 600 m long street in 5 minutes. What is his speed in km per hour?", "3.6", "7.2", "8.4", "10", 2);
insert into questions values(2, "An aeroplane covers a certain distance at a speed of 240 kmph in 5 hours. To cover the same distance in 1 hours, it must travel at a speed of", "300 kmph", "360 kmph", "600 kmph", "720 kmph", 4);
insert into questions values(3, "If a person walks at 14 km/hr instead of 10 km/hr, he would have walked 20 km more. The actual distance travelled by him is", "50", "56", "70", "80", 1);
insert into questions values(4, "Excluding stoppages, the speed of a bus is 54 kmph and including stoppages, it is 45 kmph. For how many minutes does the bus stop per hour?", "9", "10", "12", "20", 2);
insert into questions values(5, "In a flight of 600 km, an aircraft was slowed down due to bad weather. Its average speed for the trip was reduced by 200 km/hr and the time of flight increased by 30 minutes. The duration of the flight is:", "1 hour", "2 hours", "3 hours", "4 hours", 1);
insert into questions values(6, "A man complete a journey in 10 hours. He travels first half of the journey at the rate of 21 km/hr and second half at the rate of 24 km/hr. Find the total journey in km.", "220 km", "224 km", "230 km", "234 km", 2);
insert into questions values(7, "The ratio between the speeds of two trains is 7 : 8. If the second train runs 400 km in 4 hours, then the speed of the first train is:", "70 km/hr", "75 km/hr", "84 km/hr", "87.5 km/hr", 4);
insert into questions values(8, "A man on tour travels first 160 km at 64 km/hr and the next 160 km at 80 km/hr. The average speed for the first 320 km of the tour is:", "35.55 km/hr", "36 km/hr", "71.11 km/hr", "71 km/hr", 3);
insert into questions values(9, "A car travelling with 5/7 of its actual speed covers 42 km in 1 hr 40 min 48 sec. Find the actual speed of the car.", "17 6/7 kmph", "25 kmph", "30 kmph", "35 kmph", 4);
insert into questions values(10, "In covering a distance of 30 km, Abhay takes 2 hours more than Sameer. If Abhay doubles his speed, then he would take 1 hour less than Sameer. Abhay's speed is:", "5 kmph", "6 kmph", "6.25 kmph", "7.5 kmph", 1);
insert into questions values(11, "A farmer travelled a distance of 61 km in 9 hours. He travelled partly on foot @ 4 km/hr and partly on bicycle at 9 km/hr. The distance travelled on foot is", "14 km", "15 km", "16 km", "17 km", 3);
insert into questions values(12, "A, B and C can do a piece of work in 20, 30 and 60 days respectively. In how many days can A do the work if he is assisted by B and C on every third day?", "12 days", "15 days", "16 days", "18 days", 2);
insert into questions values(13, "A alone can do a piece of work in 6 days and B alone in 8 days. A and B undertook to do it for Rs. 3200. With the help of C, they completed the work in 3 days. How much is to be paid to C?", "Rs. 375", "Rs. 400", "Rs. 600", "Rs. 800", 2);
insert into questions values(14, "4 men and 6 women can complete a work in 8 days, while 3 men and 7 women can complete it in 10 days. In how many days will 10 women complete it?", "35", "40", "45", "50", 2);
insert into questions values(15, "10 women can complete a work in 7 days and 10 children take 14 days to complete the work. How many days will 5 women and 10 children take to complete the work?", "3", "5", "7", "None of these", 3);