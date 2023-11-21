def multiplication_table(n):
    """Generate and print the multiplication table for the given number."""
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number for the multiplication table: "))
    multiplication_table(number)
