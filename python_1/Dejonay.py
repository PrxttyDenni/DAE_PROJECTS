# Introduction to the game
def start_game():
    print("Welcome to the Date Decision-Maker Game!")
    print("Navigate through the questions and win the date!")
    play_game()

# Decision-making function
def ask_question(question, options):
    print("\n" + question)
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")
    choice = input("Choose an option (1/2/...): ")
    return int(choice) - 1

# Main game flow
def play_game():
    # Game questions and options based on the flowchart
    questions = [
        {"question": "What would you order for a drink?", "options": ["Tea", "Coffee"], "correct": 0},
        {"question": "Which tea does she prefer?", "options": ["Green Tea", "Black Tea"], "correct": 0},
        {"question": "Ok The real question is do you actually like her?", "options": ["Yes", "No"], "correct": 0},
    ]
    
    # Track game state
    game_over = False
    score = 0

    # Step-by-step flow control based on the flowchart
    # 1. First question
    choice = ask_question(questions[0]["question"], questions[0]["options"])
    if choice == questions[0]["correct"]:
        print("Good choice! She likes tea.")
        print("She smiles at you!")
        score += 1
    else:
        print("Uh-oh, she wanted tea!")
        game_over = True

    # 2. If the game is not over, proceed to the second question
    if not game_over:
        choice = ask_question(questions[1]["question"], questions[1]["options"])
        if choice == questions[1]["correct"]:
            print("Great! She loves Green Tea.")
            print("She gives you a teethy smile")
            score += 1
        else:
            print("She frowns; Black Tea wasn't her favorite.")
            print("Do you even know anything about her?")
            game_over = True

    # 3. If the game is still not over, proceed to the third question
    if not game_over:
        choice = ask_question(questions[2]["question"], questions[2]["options"])
        if choice == questions[2]["correct"]:
            print("You know her well! She's impressed.")
            score += 1
        else:
            print("She seems disappointed.")
            print("You start to see her tear up a little...")
            game_over = True

    # Final outcome
    if game_over:
        print("\nGame Over! You made her cry and she blocked you.")
    else:
        print("\nYou win! The date went well.")
        print("She ask you for a second date!")
    print(f"Your score: {score}")

# Start the game
start_game()
