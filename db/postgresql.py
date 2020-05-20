SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'norio',
    'password': 'norio',
    'host': '127.0.0.1',
    'name': 'db.postgresql'
})
