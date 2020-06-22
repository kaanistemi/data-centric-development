import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")
app.config["MONGO_DBNAME"] = 'cocktail_mix'
app.config["MONGO_URI"] ='mongodb+srv://root:r00tUser@myfirstcluster-hmnju.mongodb.net/cocktail_mix?retryWrites=true&w=majority'


mongo = PyMongo(app)


app=Flask(__name__,template_folder='template')
@app.route('/get_cocktails')
def get_cocktails():
    _cocktails = mongo.db.cocktails.find()
    cocktail_list = [cocktail for cocktail in _cocktails]
    return render_template('cocktails.html', cocktails = cocktail_list)

 
@app.route('/add_cocktail')
def add_task():
    categories = mongo.db.categories.find()
    category_list = [category for category in categories]
    return render_template('addcocktails.html', categories = category_list )

@app.route('/insert_cocktail', methods=['POST'])
def insert_cocktail():
    cocktails = mongo.db.cocktails
    cocktails.insert_one(request.form.to_dict())
    return redirect(url_for('get_cocktails'))
    
@app.route('/edit_cocktail/<cocktail_id>')
def edit_cocktail(cocktail_id):
    the_cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editcocktail.html', cocktail=the_cocktail, categories=all_categories)

@app.route('/get_categories')
def get_categories():
    return render_template('cocktails.html', categories = mongo.db.categories.find())

if __name__ == '__main__':
    
    app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=False)


