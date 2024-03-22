import random
import tkinter as tk
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

        if self.level == 2:
            self.questions = [
                "CH2-CH3", "CH3\n|\nCH3", "CH2-CH2-CH3\n/     \nCH2    CH2-CH2-CH2\n\\     /\nCH2-CH2",
                "CH2-CH2-CH3\n/     \nCH2    CH2-CH2-CH2-CH3\n\\     /        |\nCH2-CH2       CH3",
                "CH3-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH2-CH3",
                "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3",
                "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3",
                # new branched structures
                ["CH3-CH(CH3)-CH2-CH3", "ethyl-methane"], ["CH3-CH(CH3)-CH2-CH2-CH3", "ethyl-ethane"],
                ["CH3-CH(CH2-CH3)-CH2-CH3", "propyl-propane"],
                ["CH3-CH(CH2-CH3)-CH2-CH2-CH3", "propyl-butane"], ["CH3-CH2-CH(CH3)-CH2-CH3", "propyl-butane"],
                ["CH3-CH2-CH(CH3)-CH2-CH2-CH3", "butyl-methane"]
            ]
            self.answers = [
                "methane", "ethane", "propane", "butane", "pentane", "hexane", "heptane", "octane", "nonane", "decane",
                "ethyl-methane", "ethyl-ethane", "propyl-propane", "propyl-butane", "butyl-methane", "butyl-ethane"
            ]

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text='Welcome to the Chemical Quiz App by Michael and Justin!Level 1')
        self.label.pack()

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.master, text="Enter Answer", command=self.check_answer)
        self.submit_button.pack()

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
    app.next_question()  # Call next_question after the main loop has started
    root.mainloop()


if __name__ == "__main__":
    main()
