import os
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from dotenv import load_dotenv
load_dotenv()


db_password = os.getenv("DB_PASSWORD")

engine = create_engine(f'mysql+pymysql://addmin_user:{db_password}@local-aurora-mysql:3306/gym_db')

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(255)),
              Column('age', Integer),
              Column('email', String(255))
              )

metadata.create_all(engine)

insert_stmt = users.insert().values(
    name='Alice', age=25, email='alice@example.com')
conn = engine.connect()
conn.execute(insert_stmt)
conn.commit()
print("commit finish")
select_stmt = users.select()
result = conn.execute(select_stmt)
for row in result:
    print(row)