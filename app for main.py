import random
import tkinter as tk
import turtle
from tkinter import messagebox

class IupacNomenclatureQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("IUPAC Nomenclature Quiz App")

        self.level = 1
        self.questions = [
            ["CH4", "methane"], ["CH3-CH3", "ethane"], ["CH3-CH2-CH3", "propane"],
            ["CH3-CH2-CH2-CH3", "butane"], ["CH3-CH2-CH2-CH2-CH3", "pentane"],
            ["CH3-CH2-CH2-CH2-CH2-CH3", "hexane"], ["CH3-CH2-CH2-CH2-CH2-CH2-CH3", "heptane"],
            ["CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH3", "octane"], ["CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3", "nonane"],
            ["CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3", "decane"]
        ]

        self.label = tk.Label(master, text="Welcome to the Chemical Quiz App by Michael and Justin!\nLevel 1")
        self.label.pack()

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        self.submit_button = tk.Button(master, text="Enter Answer", command=self.check_answer)
        self.submit_button.pack()

        self.next_question()

    def next_question(self):
        if self.questions:
            self.current_question = random.choice(self.questions)
            self.label.config(text=f"What is the IUPAC name for {self.current_question[0]}?")
            self.answer_entry.delete(0, tk.END)
        else:
            self.show_result()

    def check_answer(self):
        user_answer = self.answer_entry.get().lower()
        correct_answer = self.current_question[1]

        if user_answer == correct_answer:
            messagebox.showinfo("Correct!", "Correct answer! Great work BRO")
        else:
            messagebox.showinfo("Wrong!", f"The correct answer is {correct_answer}. Try better next time, bro.")

        self.questions.remove(self.current_question)
        self.next_question()

    def show_result(self):
        messagebox.showinfo("Game Over", "Congratulations! You completed all levels.")
        self.master.destroy()

def main():
    root = tk.Tk()
    app = IupacNomenclatureQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
