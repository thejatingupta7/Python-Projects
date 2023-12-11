import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 180
AGE = 19

APP_ID = "ID"
API_KEY = "APIKEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# ----------------------sheety API----------------------------
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheet_endpoint = "https://api.sheety.co/ff263fecc8eaf32eff7296568694e393/myWorkouts/workouts"


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)