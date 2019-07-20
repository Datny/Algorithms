class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


class DoubleLinkListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prv_node = None
