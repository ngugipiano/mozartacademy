from flask import Blueprint, request, redirect, url_for
from mozart import mail
from flask_mail import Message

from flask import render_template

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        title = "CLIENT MESSAGE"
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get('subject')
        message = request.form.get('message')
        sender = "noreply@app.com"
        msg = Message(title, sender = sender,recipients=["harmonymwirigi99@gmail.com"])
        msg_body = message
        data = {
            'app_name': 'TREAVILLE EDGE',
            'title': title,
            'body': msg_body
        }
        try:
            if mail.send(msg):
                return "EMAIL SENT"
        except Exception as e:
            print(e)
            return "the email was not sent{e}"


        return "email sent successfuly"
    return render_template("index.html")

@main.route("/abrsm")
def abrsm():
    return render_template("abrsm.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/pianolesson")
def pianolesson():
    return render_template("pianolesson.html")

@main.route("/organlesson")
def organlesson():
    return render_template("organlesson.html")

@main.route("/blog")
def blog():
    return render_template("blog.html")

@main.route("/registration")
def registration():
    return render_template("registration.html")

@main.route("/cellolessons")
def cellolessons():
    return render_template("cellolessons.html")

@main.route("/violinlessons")
def violinlessons():
    return render_template("violinlessons.html")

@main.route("/hfaqs")
def hfaqs():
    return render_template("hfaqs.html")

@main.route("/partner")
def partner():
    return render_template("partner.html")
            

@main.route("/guitarlessons")
def guitarlessons():
    return render_template("guitarlessons.html")

@main.route("/saxlessons")
def saxlessons():
    return render_template("saxlessons.html")

@main.route("/trumpetlessons")
def trumpetlessons():
    return render_template("trumpetlessons.html")

@main.route("/woodwindlesson")
def woodwindlesson():
    return render_template("woodwindlesson.html")

@main.route("/voicelessons")
def voicelessons():
    return render_template("voicelessons.html")


@main.route("/orchestra")
def orchestra():
    return render_template("orchestra.html")