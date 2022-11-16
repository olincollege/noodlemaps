# python3 -m flask run in current folder
import time, redis
from flask import Flask, request

# Resource for building REST API:
#   https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/name/<visitor_name>')
def say_hi_to_visitor(visitor_name):
    return f"Hello {visitor_name}!"

# http://127.0.0.1:5000/query-example?origins=Boston%2CMA%7CNeedham%2CMA&destinations=Lexington%2CMA%7CNeedham%2CMA&departure_time=now&key=this_is_the_api_key
@app.route('/query-example')
def query_example():
    # Get origins
    origins = request.args.get('origins')
    dests = request.args.get('destinations')
    key = request.args.get('key')

    return f'''<h1>The origins value is: {origins}</h1>\n
              <h2>The destinations value is: {dests}</h2>\n
              <p>The key is: {key}</p>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0')   # run Flask app