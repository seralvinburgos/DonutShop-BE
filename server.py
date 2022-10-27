from flask import Flask, request, abort
import json
from config import me, db
from mock_data import catalog

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

        # validate price, title, etc etc

    db.products.insert_one(product)
    product["_id"] = str(product["_id"])

    return json.dumps(product)



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
    for prod in catalog:
        if prod["category"].lower() == category.lower():
            results.append(prod)

    return json.dumps(results)



# get /api/catalog/lower/<amount>
@app.get("/api/catalog/lower/<amount>")
def lower_than(amount):
    results = []
    for prod in catalog:
        if prod["price"] < float(amount):
            results.append(prod)

    return json.dumps(results)



# get /api/category/unique
# get the list of unique categories
@app.get("/api/category/unique")
def unique_cats():
    results = []
    for prod in catalog:
        category = prod["category"]
        if not category in results:
            results.append(category)
        

    return json.dumps(results)



@app.get("/api/test/colors")
def unique_colors():
    colors = ["red", "blue", "Pink", "yellow", "Red", "Black", "BLUE", "RED", "BLACK", "YELLOW"]
    results = []
    for color in colors:
        color = color.lower()
        if not color in results:
            results.append(color)

    return json.dumps(results)



@app.get("/api/test/count/<color>")
def count_color(color):
    colors = ["red", "blue", "Pink", "yellow", "Red", "Black", "BLUE", "RED", "BLACK", "YELLOW"]
    color = color.lower()
    results = []
    count = 0
    for item in colors:
        if color == item.lower():
            count += 1

    return json.dumps(count)





# app.run(debug=True)