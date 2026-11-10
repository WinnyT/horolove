import swisseph as swe
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


birth_info = {
    "name": "Winny",
    "birth_place": "New York, USA",
    "datetime": "1990-01-01 12:00:00",
    "time-zone": "America/New_York"
}


def ask_birth_info():
    print("Please provide the following birth information:")
    birth_info["name"] = input("Name: ")
    birth_info["birth_place"] = input("Birth Place: ")
    birth_info["datetime"] = input("Birth Date and Time (YYYY-MM-DD HH:MM): ")
    birth_info["time-zone"] = input("Time Zone (e.g., America/New_York): ")
    print("Name:", birth_info["name"])
    print("Birth Date:", birth_info["birth_date"])
    print("Birth Place:", birth_info["birth_place"])
    print("Birth Time:", birth_info["birth_time"])
    print("Time Zone:", birth_info["time-zone"])

def assign_time_zone(birth_info):
    tz = ZoneInfo(birth_info["time-zone"])
    birth_datetime = datetime.strptime(birth_info["birth_date"] + " " + birth_info["birth_time"], "%Y-%m-%d %H:%M")
    birth_datetime = birth_datetime.replace(tzinfo=tz)
    birth_datetime = birth_datetime.astimezone(timezone.utc)
    return birth_datetime


def calculate_planetary_positions(birth_info):
    birth_datetime = assign_time_zone(birth_info)
    jd = swe.julday(birth_datetime.year, birth_datetime.month, birth_datetime.day, birth_datetime.hour + birth_datetime.minute / 60.0)
    planets = ["Sun", "Moon", "Venus"]
    positions = {}
    for planet in planets:
        planet_id = getattr(swe, planet.upper())
        position = swe.calc_ut(jd, planet_id)[0]
        positions[planet] = position[0]
        return positions

def get_zodiac_sign(longitude):
    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio",
        "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    sign_index = int(longitude // 30) % 12
    return zodiac_signs[sign_index]

if __name__ == "__main__":
    ask_birth_info()
    for planet, position in calculate_planetary_positions(birth_info).items():
        zodiac_sign = get_zodiac_sign(position)
        print(f"{planet}: {position:.2f}° - {zodiac_sign}")




