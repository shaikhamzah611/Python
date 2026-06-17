def shutdownhandler():
    user_input = input("Enter Yes/No for shut down:")
    if user_input=='Yes':
        print("Shutting Down")
    elif user_input=='No':
        print("Abort ShutDown")
    elif user_input=='no':
        print("Abort ShutDown")
    elif user_input=='yes':
        print("Shutting Down")
    else:
        print("Sorry,Invalid input!!!")
        print("Enter the letters properly")

shutdownhandler()