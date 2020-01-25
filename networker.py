from TcpServerNode import Node
import socket
PORT = 21596
CONNECTION_LIMIT = 10
class NetworkR(Node):
    def __init__(self, host=None, port=PORT):
        if not host:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            try:
                s.connect(('10.255.255.255',1))
                host = s.getsockname()[0]
            except:
                host = '127.0.0.1'
            finally:
                s.close()
        self.host = host
        self.port = port
        self.peers = set()
        super().__init__(host, port, None)

    def discover_peers(self):
        q = self.peers
        if len(q) < CONNECTION_LIMIT:
            for node in q:
                if node not in self.nodesIn or node not in self.nodesOut:
                    self.connect_with_node(node, self.port)
                self.send_to_node(node, 'gimme_more_nodes<>')


    def broadcast_transaction(self, transaction):
        self.send_to_nodes(f"transaction_broadcasted<>{transaction}")

    def broadcast_block(self, block):
        self.send_to_nodes(f"block_broadcasted<>{block}")

    def get_nodes(self):
        return self.peers

    def received_transaction(self, transaction):
        print(transaction)
        #TODO: code -> add it to mempool, re-broadcast

    def received_block(self, block):
        print(block)
        return ''
        #TODO: code -> validate and add to blockchain, than re-broadcast

    def received_nodes(self, nodes):
        self.peers.update(nodes)
        self.discover_peers()

    def add_peer(self, ip):
        self.peers.add(str(ip))

    # Method override, implement here your own functionality
    def event_node_connected(self, node):
        self.peers.add(node.get_host())

    def event_connected_with_node(self, node):
        self.peers.add(node.get_host())

    def event_node_inbound_closed(self, node):
        self.peers.discard(node.get_host())

    def event_node_outbound_closed(self, node):
        self.peers.discard(node.get_host())

    # If a message comes in, determines what to do!
    def event_node_message(self, node, data):
        print(node)
        function, inp = data.split("<>")
        action_list = {
            'gimme_more_nodes': self.get_nodes,
            'transaction_broadcasted': self.received_transaction,
            'block_broadcasted': self.received_block,
            'OK': lambda: print('OK'),
            'your_nodes': self.received_nodes
        }
        self.send_to_node(node, action_list[function](inp))




##################
N = None
def test(x):
    global N
    N = NetworkR()
    print(N.host)
    N.add_peer(x)
    N.discover_peers()
    N.broadcast_transaction("HEYY")
