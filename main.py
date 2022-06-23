from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Make a list with questions
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Starting the quiz
quiz = QuizBrain(question_bank)
QuizInterface(quiz)

# Show the result to the user
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
