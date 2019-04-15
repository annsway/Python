########################
### Build a linked list 
########################

# create an element 

class Element(object): #
	def __init__(self, value):
		self.value = value		# an element stores a value 
		self.next = None	 	# element.next is a pointer; the element has property (variable) to refer to the next element 


class LinkedList(object):

	# Members: 
	# Element self.head // head 的类型是Element (class)

	def __init__(self, head=None):
		self.head = head

	# create a linked list

	def append(self, new_element): # 把Element(车厢) append 到 队尾
		current = self.head # 火车车头；the first element in the list. Note: if no head is defined in a linked list, it will default to None. 
		if self.head: 		# True: self.head exists; False: self.head is null
			while current.next: # True: current.next exists; False: current.next is null
				current = current.next
			current.next = new_element # .next is a hook to link the next elment 
		else:
			self.head = new_element #If there is no head already (null), you should assign new_element to it to become the head and do nothing else.

		# 如果没有head, 要存两个new_elements，那么第一个new_element进else, 第二个new_element进if

	def get_element_by_position(self, position):
		if position < 1:
			return None

		counter = 1 # counter 是个计数器，每走过一节车厢就增加1
		current = self.head
		while current and counter < position:
			current = current.next
			counter += 1

		return current

	def insert_to_position(self, new_element, position):
		counter = 1
		current = self.head
		if position > 1:
			while current and counter < position:
				if counter == position - 1:
					new_element.next = current.next
					current.next = new_element
					# the previous current_next is replaced with new_element and no longer exists 
					# both current.next and new_element.next are pointers. 
					# A pointer is an object that stores the memory address of another value located in computer memory. 
					# A pointer references a location in memory, and obtaining the value stored at that location is known as dereferencing the pointer.
				current = current.next
				counter += 1
		elif position == 1: # 插第一个时
			new_element.next = self.head # new_element 的 next 的 pointer 指向 self.head 
			self.head = new_element # both self.head and new_element have type of Element (Class)

	def delete(self, value):
		if not self.head:
			return

		if self.head.value == value: # 如果想要删除的值是head
			self.head = self.head.next

		current = self.head
		while current.next and current.next.value != value: # this is to check if the next value equals to the given value to be deleted; if not, move on to check the next 
			current = current.next

		if current.next:
			current.next = current.next.next;



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_element_by_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_element_by_position(3).value)

# Test insert_to_position
ll.insert_to_position(e4,3)
# Should print(4 now
print(ll.get_element_by_position(3).value)

# Test delete
ll.delete(1)
# Should print(2 now
print(ll.get_element_by_position(1).value)
# Should print(4 now
print(ll.get_element_by_position(2).value)
# Should print(3 now
print(ll.get_element_by_position(3).value)