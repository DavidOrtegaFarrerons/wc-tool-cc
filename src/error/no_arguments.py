def no_arguments():
    print("You have not sent the correct amount of arguments!")
    print("The following arguments are available to use:")
    print("-"*40)
    print("-c file.extension | Will count the total bytes of the given file")
    print("-l file.extension | Will count the total lines of the given file")
    print("To run this command, please use \"python -m src -[c|l] file.extension\"")
