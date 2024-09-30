from flask import Flask, request, render_template

app = Flask(__name__)

stores = [{
    "name": "My Store",
    "products": [
        {"name": "Chair", "price": 15.99},
        {"name": "Table", "price": 15.99},
        {"name": "Tisch", "price": 15.99},
        {"name": "Stuhl", "price": 15.99}
    ]   
}]

@app.get("/store")
def get_stores():
    return { "stores": stores }

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = { "name": request_data["name"], "products": [] }
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = { "name": request_data["name"], "price": request_data["price"] }
            store["products"].append(new_item)
            return new_item, 201
    return { "message": "Store not found" }, 404

@app.route("/")
def home():
    return render_template("home.html", content = stores)
