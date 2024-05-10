from flask import Flask, render_template

app = Flask(__name__)

data = [
{
    "name": "John Cena",
    "age": 25
},

{
    "name": "Jane Doe",
    "age": 55
}

]

## App routes, can be clubbed together for same method return
@app.route("/")
@app.route("/home")
def home():
    # Renders html page that we can customize
    # Parameter names can be anything, will be used in HTML doc
    return render_template("home.html", killmonger = data, title = "kukka")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

