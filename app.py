from flask import Flask, render_template,redirect,url_for, request
from flask_pymongo import PyMongo
import os
app = Flask(__name__)


app.config["MONGO_URI"]=os.getenv("MONGO_URI","mongodb+srv://dhruv11:dhruv11@cluster0.4wpek.mongodb.net/mydatabase")
mongo= PyMongo(app)
@app.route('/')
def home():
    users = mongo.db.users.find()  # Fetch all users from the MongoDB collection
    return render_template('home.html', users=users)

# Route to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    if name:
        mongo.db.users.insert_one({'name': name})
    return redirect(url_for('home'))

# Route to delete a user
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.users.delete_one({'name': user_id})
    return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
