from flask import Blueprint, request, jsonify
from app import mysql

restaurant_routes = Blueprint('restaurant_routes', __name__)

@restaurant_routes.route('/restaurants', methods=['GET'])
def get_restaurants():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, contact, opening_hours, address FROM restaurants WHERE deleted = 0")
    restaurants = cur.fetchall()
    cur.close()
    return jsonify(restaurants)


@restaurant_routes.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, contact, opening_hours, address FROM restaurants WHERE id = %s AND deleted = 0",
                (restaurant_id,))
    restaurant = cur.fetchone()
    cur.close()
    return jsonify(restaurant)


@restaurant_routes.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    name = data['name']
    contact = data['contact']
    opening_hours = data['opening_hours']
    address = data['address']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO restaurants (name, contact, opening_hours, address) VALUES (%s, %s, %s, %s)",
                (name, contact, opening_hours, address))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Restaurant created successfully"}), 201


@restaurant_routes.route('/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_restaurant(restaurant_id):
    data = request.get_json()
    name = data['name']
    contact = data['contact']
    opening_hours = data['opening_hours']
    address = data['address']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE restaurants SET name = %s, contact = %s, opening_hours = %s, address = %s "
                "WHERE id = %s AND deleted = 0", (name, contact, opening_hours, address, restaurant_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Restaurant updated successfully"})


@restaurant_routes.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE restaurants SET deleted = 1 WHERE id = %s", (restaurant_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Restaurant deleted successfully"})
