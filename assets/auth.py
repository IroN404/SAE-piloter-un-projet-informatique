import pymysql # Importing PyMySQL in order to connect to MySQL database

# Function to define DDB connection infos
def define_infos():
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'root'
    db_name = 'db_name'

# Function to authenticate a user (checking if username / password are in corresponding table)
def authenticate(username, password): # username and password are the values entered by the user in the login page
    define_infos() # calling the function to define DDB connection infos
    try: # trying to connect to the DDB
        connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)
        cursor = connection.cursor() # creating a cursor object
        # executing the query to check if username / password are in corresponding table
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone() # fetching the result of the query

        cursor.close() # closing the cursor
        connection.close() # closing the connection
    except Exception as e: # if an error occurs
        print(e) # print it
        return False # return False

# Function to signup a user (adding username / password in corresponding table)
#def signup(username, password):

# Function to get user's tasks (getting all tasks from corresponding table for a specific user)
#def get_user_tasks(username):

# Function to add a task (adding a task in corresponding table for a specific user)
#def add_task(username, task):

# Function to delete a task (deleting a task from corresponding table for a specific user)
#def delete_task(username, task):

# Function to update a task (updating a task from corresponding table for a specific user)
#def update_task(username, task):