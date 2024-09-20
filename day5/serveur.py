from flask import Flask, render_template, jsonify, request
import json
import os
from urllib.parse import urlparse
from datetime import datetime
from browser_history.browsers import Firefox

app = Flask(__name__)

CATEGORIES_FILE = 'categories.json'

def load_categories():
    if not os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, 'w') as f:
            json.dump({}, f)
    with open(CATEGORIES_FILE, 'r') as f:
        return json.load(f)

def save_categories(categories):
    with open(CATEGORIES_FILE, 'w') as f:
        json.dump(categories, f, indent=4)

def get_base_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    # Remove 'www.' prefix if present
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain

def fetch_browsing_history():
    f = Firefox()

    outputs = f.fetch_history()
    # histories is a list of (datetime.datetime, url) tuples
    histories = outputs.histories
    # Load existing categories
    categories = load_categories()
    # Convert to a list of dictionaries and extract base URLs
    site_data = {}

    for info in histories:
        
        base_url = get_base_url(info[1])
        timestamp = info[0].isoformat()
        if base_url in site_data:
            site_data[base_url]['visits'] += 1
            site_data[base_url]['timestamps'].append(timestamp)
        else:
            site_data[base_url] = {
                'url': base_url,
                'visits': 1,
                'categories': categories.get(base_url, []),
                'timestamps': [timestamp]
            }
    # Convert site_data to a list
    sites = list(site_data.values())
    return sites

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sites', methods=['GET'])
def api_get_sites():
    sites = fetch_browsing_history()
    return jsonify(sites)

@app.route('/api/sites/<string:url>/categories', methods=['POST'])
def update_site_categories(url):
    data = request.get_json()
    new_categories = data.get('categories', [])
    categories = load_categories()
    categories[url] = new_categories
    save_categories(categories)
    return jsonify({'status': 'categories updated'}), 200

if __name__ == '__main__':
    app.run(debug=True)
