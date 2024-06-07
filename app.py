# BEGIN CODE HERE
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT


# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])

app.run(debug=True)
@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    try:
        # Get the value of the 'name' parameter from the request query string
        search_name = request.args.get('name')
        
        # Find products with the given name and sort them by price in ascending order
        # Assuming 'price' is a field in the documents of the 'products' collection
        result = list(mongo.db.products.find({"name": search_name}).sort("price", 1))
        
    
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
    try:
        data = request.get_json()
        # Validate data
        if not all(k in data for k in ("id", "name", "production_year", "price", "color", "size")):
            return jsonify({"error": "Invalid input"}), 400

        if data['color'] not in [1, 2, 3] or data['size'] not in [1, 2, 3, 4]:
            return jsonify({"error": "Invalid color or size"}), 400
        
        new_product = {
            "id": data["id"],
            "name": data["name"],
            "production_year": data["production_year"],
            "price": data["price"],
            "color": data["color"],
            "size": data["size"]
        }

        result = mongo.db.products.replace_one(
            {"name": data["name"]},  # Filter to find the product by name
            new_product,  # New product data
            upsert=True  # Insert the document if it doesn't exist
        )
        
        if result.matched_count:
            message = "Product updated"
            status_code = 200
        else:
            message = "Product added"
            status_code = 201
        
        return jsonify({"message": message}), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    
    
    semester = semester = request.args.get('semester')
    url = "https://qa.auth.gr/el/x/studyguide/600000438/current"

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    elementID = "exam" + str(semester)

    exam_element = driver.find_element(By.ID, elementID)
    tbody_element = exam_element.find_element(By.TAG_NAME, "tbody")

    rows = tbody_element.find_elements(By.TAG_NAME, "tr")
    course_titles = []
    for row in rows:
            course_title = row.get_attribute("coursetitle")
            if course_title:
                course_titles.append(course_title)
            
    driver.quit()

    res = {"course_titles": course_titles}

    return res
    # END CODE HERE
