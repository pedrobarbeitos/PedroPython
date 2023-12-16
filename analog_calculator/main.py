class Calculator:
    def __init__(self):
        self.history_file = 'history.txt'
        self.history = self.read_history()

    def read_history(self):
        try:
            with open(self.history_file, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def write_history(self, calculation):
        with open(self.history_file, 'a') as file:
            file.write(calculation + '\n')
        self.history.append(calculation)

    def empty_history(self):
        with open(self.history_file, 'w') as file:
            pass
        self.history = []

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Carefull! Tried dividing by zero but the universe politely declined."
        return a / b

    def show_history(self):
        if self.history:
            print(f"{len(self.history)} calculations in history:")
            for calc in self.history:
                print(calc.strip())
        else:
            print("No history available.")


def runCalculator():
    calc = Calculator()
    print("Calculator")
    print(f"{len(calc.history)} calculations stored in history")

    def printCommands():
        print("Commands:")
        print("0 - end program")
        print("1 - calculate addition (+)")
        print("2 - calculate subtraction (-)")
        print("3 - calculate multiplication (*)")
        print("4 - calculate division (/)")
        print("5 - show history")
        print("6 - empty history")
        print("7 - show commands")

    printCommands()

    while True:

        command = input("Select command: ")

        if command == "0":
            print("Shutting down program...")
            break
        elif command in ["1", "2", "3", "4"]:
            operand1 = float(input("Input number: "))
            operand2 = float(input("Input number: "))
            result = None
            operation = ''

            if command == "1":
                result = calc.add(operand1, operand2)
                operation = '+'
            elif command == "2":
                result = calc.subtract(operand1, operand2)
                operation = '-'
            elif command == "3":
                result = calc.multiply(operand1, operand2)
                operation = '*'
            elif command == "4":
                result = calc.divide(operand1, operand2)
                operation = '/'

            if result is not None:
                print(f"Result: {result}")
                calculation = f"{operand1};{operation};{operand2};{result}"
                calc.write_history(calculation)

        elif command == "5":
            calc.show_history()
        elif command == "6":
            calc.empty_history()
            print("History cleared")
        elif command == "7":
            printCommands()
        elif command not in ["1", "2", "3", "4", "5", "6", "7", "0"]:
            print("Please input a valid command. Press 7 to show valid commands.")


if __name__ == "__main__":
    runCalculator()
