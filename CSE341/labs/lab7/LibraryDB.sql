-- Create the database
Drop DATABASE if exists LibraryDB;
CREATE DATABASE LibraryDB;
USE LibraryDB;

-- Create the authors table
CREATE TABLE IF NOT EXISTS authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    bio TEXT
);

-- Create the categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Create the books table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    category_id INT,
    isbn VARCHAR(13),
    published_date DATE,
    status ENUM('available', 'borrowed') DEFAULT 'available',
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Create the borrowers table
CREATE TABLE IF NOT EXISTS borrowers (
    borrower_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Create the book_borrowers table
CREATE TABLE IF NOT EXISTS book_borrowers (
    book_id INT,
    borrower_id INT,
    borrowed_date DATE NOT NULL,
    due_date DATE NOT NULL,
    returned_date DATE,
    PRIMARY KEY (book_id, borrower_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (borrower_id) REFERENCES borrowers(borrower_id)
);

-- Sample data insertion for authors
INSERT INTO authors (name, bio) VALUES ('J.K. Rowling', 'British author, best known for the Harry Potter series.');
INSERT INTO authors (name, bio) VALUES ('George Orwell', 'English novelist, essayist, journalist, and critic.');

-- Sample data insertion for categories
INSERT INTO categories (name, description) VALUES ('Fantasy', 'Genre of speculative fiction set in a fictional universe, often inspired by real world myth and folklore.');
INSERT INTO categories (name, description) VALUES ('Dystopian', 'A society characterized by human misery, as squalor, oppression, disease, and overcrowding.');

-- Sample data insertion for books
INSERT INTO books (title, author_id, category_id, isbn, published_date, status) 
VALUES ('Harry Potter and the Philosopher''s Stone', 1, 1, '9780747532699', '1997-06-26', 'available');
INSERT INTO books (title, author_id, category_id, isbn, published_date, status) 
VALUES ('1984', 2, 2, '9780451524935', '1949-06-08', 'available');

-- Sample data insertion for borrowers
INSERT INTO borrowers (name, email) 
VALUES ('Alice Wonderland', 'alice@example.com');
INSERT INTO borrowers (name, email) 
VALUES ('Bob Builder', 'bob@example.com');

-- Sample data insertion for book_borrowers
INSERT INTO book_borrowers (book_id, borrower_id, borrowed_date, due_date) 
VALUES ((SELECT book_id FROM books WHERE title = 'Harry Potter and the Philosopher''s Stone'), (SELECT borrower_id FROM borrowers WHERE name = 'Alice Wonderland'), CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY));
INSERT INTO book_borrowers (book_id, borrower_id, borrowed_date, due_date) 
VALUES ((SELECT book_id FROM books WHERE title = '1984'), (SELECT borrower_id FROM borrowers WHERE name = 'Bob Builder'), CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY));


-- You can insert more data in your tables