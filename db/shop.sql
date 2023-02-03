create table usr(id int PRIMARY KEY, name varchar(25));
create table product(id int PRIMARY KEY, name varchar(25));
create table suppliers(id int PRIMARY KEY, name varchar(25));
begin;
create table basket(id int PRIMARY KEY, 
id_usr int REFERENCES usr(id), 
id_product int REFERENCES product(id),
delivery_date varchar(20));
commit;
begin;
create table supply_products(id int PRIMARY KEY,
id_supply int REFERENCES suppliers(id),
id_product int REFERENCES product(id));
commit;
begin;
create table warehouse(id int PRIMARY KEY, 
id_basket int REFERENCES basket(id));
commit;
begin;
insert into usr
values (1, 'USER1');
insert into usr
values (2, 'USER2');
insert into usr
values (3, 'USER3');
commit;
begin;
insert into product
values (1, 'IPHONE');
insert into product
values (2, 'AIRPODS');
insert into product
values (3, 'MACBOOK');
insert into product
values (4, 'S21');
insert into product
values (5, 'S22');
insert into product
values (6, 'PIXEL');
commit;
begin;
insert into suppliers
values(1, 'APPLE');
insert into suppliers
values(2, 'SAMSUNG');
insert into suppliers
values(3, 'GOOGEL');
commit;
begin;
insert into basket
values (1, 1, 4, '2023.02.10');
insert into basket
values (2, 1, 6, '2023.02.10');
insert into basket
values (3, 1, 1, '2023.02.04');
insert into basket
values (4, 2, 4, '2023.02.01');
insert into basket
values (5, 3, 1, '2023.01.30');
insert into basket
values (6, 3, 4, '2023.02.10');
commit;
begin;
insert into warehouse
values (1, 1);
insert into warehouse
values (2, 1);
insert into warehouse
values (3, 4);
insert into warehouse
values (4, 4);
insert into warehouse
values (5, 4);
insert into warehouse
values (6, 6);
commit;
begin;
insert into supply_products
values (1, 1, 1);
insert into supply_products
values (2, 1, 2);
insert into supply_products
values (3, 1, 3);
insert into supply_products
values (4, 2, 4);
insert into supply_products
values (5, 2, 5);
insert into supply_products
values (6, 3, 6);
commit;
select 'task 1';
table basket;
select 'task 2';
select delivery_date from basket
where id > '3';
select 'task 3';
select * from basket
where delivery_date > '2023.02.01';
select 'task 4';
table warehouse;
select 'task 5';
table basket;