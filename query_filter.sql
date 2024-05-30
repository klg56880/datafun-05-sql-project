---Query to combine the authors table and books table AND pull data filtered by title

SELECT DISTINCT first, last, title
FROM authors
    JOIN books
        ON authors.author_id = books.author_id
    WHERE title = "The Hobbit";