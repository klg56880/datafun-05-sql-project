---Query to insert 10 new rows of data into each table

INSERT INTO authors (first, last) VALUES
('Toni', 'Morrison'),
('Ken', 'Kesey'),
('Mary', 'Shelley'),
('Virginia', 'Woolf'),
('Herman', 'Melville'),
('Victor', 'Hugo'),
('Jack', 'London'),
('Fyodor', 'Dostoevsky'),
('Charlotte', 'Bronte'),
('Gabriel', 'Garcia Marquez')
ON CONFLICT DO NOTHING;

INSERT INTO books (title, year_published) VALUES
('Beloved', '1987'),
('One Flew Over the Cuckoo''s Nest', '1962'),
('Frankenstein', '1823'),
('To the Lighthouse', '1927'),
('Moby-Dick', '1851'),
('Les Miserables', '1862'),
('The Call of the Wild', '1903'),
('Crime and Punishment', '1866'),
('Jane Eyre', '1847'),
('One Hundred Years of Solitude', '1967')
ON CONFLICT DO NOTHING;