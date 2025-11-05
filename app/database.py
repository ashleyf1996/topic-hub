from sqlalchemy import create_engine

engine = create_engine('sqlite:///topicley.db', echo = True) #ECHO = true prints swl commands to terminal

