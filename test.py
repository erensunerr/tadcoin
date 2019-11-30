# from block import Block
# from blockchain import Blockchain
# chain = Blockchain()
# b1 = Block()
# b1.add_data("Donaldo is trumpado")
# b1.add_data("Jesse is good")
# chain.add_block(b1)
# b2 = Block()
# b2.add_data("xx")
# b2.add_data("yy")
# chain.add_block(b2)
# print(chain.chain)


from TcpServerNode import Node


node = None # global variable

def callbackNodeEvent(event, node, other, data):
    print("Event Node 1 (" + node.id + "): %s: %s" % (event, data))
    node.send_to_nodes({"thank": "you"})

node = Node('localhost', 10000, callbackNodeEvent)

node.start()

node.connect_with_node('12.34.56.78', 20000)

node.terminate_flag.set() # Stopping the thread

node.send_to_nodes({"type": "message", "message": "test"})

while True:
    time.sleep(1)

node.stop()
node.join()
