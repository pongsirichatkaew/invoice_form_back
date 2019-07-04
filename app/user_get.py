from Config.config import *

# -----------------------login---------------------------------
@app.route('/api/v2/login', methods=['POST'])
@connect_sql()
def test_login(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg":"Missing JSON in request"}), 400
        else:
            username = request.json.get('username',None)
            password = request.json.get('password',None)
            if not username or not password:
                return jsonify({"msg":"Missing parameter"}), 400
            else:
                r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/login/'+username+'/'+password,headers= {'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                if r:
                    raw = r.text
                    raw = json.loads(raw)
                    sql = "SELECT role FROM user WHERE userid = %s"
                    if cursor.execute(sql,(raw['userid'])):
                        return "1"
                    else:
                        sql = """INSERT INTO `user`(name,lastname,userid) VALUES (%s,%s,%s)"""
                        cursor.execute(sql,(raw['name'],raw['lastname'],raw['userid']))
                        return "2"
                else:
                    return 'not nave user'
    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))
# # ---------------------menu-----------------------------------
@app.route('/api/v2/menu', methods=["POST"])
@connect_sql()
def menu(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg":"Missing JSON in request"}), 400
        else:
            user_id = request.json.get('user_id',None)
            if not user_id:
                return jsonify({"msg":"Missing parameter"}), 400
            else:
                sql = """SELECT role FROM user WHERE userid = %s"""
                if cursor.execute(sql,(user_id))
                    
                
    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))
# # ----------------------check_status_user---------------------------
# @app.route('/api/v2/check')

# # -----------------------------insert from-------------------
# @app.route('/api/v2/insert_from', methods=["POST"])
# @connect_sql()
# def insert_from(cursor):
#     try:

#     except Exception as e:
#         print ('error ===', e)
#         current_app.logger.info(e)
#         return jsonify(str(e))
# # ------------------------------update from-----------------------------
# @app.route('/api/v2/insert_from', methods=["POST"])
# @connect_sql()
# def insert_from(cursor):
#     try:

#     except Exception as e:
#         print ('error ===', e)
#         current_app.logger.info(e)
#         return jsonify(str(e))
# # ----------------------------approve from--------------------------

# @app.route('/jwt',methods=['POST'])
# @connect_sql()
# def jwt_ex(cursor):
#     JWT_SECRET = 'secret'
#     JWT_ALGORITHM = 'HS256'
#     JWT_EXP_DELTA_SECONDS = 20
#     payload = {
#         'user_id' : 'kkk',
#         'exp' : datetime.utcnow() + timedelta(seconds = JWT_EXP_DELTA_SECONDS)
#     }
#     jwt_token = jwt.encode(payload, JWT_SECRET,JWT_ALGORITHM)
#     return json_response({'token':jwt_token.decode('utf-8')})

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



# -------------------------------------------------------
# @app.route('/api/v1/login', methods=['POST'])
# @connect_sql()
# def login(cursor):
#     try:
#         checkUser = json.loads(getLogin())
#         f = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+checkUser['text']['userid'],headers= {'Authorization': 'a44ef9db-42c7-46a3-aea4-ee2fe6213ef3'})
#         getName = f.json()
#         if checkUser['text'] != 'fail' :
#             sql = " SELECT per_id FROM useradmin WHERE emp_id = %s"
#             cursor.execute(sql,(checkUser['text']['userid']))
#             data = cursor.fetchall()
#             columns = [column[0] for column in cursor.description]
#             report = toJson(data, columns)
#             if len(report) != 0 :
#                 return jsonify({'message': 'success', "error_message": None, "result": {'user':getName['employee_detail'][0], 'permisstion': report[0]['per_id']}}),200
#             else:
#                 return jsonify({'message': 'success', "error_message": None, "result": {'user':getName['employee_detail'][0], 'permisstion':'1'}}),200
#         else :
#             return jsonify({'message': 'fail', "error_message":"no user", "result": None}),200
#     except Exception as e:
#         current_app.logger.info(e)
#         return jsonify({'message': 'fail', "error_message": str(e), "result": None}),200
# def getLogin():
#     _data_new = request.json
#     data_new = json.loads(decode(_data_new['data']))
#     username = data_new['username']
#     password = data_new['password']
#     r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/login/'+username+'/'+password,headers= {'Authorization': 'a44ef9db-42c7-46a3-aea4-ee2fe6213ef3'})
#     if r:
#         return json.dumps({'text':r.json()})
#     else :
#         return json.dumps({'text':'fail'})