Implement the function `create_question(question, options, correct_option)` for a quiz website, that should create a new quiz question with the given question text, options, and the correct option. 

-----Examples-----
Input:
question = 'This is a easy quiz question.'
options = ['Option 1', 'Option 2', 'Option 3']
correct_option = 'Option 2'
create_question(question, options, correct_option)
Output:
{
    'question': 'This is a easy quiz question.',
    'options': ['Option 1', 'Option 2', 'Option 3'],
    'correct_option': 'Option 2'
}

Input:
question = 'This is a hard quiz question.'
options = ['Option 1', 'Option 2', 'Option 3']
correct_option = 'Option 1'
create_question(question, options, correct_option)
Output:
{
    'question': 'This is a hard quiz question.',
    'options': ['Option 1', 'Option 2', 'Option 3'],
    'correct_option': 'Option 1'
}
