import speech_recognition as sr

r = sr.Recognizer()

flag = 1
while (flag == 1):
    with sr.Microphone() as source:
        print("Speak into mic first number: ")
        num1 = r.listen(source, timeout=5)
        num1s = r.recognize_google(num1)
        print("You said: ", num1s)
        num1q = int(num1s)

        print("Speak into mic second number: ")
        num2 = r.listen(source, timeout=5)
        num2s = r.recognize_google(num2)
        print("You said: ", num2s)
        num2q = int(num2s)

        print("Speak add '+', subtract '-', divide '/', multiply 'x'")
        fun = r.listen(source, timeout=5)
        fun1 = r.recognize_google(fun)
        print("You said: ", fun1)

        if (fun1 == "ad"):
            print("Your sum is: ", num1q + num2q)
        elif (fun1 == "subtract"):
            print("Your difference is: ", num1q - num2q)
        elif (fun1 == "divide"):
            print("Your quotient is: ", num1q / num2q)
        elif (fun1 == "multiply"):
            print("Your product is: ", num1q * num2q)
        else:
            print("Sorry! Please try again")

        print("Would you like to try more? Say yes or no")
        choice = r.listen(source)
        choice1 = r.recognize_google(choice)
        if (choice1 == "yes"):
            print("Okay!")
            flag = 1
            continue

        elif (choice1 == "no"):
            print("Okay! Bye!")
            flag = 0

        else:
            print("Sorry! I didn't get what you said, please refresh!")

# code by Kushagra Gupta