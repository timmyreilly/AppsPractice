#app.py 
from flask import Flask, render_template, session, redirect, url_for 
from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField
from flask.ext.bootstrap import Bootstrap
from wtforms.validators import Required

from wiki_sentiment import * 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

bootstrap = Bootstrap(app)

class SearchForm(Form):
    searchterm = StringField('What Wikipedia article would you like to analyze?', validators=[Required()])
    submit = SubmitField('Submit')

class PhotoForm(Form):
    photo_url = StringField('What would you like your new photo to be', validators=[Required()])
    submit = SubmitField('Submit') 

@app.route("/photo", methods=["GET", "POST"])
def photo():
    form = PhotoForm()
    if form.validate_on_submit():
        session['photo_url'] = form.photo_url.data
        photo_to_new_url(form.photo_url.data) 
    return render_template('photo.html', form=form, photo_url=session.get('photo_url'))

@app.route("/resume")
def hello():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        session['searchterm'] = form.searchterm.data 
        session['sentiment'], session['titlearticle'] = get_sentiment_from_url(session.get('searchterm'))
        return redirect(url_for('search'))
    return render_template('search.html', form=form, searchterm=session.get('searchterm'), number=session.get('sentiment'), titlearticle=session.get('titlearticle'))

if __name__ == "__main__":
    app.run(debug=True)