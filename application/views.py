from flask import render_template, flash, redirect
from application import app
from forms import LoginForm

# index view function suppressed for brevity
@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
	return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])