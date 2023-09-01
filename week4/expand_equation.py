example_input ="2 x 3 + 2 ^ * 4 x 1 - x 2 + * * + 3 x 1 + * + 4 x * - 6 +"

reverse_polish_notation = example_input.split(" ")

import re

def rpn_to_infix(rpn_expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in rpn_expression.split():
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"({operand1} {token} {operand2})")
            print(stack)
        # check for pronumerals
        elif re.match(r'[a-zA-Z]', token):
            # check if previous token is a number
            if re.match(r'[0-9]', stack[-1]):
                operand1 = stack.pop()
                stack.append(f"({operand1} * {token}")
            print(stack)
        else:
            stack.append(token)
            print(stack)

    return stack[0]

rpn_expression = "2 x 3 +"
infix_expression = rpn_to_infix(rpn_expression)
print("RPN expression:", rpn_expression)
print("Infix expression:", infix_expression)