import tkinter as tk
from quiz import QuizBrain
import pygame as pg

pg.mixer.init()

BG_COLOR = "#5A827E"

class QuizUI:
    def __init__(self, quizBrain:QuizBrain):
        self.window = tk.Tk() # make it global 
        self.window.title("Quiz app")
        self.window.resizable("false", "true")
        self.window.config(bg=BG_COLOR, padx=20, pady=20) 
        self.QuizBrain = quizBrain


        self.score_label = tk.Label(self.window, text='score: 0', bg=BG_COLOR, fg="white", font=("Courier", 20, "bold"))
        self.score_label.grid(column=0, row=0, columnspan=2, ipadx=30, ipady=10)


        self.question_cont = tk.Canvas( height=250, width=300)
        self.question_cont.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.question_text = self.question_cont.create_text(150, 130, width=200, text="Wassup mcvdfevfedvdfgv gtrvgrtgv rggvefceramen",font=("Courier", 12, "bold"))


        self.true_button = tk.Button(self.window, text='true', bg="#468432", fg="#fff", activebackground="#fff", activeforeground="#468432", font=("Courier", 12, "bold"), command= lambda: self.check_answer("true"))
        self.true_button.grid(column=0, row=2, ipadx=30, ipady=10)
        self.false_button = tk.Button(self.window, text="false", bg="#EB4C4C", fg="#fff", activebackground="#fff", activeforeground="#EB4C4C", font=("Courier", 12, "bold"),  command=lambda: self.check_answer("false"))
        self.false_button.grid(column=1, row=2, ipadx=30, ipady=10)

        # Update geometry so winfo_width/height are accurate
        self.window.update_idletasks()

        # Get window size (based on content)
        self.window_width = self.window.winfo_width()
        self.window_height = self.window.winfo_height()

        # Get screen size
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate position (center)
        x = (screen_width // 2) - (self.window_width // 2)
        y = (screen_height // 2) - (self.window_height // 2)

        # Set geometry (width x height + x + y)
        self.window.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        self.update_question_text()
        self.window.mainloop()

    def update_score(self):
        self.score_label.config(text=f'score: {self.QuizBrain.score}')

    def update_question_text(self):
        if self.QuizBrain.has_questions():
            self.question = self.QuizBrain.next_question()
            self.question_cont.itemconfig(self.question_text, text=self.question)
        else:
            self.question_cont.itemconfig(self.question_text, text=f"There is no more question. Your Finals score is {self.QuizBrain.score}/{len(self.QuizBrain.questions)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

            self.restart_button = tk.Button(self.window, text="RESTART", bg="#3B7597", fg="white", activebackground="white", activeforeground="#3B7597",  font=("Courier", 12, "bold"), command=self.restart)
            self.restart_button.grid(column=0, row=3, ipadx=30, ipady=10, columnspan=2, pady=20)
            self.new_height = self.window_height + 70
            self.window.geometry(f"{self.window_width}x{self.new_height}")

            

    def check_answer(self, answer):
        if self.QuizBrain.check_answer(answer):
            self.update_score()
            self.is_right()
            pg.mixer.music.load("correct.mp3")
            pg.mixer.music.play()

        else:
            self.is_wrong()
            pg.mixer.music.load("wrong.mp3")
            pg.mixer.music.play()

        self.update_question_text()
    def restart(self):

        self.restart_button.destroy()
        self.window.geometry(f"{self.window_width}x{self.window_height}")
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.QuizBrain.restart_state()
        self.update_question_text()
        self.update_score()
        
        
    def is_right(self):
        self.question_cont.config(bg="green")
        self.window.after(100, lambda: self.question_cont.config(bg="white"))
    def is_wrong(self):
        self.question_cont.config(bg="red")
        self.window.after(100, lambda: self.question_cont.config(bg="white"))


    
    








