import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")



mongo = PyMongo(app)

users_collection = mongo.db.users
recipes_collection = mongo.db.recipes








@app.route('/get_cocktails')
def get_cocktails():
    _cocktails = mongo.db.cocktails.find()
    cocktail_list = [cocktail for cocktail in _cocktails]
    return render_template('cocktails.html', cocktails = cocktail_list, )


 
@app.route('/add_cocktail')
def add_cocktail():
    categories = mongo.db.categories.find()
    category_list = [category for category in categories]
    return render_template('addcocktails.html', categories = category_list )


@app.route('/insert_cocktail', methods=['POST'])
def insert_cocktail():
    cocktails = mongo.db.cocktails
    cocktails.insert_one(request.form.to_dict())
    return redirect(url_for('get_cocktails'))


@app.route('/edit_cocktail<cocktail_id>')
def edit_cocktail(cocktail_id):
    the_cocktail = mongo.db.cocktails.find_one({"_id": ObjectId(cocktail_id)})
    all_categories = mongo.db.categories.find()
    category_list = [category for category in all_categories]
    return render_template('editcocktail.html', cocktail=the_cocktail, categories=category_list)


@app.route('/get_categories')
def get_categories():
    return render_template('cocktails.html', categories = mongo.db.categories.find())


@app.route('/update_cocktail/<cocktail_id>', methods=["POST"])
def update_cocktail(cocktail_id):
    cocktails = mongo.db.cocktails
    cocktails.update( {'_id':ObjectId(cocktail_id)},
    {
        'category_name' : request.form.get('category_name'),
        'profile' : request.form.get('profile'),
        'cocktail_name' : request.form.get('cocktail_name'),
        'cocktail_info' : request.form.get('cocktail_info'),
        'cocktail_equipments' : request.form.get('cocktail_equipments'),
        'cocktail_ingredients' : request.form.get('cocktail_ingredients')

    })
    return redirect(url_for('get_cocktails'))




@app.route('/delete_cocktail/<cocktail_id>')
def delete_cocktail(cocktail_id):
    mongo.db.cocktails.remove({'_id':ObjectId(cocktail_id)})
    return redirect(url_for('get_cocktails'))

# Login
@app.route("/")
@app.route('/login', methods=['GET'])
def login():
	# Check if user is not logged in already
	if 'user' in session:
		user_in_db = users_collection.find_one({"username": session['user']})
		if user_in_db:
			# If so redirect user to his profile
			flash("You are logged in already!")
			return redirect(url_for('get_cocktails', user=user_in_db['username']))
	else:
		# Render the page for user to be able to log in
		return render_template("login.html")

# Check user login details from login form
@app.route('/user_auth', methods=['POST'])
def user_auth():
	form = request.form.to_dict()
	user_in_db = users_collection.find_one({"username": form['username']})
	# Check for user in database
	if user_in_db:
		# If passwords match (hashed / real password)
		if check_password_hash(user_in_db['password'], form['user_password']):
			# Log user in (add to session)
			session['user'] = form['username']
			# If the user is admin redirect him to admin area
			if session['user'] == "user":
				return redirect(url_for('get_cocktails'))
			else:
				flash("You were logged in!")
				return redirect(url_for('get_cocktails'))
			
		else:
			flash("Wrong password or user name!")
			return redirect(url_for('login'))
	else:
		flash("You must be registered!")
		return redirect(url_for('register'))
			

# Sign up
@app.route('/register', methods=['GET', 'POST'])
def register():
	# Check if user is not logged in already
	if 'user' in session:
		flash('You are already sign in!')
		return redirect(url_for('login'))
	if request.method == 'POST':
		form = request.form.to_dict()
		# Check if the password and password1 actualy match 
		if form['user_password'] == form['user_password1']:
			# If so try to find the user in db
			user = users_collection.find_one({"username" : form['username']})
			if user:
				flash(f"{form['username']} already exists!")
				return redirect(url_for('register'))
			# If user does not exist register new user
			else:				
				# Hash password
				hash_pass = generate_password_hash(form['user_password'])
				#Create new user with hashed password
				users_collection.insert_one(
					{
						'username': form['username'],
						'email': form['email'],
						'password': hash_pass
					}
				)
				# Check if user is actualy saved
				user_in_db = users_collection.find_one({"username": form['username']})
				if user_in_db:
					# Log user in (add to session)
					session['user'] = user_in_db['username']
					return redirect(url_for('get_cocktails', user=user_in_db['username']))
				else:
					flash("There was a problem saving your profile")
					return redirect(url_for('register'))

		else:
			flash("Passwords dont match!")
			return redirect(url_for('register'))
		
	return render_template("register.html")

# Log out
@app.route('/logout')
def logout():
	# Clear the session
	session.clear()
	flash('You were logged out!')
	return redirect(url_for('login'))







if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)