from sqlalchemy import create_engine, MetaData, Table, Boolean, Column, Integer, String, insert, select, text

engine = create_engine('sqlite:///topicley.db', echo = True) #ECHO = true prints swl commands to terminal
meta = MetaData()

cases = Table(
    'cases', 
    meta,
    Column('id', Integer, primary_key = True),
    Column('title', String),
    Column('solved', Boolean)
)

channels = Table(
    'channels', 
    meta,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('type', String)
)



meta.create_all(engine)

conn = engine.connect()
conn.execute(
 insert(cases).values(
  [
    {'title' : 'Jodi Arias', 'solved' : True},
    {'title' : 'Chris Watts', 'solved' : False},
    {'title' : 'Ted Bundy', 'solved' : True},
    {'title' : 'Brian Cohee', 'solved' : False},
    {'title' : 'Gabby Petito', 'solved' : True},
    ]
  )
  
 )
conn.execute(
 insert(channels).values(
  [
    {'name' : 'Jodi Arias channel', 'type' : 'true crime'},
 
    ]
  )
  
 )

# For cases table
s = cases.select().where(cases.c.title == "Jodi Arias")
conn = engine.connect()
result = conn.execute(s)

print('cases table: ')

for i in result:
    print(i )


