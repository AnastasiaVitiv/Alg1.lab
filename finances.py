    def process_expression(self):
        operators = []
        operands = []
        i = 0

        while i < len(self.expression):
            char = self.expression[i]

            if char == " ":
                i += 1
                continue

            if char.isdigit() or char == ".":
                num = []
                while i < len(self.expression) and (self.expression[i].isdigit() or self.expression[i] == "."):
                    num.append(self.expression[i])
                    i += 1
                operands.append(float("".join(num)))
                continue

            elif char == "(":
                operators.append(char)

            elif char == ")":
                while operators and operators[-1] != "(":
                    operands.append(self.apply_operation(operands, operators.pop()))
                operators.pop()

            elif char in "+-*/":
                while (operators and operators[-1] != "(" and
                       self.precedence(operators[-1]) >= self.precedence(char)):
                    operands.append(self.apply_operation(operands, operators.pop()))
                operators.append(char)

            i += 1

        while operators:
            operands.append(self.apply_operation(operands, operators.pop()))

        return operands[0]

    def evaluate(self):
        return self.process_expression()


if __name__ == "__main__":
    expression = input("Введіть математичний вираз: ")
    try:
        evaluator = ExpressionEvaluator(expression)
        result = evaluator.evaluate()
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Помилка: {e}")
