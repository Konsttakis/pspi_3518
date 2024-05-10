# BEGIN CODE HERE
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])


@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    search_name = mongo.request.args.get('name')
    result = mongo.db.products.find({"name": search_name}).sort("price")
    return result
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
    if int(mongo.request.args.get('color')) in range(1,3) and int(mongo.request.args.get('size')) in range(1,4):
        new_product = {}
        new_product['id'] = mongo.request.args.get('id')
        new_product['name'] = mongo.request.args.get('name')
        new_product['production_year'] = int(mongo.request.args.get('production_year'))
        new_product['price'] = int(mongo.request.args.get('price'))
        new_product['color'] = int(mongo.request.args.get('color'))
        new_product['size'] = int(mongo.request.args.get('size'))
        result = mongo.db.products.replace_one(new_product, upsert=True)
    return result
    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE
