from TcpServerNode import Node
PORT = 21596
KNOWN_PEERS = {'',''} #ip addresses
class NetworkR(Node):
    def __init__(self, host, port, known_peers=KNOWN_PEERS):
        super().__init__(host, port, None)
        self.known_peers = known_peers
        for p in self.known_peers:
            self.discover_peers(p)


    def discover_peers(self, known_peer):
        global PORT
        self.connect_with_node(known_peer, PORT)
        
    def get_nodes(self):
        return self.known_peers

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
        print(node)
        action_list = {
            'gimme_more_nodes':self.get_nodes
        }
        self.send_to_node(node, action_list[data]()) #calls the func associated through action list
