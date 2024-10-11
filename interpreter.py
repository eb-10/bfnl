class BfnlInterpreter:
    def __init__(self):
        self.cells = [0]  # Initialize with one cell
        self.current_cell = 0  # Start at the first cell

    def execute(self, code: str):
        # Split code into lines and execute each line
        for line in code.strip().splitlines():
            self.execute_line(line)

    def execute_from_file(self, filename: str):
        with open(filename, 'r') as file:
            code = file.read()
            self.execute(code)

    def execute_line(self, line: str):
        line = line.strip()
        
        # Remove comments from the line
        line = self.remove_comments(line)

        # Skip empty lines after comment removal
        if not line:
            return
        
        # Check for while loop
        if line.startswith("while"):
            self.execute_while(line)
            return
        
        # Check for if statement
        if line.startswith("if"):
            self.execute_if(line)
            return
        
        # Check for printing command
        if line.startswith("print"):
            self.print_value()
            return
        
        # Handle value setting
        if line.endswith('='):
            self.set_value(line[:-1].strip())
            return

        # Identify the operation and execute it
        if line.endswith(('+', '-', '*', '/', '^')):
            self.perform_operation(line)
            return

        # Move cell pointer
        if line.endswith('<') or line.endswith('>'):
            self.move_cell(line)
            return

        # Raise an error if the line is not recognized
        raise SyntaxError(f"Unrecognized command: {line}")

    def execute_while(self, line: str):
        # Parse the while condition and commands
        condition_str, commands_str = line[6:].split(':', 1)
        condition_str = condition_str.strip()
        commands_str = commands_str.strip()

        # Execute the while loop as long as the condition is met
        while self.evaluate_condition(condition_str):
            # Split commands by semicolon and execute each command
            for command in commands_str.split(';'):
                command = command.strip()
                if command:  # Execute if not empty
                    self.execute_line(command)

    def execute_if(self, line: str):
        # Parse the if condition and command
        condition_str, commands_str = line[2:].split(':', 1)
        condition_str = condition_str.strip()
        commands_str = commands_str.strip()

        # Execute the commands if the condition is met
        if self.evaluate_condition(condition_str):
            # Split commands by semicolon and execute each command
            for command in commands_str.split(';'):
                command = command.strip()
                if command:  # Execute if not empty
                    self.execute_line(command)

    def evaluate_condition(self, condition: str) -> bool:
        # Extract operator and value from the condition
        operator = ''
        value = 0
        if '>=' in condition:
            operator = '>='
            value = int(condition.split('>=', 1)[1])
        elif '<=' in condition:
            operator = '<='
            value = int(condition.split('<=', 1)[1])
        elif '>' in condition:
            operator = '>'
            value = int(condition.split('>', 1)[1])
        elif '<' in condition:
            operator = '<'
            value = int(condition.split('<', 1)[1])
        elif '!=' in condition:
            operator = '!='
            value = int(condition.split('!=', 1)[1])
        elif '=' in condition:
            operator = '='
            value = int(condition.split('=', 1)[1])

        # Check the condition based on the operator
        current_value = self.cells[self.current_cell]
        if operator == '>':
            return current_value > value
        elif operator == '>=':
            return current_value >= value
        elif operator == '<':
            return current_value < value
        elif operator == '<=':
            return current_value <= value
        elif operator == '!=':
            return current_value != value
        elif operator == '=':
            return current_value == value

        # Raise an error if the operator is unrecognized
        raise SyntaxError(f"Unrecognized comparison operator: {operator}")

    def remove_comments(self, line: str) -> str:
        # Remove comments by splitting on the comment markers
        if '//' in line:
            line = line.split('//', 1)[0]
        if '\\' in line:
            line = line.split('\\', 1)[0]
        return line.strip()

    def move_cell(self, line: str):
        direction = line[-1]
        amount = int(line[:-1]) if line[:-1].isdigit() else 1
        
        if direction == '>':
            self.current_cell += amount
            # Ensure enough cells exist
            while len(self.cells) <= self.current_cell:
                self.cells.append(0)
        elif direction == '<':
            self.current_cell -= amount
            # Ensure we don't go below zero
            if self.current_cell < 0:
                raise IndexError("Cell index out of bounds.")

    def perform_operation(self, line: str):
        operation = line[-1]
        value_str = line[:-1].strip()

        # Check if we're dealing with a string or list
        if value_str.startswith("'") and value_str.endswith("'"):
            value = value_str[1:-1]  # Extract string without quotes
            if operation == '+':
                if isinstance(self.cells[self.current_cell], str):
                    self.cells[self.current_cell] += value
                else:
                    raise SyntaxError("Cannot concatenate to a non-string value.")
            elif operation == '-':
                if isinstance(self.cells[self.current_cell], str) and self.cells[self.current_cell].find(value) != -1:
                    self.cells[self.current_cell] = self.cells[self.current_cell].replace(value, "", 1)
                else:
                    raise SyntaxError("Cannot subtract from a non-matching string.")

        elif value_str.startswith('[') and value_str.endswith(']'):
            value = eval(value_str)  # Use eval for lists
            if operation == '+':
                if isinstance(self.cells[self.current_cell], list):
                    self.cells[self.current_cell] += value
                else:
                    raise SyntaxError("Cannot concatenate to a non-list value.")
            elif operation == '-':
                if isinstance(self.cells[self.current_cell], list):
                    for item in value:
                        if item in self.cells[self.current_cell]:
                            self.cells[self.current_cell].remove(item)
                else:
                    raise SyntaxError("Cannot subtract from a non-matching list.")
        else:
            # Handle numerical operations
            value = int(value_str)
            if operation == '+':
                self.cells[self.current_cell] += value
            elif operation == '-':
                self.cells[self.current_cell] -= value
            elif operation == '*':
                self.cells[self.current_cell] *= value
            elif operation == '/':
                self.cells[self.current_cell] /= value
            elif operation == '^':
                self.cells[self.current_cell] **= value

    def set_value(self, value_str: str):
        if value_str.startswith('[') and value_str.endswith(']'):
            value = eval(value_str)  # Use eval for lists
        elif value_str.startswith("'") and value_str.endswith("'"):
            value = value_str[1:-1]  # Extract string without quotes
        else:
            value = int(value_str)  # Assume it's an integer

        self.cells[self.current_cell] = value

    def print_value(self):
        print(self.cells[self.current_cell])


def execute(file_name):
    if __name__ == "__main__":
        filename = (f'.\\examples\\{file_name}')
        interpreter = BfnlInterpreter()
        interpreter.execute_from_file(filename)

print('This will only search the examples directory')
execute(str(input('Filename: ')))