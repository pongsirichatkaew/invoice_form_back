from Config.config import *


@app.route('/api/v1/menu', methods=["POST"])
@connect_sql()
def invoice_menu(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            user_id = request.json.get('user_id', None)
            if not user_id:
                return jsonify({"msg": "Missing parameter"}), 400
            else:
                sql = """SELECT role FROM user WHERE userid = %s """
                cursor.execute(sql, (user_id))
                role = toJson(cursor.fetchall(), 'i')
                print("SSS--------------", len(role))
                if len(role) == 0:
                    print('H23')
                    return "NOT"
                elif role[0]['i'] == 1:
                    print("hh1")
                    last_sql = """SELECT * FROM approve_debt_reduction ORDER BY id_document DESC"""
                    cursor.execute(last_sql)
                    columns = [column[0] for column in cursor.description]
                    last_result = toJson(cursor.fetchall(), columns)
                    print(last_result[0]['id_document'])
                    sql = """SELECT * FROM `approve_debt_reduction` WHERE id_user = %s and status != 'สิ้นสุด' and edit_status = 0 ORDER BY id_document """
                    cursor.execute(sql, (user_id))
                    columns = [column[0] for column in cursor.description]
                    result = toJson(cursor.fetchall(), columns)
                    for employee in result:
                        employee.update(
                            {'last_row': last_result[0]['id_document']})
                        inv_sql = "SELECT * FROM `approve_dev_reduction_invoice` WHERE id_document = %s AND edit_status = 0"
                        cursor.execute(inv_sql, (employee['id_document']))
                        columns = [column[0] for column in cursor.description]
                        inv_result = toJson(cursor.fetchall(), columns)
                        if(len(inv_result) > 0):

                            employee.update({'invoice': inv_result})

                        r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(employee['id_user']),
                                         headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                        raw = r.text
                        raw = json.loads(raw)
                        if 'message' in raw:
                            return jsonify({"msg": "user not in scrope"}), 401
                        else:
                            employee.update(
                                {'employee': raw['employee_detail'][0]})

                        if(employee['approved_by']):
                            print(employee['approved_by'])
                            r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(employee['approved_by']),
                                             headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                            raw = r.text
                            raw = json.loads(raw)
                            if 'message' in raw:
                                return jsonify({"msg": "user not in scrope"}), 401
                            else:
                                employee.update(
                                    {'employee_approved': raw['employee_detail'][0]})

                        if(employee['take_by']):
                            print(employee['take_by'])
                            r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(employee['take_by']),
                                             headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                            raw = r.text
                            raw = json.loads(raw)
                            if 'message' in raw:
                                return jsonify({"msg": "user not in scrope"}), 401
                            else:
                                employee.update(
                                    {'employee_take_by': raw['employee_detail'][0]})

                        if(employee['take_from']):
                            r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(employee['take_from']),
                                             headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                            raw = r.text
                            raw = json.loads(raw)
                            if 'message' in raw:
                                return jsonify({"msg": "user not in scrope"}), 401
                            else:
                                employee.update(
                                    {'employee_take_from': raw['employee_detail'][0]})       
                                                                      
                    return jsonify(result)
                elif role[0]['i'] == 2 or role[0]['i'] == 3:
                    print("hhh2")
                    sql = """ SELECT * FROM `approve_debt_reduction` WHERE status != 'สิ้นสุด' and edit_status = 0  ORDER BY id_document """
                    cursor.execute(sql)
                    columns = [column[0] for column in cursor.description]
                    result = toJson(cursor.fetchall(), columns)
                    for employee in result:
                        inv_sql = "SELECT * FROM `approve_dev_reduction_invoice` WHERE id_document = %s  AND edit_status = 0"
                        cursor.execute(inv_sql, (employee['id_document']))
                        columns = [column[0] for column in cursor.description]
                        inv_result = toJson(cursor.fetchall(), columns)
                        if(len(inv_result) > 0):
                            employee.update({'invoice': inv_result})

                        r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(employee['id_user']),
                                         headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                        raw = r.text
                        raw = json.loads(raw)
                        if 'message' in raw:
                            return jsonify({"msg": "user not in scrope"}), 401
                        else:
                            employee.update(
                                {'employee': raw['employee_detail'][0]})

                        if(employee['approved_by']):
                            print(employee['approved_by'])
                            r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(employee['approved_by']),
                                             headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                            raw = r.text
                            raw = json.loads(raw)
                            if 'message' in raw:
                                return jsonify({"msg": "user not in scrope"}), 401
                            else:
                                employee.update(
                                    {'employee_approved': raw['employee_detail'][0]})

                        if(employee['take_by']):
                            print(employee['take_by'])
                            r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(employee['take_by']),
                                             headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                            raw = r.text
                            raw = json.loads(raw)
                            if 'message' in raw:
                                return jsonify({"msg": "user not in scrope"}), 401
                            else:
                                employee.update(
                                    {'employee_take_by': raw['employee_detail'][0]})

                        if(employee['take_from']):
                            r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(employee['take_from']),
                                             headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                            raw = r.text
                            raw = json.loads(raw)
                            if 'message' in raw:
                                return jsonify({"msg": "user not in scrope"}), 401
                            else:
                                employee.update(
                                    {'employee_take_from': raw['employee_detail'][0]})                                    
                    return jsonify(result)

    except Exception as e:
        print('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))


@app.route('/api/v1/create', methods=["POST"])
@connect_sql()
def create(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            id_document = request.json.get('id_document', None)
            id_form = request.json.get('id_form', None)
            id_customer = request.json.get('id_customer', None)
            customer_name = request.json.get('customer_name', None)
            change_income = request.json.get('change_income', None)
            full = request.json.get('full', None)
            full_text = request.json.get('full_text', None)
            some = request.json.get('some', None)
            some_text = request.json.get('some_text', None)
            not_change_income = request.json.get('not_change_income', None)
            other = request.json.get('other', None)
            other_text = request.json.get('other_text', None)
            debt_text = request.json.get('debt_text', None)
            id_user = request.json.get('id_user', None)
            create_at = request.json.get('create_at', None)
            invoice = request.json.get('invoice', None)
            status = "รออนุมัติ"  # 3  N
            approved_by = request.json.get('approved_by', None)
            comment = request.json.get('comment', None)

            if not id_document or not id_form or not id_form or not id_customer or not customer_name:
                return jsonify({"msg": "Missing parameter"}), 400
            else:
                sql = """SELECT role FROM user WHERE userid = %s"""
                cursor.execute(sql, (id_user))
                role = toJson(cursor.fetchall(), 'i')
                if role:
                    create_at = datetime.now()
                    sql = """INSERT INTO `approve_debt_reduction`(`id_document`, `id_form`, `id_customer`, `customer_name`, `change_income`, `full`, `full_text`, `some`,
                    `some_text`, `not_change_income`, `other`, `other_text`, `debt_text`, `id_user`, `create_at`, `status`, `approved_by`, `comment`)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                     %s,%s,%s,%s,%s,%s)"""
                    cursor.execute(sql, (id_document, id_form, id_customer, customer_name, change_income, full, full_text, some, some_text, not_change_income, other, other_text, debt_text, id_user,
                                         create_at, status, approved_by, comment))
                    for inv in invoice:
                        inv_sql = """INSERT INTO  approve_dev_reduction_invoice(`id_document`, `invoice_no`, `ref_so`, `amount_no_vat`, `service`, `from_date`, `to_date`,edit_status)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,0)"""
                        cursor.execute(inv_sql, (id_document, inv['invoiceSlip'], inv['soNumber'],
                                                 inv['invoiceAmount'], inv['service'], inv['from_date'], inv['to_date']))
                    return jsonify("ss")
                else:
                    return jsonify("nss")
    except Exception as e:
        print('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))


@app.route('/api/v1/edit', methods=["POST"])
@connect_sql()
def edit(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            id_document = request.json.get('id_document', None)
            id_form = request.json.get('id_form', None)
            id_customer = request.json.get('id_customer', None)
            customer_name = request.json.get('customer_name', None)
            change_income = request.json.get('change_income', None)
            full = request.json.get('full', None)
            full_text = request.json.get('full_text', None)
            some = request.json.get('some', None)
            some_text = request.json.get('some_text', None)
            not_change_income = request.json.get('not_change_income', None)
            other = request.json.get('other', None)
            other_text = request.json.get('other_text', None)
            debt_text = request.json.get('debt_text', None)
            id_user = request.json.get('id_user', None)
            create_at = request.json.get('create_at', None)
            invoice = request.json.get('invoice', None)
            status = "รออนุมัติ"  # 3  N
            approved_by = request.json.get('approved_by', None)
            comment = request.json.get('comment', None)

            if not id_user or not create_at or not id_form or not id_customer or not customer_name:
                return jsonify({"msg": "Missing parameter"}), 400
            else:
                sql = """SELECT role FROM user WHERE userid = %s"""
                cursor.execute(sql, (id_user))
                role = toJson(cursor.fetchall(), 'i')
                if role[0]['i'] == 1:
                    sql = """UPDATE `approve_debt_reduction` SET status = 'สิ้นสุด',edit_status = 1 WHERE id_document = %s"""
                    cursor.execute(sql, (id_document))

                    del_sql = "UPDATE `approve_dev_reduction_invoice` SET edit_status = 1 WHERE id_document = %s"""
                    cursor.execute(del_sql, (id_document))

                    create_at = datetime.now()
                    sql = """INSERT INTO `approve_debt_reduction`(`id_document`, `id_form`, `id_customer`, `customer_name`, `change_income`, `full`, `full_text`, `some`,
                    `some_text`, `not_change_income`, `other`, `other_text`, `debt_text`, `id_user`, `create_at`, `status`, `approved_by`, `comment`)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                     %s,%s,%s,%s,%s,%s)"""
                    cursor.execute(sql, (id_document, id_form, id_customer, customer_name, change_income, full, full_text, some, some_text, not_change_income, other, other_text, debt_text, id_user,
                                         create_at, status, approved_by, comment))
                    for inv in invoice:
                        inv_sql = """INSERT INTO  approve_dev_reduction_invoice(`id_document`, `invoice_no`, `ref_so`, `amount_no_vat`, `service`, `from_date`, `to_date`, edit_status)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,0)"""
                        cursor.execute(inv_sql, (id_document, inv['invoiceSlip'], inv['soNumber'],
                                                 inv['invoiceAmount'], inv['service'], inv['from_date'], inv['to_date']))
                    return jsonify("ss")
                else:
                    return jsonify("nss")
    except Exception as e:
        print('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))


@app.route('/api/v1/approve', methods=["POST"])
@connect_sql()
def approve(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            status = request.json.get('status', None)
            id_from = request.json.get('id_from', None)
            edit_at = request.json.get('edit_at', None)
            id_user = request.json.get('id_user', None)
            comment = request.json.get('comment', None)
            sql = """SELECT role FROM user WHERE userid = %s"""
            cursor.execute(sql, (id_user))
            role = toJson(cursor.fetchall(), 'i')
            if role[0]['i'] == 2 or role[0]['i'] == 3:
                edit_at = datetime.now()
                sql = """UPDATE `approve_debt_reduction` SET status = %s,approved_by = %s,create_at = %s,comment = %s WHERE id_document = %s"""
                cursor.execute(
                    sql, (status, id_user, edit_at, comment, id_from))
                return jsonify("SS")
            else:
                return jsonify("wrong id"), 401
    except Exception as e:
        print('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))


@app.route('/api/v1/confirm', methods=["POST"])
@connect_sql()
def confirm(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            id_from = request.json.get('id_from', None)
            id_user = request.json.get('id_user', None)
            password = request.json.get('password', None)
            print(id_from)
            print(id_user)
            print(password)

            if not id_from or not id_user or not password:
                return jsonify({"msg": "Missing parameter"}), 400
            else:
                sql = """SELECT id_document FROM approve_debt_reduction  WHERE id_document = %s and id_user =%s and status = 'อนุมัติ' """
                cursor.execute(sql, (id_from, id_user))
                print(id_from, password)
                id_from2 = toJson(cursor.fetchall(), 'i')
                print(id_from2)
                if id_from2:
                    r = requests.get('http://hr.devops.inet.co.th:9999/api/v1/employee/'+str(password),
                                             headers={'Authorization': 'd0aa5a1d-a58b-4a45-9c99-1e1007408ef4'})
                    raw = r.text
                    raw = json.loads(raw)
                    if 'message' in raw:
                        return jsonify({"msg": "user not in scrope"}), 401
                    else:
                        edit_at = datetime.now()
                        sql = """UPDATE approve_debt_reduction SET status = 'รอส่งคืนเอกสาร',take_by = %s,take_at = %s WHERE id_document = %s"""
                        cursor.execute(sql, (password,edit_at, id_from))
                        return jsonify("SS")
                else:
                    return jsonify("No document_id"), 401
    except Exception as e:
        print('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))


@app.route('/api/v1/take', methods=["POST"])
@connect_sql()
def takeDocument(cursor):
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        else:
            id_from = request.json.get('id_from', None)
            id_user = request.json.get('id_user', None)
            password = request.json.get('password', None)
            take_from = request.json.get('take_from',None)

            if not id_from or not id_user or not password:
                return jsonify({"msg": "Missing parameter"}), 400
            else:
                sql = """SELECT id_document FROM approve_debt_reduction  WHERE id_document = %s and id_user =%s and status = 'รอส่งคืนเอกสาร' """
                cursor.execute(sql, (id_from, id_user))
                print(id_from, password)
                id_from2 = toJson(cursor.fetchall(), 'i')
                print(id_from2)
                if id_from2:
                    edit_at = datetime.now()
                    sql = """UPDATE approve_debt_reduction SET status = 'คืนเอกสารเรียบร้อยแล้ว',take_by = %s,take_from = %s,take_at = %s WHERE id_document = %s"""
                    cursor.execute(sql, (password, take_from,edit_at, id_from))
                    return jsonify("SS")
                else:
                    return jsonify("No document_id"), 401
    except Exception as e:
        print('error ===', e)
        current_app.logger.info(e)
        return jsonify(str(e))
