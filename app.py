from flask import Flask, render_template, request
from utils.brain import ask_ai
import markdown


app = Flask(__name__)

app.jinja_env.filters["markdown"] = markdown.markdown   # ← add this line


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/chat", methods= ['GET', 'POST'])
def chat_bot():
    reply = ""
    if request.method == "POST":
        reply = ask_ai(request.form["prompt"])
    return render_template("chatBot.html", reply=reply)


if __name__ == "__main__":
    app.run(debug= True)
