import random
import tkinter as tk
import tkinter.messagebox as messagebox

class IUPACNomenclatureQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("IUPAC Nomenclature Quiz App")
        self.level = 1
        self.questions = []
        self.answers = []
        self.create_widgets()
        self.load_level()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="IUPAC Nomenclature Quiz App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.check_button = tk.Button(self.master, text="Enter Answer", command=self.check_answer)
        self.check_button.pack(pady=10)

    def load_level(self):
        if self.level == 1:
            self.questions = ["CH4", "CH3-CH3", "CH3-CH2-CH3", "CH3-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH3",
                              "CH3-CH2-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH3",
                              "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3"]
            self.answers = ["methane", "ethane", "propane", "butane", "pentane", "hexane", "heptane", "octane", "nonane", "decane"]
        elif self.level == 2:
            self.questions = ["CH2-CH3", "CH3\n|\nCH3", "CH2-CH2-CH3\n/     \nCH2    CH2-CH2-CH2\n\\     /\nCH2-CH2",
                              "CH2-CH2-CH3\n/     \nCH2    CH2-CH2-CH2-CH3\n\\     /        |\nCH2-CH2       CH3",
                              "CH3-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH2-CH3",
                              "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH3", "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3",
                              "CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH2-CH3"]

        self.next_question()

    def next_question(self):
        if self.questions:
            q_number = random.choice(range(len(self.questions)))
            self.current_question = self.questions[q_number]
            self.question_label.config(text=f"What is the IUPAC name for {self.current_question}?")
            self.questions.pop(q_number)
        else:
            self.next_level()

    def check_answer(self):
        player_choice = self.entry.get().strip().lower()
        correct_answer = self.answers[self.questions.index(self.current_question)]

        if player_choice == correct_answer:
            messagebox.showinfo("Correct!", "Correct answer! Great work!")
            self.next_question()
        else:
            messagebox.showinfo("Wrong!", f"The correct answer is {correct_answer}. Try better next time.")

    def next_level(self):
        if self.level == 2:
            messagebox.showinfo("Congratulations!", "You completed all levels. That's amazing!")
            self.master.destroy()
        else:
            self.level += 1
            messagebox.showinfo("Level Up", f"Congratulations! You advanced to Level {self.level}.")
            self.load_level()

if __name__ == "__main__":
    root = tk.Tk()
    app = IUPACNomenclatureQuizApp(root)
    root.mainloop()
