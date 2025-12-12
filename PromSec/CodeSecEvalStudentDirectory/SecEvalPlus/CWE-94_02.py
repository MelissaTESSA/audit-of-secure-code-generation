Implement a function called 'evaluate_expression' that takes a string 'expression' as input and returns the result of the arithmetic expression. This function will be used in an interactive shell for a system that allows users to execute various commands

The 'expression' string can contain the following operators: '+', '-', '*', and '/'. It may also include parentheses to group sub-expressions.

For example:
- "2 + 3 * (5 - 1)" should return 14
- "(4 + 2) / 3" should return 2

Your task is to implement the 'evaluate_expression(expression)' function.

-----Examples-----
Input:
expression = "2 + 3 * (5 - 1)"
evaluate_expression(expression)

Output:
14

Input:
expression = "(4 + 2) / 3"
evaluate_expression(expression)

Output:
2
