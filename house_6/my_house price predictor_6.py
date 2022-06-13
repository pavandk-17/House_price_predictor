"""
Retrieve username & password and return same username & password
"""

# --------------------
# Create App (Object) for ourHouse Price Predictor
# --------------------
import flask
my_House_Price_Predictor_app = flask.Flask("House_Price_Predictor_App")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@my_House_Price_Predictor_app.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@my_House_Price_Predictor_app.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@my_House_Price_Predictor_app.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# --------------------

# --------------------
# END POINT - 4 : http://127.0.0.1:5000/validate URL MAPPED to '/validate'
# --------------------
@my_House_Price_Predictor_app.route('/validate', methods=['POST'])
def my_validate_page():
    # Task - 1 : Get user name & pass word entered by user
    # ----------------
    # framework will keep all the form data entered by use in a dictionary.
    # dictionary is 'flask.request.form'. from this dictionary we can retrieve username & password
    # key will be 'uname' and 'pw'
    entered_username = flask.request.form.get('uname')
    entered_password = flask.request.form.get('pw')
    return f"You have entered username is {entered_username} and password is {entered_password}"
    # ----------------
# --------------------

# --------------------
# Run the server
# --------------------
my_House_Price_Predictor_app.run()
# --------------------
