import os

import orjson
from flask import Blueprint, current_app, render_template
from main import main
from titantv.config import CONFIG

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    status_file = os.path.join(CONFIG["data_folder"], "api_output.json")
    if os.path.exists(status_file):
        with open(status_file, "rb") as f:
            status = orjson.loads(f.read())
    else:
        status = {"message": "No data available"}
    return render_template("index.html", status=status)


@bp.route("/update", methods=["POST"])
def update():
    try:
        result = main()
        return current_app.json.response(result)
    except Exception as e:
        return current_app.json.response({"status": "error", "message": str(e)})


@bp.route("/logs")
def logs():
    log_file = os.path.join(CONFIG["logs_folder"], CONFIG["log_file"])
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = f.readlines()[-100:]  # Last 100 lines
    else:
        logs = ["No logs available"]
    return render_template("logs.html", logs=logs)
