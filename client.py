from AppModules.clientModules import *
from AppModules.socketParams import *


def dataHandler():
    menu()
    choice = input("Key in your choice as per the menu : ")

    if choice not in ["1","2","3" ,"4"]:
        print("Error. Key in the right value as per the menu.")

    else:
        if choice == "1":
            query = "get:" + input("Key in country name : ").capitalize()
            print("Query : ",query)
            results = ClientChat(query).messaging()
            print(results)

        elif choice == "2":
            pass
        
        elif choice == "3":
            pass
        
        elif choice == "4":
            pass



def main():

    # Initialize the program
    choice = "Y"
    
    while True:
      dataHandler()
      choice = input("\nContinue with program? y/n : ").capitalize()

      if choice != "Y":
        print("\nProgram ended....\n")
        break
        
      



if __name__ == "__main__":
    main()
