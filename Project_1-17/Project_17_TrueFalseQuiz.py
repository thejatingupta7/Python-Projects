from Project_17_data import question_data, Question, QuizBrain
from pic_art import true_false_quiz


print(true_false_quiz)


question_bank = []
for i in question_data:
    q_text = i["text"]
    q_answer = i["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_q():
    quiz_brain.next_q()
