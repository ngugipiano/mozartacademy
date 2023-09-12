from flask import Blueprint

from flask import render_template

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
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