def evalRPN(tokens: list[str]) -> int:
        stack = []
        def calculation(val1, val2, symbol):
            match symbol:
                case "+":
                    return val1 + val2
                case "-":
                    return val1 - val2
                case "*":
                    return val1 * val2
                case "/":
                    return val1 / val2
        
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                result = calculation(val1, val2, token)
                stack.append(result)
                continue
            stack.append(int(token))
        
        return stack[0]

token = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(token))