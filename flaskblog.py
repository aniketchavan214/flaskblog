from flask import Flask, render_template
app = Flask(__name__)

posts =[
    {
    "Author" : "Aniket Chavan",
    "Title" : "Blog Post1",
    "Content" : "First post content",
    "Date_posted" : "22 April 2023"
    },
    {
    "Author" : "Corey Schafer",
    "Title" : "Blog Post2",
    "Content" : "First post content",
    "Date_posted" : "22 April 2023"
    }
]
@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)