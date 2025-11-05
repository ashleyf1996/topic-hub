from sqlalchemy import create_engine, MetaData, Table, Boolean, Column, Integer, String


engine = create_engine('sqlite:///topicley.db', echo = True) #ECHO = true prints swl commands to terminal
meta = MetaData()

cases = Table(
    'cases', 
    meta,
    Column('id', Integer, primary_key = True),
    Column('title', String),
    Column('solved', Boolean)
)

meta.create_all(engine)