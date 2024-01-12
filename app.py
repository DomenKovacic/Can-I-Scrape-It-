from flask import Flask, render_template, request
import requests
from urllib.parse import urlparse,urljoin

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/check-url', methods=['POST'])
def check_url():
    url = request.form['url']
    return f"Checking URL: {url} "

def fetch_robots_txt(url):
    parsed_url = urlparse(url)
    robots_txt = urljoin(parsed_url, '/robots.txt')
    try:
        request_call = requests.get(robots_txt)
        if request_call.status_code == 200:
            return request_call.text
        else:
            return f"Unable to fetch robots from {url}"
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)