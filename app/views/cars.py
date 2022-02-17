from flask import render_template, redirect, request, Blueprint, url_for, jsonify

cars_bp = Blueprint('cars', __name__)
cars = [
    {
        "id": 1,
        "brand": "Porshe",
        "model": "911",
        "price": 30000
    },
    {
        "id": 2,
        "brand": "Porshe",
        "model": "Cayenne",
        "price": 15000
    },
    {
        "id": 3,
        "brand": "BMW",
        "model": "M5",
        "price": 13500
    },
    {
        "id": 4,
        "brand": "Audi",
        "model": "A6",
        "price": 9500
    }
]


@cars_bp.route("/cars", methods=["GET"])
def get_cars():
    if request.args.get("name"):
        name_bit = request.args["name"]
        cars_ = [car for car in cars if name_bit in cars["name"].lower()]
        return jsonify(cars_)

    return jsonify(cars)


@cars_bp.route("/cars/<int:id>", methods=["GET"])
def get_car(id):
    result = False
    for car in cars:
        if car['id'] == id:
            result = car
    if not result:
        return jsonify({"message": "Car not found."}), 404

    return jsonify(result)


@cars_bp.route("/cars", methods=["GET", "POST"])
def create_car():
    if not request.json:
        return jsonify({"message": 'Please, specify "brand" and "model" and "price".'}), 400

    brand = request.json.get("brand")
    model = request.json.get("model")
    price  = request.json.get("price")
    if not brand or not model or not price:
        return jsonify({"message": 'Please, specify "brand" and "model" and "price".'}), 400

    id = len(cars) + 1
    cars.append(
        {
            "brand": brand,
            "model": model,
            "price": int(price),
            "id": id
        }
    )
    return jsonify({'id':id})


@cars_bp.route("/cars/<int:id>", methods=["PATCH"])
def update_car(id):
    brand = request.json.get("brand")
    model = request.json.get("model")
    price = request.json.get("price")

    if not brand or not model or not price:
        return jsonify({'message': 'Data not valied'})

    result = False
    for car in cars:
        if car['id'] == id:
            result = car

    if not result:
        return jsonify({"message": "Car not found."}), 404

    result["brand"] = brand
    result["model"] = model
    result["price"] = price
    return jsonify({"message": "Updated"})


@cars_bp.route("/cars/<int:id>", methods=["DELETE"])
def delete_car(id):
    result = False
    for car in cars:
        if car['id'] == id:
            result = car


    if not result:
        return jsonify({"message": "Car not found."}), 404

    cars.remove(result)
    return jsonify({"message": "Car deleted"})
