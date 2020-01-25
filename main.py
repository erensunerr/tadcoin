
KEY_PAIR=None


from crypto import
def setup_crypto():
    global KEY_PAIR = 

def setup_networking():

def setup_other():

def setup_ui():
    print("""
    1) make a transaction
    2) input a known peer
    3) input key pair location
    4) take a look at your balance
          """)
    choice = input("->")
    if choice == 1:
        t = Transaction()
    elif choice == 2:
    elif choice == 3:
    elif choice == 4:
    else:
        print("Invalid choice")
def run():

run()
