from flask import Flask, render_template, request
import requests
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-url', methods=['POST'])
def check_url():
    url = request.form['url']
    robots_txt_content = fetch_robots_txt(url)
    return f"Checking URL: {url}\nRobots.txt content:\n{robots_txt_content}"

def fetch_robots_txt(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'http://' + url
    robots_txt_url = urljoin(url, '/robots.txt')
    try:
        request_call = requests.get(robots_txt_url)
        if request_call.status_code == 200:
            return request_call.text
        else:
            return f"Unable to fetch robots from {url}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)