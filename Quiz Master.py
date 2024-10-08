# All 10 questions combined in one list
questions = [
    {'question': '1. Solve for x: 2x + 5 = 11.', 'answer': '3', 'options': ['4', '3', '2', '1']},
    {'question': '2. What is the capital of France?', 'answer': 'Paris', 'options': ['London', 'Berlin', 'Paris', 'Madrid']},
    {'question': '3. Which element has the chemical symbol "Au"?', 'answer': 'Gold', 'options': ['Gold', 'Silver', 'Iron', 'Copper']},
    {'question': '4. Who developed the theory of general relativity?', 'answer': 'Einstein', 'options': ['Newton', 'Einstein', 'Tesla', 'Galileo']},
    {'question': '5. What is the perimeter of a rectangle with length 6cm and width 4cm?', 'answer': '20 cm', 'options': ['20 cm', '24 cm', '18 cm', '30 cm']},
    {'question': '6. What is the next number in the sequence: 2, 6, 12, 20, 30?', 'answer': '42', 'options': ['42', '36', '50', '40']},
    {'question': '7. What starts with an E, ends with an E, but only contains one letter?', 'answer': 'envelope', 'options': ['elephant', 'eagle', 'envelope', 'eye']},
    {'question': '8. How do introverts usually prefer to communicate?', 'answer': 'By texting or writing', 'options': ['By talking on the phone', 'By texting or writing', 'By video calls', 'In person only']},
    {'question': "9. Which planet is known as the Red Planet?", 'answer': 'Mars', 'options': ['Earth', 'Mars', 'Venus', 'Jupiter']},
    {'question': '10. What is a six-letter word that can be written forward, backward, and upside down and still be read the same?', 'answer': 'SIXES', 'options': ['NOON', 'LEVEL', 'DEIFIED', 'SIXES']}
]

score = 0

def play_quiz():
    global score
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        
        player_ans = input("Enter the option number: ")
        
        if player_ans.isdigit() and 1 <= int(player_ans) <= len(question['options']):
            if question['options'][int(player_ans) - 1].lower() == question['answer'].lower():
                score += 1
                print("Correct!\n")
            else:
                print(f"Incorrect! The correct answer is: {question['answer']}\n")
        else:
            print("Invalid input! Moving to the next question.\n")
    
    print(f"Quiz over! You scored: {score}/{len(questions)}")

# Start the quiz
play_quiz()


