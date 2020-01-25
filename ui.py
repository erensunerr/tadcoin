#TODO: make it more beautiful https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
class UserInterface:
    def ask():
        print(f"""
        1) Send money to pubkey
        2) View Balance
        3) Turn mining on or off
        4) Keypair Operations
        5) Add peer
        """)
        x = int(input())
        return x
