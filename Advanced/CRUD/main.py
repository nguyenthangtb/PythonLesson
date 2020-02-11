from flask import Flask, request
import pymysql
from flask import jsonify
import datetime

app = Flask(__name__)


class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "123"
        db = "demo"

        self.con = pymysql.connect(host=host,
                                   user=user, password=password,
                                   db=db, cursorclass=pymysql.cursors.DictCursor)

        self.cur = self.con.cursor()


@app.route('/users', methods=['POST'])
def userAdd():
    try:
        _jsonData = request.json
        _userName = _jsonData['user_name']
        _userEmail = _jsonData['user_email']
        _userPass = _jsonData['user_password']
        _userBirthday = ''

    
        db = Database()

        sql = "INSERT INTO tbl_user(user_name, user_email, user_password, birthday_date) VALUES(%s, %s, %s, %s)"
        data = (_userName, _userEmail, _userPass, _userBirthday)
        db.cur.execute(sql, data)
        db.con.commit()
        message = {
            'status': 200,
            'message': 'User added successfully!'
        }
        return jsonify(message)

    except Exception as e:
        message = {
            'status': 500,
            'message': 'User added fail!',
        }
        return jsonify(message)
    finally:
        db.cur.close()
        db.con.close()


@app.route('/users/<int:id>', methods=['PUT'])
def userUpdate(id):
    try:
        _jsonData = request.json
        _userName = _jsonData['user_name']
        _userEmail = _jsonData['user_email']
        _userPass = _jsonData['user_password']

        db = Database()
        sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
        data = (_userName, _userEmail, _userPass, id)
        db.cur.execute(sql, data)
        db.con.commit()
        message = {
            'status': 200,
            'message': 'User updated successfully!'
        }
        return jsonify(message)

    except Exception as e:
        message = {
            'status': 500,
            'message': 'User updated fail!'
        }
        return jsonify(message)
    finally:
        db.cur.close()
        db.con.close()


@app.route('/users', methods=['GET'])
def users():
    db = Database()
    db.cur.execute("select * from tbl_user LIMIT 50")
    result = db.cur.fetchall()
    result[3]['birthday_date'] = datetime.datetime.strptime(str(result[3]['birthday_date']), '%Y-%m-%d %H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(result)


@app.route('/user/<id>', methods=['GET'])
def userDetail(id):
    count = checkData(id)
    if count != 0:
        db = Database()
        db.cur.execute("select * from tbl_user where user_id=%s", id)
        result = db.cur.fetchone()
        return jsonify(result)
    else:
        message = {
            'status': 404,
            'message': 'User not found ',
        }
        return jsonify(message)


@app.route('/user/<id>', methods=['DELETE'])
def userDelete(id):

    count = checkData(id)
    if count != 0:
        db = Database()
        db.cur.execute('delete from tbl_user where user_id=%s', id)
        db.con.commit()
        message = {
            'status': 200,
            'message': 'User deleted successfully!'
        }
        return jsonify(message)
    else:
        message = {
            'status': 404,
            'message': 'User not found!'
        }
        return jsonify(message)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


def checkData(id):
    db = Database()
    db.cur.execute("select * from tbl_user where user_id=%s", id)
    result = db.cur.rowcount
    return result


if __name__ == "__main__":
    app.run(debug=True)
