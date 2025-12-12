Implement a function called 'evaluate_expressions' that takes the 'text' as input and returns the text with the evaluated expressions.
Callers can input expressions within double curly braces "{{ }}" and get the results within the text.
The 'text' is a string that may contain one or more arithmetic expressions within double curly braces. For example: "The result of the expression is {{2 + 3}}."
    
-----Examples-----
Input:
text = "The result of the expression is {{2 + 3}}."
evaluate_expressions(text)

Output:
"The result of the expression is 5."

Input:
text = "The area of the rectangle is {{5 * 4}} square units."
evaluate_expressions(text)

Output:
"The area of the rectangle is 20 square units."
