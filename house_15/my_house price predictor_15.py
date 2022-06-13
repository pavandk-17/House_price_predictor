"""
we are validating username and password with registered users
in database
create a logout page
"""

# --------------------
# Create App (Object) for our website
# --------------------
import flask
from flask_session import Session
from flask import session
my_House_Price_Predictor_app = flask.Flask("my_House_Price_Predictor")
my_House_Price_Predictor_app.secret_key = "My Secrete paswword"
my_House_Price_Predictor_app.config["SESSION_TYPE"] = "filesystem"
Session(my_House_Price_Predictor_app)
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
    entered_username = entered_username.lower()
    entered_username = entered_username.strip()
    # Connect to user_db.sqlite, check whether entered username and password
    # present. If not present then return login failed
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect(r'users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Executing select query")
    my_db_cursor.execute(f"SELECT NAME, PASSWORD FROM USERS_TABLE WHERE NAME='{entered_username}' AND PASSWORD = '{entered_password}'")
    print("Done")

    print("Retrieve all data from cursor")
    my_db_result = my_db_cursor.fetchall()
    print("Done")
    # if we get record then username & password correct else wrong

    # This work is done, so close db connection
    my_db_connection.close()

    if len(my_db_result) > 0:
        # Store Username in Session Object
        session['username'] = entered_username
        # All the data is in my_db_result
        return "Login success"

    else:
        return "Login Failed. Invalid Credentials <br><br> <a href='/login'>Go Back To Login</a>"

# ----------------
# POINTS - 1
# ----------------
# - We are sending data inside python object to html file
# - If we need to display python variable in html then we need to
#   write python code inside html
# - We can write python code inside html file using below syntax
#   1) Use this {{variable_name}} to display any python variable value
#   2) Use this {% to write any python code %}
#   3) Use this {% if condn%}  for any block like if, for etc
#               {% endif %}
# ----------------
# --------------------

# --------------------
# END POINT - 5 : http://127.0.0.1:5000/newuser URL MAPPED to '/newuser'
# --------------------
@my_House_Price_Predictor_app.route('/newuser')
def my_newuser_page():
    return flask.render_template('newuser.html')
# --------------------

# --------------------
# END POINT - 6 : http://127.0.0.1:5000/register URL MAPPED to '/register'
# --------------------
@my_House_Price_Predictor_app.route('/register', methods=['POST'])
def my_register_page():

    # Get all data
    entered_username = flask.request.form.get('uname')
    entered_password_1 = flask.request.form.get('pw1')
    entered_password_2 = flask.request.form.get('pw2')
    entered_email = flask.request.form.get('email')
    entered_username = entered_username.lower()
    entered_username = entered_username.strip()
    # Check whether both the passwords are matching
    if entered_password_1 != entered_password_2:
        return "Both Passwords Are Not Matching. <br><br><a href='/login'>Go Back To Registration</a>"

    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect('users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table if not exists")
    my_query = '''CREATE TABLE IF NOT EXISTS users_table(
    NAME    VARCHAR(100),
    PASSWORD    VARCHAR(100),
    EMAIL   VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # ------------------------

    # verify whether user already exists in the database
    # How? select from table where username = entered_username
    # if we get records then we decide found
    # if we get 0 records the we can decide not found
    my_query = f"SELECT * FROM users_table WHERE name='{entered_username}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()
    if len(my_db_result) > 0:
        return "User Already Exists. <br><br><a href='/login'>Go Back To Registration</a>"

    # if user not exists then add new record to database and return account created successfully
    my_query = f"INSERT INTO USERS_TABLE VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "User Created Successfully. <a href='/login'>Click Here To Login</a>"

# --------------------
# END POINT - 7 : http://127.0.0.1:5000/newhouse URL MAPPED to '/newhouse'
# --------------------
@my_House_Price_Predictor_app.route('/newhouse')
def my_newhouse_page():
    return flask.render_template('newhouse.html')
# --------------------

# --------------------
# END POINT - 8 : http://127.0.0.1:5000/addnewhouse URL MAPPED to '/addnewhouse'
# --------------------
@my_House_Price_Predictor_app.route('/newhouse', methods=['POST'])
def my_addnewhouse_page():

    # Get all data
    entered_customername = flask.request.form.get('cname')
    entered_customercontact= flask.request.form.get('ccontact')
    entered_area = flask.request.form.get('area')
    entered_address = flask.request.form.get('address')
    entered_avg_areaincome = flask.request.form.get('aareaincome')
    entered_avg_areahouseage = flask.request.form.get('ahouseage')
    entered_avg_areanumberofrooms= flask.request.form.get('anumberofrooms')
    entered_avg_areanumberofbedrooms = flask.request.form.get('anumberofbedrooms')
    entered_areapopulation = flask.request.form.get('apopulation')
    entered_price = flask.request.form.get('price')
    entered_remarks = flask.request.form.get('remarks')
    entered_customername = entered_customername.lower()
    entered_customername = entered_customername.strip()

    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect('users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table")
    my_query = '''CREATE TABLE IF NOT EXISTS newhouse_table(
    CUSTOMERNAME    VARCHAR(100),
    CUSTOMERCONTACT   VARCHAR(100),
    AREA              VARCHAR(100),
    ADDRESS           VARCHAR(100),
    AVG_AREAINCOME     INTGER,
    AVG_AREAHOUSEAGE    INTGER,
    AVG_AREANUMBEROFROOMS  INTGER,
    AVG_AREANUMBEROFBEDROOMS   INTGER,
    AREAPOPULATION       INTGER,
    PRICE           INTGER, 
    REMARKS   VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # ------------------------
    # verify whether user already exists in the database
    my_query = f"SELECT * FROM NEWHOUSE_TABLE WHERE CUSTOMERNAME='{entered_customername}'AND CUSTOMERCONTACT='{entered_customercontact}' AND  AREA='{entered_area}' AND ADDRESS='{entered_address}' AND AVG_AREAINCOME='{entered_avg_areaincome}' AND AVG_AREAHOUSEAGE='{entered_avg_areahouseage}' AND AVG_AREANUMBEROFROOMS='{entered_avg_areanumberofrooms}'AND AVG_AREANUMBEROFBEDROOMS='{entered_avg_areanumberofbedrooms}'AND  AREAPOPULATION='{entered_areapopulation}' AND PRICE='{entered_price}' AND REMARKS='{entered_remarks}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()  # [(),()]
    if len(my_db_result) > 0:
        return "Record Already Exists. Continuing with next record"
    # ------------------------
    # if user not exists then add new record to database and return account created successfully
    my_query = f"INSERT INTO NEWHOUSE_TABLE( CUSTOMERNAME,CUSTOMERCONTACT, AREA,ADDRESS,AVG_AREAINCOME,AVG_AREAHOUSEAGE,AVG_AREANUMBEROFROOMS,AVG_AREANUMBEROFBEDROOMS,AREAPOPULATION,PRICE,REMARKS) VALUES('{entered_customername}', '{entered_customercontact}', '{entered_area}', '{entered_address}', '{entered_avg_areaincome}', '{entered_avg_areahouseage}', '{entered_avg_areanumberofrooms}', '{entered_avg_areanumberofbedrooms}', '{entered_areapopulation}', '{entered_price}', '{entered_remarks}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "We Received your form.  <a href='/'>Click Here To fill your qureirs</a>"
# --------------------
# END POINT - 9 : http://127.0.0.1:5000/customer URL MAPPED to '/customer'
# --------------------
@my_House_Price_Predictor_app.route('/customer')
def my_customer_page():
    return flask.render_template('customer.html')
# --------------------

# --------------------
# END POINT - 10 : http://127.0.0.1:5000/addnewcustomer URL MAPPED to '/addnewcustomer'
# --------------------
@my_House_Price_Predictor_app.route('/customer', methods=['POST'])
def my_addcustomer_page():

    # Get all data
    entered_customername = flask.request.form.get('cname')
    entered_customercontact= flask.request.form.get('ccontact')
    entered_area = flask.request.form.get('area')
    entered_avg_areahouseage = flask.request.form.get('ahouseage')
    entered_avg_areanumberofrooms= flask.request.form.get('anumberofrooms')
    entered_avg_areanumberofbedrooms = flask.request.form.get('anumberofbedrooms')
    entered_remarks = flask.request.form.get('remarks')
    entered_customername = entered_customername.lower()
    entered_customername = entered_customername.strip()

    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect('users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table")
    my_query = '''CREATE TABLE IF NOT EXISTS customer_table(
    CUSTOMERNAME    VARCHAR(100),
    CUSTOMERCONTACT   VARCHAR(100),
    AREA              VARCHAR(100),
    AVG_AREAHOUSEAGE    INTGER,
    AVG_AREANUMBEROFROOMS  INTGER,
    AVG_AREANUMBEROFBEDROOMS   INTGER,
    REMARKS   VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # -------------------------
    # verify whether user already exists in the database
    my_query = f"SELECT * FROM CUSTOMER_TABLE WHERE CUSTOMERNAME='{entered_customername}'AND CUSTOMERCONTACT='{entered_customercontact}' AND  AREA='{entered_area}' AND AVG_AREAHOUSEAGE='{entered_avg_areahouseage}' AND AVG_AREANUMBEROFROOMS='{entered_avg_areanumberofrooms}'AND AVG_AREANUMBEROFBEDROOMS='{entered_avg_areanumberofbedrooms}'AND REMARKS='{entered_remarks}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()  # [(),()]
    if len(my_db_result) > 0:
        return "Record Already Exists. Continuing with next record"
    # ------------------------
    # if user not exists then add new record to database and return account created successfully
    my_query = f"INSERT INTO CUSTOMER_TABLE( CUSTOMERNAME,CUSTOMERCONTACT, AREA,AVG_AREAHOUSEAGE,AVG_AREANUMBEROFROOMS,AVG_AREANUMBEROFBEDROOMS,REMARKS) VALUES('{entered_customername}', '{entered_customercontact}', '{entered_area}', '{entered_avg_areahouseage}', '{entered_avg_areanumberofrooms}', '{entered_avg_areanumberofbedrooms}', '{entered_remarks}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "We Received your form.  <a href='/'>Click Here To fill your qureirs</a>"
# --------------------
# END POINT - 11 : http://127.0.0.1:5000/logout URL MAPPED to '/logout'
# --------------------
@my_House_Price_Predictor_app.route('/logout')
def my_logout_page():
    session['username'] = None
    return flask.render_template('logout.html')
# --------------------
# Run the server
# --------------------
my_House_Price_Predictor_app.run()
# --------------------
