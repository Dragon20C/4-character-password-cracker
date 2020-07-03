password = ["F", "o", "o", "d"]

char1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
char2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
char3 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
char4 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
guess = [char1[0], char2[0], char3[0], char4[0]]
number = 0
number1 = 0
number2 = 0
number3 = 0


while True:
    if guess == password:
        print("The password is: " + str(guess))
        break
    else:
        guess[0] = char1[number]
        guess[1] = char2[number1]
        guess[2] = char3[number2]
        guess[3] = char4[number3]
        number += 1
        if number == 61:
            number = 0
            number1 += 1
            if number1 == 61:
                number1 = 0
                number2 += 1
                if number2 == 61:
                    number2 = 0
                    number3 += 1
                    if number3 == 61:
                        number3 = 0
        print(guess)
