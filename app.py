from flask import Flask, render_template, request

app = Flask(__name__)

item_name = ''
item_quantity = 0
item_weight = 0

@app.route('/')
def default(): 
    return render_template('html.html', item_name=item_name, item_quantity=item_quantity, item_weight=item_weight)

@app.route('/', methods = ['POST'])
def updateItemData():
    global item_name 
    global item_quantity
    global item_weight

    item_name = request.form['item_name']
    item_quantity = request.form['item_quantity']
    item_weight = request.form['item_weight']
    return default()

@app.route('/getItemData')
def getItemData():
    return {'item_name': item_name, 'item_quantity': item_quantity, 'item_weight': item_weight}

if __name__ == "__main__":
    app.run()