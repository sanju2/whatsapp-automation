from flask import Flask, redirect
import json

app = Flask(__name__)

# Load group URLs from a JSON file
with open('groups.json') as f:
    groups = json.load(f)

current_group = 1

@app.route('/')
def redirect_to_group():
    global current_group
    # Redirect to the current group
    group_url = groups[current_group]
    return redirect(group_url)

@app.route('/update_group')
def update_group():
    global current_group
    # Logic to update the group when full
    if current_group < len(groups) - 1:
        current_group += 1
    return "Group updated"

if __name__ == '__main__':
    app.run(debug=True)

