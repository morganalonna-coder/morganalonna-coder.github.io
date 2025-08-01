import os
import json
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Simulate checked_users.json as a Python dictionary
checked_users = {
    "yong.lixx": False,
    "gnabnahc": False,
    "hynjinnn": False,
    "miniseungkim": False,
    "t.leeknowsaurus": False,
    "i.2.n.8": False,
    "jutdwae": False,
    "_doolsetnet": False
}

# HTML and CSS combined as a template string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>STAY-Watcher</title>
  <style>
    body {
      background-color: #f5f0e6;
      font-family: 'Georgia', serif;
      color: #5c4438;
      text-align: center;
      padding: 40px;
    }
    .box {
      background: #fffaf3;
      padding: 25px;
      border-radius: 10px;
      box-shadow: 0 5px 10px rgba(0,0,0,0.1);
      display: inline-block;
    }
    h1 {
      font-size: 2.4em;
      margin-bottom: 10px;
    }
    p {
      font-size: 1.2em;
    }
  </style>
</head>
<body>
  <div class="box">
    <h1>STAY-Watcher</h1>
    <p>Keeping watch for SKZ Instagram Lives so you never miss a beat 💌</p>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/check")
def check():
    return jsonify({
        "message": "STAY-Watcher is running 🐺",
        "users_checked": list(checked_users.keys())
    })

@app.route("/healthz")
def healthz():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
