
import os, time
from datetime import datetime
from flask import Flask, render_template, jsonify
from strategy import Bot

app = Flask(__name__)
bot = Bot()

LAST_UPDATE = 0
INTERVAL_SEC = int(os.getenv("INTERVAL_SEC", "60"))

@app.route("/")
def index():
    pocket_url = "https://pocketoption.com/en/"
    return render_template("index.html", pocket_url=pocket_url, interval=INTERVAL_SEC)

@app.route("/api/status")
def api_status():
    global LAST_UPDATE
    now = time.time()
    refreshed = False
    if now - LAST_UPDATE >= INTERVAL_SEC:
        bot.update()
        LAST_UPDATE = now
        refreshed = True
    payload = {
        "signal": bot.signal,
        "confidence": bot.confidence,
        "stats": bot.stats,
        "updated_at": datetime.utcnow().isoformat()+"Z",
        "refreshed": refreshed,
        "next_in": max(0, INTERVAL_SEC - int(now - LAST_UPDATE)),
        "chart": bot.chart_data
    }
    return jsonify(payload)

if __name__ == "__main__":
    port = int(os.getenv("PORT","5000"))
    app.run(host="0.0.0.0", port=port)
