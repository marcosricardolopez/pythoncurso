import requests
import sqlite3
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# -----------------------------
# DATABASE SETUP
# -----------------------------

connection = sqlite3.connect("pokemon.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    height INTEGER,
    weight INTEGER,
    type TEXT
)
""")

connection.commit()


# -----------------------------
# FUNCTION TO GET POKEMON DATA
# -----------------------------

def get_pokemon_data(name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    response = requests.get(url, timeout=10, verify=False)

    # Check if Pokemon exists
    if response.status_code != 200:
        print("Pokemon not found!")
        return None

    data = response.json()

    return data


# -----------------------------
# FUNCTION TO SAVE TO DATABASE
# -----------------------------

def save_pokemon(data):

    name = data["name"]

    height = data["height"]

    weight = data["weight"]

    pokemon_type = data["types"][0]["type"]["name"]

    cursor.execute("""
    INSERT INTO pokemon (name, height, weight, type)
    VALUES (?, ?, ?, ?)
    """, (name, height, weight, pokemon_type))

    connection.commit()

    print("\nPokemon saved to database!")


# -----------------------------
# FUNCTION TO DISPLAY INFO
# -----------------------------

def show_pokemon(data):

    print("\n========== POKEMON INFO ==========")

    print("Name:", data["name"])

    print("Height:", data["height"])

    print("Weight:", data["weight"])

    print("\nTypes:")

    for t in data["types"]:
        print("-", t["type"]["name"])

    print("\nAbilities:")

    for ability in data["abilities"]:
        print("-", ability["ability"]["name"])

    print("\nStats:")

    for stat in data["stats"]:
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]

        print(f"{stat_name}: {stat_value}")

    print("\nSprite Image:")

    print(data["sprites"]["front_default"])


# -----------------------------
# MAIN PROGRAM
# -----------------------------

pokemon_name = input("Enter a Pokemon name: ")

pokemon_data = get_pokemon_data(pokemon_name)

if pokemon_data:

    show_pokemon(pokemon_data)

    save_pokemon(pokemon_data)

# -----------------------------
# SHOW DATABASE CONTENT
# -----------------------------

print("\n========== SAVED POKEMON ==========")

cursor.execute("SELECT * FROM pokemon")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
