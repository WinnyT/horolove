import swisseph as swe
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from interpretations import interpretations


birth_info = {
    "name": "Winny",
    "birth_place": "New York, USA",
    "birth_date": "2000-09-22",
    "birth_time": "14:30",
    "time-zone": "America/New_York"
}


def ask_birth_info():
    print("Please provide the following birth information:")
    birth_info["name"] = input("Name: ")
    birth_info["birth_place"] = input("Birth Place: ")
    birth_info["birth_date"] = input("Birth Date (YYYY-MM-DD): ")
    birth_info["birth_time"] = input("Birth Time (HH:MM): ")
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

def get_current_positions():
    now = datetime.now(timezone.utc)
    jd = swe.julday(now.year, now.month, now.day, now.hour + now.minute / 60.0)
    planets = ["Sun", "Moon", "Venus"]
    positions = {}
    for planet in planets:
        planet_id = getattr(swe, planet.upper())
        position = swe.calc_ut(jd, planet_id)[0]
        positions[planet] = position[0]
    return positions

def calculate_aspects(longtitude1, longtitude2):
    aspects = {
        "Conjunction": 0,
        "Sextile": 60,
        "Square": 90,
        "Trine": 120,
        "Opposition": 180
    }
    closest_aspect = None
    smallest_difference = float('inf')
    different = abs(longtitude1 - longtitude2) % 360
    distance = min(different, 360 - different)
    for aspect, angle in aspects.items():
        deviation = abs(distance - angle)

        if deviation < smallest_difference:
            smallest_difference = deviation
            closest_aspect = aspect
            closest_angle = angle

    if smallest_difference <= 5:
        return closest_aspect, closest_angle, smallest_difference

    return None, None, None

def analyze_transits(birth_positions, current_positions):
    aspects = {}
    for planet1, position1 in birth_positions.items():
        for planet2, position2 in current_positions.items():
            aspect, angle, deviation = calculate_aspects(position1, position2)
            if aspect:
                aspects[(planet1, planet2)] = (aspect, angle, deviation)
    return aspects

def print_transits(birth_positions, current_positions):
    for (natal, transit), (aspect, angle, deviation) in analyze_transits(birth_positions, current_positions).items():
        print(f"{transit} {aspect} natal {natal} (orb: {deviation:.2f}°)")

def get_interpretation(transit, natal, aspect):
    if transit in interpretations and aspect in interpretations[transit]:
        if natal in interpretations[transit][aspect]:
            return interpretations[transit][aspect][natal]
    return None

def rank_transits(transits):
    ranked_transits = sorted(transits.items(), key=lambda x: x[1][2])
    return ranked_transits

def generate_daily_letter(name,transits):
    letter = f"Dear {name},\n\n"
    letter += "Here's what the stars have to say today:\n\n"
    ranked_transits = rank_transits(transits)[:2]
    reading_added = 0
    for (natal, transit), (aspect, angle, deviation) in ranked_transits:
        interpretation = get_interpretation(transit, natal, aspect)
        if interpretation:
            letter += f"\n{transit} {aspect} natal {natal} (orb: {deviation:.2f}°)\n"
            letter += interpretation["title"] + "\n"
            letter += interpretation["message"] + "\n"
            reading_added += 1
    if reading_added == 0:
        letter += "Today is a quieter day in your celestial chart. Take a moment to reflect on what matters most to you.\n"
    letter += "\nWith love, the stars"
    return letter

if __name__ == "__main__":
    ask_birth_info()
    birth_positions = calculate_planetary_positions(birth_info)
    current_positions = get_current_positions()
    transits = analyze_transits(birth_positions, current_positions)
    for planet, position in birth_positions.items():
        zodiac_sign = get_zodiac_sign(position)
        print(f"{planet}: {position:.2f}° - {zodiac_sign}")
    for (natal, transit), (aspect, angle, deviation) in transits.items():
        interpretation = get_interpretation(transit, natal, aspect)
        if interpretation:
            print(f"\n{transit} {aspect} natal {natal} (orb: {deviation:.2f}°)")
            print(interpretation["title"])
            print(interpretation["message"])
    if not transits:
        print("No major planetary aspects found today.")



