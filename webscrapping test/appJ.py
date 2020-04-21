from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
import scrapeMarsJ
from pymongo import MongoClient
#import scrape_craigslist

#app = Flask(__name__)
mongo = MongoClient()

mongo = MongoClient('mongodb://localhost:27017/mars_app')
app = Flask(__name__)
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")
@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    return render_template("indexJ.html", mars_data=mars_data)
@app.route("/scrape")
def scraper():
    mars_data = mongo.db.mars_data
    scrape_data = scrapeMarsJ.scrape()
    mars_data.replace_one({}, scrape_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
