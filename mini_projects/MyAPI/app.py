from flask import Flask, jsonify, request, render_template
 # capital letters- classes, lower letter - methods and packages
 # jsonify turns python dictionary element into a string of text

app = Flask(__name__)

stores = [
    {"name": "My Perfect store",
     "items": [
         {"name": "My first Item",
          "price": 15.99
          },
         {"name": "My second Item",
          "price": 8.99
          }
     ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stores')
def get_stores():
    return jsonify({"stores": stores}) #turned into the dictionary so json can read it

@app.route('/stores', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "itmes":[]}
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/stores/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"]==name:
            return jsonify(store)
    return jsonify({"message":"Store not found"})

@app.route('/stores/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        new_item = {"name": request_data["name"], "price":request_data["price"]}
        if store["name"]==name:
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({"message":"Store not found"})

@app.route('/stores/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store["name"]==name:
            return jsonify({"items": store["items"]})
    return jsonify({"message":"Store not found"})

app.run(port=5000)
