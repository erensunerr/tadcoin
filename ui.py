#TODO: make it more beautiful https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
class UserInterface:
    def __init__(self):
        print(f"Welcome to tadcoin!")

    def ask(self):
        print(f"""
        0) Quit
        1) Send money to pubkey
        2) View Balance
        3) Turn mining on or off
        4) Keypair Operations
        """)
        x = int(input())
        if x == 0:




    
        elif x == 1:





        elif x == 2:




            pass
        elif x == 3:
        elif x == 4:
        else:
            print("Please enter a valid option")
        return x
    def send_money(self):
        self.event_handler.register_event()
    def keypair_operations(self):
        print(f"""
        1) Generate new key pair
        2) Open a key pair
        3) Save the key pair
        """)
        x = int(input())
        return x
    def
