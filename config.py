import web

db_host = 'localhost'
db_name = 'ferreteriaamv'
db_user = 'agusmv'
db_pw = 'agusmv.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
