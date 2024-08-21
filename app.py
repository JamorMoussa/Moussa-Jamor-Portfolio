from flask import Flask, render_template

import json 


app = Flask(__file__)



@app.route('/', methods = ["GET"])
def home():

    # with open("./posts/post.json", "rb") as f: 
    #     data = json.load(f)["data"]
    return render_template("portfolio.html") # , data=data)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)