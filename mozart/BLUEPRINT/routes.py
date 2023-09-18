from flask import Blueprint, request, redirect, url_for
from mozart import mail
from flask_mail import Message
from flask import Blueprint

from flask import render_template

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        title = "MOZART ACADEMY ENROLMENT NEWS!!!"
        name = request.form.get('student_name')
        email = request.form. get('email_address')
        phonenumber = request.form. get('phone_number')
        instrument = request.form. get('instrument')
        level = request.form. get('level')
        residence = request.form. get('residence')
        sender = "customer@mozartacademyofmusic.com"
        msg = Message(title, sender=sender, recipients=["mozartacademy17@gmail.com"])
        data ={
            'name' : name,
            'email' : email,
            'phonenumber' : phonenumber,
            'instrument' : instrument,
            'level' : level,
            'residence' : residence
        }
        msg.html = render_template("enrolment.html", data = data)
        try:
            if mail.send(msg):
                return redirect(url_for("main.home"))
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
    
    
    return render_template("index.html")
    

@main.route("/abrsm", methods = ['POST', 'GET'])
def abrsm():
    return render_template("abrsm.html")

@main.route("/about", methods = ['POST', 'GET'])
def about():
    if request.method == 'POST':
        title = "MOZART SUBSCRIBTION"
        sender = "customer@mozartacademyofmusic.com"
        email = request.form.get('email')
        msg = Message(title, sender=sender, recipients=["mozartacademy17@gmail.com"])
        msg_body = "You have received a new subscription request from:"
        data = {
            'title': title,
            'body': msg_body,
            'email': email
        }
        msg.html = render_template("subscribers.html", data = data)
        try:
            if mail.send(msg):
                return redirect(url_for("main.home"))
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
    return render_template("about.html")

@main.route("/pianolesson", methods = ['POST', 'GET'])
def pianolesson():
    if request.method == 'POST':
        title = "CLIENT MESSAGE"
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get('subject')
        message = request.form.get('message')
        sender = "customer@mozartacademyofmusic.com"
        msg = Message(title, sender = sender,recipients=["mozartacademy17@gmail.com"])
        data = {
            "name": name,
            "email" : email,
            'subject': subject,
            'message' : message
        }
        msg.html = render_template("emailtemplate.html", data = data)
        try:
            if mail.send(msg):
                return redirect(url_for("main.home"))
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
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