import sqlalchemy as db
from sqlalchemy import text
import pandas as pd

connection_string = 'postgresql://postgres.orkyzebkktkifsjmlzpi:Nurlybekov123@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres'
engine = db.create_engine(connection_string)

def add_data(table_name, arr):
	with engine.connect().execution_options(autocommit=True) as con:
		con.execute(text("insert into {table_name} values {arr}".format(table_name=table_name, arr='(\'' + '\' ,\''.join(arr) + '\')')))

def update_data(table_name, row, data):
	with engine.connect().execution_options(autocommit=True) as con:
		id_name = data.columns[0]
		query = 'update '+ table_name + ' set ' 
		for i in range(1, len(data.columns)):
			query += str(data.columns[i]) + ' =\'' + str(data.iloc[row, i]) + '\','
		query = query[:-1] + ' where ' + str(id_name) + ' = ' + '\''+str(data.iloc[row,0]+'\'')
		con.execute(query)


def read_data(table_name):
    with engine.connect() as con:
        query = db.text(f'SELECT * FROM "{table_name}"')  # Using db.text for SQL statement
        result = con.execute(query)
        df = pd.DataFrame(result.fetchall())
        if len(df.columns) > 0:
            df.columns = result.keys()
        return df

def delete_data(table_name, row, data):
	with engine.connect().execution_options(autocommit=True) as con:
		id_name = data.columns[0]
		query = 'delete from ' + table_name + ' where ' + str(id_name) + ' = \'' + str(data.iloc[row,0])+'\''
		con.execute(query)

def check_user_id_exists(user_id):
    with engine.connect() as con:
        query = db.text("SELECT EXISTS(SELECT 1 FROM Users WHERE user_id = :user_id)")
        result = con.execute(query, {'user_id': user_id}).fetchone()
        return result[0]
	
def check_member_id_exist(user_id):
	with engine.connect() as con:
		query = db.text("SELECT EXISTS(SELECT 1 FROM Member WHERE member_user_id = :user_id)")
		result = con.execute(query, {'user_id': user_id}).fetchone()
		return result[0]

def check_job_id_exist(job_id):
	with engine.connect() as con:
		query = db.text("SELECT EXISTS(SELECT 1 FROM Job WHERE job_id = :job_id)")
		result = con.execute(query, {'job_id': job_id}).fetchone()
		return result[0]

