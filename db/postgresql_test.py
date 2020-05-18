import psycopg2

hostname = 'localhost'
username = 'norio'
password = 'norio'
database = 'a'

conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
cur = conn.cursor()

# Doping EMPLOYEE table if already exists.
cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
cur.execute("CREATE TABLE EMPLOYEE(fname CHAR(20) NOT NULL, lname CHAR(20));")
cur.execute("INSERT INTO EMPLOYEE(fname, lname) VALUES('A', 'B');")
res = cur.execute("SELECT fname, lname FROM EMPLOYEE;")
conn.close()
print(res)
