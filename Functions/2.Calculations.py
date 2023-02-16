def result_form_action(act, num1, num2):
    if act == "multiply":
        return num1*num2
    elif act == "divide":
        return num1//num2
    elif act == "add":
        return num1+num2
    elif act == "subtract":
        return num1-num2


action = input()
number_one = int(input())
number_two = int(input())

print(result_form_action(action, number_one, number_two))