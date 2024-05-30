---Query to group books by title

SELECT
title,
year_published,
AVG(year_published) as average_year_published
FROM authors
    INNER JOIN books
        ON authors.author_id = books.author_id
GROUP BY title;