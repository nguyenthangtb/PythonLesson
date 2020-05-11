import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/users/<int:id>')
def student(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user WHERE id=%s", id)
        result = cursor.fetchone()
        res = jsonify(result)
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'There is no record: ' + request.url,
    }
    res = jsonify(message)
    res.status_code = 404

    return res

if __name__ == "__main__":
    app.run(debug=True)
