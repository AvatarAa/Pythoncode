import random

# Define a list of compounds and their IUPAC names
compounds = [("CH4", "Methane"), ("C2H6", "Ethane"), ("C3H8", "Propane"), ("C4H10", "Butane"), ("C8H18", "Octane")]


def generate_question(used_compounds):
    # Filter out compounds that have already been used
    available_compounds = [comp for comp in compounds if comp not in used_compounds]

    # Check if all compounds have been used
    if not available_compounds:
        return None, None

    # Randomly select a compound from the list
    compound, iupac_name = random.choice(available_compounds)

    # Add the used compound to the set
    used_compounds.add((compound, iupac_name))

    return compound, iupac_name


def play_game():
    score = 0
    num_questions = 5  # Set the number of questions
    used_compounds = set()

    for _ in range(num_questions):
        compound, correct_iupac_name = generate_question(used_compounds)

        # Check if there are no more available questions
        if compound is None:
            break

        # Ask the user for input
        user_answer = input(f"What is the IUPAC name for {compound}? ")

        # Check if the user's answer is correct
        if user_answer.lower() == correct_iupac_name.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_iupac_name}.\n")

    print(f"Game over. Your score: {score}/{num_questions}")


# Start the game
play_game()
