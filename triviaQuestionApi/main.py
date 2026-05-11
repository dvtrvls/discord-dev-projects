import requests
from question_model import Question
import html
from ui import QuizUI
from quiz import QuizBrain



params = {"amount": 10, "type": "boolean", "category":18}

response = requests.get("https://opentdb.com/api.php", params=params)
questions = response.json()['results']

quiz_brain = QuizBrain()

for q in questions:
    quiz_brain.add_question(Question(q['question'], q['correct_answer']))

quiz_ui = QuizUI(quiz_brain)

