class Node:
    def __init__(self, data, next_node_ref):
        self.data = data
        self.next_node = next_node_ref


class LinkedList:
    def __init__(self):
        self.list = None
        self.last_node = None

    def add(self, data, next_node_ref):
        if not data:
            return

        new_node = Node(data, next_node_ref)
        if not self.list:
            self.list = new_node
            self.last_node = self.list
        elif next_node_ref:
            self.list.next_node = new_node
        elif not next_node_ref:
            self.last_node.next_node = new_node
        return new_node

    def remove(self, node_ref):
        pass

    def display(self):
        print_list = ""
        if self.list:
            print_node = self.list
            while print_node.data:
                if print_node.next_node:
                    print_list += str(print_node.data)+"->"
                    print_node = print_node.next_node
                else:
                    print_list += str(print_node.data)
                    break
            print print_list
        else:
            print "List not initialized"

    def find_location_of(self, node_ref):
        pass


ll = LinkedList()
ll.add(12, None)
ll.add(13, None)
ll.add(14, None)
ll.add(15, None)
ll.add(16, None)
ll.add(17, None)
ll.add(18, None)
ll.add(19, None)
ll.display()
