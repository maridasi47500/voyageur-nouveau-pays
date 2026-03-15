from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,country_id,adresse,dateofbirth) values (:username,:country_id,:adresse,:dateofbirth)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_sport", methods=["GET","POST"])
def add_one_sport():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into sport (name) values (:name)",request.form)
        user = query_db('select * from sport')
        return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")
    user = query_db('select * from sport')
    one_user = query_db("select * from sport limit 1", one=True)
    return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into country (name) values (:name)",request.form)
        user = query_db('select * from country')
        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")
    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_article", methods=["GET","POST"])
def add_one_article():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into article (title,content,aboutuser_id,country_id,user_id,sport_id) values (:title,:content,:aboutuser_id,:country_id,:user_id,:sport_id)",request.form)
        user = query_db('select * from article')
        return render_template("articleform.html", articles=user, one_user=one_user, the_title="add new article")
    user = query_db('select * from article')
    one_user = query_db("select * from article limit 1", one=True)
    return render_template("articleform.html", articles=user, one_user=one_user, the_title="add new article")

