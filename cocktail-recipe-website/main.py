import requests
from flask import Flask , render_template



def get_data():

    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    response.raise_for_status()
    data = response.json()

    global drink_name
    global drink_instructions
    global drink_img
    global drink_ingredient


    drink_name = data["drinks"][0]["strDrink"]
    drink_instructions = data["drinks"][0]["strInstructions"]
    drink_img = data["drinks"][0]["strDrinkThumb"]

    drink_ingredient = []

    for i in range(1, 16):

        ingredient = data["drinks"][0][f"strIngredient{i}"]
        measure = data["drinks"][0][f"strMeasure{i}"]

        if str(ingredient) != "None":
            drink_ingredient.append(str(measure) + " - " + str(ingredient).replace("None",""))
        else:
            drink_ingredient.append("")


app = Flask(__name__)

@app.route("/")
def index():
    get_data()
    return render_template("index.html", drink_name=drink_name, drink_instructions=drink_instructions, drink_img=drink_img, drink_ingredient=drink_ingredient)

