Create a function named `evaluate_expression(expression)` that takes a string as input. The string should contain simple mathematical expressions composed of digits and four operators: '+', '-', '*', and '/'. The function should evaluate the provided expression and return the result. You should not use the built-in `eval` function. The operators are limited to operations between single-digit numbers (0-9), so expressions like "11+2" are not considered. Assume that the expressions only contain digits (0-9), four valid operators and whitespaces.
-----Examples-----
Input:
expression = "3+2*2"
evaluate_expression(expression)
Output:
7

Input:
expression = " 3/2 "
evaluate_expression(expression)
Output:
1.5

Input:
expression = " 3+5/2 "
evaluate_expression(expression)
Output:
5.5
