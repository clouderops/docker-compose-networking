import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'do a GET on /db'

@app.route('/database')
def write_to_db():
    print("postgres")
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password = "WRONG_PASSWORD",
                                    host = "database",
                                    port = "5432",
                                    database = "postgres")

        return("connected to postgresql")

    except (Exception, psycopg2.Error) as error :
        return ("Error while connecting to PostgreSQL", error)


     

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)