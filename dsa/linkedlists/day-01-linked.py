class Node:
    def __init__(self, data) -> None:
        self.data = data # The value the node holds
        self.next = None # Pointer/Reference to the next node(None by default)
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def __str__(self) -> str:
        curr = self.head
        if not curr:
            return "[]"
        items = []
        while curr:
            items.append(str(curr.data))
            curr = curr.next
        # results = " --> ".join(items)
        return "[" + " ——→ ".join(items) + "]"
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def insert_at_end(self, item) -> None:
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
    def insert_at_beginging(self, item) -> None:
        new_node = Node(item)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def count(self, item):
        curr = self.head
        num = 0
        while curr:
            if curr.data == item:
                num += 1
            curr = curr.next
        return num
        
    def insert_at_index(self, index, item) -> None:
        new_node = Node(item)
        if index <= 0:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                print("Index out of bound!")
                return
            print(_, "-->", curr.data)
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        
    def traverse(self) -> None:
        current = self.head
        if not current:
            print('Nothing to traverse')
        while current:
            print(current.data, end=" ——→ ")
            current = current.next
            
    def find(self, value) -> bool:
        curr = self.head
        if not curr:
            return False
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False
    
    def delete_at_beginning(self) -> bool:
        curr = self.head
        if not curr:
            return False
        self.head = curr.next
        return True
    
    def end(self):
        prev, curr = None,  self.head
        if not curr:
            print("This list is empty!")
            return
        if not curr.next:
            self.head = None
            return
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
    def put_end(self, item) -> None:
        new_node = Node(item)
        curr = self.head
        if not curr:
            self.head = new_node
            return
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
    def delete_by_value(self, value) -> bool:
        if self.is_empty():
            print("Empty list!!")
            return False
        curr = self.head
        if curr.data == value:
            self.head = curr.next
            print(f"Deleted {value} from the beginning of the list!")
            return True
        while curr:
            if curr.next and curr.next.data == value:
                curr.next = curr.next.next
                print(f"Deleted {value} from the list!")
                return True
            curr = curr.next
        return False
    
    # update the first 9 to 999
    def update(self, old, new) -> bool:
        if self.is_empty():
            print("No action taken. The list is empty!")
            return False
        curr = self.head
        while curr:
            if curr.data == old:
                curr.data = new
                print(f"Updated {old} with {new}")
                return True
            curr = curr.next
        print(f"The value {old} does not exist in the list!")
        return False
        
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next # Store the next node
            current.next = previous # Reverse the current nodeâs pointer
            previous = current # Move the previous pointer to current node
            current = next_node # Move to the next node in the list
        self.head = previous # Update head to the last node (previous)
                
    
if __name__ == '__main__':            

    lk = LinkedList()
    lk.delete_by_value(120)
    print(lk)
    lk.put_end(80)
    lk.put_end(90)
    print(lk)
    lk.put_end(100)
    # print(lk.delete_at_beginning())
    lk.put_end(110)
    lk.put_end(120)
    lk.put_end(120)
    lk.put_end(120)
    print(lk)
    print(lk.update(120, 988))
    # lk.delete_by_value(120)
    print(lk)
    