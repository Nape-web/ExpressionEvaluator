import re

# function for evaluating algebraic expressions.
def expressionEvaluation(expression):
    # Define a recursive function to calculate the result of an expression.
    def calculate(tokens):
        if not tokens:
            return None, tokens

        # Get the operands (numbers) from the expression.
        num, tokens = getOperands(tokens)
        if num is None:
            return None, tokens

        while tokens:
            # Get the operator (+, -, *, /) from the expression.
            op, tokens = getOperator(tokens)
            if op is None:
                return num, tokens

            # Recursively calculate the result of the remaining expression.
            next_num, tokens = calculate(tokens)
            if next_num is None:
                return None, tokens

            # Apply the operator to the numbers.
            if op == '+':
                num += next_num
            elif op == '-':
                num -= next_num
            elif op == '*':
                num *= next_num
            elif op == '/':
                if next_num == 0:
                    return None, tokens  # Division by zero is not allowed.

        return num, tokens

    # Get operands (numbers) from the expression.
    def getOperands(tokens):
        num = re.match(r'(\d+\.\d+|\d+)', tokens)
        if num:
            return float(num.group()), tokens[num.end():]
        if tokens.startswith('('):
            num, tokens = calculate(tokens[1:])  # Handle expressions inside parentheses.
            if num is not None and tokens.startswith(')'):
                return num, tokens[1:]
        return None, tokens

    # Get operators (+, -, *, /) from the expression.
    def getOperator(tokens):
        op = re.match(r'([+\-*/])', tokens)
        if op:
            return op.group(), tokens[op.end():]
        return None, tokens

    try:
        # Remove spaces from the expression.
        tokens = expression.replace(" ", "")
        # Calculate the result of the expression and check if it's valid.
        result, remaining_tokens = calculate(tokens)
        
        if remaining_tokens == "":
            return str(result) if result is not None else "Invalid Expression"
        else:
            return "Invalid Expression"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    while True:
        # Prompt the user to input an algebraic expression.
        expression = input("Please Enter Algebraic Expression : ")
  
        # Evaluate the expression and print the result.
        result = expressionEvaluation(expression)
        print(f"Result: {result}")