# 1. Import Psycopg2
# 2. Create connection
# 3. Create Cursor
# 4. Execute The Query
# 5. Close the Cursor
# 6. Close Connection


########## 1. Import Psycopg2 ##############

import psycopg2
import os , sys

####### 2. Create connection #########

conn = None

conn =  psycopg2.connect(database = "test_db",
user = 'postgres',
password = "write_passward_here", # write the password here 
host = "localhost",
port = "5432")


########### 3. Create Cursor ##########

cur = conn.cursor()

########## # 4. Execute The Query ##########

cur.execute('''create table examployee (emp_num int primary key, emp_name varchar(40),dep_name varchar(40))''')

conn.commit()


######### 5. Close the Cursor #############
cur.close()

############ 6. Close Connection ########
conn.close()
