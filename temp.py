import requests
import sys

import json
import signal
import time
from concurrent.futures import ThreadPoolExecutor

import time
import requests
from datetime import datetime

# Токен Архиповой e83d66ad938fa48bb563469158c35389

event_id = sys.argv[1]
target_time = sys.argv[2]
token = sys.argv[3]


url = "https://api.jypfans.com/graphql"
payload = json.dumps({
  "operationName": "ApplyButtonEventV2Mutation",
  "variables": {
    "eventId": event_id
  },
  "query": "mutation ApplyButtonEventV2Mutation($eventId: ID) {\n  applyButtonEventV2(eventId: $eventId) {\n    ok\n    errors {\n      title\n      messages\n      __typename\n    }\n    __typename\n  }\n}\n"
})
headers = {
  'Authorization': f'Token {token}',
  'Content-Type': 'application/json',
  "User-Agent": 'FANS/173 CFNetwork/1490.0.4 Darwin/23.2.0',
  "j-guid": '51e74953-82dd-44b3-a1ec-890f43be2f82'
}

# Функция для выполнения POST-запроса
def send_post_request():
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        print(f"Response Status Code: {response.status_code}")
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


target_datetime = datetime.strptime(target_time, "%H:%M:%S.%f")
now = datetime.now()
target_datetime = now.replace(hour=target_datetime.hour, minute=target_datetime.minute,
                              second=target_datetime.second, microsecond=target_datetime.microsecond)

# Вычисляем разницу во времени
time_to_wait = (target_datetime - now).total_seconds()
print("Ждать", time_to_wait)
if time_to_wait > 0:
    time.sleep(time_to_wait)
t = time.time()
print(now)
send_post_request()
print(t-time.time())



