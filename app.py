from flask import Flask, render_template, request, jsonify
import os
import secrets


from main import (
    calculate_planetary_positions,
    get_current_positions,
    analyze_transits,
    generate_daily_letter
)
from datetime import date, datetime

app = Flask(__name__)

@app.get("/")
def display():
    birth_info = {
        "name": "Winny",
        "birth_date": "2000-09-22",
        "birth_time": "14:30",
        "birth_place": "Vietnam",
        "time-zone": "Asia/Ho_Chi_Minh"
    }

    birth_positions = calculate_planetary_positions(birth_info)
    current_positions = get_current_positions()
    transits = analyze_transits(birth_positions, current_positions)

    letter = generate_daily_letter(birth_info["name"], transits)

    today = date.today().strftime("%d %b %Y").upper()

    return render_template("display.html", letter=letter, date=today)

@app.post("/api/daily-letter")
def daily_letter_api():
    expected_key = os.environ.get("CELESTIAL_API_KEY")
    provided_key = request.headers.get("X-API-Key", "")

    if not expected_key or not secrets.compare_digest(
        provided_key, expected_key
    ):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}

    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")
    birth_timezone = data.get("timezone")


    if not all([name, birth_date, birth_time, birth_place, birth_timezone]):
        return jsonify({"error": "Missing birth information"}), 400

    birth_info = {
        "name": name,
        "birth_date": birth_date,
        "birth_time": birth_time,
        "birth_place": birth_place,
        "time-zone": birth_timezone
    }

    birth_positions = calculate_planetary_positions(birth_info)
    current_positions = get_current_positions()
    transits = analyze_transits(birth_positions, current_positions)
    letter = generate_daily_letter(name, transits)

    return jsonify({
        "date": date.today().strftime("%d %b %Y").upper(),
        "letter": letter
    })

if __name__ == "__main__":
    app.run(debug=True)