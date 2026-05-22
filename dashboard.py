from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


DATABASE = "database.db"


def get_logs():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT timestamp, severity, message
        FROM security_logs
        ORDER BY id DESC
        LIMIT 20
    """)

    logs = cursor.fetchall()

    connection.close()

    return logs


@app.route("/")
def dashboard():

    logs = get_logs()

    total_alerts = len(logs)

    critical_count = sum(
        1 for log in logs
        if log[1] == "CRITICAL"
    )

    high_count = sum(
        1 for log in logs
        if log[1] == "HIGH"
    )

    return render_template(
        "dashboard.html",
        logs=logs,
        total_alerts=total_alerts,
        critical_count=critical_count,
        high_count=high_count
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )