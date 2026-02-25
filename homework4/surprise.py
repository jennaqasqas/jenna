# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def star_name(dic):
    for name in dic.keys():
        print(name)

star_name(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_name_type(targets: dict) -> None:
    for name, info in targets.items():
        print(f"{name}: {info['Spectral Type']}")
 
print_name_type(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def dim_stars(targets: dict) -> list[str]:
    result = []
    for name, info in targets.items():
        if info["Magnitude"] > 0.1:
            result.append(name)
    return result

dim_stars(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Altair"] = {
    "RA": "19h 50m 46.99855s",
    "Dec": "+08° 52′ 05.9563″",
    "Magnitude": 0.77,
    "Spectral Type": "A7 V"
}

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_closest_to_20(targets):
    brightest_star = None
    
    for name in targets:
        dec = int(targets[name]["Dec"].split("°")[0].replace("+", "").replace("−", "-"))
        diff = abs(dec - 20)
        
        if brightest_star is None:
            brightest_star = name
        else:
            best_dec = int(targets[brightest_star]["Dec"].split("°")[0].replace("+", "").replace("−", "-"))
            best_diff = abs(best_dec - 20)
            
            if diff < best_diff or (diff == best_diff and targets[name]["Magnitude"] < targets[best_star]["Magnitude"]):
                brightest_star = name
    
    return brightest_star

brightest_closest_to_20(targets)
# 6) What is your favorite constellation?
# Orion