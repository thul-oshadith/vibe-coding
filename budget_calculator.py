def main():
    while True:
        try:
            # Ask for the total budget or check for exit command
            user_input = input("Enter your total budget (or type 'done' to exit): ")
            
            if user_input.lower() == 'done':
                break
                
            budget = float(user_input)

            # Ask for three expenses
            total_expenses = 0
            for i in range(1, 4):
                total_expenses += float(input(f"Enter expense {i}: "))

            # Calculate remaining balance
            balance = budget - total_expenses

            # Display the remaining balance
            print(f"Remaining Balance : {balance}")

            # Warning if budget is exceeded or low
            if balance <= 0:
                print("The budget exceeded")
            elif balance < 500:
                print("Warning: Low Funds")

        except ValueError:
            print("Invalid input. Please enter a numeric value or 'done'.")
        except EOFError:
            break

if __name__ == "__main__":
    main()
