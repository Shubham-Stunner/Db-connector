from flask import Flask, jsonify
import mysql.connector
import cx_Oracle
import teradatasql
import pyhive.hive
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_mysql_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

def get_oracle_connection():
    dsn_tns = cx_Oracle.makedsn(app.config['ORACLE_HOST'], app.config['ORACLE_PORT'], service_name=app.config['ORACLE_DB'])
    return cx_Oracle.connect(user=app.config['ORACLE_USER'], password=app.config['ORACLE_PASSWORD'], dsn=dsn_tns)

def get_teradata_connection():
    return teradatasql.connect(
        host=app.config['TERADATA_HOST'],
        user=app.config['TERADATA_USER'],
        password=app.config['TERADATA_PASSWORD']
    )

def get_hive_connection():
    return pyhive.hive.connect(
        host=app.config['HIVE_HOST'],
        port=app.config['HIVE_PORT'],
        username=app.config['HIVE_USER'],
        password=app.config['HIVE_PASSWORD'],
        database=app.config['HIVE_DB']
    )

def check_db_connection(get_connection, db_type):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if db_type == 'mysql':
            cursor.execute("SELECT DATABASE()")
        elif db_type == 'oracle':
            cursor.execute("SELECT * FROM global_name")
        elif db_type == 'teradata':
            cursor.execute("SELECT DATABASE")
        elif db_type == 'hive':
            cursor.execute("SELECT current_database()")

        db_name = cursor.fetchone()[0]

        cursor.execute("SELECT 1 FROM dual" if db_type == 'oracle' else "SELECT 1")
        result = cursor.fetchone()

        return jsonify({"status": "Database online", "database": db_name}) if result else jsonify({"status": "Database offline", "database": db_name})
    except Exception as err:
        return jsonify({"status": "Database offline", "error": str(err)})
    finally:
        if conn:
            cursor.close()
            conn.close()

@app.route('/check_mysql', methods=['GET'])
def check_mysql():
    return check_db_connection(get_mysql_connection, 'mysql')

@app.route('/check_oracle', methods=['GET'])
def check_oracle():
    return check_db_connection(get_oracle_connection, 'oracle')

@app.route('/check_teradata', methods=['GET'])
def check_teradata():
    return check_db_connection(get_teradata_connection, 'teradata')

@app.route('/check_hive', methods=['GET'])
def check_hive():
    return check_db_connection(get_hive_connection, 'hive')

if __name__ == '__main__':
    app.run(debug=True)

