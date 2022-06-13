"""
call index.html page
"""
'''
as per flask framework, 
keep all html files inside 'templates' folder.
so create new folder 'templates' and store all html files we are creating
finally,
'templates' folder & my_House_Price_Predictor_3.py should be in same directory 
'''

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
# Run the server
# --------------------
my_House_Price_Predictor_app.run()
# --------------------
