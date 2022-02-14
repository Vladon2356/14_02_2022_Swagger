from flask import render_template, redirect, request, Blueprint, url_for

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
        return render_template("carscars/list_cars.html", cars=cars_)

    return render_template("cars/list_cars.html", cars=cars)


@cars_bp.route("/cars/<int:id>", methods=["GET"])
def get_car(id):
    result = False
    for car in cars:
        if car['id'] == id:
            result = car
    if not result:
        return render_template("cars/error.html", message="Car not found.")

    return render_template("cars/show_car.html", car=result)


@cars_bp.route("/cars/create", methods=["GET", "POST"])
def create_car():
    if request.method == "GET":
        return render_template("cars/create_car.html")

    if not request.form:
        return render_template("cars/error.html", message='Data not valied')

    brand = request.form.get("brand")
    model = request.form.get("model")
    price  = request.form.get("price")
    if not brand or not model or not price:
        return render_template("cars/error.html", message='Data not valied')

    id = len(cars) + 1
    cars.append(
        {
            "brand": brand,
            "model": model,
            "price": int(price),
            "id": id
        }
    )
    return redirect(url_for('cars.get_cars'))


@cars_bp.route("/cars/<int:id>/update", methods=["POST"])
def update_car(id):
    brand = request.form.get("brand")
    model = request.form.get("model")
    price = request.form.get("price")

    if not brand or not model or not price:
        return render_template("cars/error.html", message='Data not valied')

    result = False
    for car in cars:
        if car['id'] == id:
            result = car

    if not result:
        return render_template("cars/error.html", message="Car not found.")

    result["brand"] = brand
    result["model"] = model
    result["price"] = price
    return redirect(url_for('cars.get_cars'))


@cars_bp.route("/cars/<int:id>/delete", methods=["GET", "POST"])
def delete_car(id):
    result = False
    for car in cars:
        if car['id'] == id:
            result = car


    if not result:
        return render_template("cars/error.html", message="Car not found.")

    cars.remove(result)
    return redirect(url_for('cars.get_cars'))
