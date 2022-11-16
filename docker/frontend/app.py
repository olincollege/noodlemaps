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

# http://127.0.0.1:5000/query?origins=Boston%2CMA&end=Lexington%2CMA&midpoints=Needham%2CMA&departure_time=now&key=this_is_the_api_key
@app.route('/query')
def query():
    # Get keys, or return None if they don't exist
    start = request.args.get('start')
    end = request.args.get('end')
    midpoints = request.args.get('midpoints')
    key = request.args.get('key')

    return f'''<h1>The start location is: {start}</h1>\n
              <h2>The end location is: {end}</h2>\n
              <p>The midpoints are: {midpoints}</p>
              <p>The key is: {key}</p>'''

@app.route('/form', methods=['GET', 'POST'])
def form():
    # Handle the POST request
    if request.method == 'POST':
        # Get keys, or return None if they don't exist
        start = request.args.get('start')
        end = request.args.get('end')
        midpoints = request.args.get('midpoints')
        key = request.args.get('key')

        return f'''<h1>The start location is: {start}</h1>\n
                <h2>The end location is: {end}</h2>\n
                <p>The midpoints are: {midpoints}</p>
                <p>The key is: {key}</p>'''

    # Handle the GET request otherwise
    return '''
        <form method="POST">
            <p>Enter all values as comma-separated values <3 (ex. "Needham MA, Somerville MA, Seattle WA")</p>
            <div><label>Start: <input type="text" name="start"></label></div>
            <div><label>End: <input type="text" name="end"></label></div>
            <div><label>Midpoints: <input type="text" name="midpoints"></label></div>
            <div><label>API Key: <input type="text" name="key"></label></div>
            <input type="submit" value="Submit">
        </form>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')   # run Flask app