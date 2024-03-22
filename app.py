import random
import tkinter as tk
from tkinter import messagebox

# Define a list of compounds and their IUPAC names
compounds = [("CH4", "Methane"), ("C2H6", "Ethane"), ("C3H8", "Propane"), ("C4H10", "Butane"), ("C8H18", "Octane")]

class ChemicalQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("IUPAC Nomenclature Quiz App")

        self.score = 0
        self.num_questions = 5
        self.used_compounds = set()

        self.label = tk.Label(master, text="Welcome to the IUPAC Quiz App!")
        self.label.pack()

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack()

        self.next_question()

    def generate_question(self):
        available_compounds = [comp for comp in compounds if comp not in self.used_compounds]

        if not available_compounds:
            return None, None

        compound, iupac_name = random.choice(available_compounds)
        self.used_compounds.add((compound, iupac_name))

        return compound, iupac_name

    def next_question(self):
        if len(self.used_compounds) >= self.num_questions:
            self.show_result()
        else:
            self.compound, self.correct_iupac_name = self.generate_question()
            self.label.config(text=f"What is the IUPAC name for {self.compound}?")
            self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        user_answer = self.answer_entry.get().lower()

        if user_answer == self.correct_iupac_name.lower():
            self.score += 1
            messagebox.showinfo("Correct!", "Correct answer!")
        else:
            messagebox.showinfo("Wrong!", f"The correct answer is {self.correct_iupac_name}.")

        self.next_question()

    def show_result(self):
        messagebox.showinfo("Game Over", f"Your final score: {self.score}/{self.num_questions}")
        self.master.destroy()

def main():
    root = tk.Tk()
    app = ChemicalQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
