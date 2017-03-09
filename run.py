import os
from eve import Eve

'''
# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'
'''

my_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'the_db_name',
    'DOMAIN': {
        'contacts': {},
    }
}

app = Eve()
# app.run(host='127.0.0.1', port=5000, settings=my_settings)
app.run(host='127.0.0.1', port=5000)

'''
if __name__ == '__main__':
    app.run(host=host, port=port)
'''

