# Write a function to reverse a Linked List in place.
# The function will take in the head of the list as input
# and return the new head of the list.

# TODO: Rewrite + learn.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head):
    # Set up current,previous, and next nodes
    current = head
    previous = None
    nextnode = None

    # until we have gone through to the end of the list
    while current:
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        nextnode = current.nextnode

        # Reverse the pointer ot the next_node
        current.nextnode = previous

        # Go one forward in the list
        previous = current
        current = nextnode

    return previous
