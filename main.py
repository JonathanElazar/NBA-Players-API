import pandas as pd
from flask import Flask, request, jsonify, render_template
import markdown
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


needs_ratelimiting = True  # Set to True to enable rate limiting, False to disable it

app = Flask(
    __name__,
    static_folder="frontend/dist/assets",
    template_folder="frontend/dist"
)

if needs_ratelimiting:
    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["100 per hour"]
    )

db = pd.read_csv('NBA_PLAYERS.csv')

@app.errorhandler(404)
def not_found(error):
    return ("404 Not Found")

@app.errorhandler(500)
def internal_error(error):
    return ("500 Internal Server Error")



@app.route('/name/<first_name>/<last_name>')
def get_player_by_name(first_name, last_name):
    name = first_name.lower() + " " + last_name.lower()
    matched = db[db['Name'].str.lower() == name]
    return jsonify(matched.to_dict(orient='records'))

@app.route('/active-players/')
@app.route('/active-players/<amount>')
def get_players_by_active(amount=None):
    matched = db[db['Active'] == True]
    if amount is not None:
        matched = matched.head(int(amount))
    
    return jsonify(matched.to_dict(orient='records'))

@app.route('/players/top/pts/')
@app.route('/players/top/pts/<amount>')
def get_top_scorers(amount=None):
    top_amount = db.sort_values(by='PTS', ascending=False)
    if amount is not None:
        top_amount = top_amount.head(int(amount))
    
    return jsonify(top_amount.to_dict(orient='records'))

@app.route('/players/')
@app.route('/players/<amount>')
def get_all_players(amount=None):
    top_amount = db.sort_values(by='Name', ascending=True)
    if amount is not None:
        top_amount = top_amount.head(int(amount))
    
    return jsonify(top_amount.to_dict(orient='records'))

@app.route('/report_issue', methods=['POST'])
def report_issue():
    issue = request.get_json()
    with open('issues.txt', 'a') as f:
        f.write(markdown.markdown(issue['issue']) + "\n")
    
    return jsonify({"status": "success", "message": "Issue recorded"})


@app.route('/docs')
def docs():
    with open('docs.md', 'r', encoding='utf-8') as f:
        return markdown.markdown(f.read(), extensions=['fenced_code', 'codehilite'])

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)