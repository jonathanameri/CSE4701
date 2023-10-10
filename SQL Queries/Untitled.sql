show databases;
use 4701_p1;
describe shipment;
show tables;
describe ITEM;
alter table shipment add COLUMN ItemNum varchar(10);
alter table shipment add constraint foreign key (ItemNum) REFERENCES ITEM(ItemNum);
describe shipment;
select * from shipment;


create database ORDER_DB;
use ORDER_DB;
CREATE TABLE CUSTOMER (
 Cust VARCHAR(255) PRIMARY KEY,
 Cname VARCHAR(255),
 City VARCHAR(255)
);
CREATE TABLE `ORDER` (
 `Order` VARCHAR(255) PRIMARY KEY,
 ODate DATE,
 Cust VARCHAR(255),
 Ord_amt INT,
 FOREIGN KEY (Cust) REFERENCES CUSTOMER(Cust)
);
CREATE TABLE ITEM (
 Item VARCHAR(255) PRIMARY KEY,
 Unit_price DECIMAL(10, 2)
);
CREATE TABLE WAREHOUSE (
 Warehouse VARCHAR(255) PRIMARY KEY,
 City VARCHAR(255)
);
CREATE TABLE `ORDER_ITEM` (
 `Order` VARCHAR(255),
 `Item` VARCHAR(255),
 QTY INT,
 PRIMARY KEY (`Order`, `Item`),
 FOREIGN KEY (`Order`) REFERENCES `ORDER`(`Order`),
 FOREIGN KEY (`Item`) REFERENCES `ITEM`(`Item`)
);
CREATE TABLE SHIPMENT (
 `Order` VARCHAR(255),
 Warehouse VARCHAR(255),
 Ship_date DATE,
 PRIMARY KEY (`Order`, Warehouse),
 FOREIGN KEY (`Order`) REFERENCES `ORDER`(`Order`),
 FOREIGN KEY (Warehouse) REFERENCES WAREHOUSE(Warehouse)
);

SET GLOBAL local_infile=1;
show global variables like 'local_infile';
show tables;

LOAD DATA LOCAL INFILE '/Users/jonathanameri/Downloads/order_db/customer.csv' INTO TABLE
CUSTOMER
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

LOAD DATA LOCAL INFILE '/Users/jonathanameri/Downloads/order_db/item.csv' INTO TABLE
ITEM
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

LOAD DATA LOCAL INFILE '/Users/jonathanameri/Downloads/order_db/order.csv' INTO TABLE
`ORDER`
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

LOAD DATA LOCAL INFILE '/Users/jonathanameri/Downloads/order_db/order_item.csv' INTO TABLE
ORDER_ITEM
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

LOAD DATA LOCAL INFILE '/Users/jonathanameri/Downloads/order_db/shipment.csv' INTO TABLE
SHIPMENT
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

LOAD DATA LOCAL INFILE '/Users/jonathanameri/Downloads/order_db/warehouse.csv' INTO TABLE
WAREHOUSE
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

select * from CUSTOMER;
select * from ITEM;
select * from `ORDER`;
select * from ORDER_ITEM;
select * from SHIPMENT;
select * from WAREHOUSE;
use ORDER_DB;

#part 5
#5a
select `Order`, Ship_date from SHIPMENT where Warehouse="W2";

#5b
SELECT o.`Order`, s.Warehouse
FROM CUSTOMER c
JOIN `ORDER` o ON c.Cust = o.Cust
JOIN `SHIPMENT` s ON o.`Order` = s.`Order`
WHERE c.Cname = 'Jose Lopez';

#5c
SELECT c.Cname, COUNT(o.Order) AS No_of_orders, AVG(o.Ord_amt) AS Avg_order_amt
FROM CUSTOMER c
JOIN `ORDER` o ON c.Cust = o.Cust
GROUP BY c.Cname;

#5d
SELECT o.`Order`
FROM `ORDER` o
JOIN `SHIPMENT` s ON o.`Order` = s.`Order`
WHERE s.Ship_date > DATE_ADD(o.ODate, INTERVAL 25 DAY)
  AND o.Ord_amt > 0;

#5e
SELECT s.Order
FROM `ORDER` o
JOIN `SHIPMENT` s ON o.Order = s.Order
JOIN WAREHOUSE w ON s.Warehouse = w.Warehouse
WHERE w.City = 'New York'
GROUP BY s.Order
HAVING COUNT(DISTINCT s.Warehouse) = (
  SELECT COUNT(*)
  FROM WAREHOUSE
  WHERE City = 'New York'
);

#5f
SELECT s.Order, COUNT(DISTINCT s.Warehouse) AS CNT_Warehouse
FROM `ORDER` o
JOIN `SHIPMENT` s ON o.Order = s.Order
GROUP BY s.Order
HAVING COUNT(DISTINCT s.Warehouse) > 1;

#5g
SELECT o.Order
FROM `ORDER` o
LEFT JOIN SHIPMENT s ON o.Order = s.Order
WHERE s.Order IS NULL;

#5h
SELECT c.Cname, SUM(o.Ord_amt) AS C_Ord_amt, SUM(oi.QTY) AS C_QTY
FROM CUSTOMER c
JOIN `ORDER` o ON c.Cust = o.Cust
JOIN `ORDER_ITEM` oi ON o.Order = oi.Order
GROUP BY c.Cname;


#5i
SELECT c.Cname, SUM(oi.QTY) AS Total_QTY
FROM CUSTOMER c
JOIN `ORDER` o ON c.Cust = o.Cust
JOIN `ORDER_ITEM` oi ON o.Order = oi.Order
JOIN ITEM i ON oi.Item = i.Item
GROUP BY c.Cname
ORDER BY Total_QTY DESC
LIMIT 1;

#5j
SELECT c.Cname, SUM(o.Ord_amt) AS Total_Sales
FROM CUSTOMER c
JOIN `ORDER` o ON c.Cust = o.Cust
GROUP BY c.Cname
ORDER BY Total_Sales DESC
LIMIT 1;

