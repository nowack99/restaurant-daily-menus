from flask import Blueprint, request, jsonify
from app import mysql

menu_routes = Blueprint('menu_routes', __name__)

@menu_routes.route('/restaurants/<int:restaurant_id>/menu', methods=['POST'])
def add_menu_item(restaurant_id):
    data = request.get_json()
    name = data['name']
    day = data['day']
    price = data['price']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO menu_items (restaurant_id, name, day, price) VALUES (%s, %s, %s, %s)",
                (restaurant_id, name, day, price))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Menu item added successfully"}), 201


@menu_routes.route('/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>', methods=['PUT'])
def update_menu_item(restaurant_id, menu_item_id):
    data = request.get_json()
    name = data['name']
    day = data['day']
    price = data['price']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE menu_items SET name = %s, day = %s, price = %s "
                "WHERE id = %s AND restaurant_id = %s", (name, day, price, menu_item_id, restaurant_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Menu item updated successfully"})


@menu_routes.route('/restaurants/<int:restaurant_id>/menu/<int:menu_item_id>', methods=['DELETE'])
def delete_menu_item(restaurant_id, menu_item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM menu_items WHERE id = %s AND restaurant_id = %s", (menu_item_id, restaurant_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Menu item deleted successfully"})
