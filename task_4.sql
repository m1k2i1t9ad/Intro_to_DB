-- Use the database passed as an argument
USE alx_book_store;

-- Query to get the full description of the books table
SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_DEFAULT
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME= 'Books'
    AND TABLE_SCHEMA = 'alx_book_store';
