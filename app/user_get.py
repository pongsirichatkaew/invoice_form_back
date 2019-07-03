from config import *

@app.route('/jwt',methods=['POST'])
@connect_sql()
def jwt_ex(cursor):
    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'
    JWT_EXP_DELTA_SECONDS = 20
    payload = {
        'user_id' : 'kkk',
        'exp' : datetime.utcnow() + timedelta(seconds = JWT_EXP_DELTA_SECONDS)
    }
    jwt_token = jwt.encode(payload, JWT_SECRET,JWT_ALGORITHM)
    return json_response({'token':jwt_token.decode('utf-8')})

@app.route('/getUserID/<id>',methods = ['GET'])
@connect_sql()
def getUserID(cursor,id):
    sql = "SELECT * FROM `user` WHERE `id` = %s"
    cursor.execute(sql,(id))
    columns = [column[0] for column in cursor.description]
    result = toJson(cursor.fetchall(),columns)
    return jsonify(result)

@app.route('/test',methods = ['GET'])
@connect_sql()
def test(cursor):
    sql = "SELECT * FROM `user` WHERE `id` = %s"
    cursor.execute(sql,1)
    columns = [column[0] for column in cursor.description]
    print(columns)
    print('-------------------------------------')
    # print(cursor.fetchall())
    result = toJson(cursor.fetchall(),columns)
    return jsonify(send_success(result[0]))

@app.route('/login/<user>', methods=['GET'])
@connect_sql()
def check_user(cursor,user):
    try:
        sql = "SELECT user_img FROM `user` WHERE `username` =%s"
        if cursor.execute(sql,user):
            cursor.execute(sql,user)
            columns = [column[0] for column in cursor.description]
            result = toJson(cursor.fetchall(),columns)
            return jsonify(result)
            print('kkk')
        else:
            return 'not'
            print('nnnn')
        print('cursor.execute:',cursor.execute(sql,user))
       
    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))

@app.route('/login', methods=['POST'])
@connect_sql()
def login(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            username = request.json.get('username', None)
            password = request.json.get('password', None)
            if not username or not password:
                return jsonify({"msg": "Missing username parameter"}), 400
            else:
                sql = "SELECT * FROM `user` WHERE `username` =%s AND `password` =%s"
                if cursor.execute(sql,(username,password)):
                    cursor.execute(sql,(username,password))
                    columns = [column[0] for column in cursor.description]
                    result = toJson(cursor.fetchall(),columns)
                    return jsonify(result)
                else:
                    return 'worng'
    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))

@app.route('/confirm_register/<username>/<password>', methods=['GET'])
@connect_sql()
def confirm_register(cursor,username,password):
    try:
        sql = "UPDATE `user` SET `confirm_status` = '1' WHERE `username` = %s AND `password` = %s"
        cursor.execute(sql,(username,password))
        return jsonify({"status":200,"msg":"ok","data":"ss"})
    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))

@app.route('/register', methods=['POST'])
@connect_sql()
def register(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg":"Missing JSON in request"}), 400
        else:
            tell = request.json.get('tell',None)
            email = request.json.get('email',None)
            fname = request.json.get('fname',None)
            lname = request.json.get('lname',None)
            username = request.json.get('username',None)
            password = request.json.get('password',None)
            confirm_status = 0
            if not tell or not email or not fname or not lname or not username or not password:
                return jsonify({"msg": "Missing parameter"}), 400
            else:
                sql = "INSERT INTO user (fname, lname, username, password, email, tell, confirm_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql,(fname,lname,username,password,email,tell,confirm_status))
                # ----------------------send mail-------------------------
                msg = Message('Hello2', sender = 'navamail@pasail.com', recipients = [email])
                msg.html = "<h2>Hello Flask message sent from Flask-Mail3</h2> <h3>check mail :</h3> http://localhost:5000/confirm_register/%s/%s"%(username,password)
                mail.send(msg)
                # ----------------------show database---------------------
                # sql = "SHOW DATABASES"
                # cursor.execute(sql)
                # columns = [column[0] for column in cursor.description]
                # ShowDatabases = toJson(cursor.fetchall(),columns)
                # print('SHDB:',ShowDatabases)
                # for x in range(len(ShowDatabases)):
                #     print(ShowDatabases[x]['Database'])
                # if 'Database' in ShowDatabases:
                #     print('have')
                # print('not have')
                # ----------------------show tables-----------------------
                # sql = "SHOW TABLES"
                # cursor.execute(sql)
                # ShowTables = cursor.fetchall()
                # print('SHTB:',ShowTables)
                return jsonify({"msg": "ss"})

    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))

            
            
@app.route("/mail")
def index():
   msg = Message('ปลาแซลเองจ้า', sender = 'navamail@pasail.com', recipients = ['pongsiri.ch@inet.co.th'])
   msg.html = "<h2>this is PASAILMON</h2> <h3>check mail :</h3> http://localhost:5000/login"
   mail.send(msg)
   return "Sent"