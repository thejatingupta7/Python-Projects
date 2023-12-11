from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=1, column=2, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(150, 125, text="Amazon?",width=280, font=("Arial", 18, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20, padx=20)

        self.true = PhotoImage(file="true.png")
        self.button_correct = Button(image=self.true, command=self.true_click, highlightthickness=0, borderwidth=0)
        self.button_correct.grid(row=3, column=1, padx=20, pady=20)

        self.false = PhotoImage(file="false.png")
        self.button_wrong = Button(image=self.false, command=self.false_click, highlightthickness=0, borderwidth=0)
        self.button_wrong.grid(row=3, column=2, pady=20, padx=20)

        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            next_q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=next_q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="Quiz Ended")
            self.button_correct.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def true_click(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_click(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_ques)

