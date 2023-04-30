# import cx_Oracle

# cx_Oracle.init_oracle_client(lib_dir="C:\Oracle\Client\instantclient_21_9") # init Oracle instant client 位置
# connection = cx_Oracle.connect('GROUP10', 'Tp1wO39OPg', cx_Oracle.makedsn('140.117.69.60', 1521, service_name='ORCLPDB1'))
# cursor = connection.cursor()
# try:    
#     cx_Oracle.init_oracle_client(lib_dir="C:\Oracle\Client\instantclient_21_9") # init Oracle instant client 位置
#     connection = cx_Oracle.connect('GROUP10', 'Tp1wO39OPg', cx_Oracle.makedsn('140.117.69.60', 1521, service_name='ORCLPDB1'))
#     cursor = connection.cursor()

#     cursor.execute('SELECT * FROM MEMBER')
#     record = cursor.fetchall()
#     print(record)
#     print("okkkk")
#     connection.close()

# except Exception as e:
#     print(e)


import getpass
import cx_Oracle

connection = cx_Oracle.connect(
    user="GROUP10",
    password='Tp1wO39OPg',
    dsn="140.117.69.60/ORCLPDB1")

print("Successfully connected to Oracle Database")
cursor = connection.cursor() #創建一個游標(cursor)，用來執行sql查詢