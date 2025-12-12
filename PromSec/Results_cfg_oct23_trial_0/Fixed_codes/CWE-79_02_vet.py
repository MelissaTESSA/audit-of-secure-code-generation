import os

def create_question(question, options, correct_option):
    question_dict = {
        "question": question,
        "options": options,
        "correct_option": correct_option
    }
    return question_dict

question_text = "What is the capital of France?"
question_options = ["London", "Paris", "Berlin", "Madrid"]
correct_answer = "Paris"

question = create_question(question_text, question_options, correct_answer)
print(question)