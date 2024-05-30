---Query to perform aggregate functions to the selected table

SELECT
Count(*) as total_books,
AVG(year_published) as average_year_published,
MIN(year_published) as oldest_book_published,
MAX(year_published) as newest_book_published
FROM books;