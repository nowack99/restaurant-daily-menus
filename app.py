from flask import Flask
from flask_mysqldb import MySQL

from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from routes import routes_blueprint
from db import create_table_restaurants, create_table_menu_items

app = Flask(__name__)

app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DB

mysql = MySQL(app)

# main route blueprint
app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run()
