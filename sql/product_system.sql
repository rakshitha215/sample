
create table product(
id int PRIMARY KEY,
name varchar(60) NOT NULL,
quantity int,
price float
);
INSERT INTO product values(1,"john",100,250);
INSERT INTO product values(2,"mike",200,1000);
INSERT INTO product values(3,"arvin",300,2000);
INSERT INTO product values(4,"nick",2000,7000);
INSERT INTO product (id, name, quantity, price) VALUES
(6, 'Tablet', 8, 30000),
(7, 'Headphones', 12, 2500),
(8, 'Printer', 4, 15000),
(9, 'Webcam', 6, 3500),
(10, 'Speaker', 5, 4000);
SELECT *
FROM product
WHERE quantity < 5;
SELECT SUM(quantity * price) AS total_inventory_value
FROM product;
