---Query to combine the authors table and books table AND pull author first name, last name, and book title

SELECT first, last, title
FROM authors
    INNER JOIN books
        ON authors.author_id = books.author_id;
