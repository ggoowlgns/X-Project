import MySQLdb

connection = MySQLdb.connect (host = "localhost",
                              user = "root",
                              passwd = "root",
                              db = "xproj")

cursor = connection.cursor()

id = 'ggoowlgns'
passwd = '1234'
name = 'park-ji-hoon'
email = 'ggoowlgns@naver.com'

staff_data = [(id,passwd,name,email),
              (id, passwd, name, email)]

for p in staff_data:
    format_str = """INSERT INTO MEMBERS (id , passwd , name , email)
    VALUES ( '{id}' , '{passwd}', '{name}' , '{email}');
    """

    sql_command = format_str.format(id = p[0], passwd = p[1], name = p[2] , email = p[3])
    print(sql_command)
    cursor.execute(sql_command)

connection.commit()
cursor.close()
connection.close()