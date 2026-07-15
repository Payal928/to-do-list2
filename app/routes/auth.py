from flask import render_template , flash , session , request , url_for , redirect , Blueprint

auth_bp = Blueprint('auth' , __name__)

user_credentials = {
    'username':'admin',
    "password":'1234'
}

@auth_bp.route('/login' , methods = ['GET' , 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get("password")

        if username == user_credentials['username'] and password == user_credentials['password']:
            session['user'] = username
            flash('login successful' , 'success')
            return redirect(url_for('tasks.view')) 
        else:
            flash('WRONG USERNAME OR PASSWORD' , 'danger')

    return render_template('login.html')
    

@auth_bp.route('/logout')
def logout():
    session.pop('user' , None)
    flash('You are logged out' , 'info')
    return redirect(url_for('auth.login'))
