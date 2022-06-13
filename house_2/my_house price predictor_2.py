"""
Added welcome message for Default page
"""

# --------------------
# Create App (Object) for our website
# --------------------
import flask
my_House_Price_Predictor_app = flask.Flask("House_Price_Predictor_App")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@my_House_Price_Predictor_app.route('/')
def my_index_page():
    return "Welcome to House Price Predictor"
# --------------------

# --------------------
# Run the server
# --------------------
my_House_Price_Predictor_app.run()
# --------------------
