
birth_info = {
    "name": "Winny",
    "birth_date": "2020-05-15",
    "birth_place": "New York, USA",
    "birth_time": "14:30",
    "time-zone": "America/New_York"
}


def ask_birth_info():
    print("Please provide the following birth information:")
    birth_info["name"] = input("Name: ")
    birth_info["birth_date"] = input("Birth Date (YYYY-MM-DD): ")
    birth_info["birth_place"] = input("Birth Place: ")
    birth_info["birth_time"] = input("Birth Time (HH:MM): ")
    birth_info["time-zone"] = input("Time Zone (e.g., EST, PST): ")
    print("Name:", birth_info["name"])
    print("Birth Date:", birth_info["birth_date"])
    print("Birth Place:", birth_info["birth_place"])
    print("Birth Time:", birth_info["birth_time"])
    print("Time Zone:", birth_info["time-zone"])


if __name__ == "__main__":
    ask_birth_info()