

-- Step 2: Insert data into the table
INSERT INTO customers (Customer_Id, Occupation, Type) VALUES
(1, 'Jedi', 'Red'),
(2, 'Batman', 'Orange'),
(3, 'Santa Claus', 'Blue'),
(4, 'Mover', 'Orange'),
(5, 'Orange', 'Blue'),
(6, 'pineapple', 'Red'),
(7, 'Sausage', 'Red'),
(8, 'Milkman', 'Red'),
(9, 'Pirate', 'Orange'),
(10, 'Lawyer', 'Blue'),
(11, 'Doctor', 'Orange'),
(12, 'Plummer', 'Red'),
(13, NULL, NULL);

INSERT INTO interactions (date_start, interaction, customers) VALUES
('2019-10-04 09:00:00', 'Email', 1),
('2020-02-11 16:10:00', 'Call', 4),
('2020-03-05 11:23:00', 'Bird', 4),
('2020-02-11 16:24:00', 'Call', 5),
('2020-02-11 16:14:00', 'Chatbot', 4),
('2020-03-05 11:20:00', 'Boat', 5),
('2020-02-11 16:21:00', 'Email', 6),
('2020-02-11 16:34:00', 'Call', 7),
('2020-02-17 18:24:00', 'Chatbot', 1),
('2020-03-05 11:23:00', 'Bird', 8),
('2020-02-11 15:22:00', 'Boat', 9),
('2020-03-05 11:24:00', 'Email', 10),
('2020-02-11 16:32:00', 'Email', 1),
('2020-02-11 16:38:00', 'Email', 11),
('2020-03-05 11:30:00', 'Bird', 12),
('2020-03-05 11:33:00', 'Bird', 2),
('2020-03-05 18:24:00', 'Chatbot', 4),
('2020-01-16 09:15:00', 'Bird', 12),
('2020-06-03 13:01:00', 'Post', 5),
('2021-06-04 13:01:00', 'Email', 3);

INSERT INTO products (date, product) VALUES
('01-2019', 'Sand'),
('02-2019', 'Sand'),
('03-2019', 'Sand'),
('04-2019', 'Sand'),
('05-2019', 'Sand'),
('06-2019', 'Sand'),
('07-2019', 'Sand'),
('08-2019', 'Sand'),
('09-2019', 'Sand'),
('10-2019', 'Sand'),
('11-2019', 'Sand'),
('12-2019', 'Sand'),
('01-2020', 'Sand'),
('02-2020', 'Sand'),
('03-2020', 'Sand'),
('04-2020', 'Sand'),
('05-2020', 'Sand'),
('06-2020', 'Sand'),
('07-2020', 'Sand'),
('08-2020', 'Sand'),
('09-2020', 'Sand'),
('10-2020', 'Sand'),
('11-2020', 'Sand');