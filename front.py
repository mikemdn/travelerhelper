########### Partie Front ##################
def ask_input(question):
    while True:
        data = input("{} (y/n) : ".format(question))
        if data == "y" or data == "Y":
            return True
        elif data == "n" or data == "N":
            return False
        else:
            print("The answer is not valid.\n")

def display_summary(array):
    print("Your destination is : {}".format(array['destination']))
    print("Your criteria are :")
    for item in array:
        if array[item] == True:
            print(item)

def main():
    search = False
    while search == False:
        criteria = {}

        destination = input("Where are you going ? : ")
        criteria['destination'] = destination

        charged = ask_input("Are you carrying a heavy charge ?")
        criteria["You are charged"] = charged

        walk = ask_input("Do you want to walk ?")
        criteria["You want to walk"] = walk

        driving_licence = ask_input("Do you have a driving licence ?")
        criteria["You have a driving licence"] = driving_licence

        bike = ask_input("Do you want to use a bike ?")
        criteria["You don't ming using a bike"] = bike

        price = ask_input("Is the price important for you ?")
        criteria["The price is important for you"] = price

        navigo = ask_input("Do you have a Navigo card ?")
        criteria["You have a Navigo card"] = navigo

        credit_card = ask_input("Do you have a credit card ?")
        criteria["You have a credit card"] = credit_card

        print(criteria)
        # print(display_summary(criteria))
        confirm = input("Do you confirm ? (y/n) :")
        if confirm == "y" or confirm == "Y":
            search = True

if __name__ == "__main__":
    main()