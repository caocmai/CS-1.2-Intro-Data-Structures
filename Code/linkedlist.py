#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node

        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
       
        Run Time (Best and worst): O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
       
        items = [] # O(1) only one step to do this
        # Start at head node
        current_node = self.head  # O(1) only one step to do this
        # Loop until node is None, meaning at the end
        while current_node is not None:   # O(n) loop through all of the list
            items.append(current_node.data) # O(1) only one step to do this
            # Now the node is equal to the node.next to move to the next item
            current_node = current_node.next  # O(1) only one step to do this
        return items   # O(1) only one step to do this

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        """Run time(Best and Worst): O(1) because only have to check once wether the head exists """


        # Checking wether the head exists
        if self.head is None:
            return True
        else:
            return False

        # return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
       
        Run time(Best and Worst): O(n) because have to go through all of the nodes to get the number of items in list"""
       
        # TODO: Loop through all nodes and count one for each

        count = 0
        # Set current node to point to head node, rememeber self.head points to a Node object, which has data and next
        current_node = self.head

        # Iterate through all the list until current_node is not None, because if none then last item
        while current_node is not None: # Meaning the head exists
            current_node = current_node.next # This is only possible becauase not None, so must/can have .next property
            count += 1
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        
        Run time(Best and Worst): O(1) because the tail can be accessed in one step"""
        
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        new_node = Node(item) # Create a new Node object with the spcified item

        if self.tail is not None:
            # Appending node after tail, if tail exists, and tail currently points at None
            self.tail.next = new_node # Note! Can only do this if tail is NOT None, meaning it exists
            self.tail = new_node # Then you set the self.tail to the newly last node, updating the tail

        else:
            self.head = new_node # If no tail then set the self.head to point to newly created Node object
            self.tail = new_node # And self.tail also equals this newly created node
        


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        
        Run time(Best and Worst): O(1) because like head, the head can be accessed in one step"""
        
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

        new_node = Node(item)

        if self.head is not None:
            new_node.next = self.head
            self.head = new_node # Resets head to be this new node

        else:
            self.tail = new_node # Sets head to be this new node
            self.head = new_node # Sets head to be this new node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?
        
        Run time(Best Case): O(1), becuse if you let lucky you can find it running just once
        Run time(Worst Case): O(n), becuase you have to go every single one"""
        
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        current_node = self.head

        while current_node is not None: # Check make sure there's a list
            if quality(current_node.data) == True:
                return current_node.data
            else:
                current_node = current_node.next

        return None # To catch if item doesn't exist in list

    def replace(self, to_replace_item, new_item):
        """Replaces an item in the list with a new item"""
        """Run time(Worst): O(n) because have to go through the entire list"""
        """Run time(Best): O(1) because found on first instance"""


        current_node = self.head

        while current_node is not None:
            if current_node.data == to_replace_item: # If the data in the node is found in list.
                current_node.data = new_item # Sets the current_node data to be the new stuff
                return
            else:
                current_node.current_node.next
            


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?

        Run time(Best Case): O(1), becuse find it after the head pointer and delete it by running just once
        Run time(Worst Case): O(n), becuase you have to go every single one to find it and delete"""
        
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        previous_node = None
        current_node = self.head

        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        elif self.head == self.tail: # If there is only one node in the list
            if current_node.data == item:
                self.head = None # This to delete both the pointers of head and tail, because only have one
                self.tail = None
            else:
                raise ValueError('Item not found: {}'.format(item)) # If item is not in list
        
        else:
            while current_node is not None: # To traverse through list
                if current_node.data == item:
                    # If the item found in list to be removed, then executed
                    if previous_node is None: # To remove item at the head cause head doesn't have previous node
                        self.head = current_node.next # Reset so head points to the next node
                        # if current_node == self.tail: # To remove at the tail
                        #     self.tail = previous_node
                    # Removing item from tail, b/c tail.next points to None
                    elif current_node.next is None:
                        previous_node.next = None # To delete previous node next pointer
                        self.tail = previous_node # Reset tail to point to the previous node

                    # Item to remove is not tail or head
                    else:
                        previous_node.next = current_node.next # Set previous pointer next to current next

                    return # Finished deleting
                # If item not yet found so moving to next node
                else:
                    previous_node = current_node
                    current_node = current_node.next
            
            raise ValueError('Item not found: {}'.format(item)) # To make sure the item is in the list after going through the list
        


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
