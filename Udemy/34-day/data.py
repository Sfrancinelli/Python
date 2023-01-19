import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()

question_data = [data]

count = 0

# for _ in question_data:
#     print(question_data[0]['results'][count]['question'])
#     print(question_data[0]['results'][count]['correct_answer'])
#     count += 1

print(question_data[0]['results'][9]['question'])

# print(question_data[0]['results'][0]['question'])