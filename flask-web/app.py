from flask import Flask, jsonify, request, abort, redirect, url_for
from flask import render_template
from flask_restful import Api, Resource

app = Flask(__name__)

PROFILE_INFO = {
    'AUG': {
        'name_detail': 'AUG',
        'products': 'electro, music, parts',
        'active': 1000000,
        'avg_purchase': 55.50,
        'avg_shop_time': 18,
        'status': 'Active'
    },
    'MGH': {
        'name_detail': 'MGH',
        'products': 'electro, parts',
        'active': 2000000,
        'avg_purchase': 23.50,
        'avg_shop_time': 28,
        'status': 'Active'
    }
}

@app.route('/')
def index():
    item_list = ['Beam','Kafka','ElasticSearch']
    rendered_html = render_template('index.html', items=item_list)
    return rendered_html

@app.route('/profiles')
def profiles():
    return render_template('routing/profiles.html')

@app.route('/profile/<profile_name>')
def profile(profile_name):
    if profile_name not in PROFILE_INFO:
        abort(404)
    return render_template('routing/profile.html', profile=PROFILE_INFO[profile_name])

@app.route('/info')
def info():
    return redirect(url_for('request_info'), code=301)

@app.route('/request-info')
def request_info():
    return render_template('routing/request-info.html')

@app.route('/profile/<string:profile_name>/edit')
def profile_admin(profile_name):
    abort(401)

@app.errorhandler(404)
def not_found(error):
    return render_template('routing/404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=9090)
