import speech_recognition as sr

r = sr.Recognizer()
def recognise():
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=5)
    try:
        sp=r.recognize_google(audio)
        s=int(sp)
        print("You said ",s)
        return s
    except Exception as e:
        print(e)
        print("Didn't get you, can you say it again?")
        return recognise()

flag = 1
while (flag == 1):
    with sr.Microphone() as source:
        print("Speak into mic first number: ")
        num1q = recognise()

        print("Speak into mic second number: ")
        num2q = recognise()

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