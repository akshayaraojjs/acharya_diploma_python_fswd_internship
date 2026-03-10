import MySQLdb

try:
    con = MySQLdb.connect(host='localhost', port=3307, user='root', password='')
    con.cursor().execute('CREATE DATABASE IF NOT EXISTS student_enrollment_system')
    print("Database created or already exists")
except Exception as e:
    print(f"Error: {e}")
