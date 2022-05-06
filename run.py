from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecrectkey'

posts = [
  {
    'author': 'Haris Nasir',
    'title' : 'Blog Post 1',
    'content': 'First Post Content Here',
    'date_posted'   : 'April 23, 2022' 
  },
  {
    'author': 'Liyana Nasir',
    'title' : 'Blog Post 2',
    'content': 'Second Post Content Here',
    'date_posted'   : 'April 25, 2022' 
  },
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.username.data == 'haris' and form.password.data =="password":
			flash(f'You are signed in as: {form.username.data} !', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Login unsuccessful, Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)	

if __name__ == "__main__":
	app.run(debug=True)
