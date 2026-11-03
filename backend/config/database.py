import mariadb

def get_connection():

    return mariadb.connect(
        host="localhost",
        port=3306,
        user="crowedu",
        password="password",
        database="crowedu"
    )