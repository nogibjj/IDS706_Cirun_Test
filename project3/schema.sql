
-- DROP TABLE udemy;
CREATE TABLE udemy (
    id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    link VARCHAR(255) NOT NULL,
    price DECIMAL(10 , 2 ) NULL,
    subscribers INT NULL,
    reviews INT NULL,
    levels VARCHAR(255) NOT NULL,
    rating DECIMAL(10 , 2 ) NULL,
    subjectName VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

--INSERT INTO udemy (id, title, link, price, subscribers, reviews, levels, rating, subjectName) VALUES (41295,'Learn HTML5 Programming From Scratch','https://www.udemy.com/learn-html5-programming-from-scratch',0,268923,8629,45,'Beginner Level',0.82,10.5,'Web
--Development');