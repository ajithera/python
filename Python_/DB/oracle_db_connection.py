# To connect oracle db to python we need 'cx_oracle'.
# Try this 'pip install cx_Oracle' in python terminal. If it throws any error,
# then try 'pip3 install cx_Oracle' in command promt(run as admin).

import cx_Oracle

#create connection - 'username/password@//hostname:port/sid'  --You can find this values in connection properties

conn = cx_Oracle.connect('HR/hr@//localhost:1521/orcl')
print(conn.version)

# opening cursor for executing sql
cur = conn.cursor()

# Executing select statement
cur.execute('select employee_id,first_name,salary from employees')
for line in cur:
    print(line)

# Create table

cur.execute("""
CREATE TABLE AJITHERA
(
    NAME VARCHAR2(10),
    AGE NUMBER

)
""")

drop_tbl = 'DROP TABLE AJITHERA '

cur.execute(drop_tbl)

# after working it is neccessary to close cursor and conection

cur.close()
conn.close()