# Practice

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

# 1 -- 2 -- 3 -- 4 -- 6 -- 7 -- 8
# 1 -- 2 -- 3 -- 4 -- 6 -- 7 -- 8
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                print(current.value)
                print("iter", counter)
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

e56 = Element(56)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)

ll.insert(e56, 4)


print(ll.get_position(1).value)
print(ll.get_position(2).value)
print(ll.get_position(3).value)
print(ll.get_position(4).value)
print(ll.get_position(5).value)


