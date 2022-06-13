"""
added about.html page
"""

# --------------------
# Create App (Object) for our House Price Predictor
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
# Run the server
# --------------------
my_House_Price_Predictor_app.run()
# --------------------
