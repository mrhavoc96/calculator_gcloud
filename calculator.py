# Simple Calculator using Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please select from 1 to 5.")



'''
public static void add()
{
 Integer a = 4;
 Integer b = 5;
 Integer c = a + b;
 Integer d = 4 + 5;
 Integer e = a + 5;
 System.debug('Add = ' + c);
 System.debug('Add =' + d);
 System.debug('Add =' + e);
}
 public static void sub()
 {


 Integer a = 4;
 Integer b = 5;
 Integer c1 = a - b;
 Integer d1 = b - a;
Integer e1 = 4 - 5;
Integer f1 = a - 5;
System.debug('Sub ='+ c1);
System.debug('Sub =' + d1);
System.debug('Sub =' + e1);
System.debug('Sub =' + f1);
 }

 add this -> cal.sub(); cal.add()
 

'''
