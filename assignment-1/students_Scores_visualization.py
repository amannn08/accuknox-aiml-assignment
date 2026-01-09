import requests
import matplotlib.pyplot as plt


api_url = "https://jsonplaceholder.typicode.com/users"


response = requests.get(api_url)
students = response.json()

names = []
scores = []


for student in students[:5]:
    names.append(student["name"])
    score = len(student["username"]) * 10
    scores.append(score)

#  average score
average_score = sum(scores) / len(scores)
print("Average Score:", average_score)

# Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(names, scores)
plt.axhline(y=average_score)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
