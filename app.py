from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	oppiboii = False
	foodslist = ["Steak", "Burger", "Chibito", "Schnitzel"]
	hatedefs = ["Tofu", "Cauliflower Chickpea Patties","Zucchini and Tomato Lasagna With Cashew Herb Cheese"]
	return render_template("index.html",listboii = foodslist,oppoday = oppiboii, oppolist = hatedefs)

if __name__ == '__main__':
   app.run(debug = True)
