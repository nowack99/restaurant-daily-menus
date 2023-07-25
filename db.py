from app import mysql

def create_table_restaurants():
    query = """
    CREATE TABLE IF NOT EXISTS restaurants (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        contact VARCHAR(100),
        opening_hours VARCHAR(100),
        address VARCHAR(255),
        deleted INT DEFAULT 0
    )
    """
    with mysql.connection.cursor() as cursor:
        cursor.execute(query)
        mysql.connection.commit()

def create_table_menu_items():
    query = """
    CREATE TABLE IF NOT EXISTS menu_items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        restaurant_id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        day VARCHAR(100),
        price DECIMAL(10, 2),
        FOREIGN KEY (restaurant_id) REFERENCES restaurants(id) ON DELETE CASCADE
    )
    """
    with mysql.connection.cursor() as cursor:
        cursor.execute(query)
        mysql.connection.commit()
