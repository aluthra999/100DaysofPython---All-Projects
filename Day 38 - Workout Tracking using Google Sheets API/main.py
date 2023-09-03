import requests
import datetime
import os

NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_APP_KEY"]

SHEET_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]

GENDER = "MALE"
WEIGHT_KG = "66.22"
HEIGHT_CM = "168"
AGE = "23"

exercise_input = input("Tell which exercise you did today?: ")

nutrition_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
today_time = datetime.datetime.now().strftime("%H:%M:%S")

response = requests.post(url=NUTRITION_ENDPOINT, json=parameters, headers=nutrition_header)
response.raise_for_status()

result = response.json()

for exercise in result["exercises"]:
    exercise_name = exercise["name"]
    duration_min = exercise.get("duration_min")
    nf_calories = exercise.get("nf_calories")

    sheet_header = {
        "Authorization": f"Basic {os.environ['ENV_SHEETY_TOKEN']}"
    }

    sheet_params = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise_name,
            "duration": duration_min,
            "calories": nf_calories,
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_params, headers=sheet_header)
    print(sheet_response.text)

    # print(f"Exercise Name: {exercise_name}")
    # if duration_min is not None:
    #     print(f"Duration (minutes): {duration_min}")
    # if nf_calories is not None:
    #     print(f"Calories Burned: {nf_calories}")
