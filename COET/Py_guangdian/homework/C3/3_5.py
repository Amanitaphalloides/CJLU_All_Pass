def print_tic_tac_toe():
    for i in range(11):
        if i % 5 == 0:
            print("+ - - - - + - - - - +")
        else:
            print("|         |         |")

print_tic_tac_toe()