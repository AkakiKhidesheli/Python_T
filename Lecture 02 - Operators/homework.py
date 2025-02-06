# დავალება 1
number1 = int(input("Enter a number: "))
if number1 % 2 == 1:
    print("Odd")
else:
    print("Even")

# დავალება 2
text1 = input("Enter a text: ")
if 'small' in text1:
    print("small")

if 'tall' in text1:
    print("tall")

if 'middle' in text1:
    print("middle")

if 'small' not in text1 and 'tall' not in text1 and 'middle' not in text1:
    print('small, tall and middle not in text')

# დავალება 3
a = int(input("შეიყვანეთ მთელი რიცხვი a: "))
b = int(input("შეიყვანეთ მთელი რიცხვი b: "))
operator = input('შეიყვანეთ მათემატიკური ოპერატორი: ')
if operator == '+':
    print(f'a+b={a + b}')
elif operator == '-':
    print(f'a-b={a - b}')
elif operator == '*':
    print(f'a*b={a * b}')
elif operator == '/':
    print(f'a/b={a / b}')
elif operator == '//':
    print(f'a-ს b-ზე გაყოფისას მთელი ნაწილია {a // b}')
elif operator == '%':
    print(f'a-ს b-ზე გაყოფისას ნაშთია {a % b}')
elif operator == '**':
    print(f'a^b={a ** b}')
