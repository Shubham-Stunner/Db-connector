import mysql.connector
import cx_Oracle
import teradatasql
from pyhive import hive
from config import Config

def check_mysql():
    try:
        conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        return "online" if result else "offline"
    except mysql.connector.Error as err:
        return f"offline, error: {str(err)}"

def check_oracle():
    try:
        dsn = cx_Oracle.makedsn(Config.ORACLE_HOST, Config.ORACLE_PORT, sid=Config.ORACLE_DB)
        conn = cx_Oracle.connect(user=Config.ORACLE_USER, password=Config.ORACLE_PASSWORD, dsn=dsn)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM DUAL")
        result = cursor.fetchone()
        conn.close()
        return "online" if result else "offline"
    except cx_Oracle.DatabaseError as err:
        return f"offline, error: {str(err)}"

def check_teradata():
    try:
        conn = teradatasql.connect(
            host=Config.TERADATA_HOST,
            user=Config.TERADATA_USER,
            password=Config.TERADATA_PASSWORD,
            database=Config.TERADATA_DB
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        return "online" if result else "offline"
    except teradatasql.DatabaseError as err:
        return f"offline, error: {str(err)}"

def check_hive():
    try:
        conn = hive.Connection(
            host=Config.HIVE_HOST,
            port=Config.HIVE_PORT,
            username=Config.HIVE_USER,
            password=Config.HIVE_PASSWORD,
            database=Config.HIVE_DB
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        return "online" if result else "offline"
    except Exception as err:
        return f"offline, error: {str(err)}"
