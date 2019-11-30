from TcpServerNode import Node
PORT=21596
NAMESPACE_SERVERS=[]
class P2PNode (Node):
    def __init__(self, host, port):
        super(P2PNode, self).__init__(host, port, None)
        print("MyPeer2PeerNode: Started")

    # Method override, implement here your own functionality
    def event_node_connected(self, node):
        print("p2p_event_node_connected: " + node.getName())

    def event_connected_with_node(self, node):
        print("p2p_event_node_connected: " + node.getName())

    def event_node_inbound_closed(self, node):
        print("p2p_event_node_inbound_closed: " + node.getName())

    def event_node_outbound_closed(self, node):
        print("p2p_event_node_outbound_closed: " + node.getName())

    # If a message comes in, determines what to do!
    def event_node_message(self, node, data):
        print("p2p_event_node_message: " + node.getName() + ": " + str(data))
