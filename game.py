class User:
    def __init__ (self, name, money, tools):
        self.name = name
        self.money = money
        self.tools = tools

user = User("", 0, ["Teeth"])



def startGame():
    user.name = input("\nEnter your name here: ")
    print("****************************************************************")
    print(f"\nHey {user.name.capitalize()}! Welcome to the Landscaper game!\n\nThe objective of the game is to gather enough money to kickstart your new landscaping business!\n**ALSO JUST AS IMPORTANT, you will need to hire a workforce to keep future iterations of the company alive to win as well!\n...but nobody said this was going to be easy.\n\nYou'll start off solely with your teeth to cut lawns and gain revenue.\nDon't fret! As you advance, you will be able to afford different types of tools for more efficient progress!\n\nLet's Start!\n")
    userPrompt()

def userPrompt():
    print(f"\n{user.name.capitalize()}, what would you like to do now?\n\tYou currently have ${user.money}.\n\tThese are your available tools: (1): {', '.join( str(e) for e in user.tools)}\n")
    userInput = input("Type - (1): to cut grass (2): to visit the store (3) to quit the game\n\n")
    if userInput == "1":
        print("****************************************************************")
        print("\nYou chose to go cut grass!\n")
        cutGrass()
    elif userInput == "2":
        print("****************************************************************")
        print("\nTime to go shopping!\n")
        goStore()
    elif userInput == "3":
        print("\nGame Over\n")
    else:
        print("\nThat wasn't one of the options! Try again!\n")
        userPrompt()

def cutGrass():
    print("Now that we're at work, lets make some money!")
    toolChoice = input(f"Which tool would you like to use?\nAvailable tools:\n\t(1): {', '.join( str(e) for e in user.tools)}\n\n")
    if toolChoice == "1":
        user.money += 1
        print("****************************************************************")
        print(f"\nYou made $1 and now have ${user.money} in your bank account!")
        userPrompt()
    elif toolChoice == "2":
        user.money += 5
        print("****************************************************************")
        print(f"\nYou made $5 and now have ${user.money} in your bank account!")
        userPrompt()
    elif toolChoice == "3":
        user.money += 50
        print("****************************************************************")
        print(f"\nYou made $50 and now have ${user.money} in your bank account!")
        userPrompt()
    elif toolChoice == "4":
        user.money += 100
        print("****************************************************************")
        print(f"\nYou made $100 and now have ${user.money} in your bank account!")
        userPrompt()
    elif toolChoice == "5":
        user.money += 250
        print("****************************************************************")
        print(f"\nYou made $250 and now have ${user.money} in your bank account!")
        userPrompt()

def goStore():
    print("We're here at the shop, lets spend our hard-earned cash!")
    print(f"\tCurrent balance: ${user.money}")
    purchaseChoice = input("What do you want to purchase?\n\nType (number) to buy - \n(1):Rusty Scissors for $5\n(2):Old-timey Push Lawnmower for $50\n(3):Battery-powered Lawnmower for $250\n(4):A Team of Starving Students for $500\n(5):Go Back\n\n")
    if (purchaseChoice == "1") and (user.money >=5):
        print("****************************************************************")
        print ("You bought a pair of Rusty Scissors and will now make $5 each job!")
        user.tools.append("(2): Rusty Scissors")
        user.money -= 5
        print(f"Your new account balance is {user.money} and your available tools are now (1): {', '.join( str(e) for e in user.tools)}")
        userPrompt()
    elif (purchaseChoice == "2") and (user.money >=25):
        print("****************************************************************")
        print ("You bought an Old-timey Push Lawnmower and will now make $50 each job!")
        user.tools.append("(3): Old-timey Push Lawnmower")
        user.money -= 25
        print(f"Your new account balance is {user.money} and your available tools are now (1): {', '.join( str(e) for e in user.tools)}")
        userPrompt()
    elif (purchaseChoice == "3") and (user.money >=250):
        print("****************************************************************")
        print ("You bought an Battery-powered Lawnmower and will now make $100 each job!")
        user.tools.append("(4): Battery-powered Lawnmower")
        user.money -= 250
        print(f"Your new account balance is {user.money} and your available tools are now (1): {', '.join( str(e) for e in user.tools)}")
        userPrompt()
    elif (purchaseChoice == "4") and (user.money >=500):
        print("****************************************************************")
        print ("You bought a Team of Starving Students and will now make $250 each job!")
        user.tools.append("(5): A Team of Starving Students")
        user.money -= 500
        print(f"Your new account balance is {user.money} and your available tools are now (1): {', '.join( str(e) for e in user.tools)}")
        userPrompt()
    elif purchaseChoice == "5":
        userPrompt()
    else:
        print("****************************************************************")
        print("\nYou can't afford that yet! Choose another option!\n")
        goStore()

def endGame():
    while True:
        user.money >= 1000
        print("You did it! You have finally achieved your goal of owning a successful landscaping company!")
        print("\nCongrats! You now have dirty teeth, rusty scissors, 2 types of lawnmowers\n...and most importantly, a community of starving students.")
        break

startGame()
endGame()