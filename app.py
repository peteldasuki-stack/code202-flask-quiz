app.<i class="fas fa-python    "></i>
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# -------- OOP CLASS --------
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        if user_answer is None:
            return False
        return user_answer.strip().lower() == self.answer.lower()


# -------- STACK DATA STRUCTURE --------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def show(self):
        return self.items


# Create stack for submission history
history = Stack()


# -------- QUIZ QUESTIONS --------
questions = [
    Question("What is 2 + 2?", "4"),
    Question("Capital of Nigeria?", "abuja"),
    Question("Python is a programming language? (yes/no)", "yes")
]

current_question = 0
score = 0


# -------- HOME PAGE --------
@app.route("/")
def home():
    return """
    <h1>Mini CBT Quiz System</h1>
    <p>Welcome to the quiz!</p>
    <a href="/quiz">Start Quiz</a>
    """


# -------- QUIZ PAGE --------
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global current_question, score

    if request.method == "POST":
        answer = request.form.get("answer")

        if questions[current_question].check_answer(answer):
            score += 1

        current_question += 1

    if current_question >= len(questions):

        time = datetime.now()
        history.push(time)

        history_list = "<br>".join(str(x) for x in history.show())

        result = f"""
        <h1>Quiz Finished</h1>

        <p>Your Score: {score} / {len(questions)}</p>

        <p>Submitted at: {time}</p>

        <h3>Submission History</h3>
        <p>{history_list}</p>

        <br>
        <a href="/">Restart Quiz</a>
        """

        current_question = 0
        score = 0

        return result

    q = questions[current_question]

    return f"""
    <h2>Question {current_question + 1}</h2>

    <p>{q.question}</p>

    <form method="POST">
        <input type="text" name="answer" placeholder="Enter your answer">
        <button type="submit">Submit</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)