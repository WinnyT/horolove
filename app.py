from flask import Flask, render_template
from main import (
    calculate_planetary_positions,
    get_current_positions,
    analyze_transits,
    generate_daily_letter
)

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

    return render_template("display.html", letter=letter)

if __name__ == "__main__":
    app.run(debug=True)