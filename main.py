import requests
from datetime import datetime

APP_ID = "09747bca"
API_KEY = "b1c5b23f149bee235ff0856aa11eeff1"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

data = {
    "query": input("What exercise did you do today?"),
    "gender": "male",
    "weight_kg": 69,
    "height_cm": 171,
    "age": 31,
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/c07bff9be7156b1016f5205e9202ff93/myWorkouts/workouts"

response = requests.post(url=nutritionix_endpoint, json=data, headers=headers)
result = response.json()

for exercise in result['exercises']:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": f"{exercise['duration_min']}min",
            "calories": exercise['nf_calories']
        }
    }

    sheet_row = requests.post(url=sheety_endpoint, json=sheety_params)
