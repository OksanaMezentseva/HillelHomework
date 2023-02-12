from flask import Flask, request
from utils import execute_sql


app = Flask(__name__)


@app.route("/phones/create")
def phones_create():
    contact_name = request.args['contact_name']
    phone_value = request.args['phone_value']

    sql = f'''
    INSERT INTO Phones (contactName, phoneValue)
    VALUES ('{contact_name}', '{phone_value}');
    '''
    execute_sql(sql)
    return ''


@app.route("/phones/read")
def phones_read():
    import sqlite3
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()

    sql = '''
        SELECT * FROM Phones;
        '''
    res = cur.execute(sql)
    phones = res.fetchall()
    con.close()
    return phones

@app.route("/phones/update")
def phones_update():
    phone_id = request.args['phone_id']
    phone_value = request.args['phone_value']
    sql = f'''
    UPDATE Phones
    SET phoneValue = '{phone_value}'
    WHERE phoneID = {phone_id};
    '''
    execute_sql(sql)
    return ''


@app.route("/phones/delete")
def phones_delete():
    phone_id = request.args['phone_id']
    sql = f'''
    DELETE FROM Phones
    WHERE phoneID = {phone_id};
    '''
    execute_sql(sql)
    return ''


if __name__ == '__main__':
    app.run(debug=True)


