from flask import Flask, request, abort
import json
from config import me, db
from mock_data import catalog
from bson import ObjectId

app = Flask("Server")


@app.get("/")
def home():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "This is a test"

@app.get("/about")
def about():
    return "Alvin Burgos"


################################################################
#     API ENDPOINTS
#     JSON 
################################################################


@app.get("/api/version")
def version():
    v = {
        "version": "1.0.0",
        "build": 42,
        "name": "sloth",
        "developer": me
    }

    return json.dumps(v)


def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

# get /api/catalog
@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)


@app.post("/api/catalog")
def save_product():
    product = request.get_json()

    if product is None:
        return abort(400, "Product required")

    product["category"] = product["category"].lower()

        # validate price, title, etc etc

    db.products.insert_one(product)
    product["_id"] = str(product["_id"])

    return json.dumps(product)


@app.put("/api/catalog")
def update_product():
    product = request.get_json()
    id = product.pop("_id") # read it and remove it
    # del product["_id"]    # remove

    db.products.update_one({"_id": ObjectId(id)}, {"$set": product})
    return json.dumps("Ok")


@app.delete("/api/catalog/<id>")
def delete_product(id):
    res = db.products.delete_one({"_id": ObjectId(id)})
    return json.dumps({"count": res.deleted_count})


@app.get("/api/product/details/<id>")
def get_details(id):
    prod = db.products.find_one({"_id": ObjectId(id)})
    if prod:
        return json.dumps(fix_id(prod))

    return abort(404, "Product not found")


# get /api/products/count
# return the number of products in the catalog
@app.get("/api/products/count")
def total_count():
    count = db.products.count_documents({})
    return json.dumps(count)



# get /api/products/total
# return the sum of all the prices
@app.get("/api/products/total")
def total_price():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total += prod["price"]

    return json.dumps(total)


# get /api/catalog/<category>
# return all the products that belong to the received category
@app.get("/api/catalog/<category>")
def by_category(category):
    results = []
    cursor = db.products.find({"category": category})
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)



# get /api/catalog/lower/<amount>
@app.get("/api/catalog/lower/<amount>")
def lower_than(amount):
    results = []
    cursor = db.products.find({"price": {"$lt": float(amount)}})
    for prod in cursor:
            results.append(fix_id(prod))

    return json.dumps(results)


@app.get("/api/catalog/higher/<amount>")
def higher_than(amount):
    results = []
    cursor = db.products.find({"price": {"$gte": float(amount)}})
    for prod in cursor:
            results.append(fix_id(prod))

    return json.dumps(results)



# get /api/category/unique
# get the list of unique categories
@app.get("/api/category/unique")
def unique_cats():
    results = []
    cursor = db.products.distinct("category")
    for cat in cursor:
            results.append(cat)
        

    return json.dumps(results)



# app.run(debug=True)


# create an endpoint that allows us to retrieve products with prices greater than a certain value