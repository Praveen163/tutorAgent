from agents import  function_tool


@function_tool
def arithmetic_tool(numbers: list[float], operation: str):
        """Perform basic arithmetic operations on a list of numbers.
        
        Args:
            numbers: List of numbers to perform operation on
            operation: One of '+', '-', '*', '/' for addition, subtraction, multiplication, or division
            
        Returns:
            Result of the arithmetic operation
        """
        if not numbers:
            return {"error": "No numbers provided"}
            
        if operation not in ['+', '-', '*', '/']:
            return {"error": "Invalid operation. Must be one of: +, -, *, /"}
            
        if operation == '+':
            result = sum(numbers)
        elif operation == '-':
            result = numbers[0] - sum(numbers[1:])
        elif operation == '*':
            result = 1
            for num in numbers:
                result *= num
        elif operation == '/':
            if 0 in numbers[1:]:
                return {"error": "Cannot divide by zero"}
            result = numbers[0]
            for num in numbers[1:]:
                result /= num
                
        return {"result": result}
