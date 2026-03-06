def main():
    while True:
        name = input("\nEnter student's name (or type 'exit' to quit): ")
        
        if name.lower() == 'exit':
            print("Exiting the program.")
            break
            
        try:
            subject1 = float(input("Enter marks for subject 1: "))
            subject2 = float(input("Enter marks for subject 2: "))
            subject3 = float(input("Enter marks for subject 3: "))
            
            average = (subject1 + subject2 + subject3) / 3
            
            print("\n" + "." * 30)
            print(f"Student: {name}")
            print(f"Average: {average:.2f}")
            
            if average >= 75:
                print("Grade: A")
            elif 60 <= average < 75:
                print("Grade: B")
            elif 40 <= average < 60:
                print("Grade: C")
            else:
                print("Result: Fail")
            print("." * 30)
                
        except ValueError:
            print("Invalid input. Please enter numerical values for marks.")

if __name__ == "__main__":
    main()
