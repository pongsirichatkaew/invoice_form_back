from Config.config import *

# -----------------------login---------------------------------every User
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
                        columns = [column[0] for column in cursor.description]
                        result = toJson(cursor.fetchall(),columns)
                        raw.update(result[0])
                        return jsonify(raw) ,200
                    else:
                        sql = """INSERT INTO `user`(name,lastname,userid) VALUES (%s,%s,%s)"""
                        cursor.execute(sql,(raw['name'],raw['lastname'],raw['userid']))
                        raw.update({"role":"1"})
                        return jsonify(raw) ,200
                else:
                    return 'not nave user'
    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))
# ----------------------------- Add Admin ---------------------------User Level 2&3
# @app.route('/api/v2/add_admin', methods=["POST"])
# @connect_sql()
# def add_admin(cursor):
#     try:
#         if not request.is_json:
#             return jsonify({"msg":"Missing JSON in request"}), 400
#         else:
#             user_id = request.json.get('user_id',None)
#             if not user_id:
#                 return jsonify({"msg":"Missing parameter"}), 400
#             else:

#                 sql = """SELECT role FROM user WHERE userid = %s"""
#                 cursor.execute(sql,(user_id))
#                 role = toJson(cursor.fetchall(),'i')
#                 print ("SSS--------------",role[0]['i'])
#                 if role[0]['i'] == 1:
#                     print("hh1")
#                     sql = """SELECT * FROM from_debt WHERE userid = %s"""
#                     cursor.execute(sql,(user_id))
#                     columns = [column[0] for column in cursor.description]
#                     result = toJson(cursor.fetchall(),columns)
#                     return jsonify(result)
#                 elif role[0]['i'] == 2 or role[0]['i'] == 3:
#                     print("hhh2")
#                     sql = """SELECT * FROM from_debt"""
#                     cursor.execute(sql)
#                     columns = [column[0] for column in cursor.description]
#                     result = toJson(cursor.fetchall(),columns)
#                     return jsonify(result)
#                 else: 
#                     print('H23')
#                     return "NOT"

#     except Exception as e:
#         print ('error ===', e)
#         current_app.logger.info(e)
#         return jsonify(str(e))
# ---------------------menu------------------------------------------every User
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
                cursor.execute(sql,(user_id))
                role = toJson(cursor.fetchall(),'i')
                print ("SSS--------------",role[0]['i'])
                if role[0]['i'] == 1:
                    print("hh1")
                    sql = """SELECT * FROM from_debt WHERE userid = %s"""
                    cursor.execute(sql,(user_id))
                    columns = [column[0] for column in cursor.description]
                    result = toJson(cursor.fetchall(),columns)
                    return jsonify(result)
                elif role[0]['i'] == 2 or role[0]['i'] == 3:
                    print("hhh2")
                    sql = """SELECT * FROM from_debt"""
                    cursor.execute(sql)
                    columns = [column[0] for column in cursor.description]
                    result = toJson(cursor.fetchall(),columns)
                    return jsonify(result)
                else: 
                    print('H23')
                    return "NOT"

    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))
# ----------------------create from----------------------------------user Lv1
@app.route('/api/v2/create', methods=["POST"])
@connect_sql()
def create(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg":"Missing JSON in request"}), 400
        else:
            id_from           = request.json.get('id_from',None)
            id_customer       = request.json.get('id_customer',None)
            customer_name     = request.json.get('customer_name',None)
            Invoice_no        = request.json.get('Invoice_no',None)
            ref_SO            = request.json.get('ref_SO',None)
            amount_no_vat     = request.json.get('amount_no_vat',None)
            service           = request.json.get('service',None)
            from_year         = request.json.get('from_year',None)
            from_month        = request.json.get('from_month',None)
            to_year           = request.json.get('to_year',None)
            to_month          = request.json.get('to_month',None)
            change_income     = request.json.get('change_income',None)
            full              = request.json.get('full',None)
            full_text         = request.json.get('full_text',None)
            some              = request.json.get('some',None)
            some_text         = request.json.get('some_text',None)
            not_change_income = request.json.get('not_change_income',None)
            other             = request.json.get('other',None)
            text              = request.json.get('text',None)
            
            id_user           = request.json.get('id_user',None)
            if not id_user:
                return jsonify({"msg":"Missing parameter"}), 400
            else:
                sql = """SELECT role FROM user WHERE userid = %s"""
                if cursor.execute(sql,(id_from)):
                    print("A")
                else:
                    print("B")
    except Exception as e:
        print ('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))
# ----------------------Load from--------------------------- every User
# @app.route('/api/v2/load_from', methods=["POST"])
# @connect_sql()
# def load_from(cursor):
#     try:
#         if not request.is_json:
#             return jsonify({"msg":"Missing JSON in request"}), 400
#         else:
#             user_id = request.json.get('user_id',None)
#             id_from = request.json.get('id_from',None)
#             if not user_id or not id_from:
#                 return jsonify({"msg":"Missing parameter"}), 400
#             else:
#                 sql = """SELECT role FROM user WHERE userid = %s"""
#                 if cursor.execute(sql,(user_id)) :
                    
                    
#     except Exception as e:
#         print ('error ===', e)
#         current_app.logger.info(e)
#         return jsonify(str(e))
# ----------------------edit from----------------------------------user Lv1
# @app.route('/api/v2/edit', methods=["POST"])
# @connect_sql()
# def edit(cursor):
#     try:
#         if not request.is_json:
#             return jsonify({"msg":"Missing JSON in request"}), 400
#         else:
#             user_id = request.json.get('user_id',None)
#             if not user_id:
#                 return jsonify({"msg":"Missing parameter"}), 400
#             else:
#                 sql = """SELECT role FROM user WHERE userid = %s"""
#                 if cursor.execute(sql,(user_id))
                    
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