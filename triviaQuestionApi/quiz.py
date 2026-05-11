import html

class QuizBrain:
    def __init__(self):
        self.questions = []
        self.current_index = 0
        self.score = 0
        self.current_question = None

    def add_question(self, question):
        self.questions.append(question)
    def has_questions(self):
        return self.current_index < len(self.questions)
    def next_question(self):
        self.current_question = self.questions[self.current_index]
        self.question_text = html.unescape(self.current_question.question)
        self.current_index += 1
        return f"Q{self.current_index}:  {self.question_text}"
    def check_answer(self, user_ans):
        if self.current_question.answer.lower() == user_ans.lower():
            self.score += 1
            return True
        return False
    def restart_state(self):
        self.score = 0
        self.current_question = None
        self.current_index = 0