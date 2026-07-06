


class Node:
    def __init__(self, data):
        self.data = data  # ინახავს მონაცემს
        self.next = None  # ინახავს შემდეგი მონაცემის მისამართს, რომელიც თავდაპირველად არის None
       

class LinkedList:
    def __init__(self):
        self.head = None  # ინახავს სიას, რომელიც თავდაპირველად ცარიელია, სანამ არ დავამატებთ პირველ ელემენტს

    def append(self, data):
        """Adds a new node containing 'data' to the very end of the list."""
        new_node = Node(data)
        
        # თუკი სია ცარიელია, ახალი ელემენტი ხდება სიასის თავი
        if not self.head:
            self.head = new_node
            return
        
        # თუ სია არ არის ცარიელი, უნდა გავიდეთ ბოლომდე და დავამატოთ ახალი ელემენტი ბოლოში.
        current = self.head
        while current.next is not None:
            current = current.next
            
        # დავამატოთ ახალი ელემენტი ბოლოში
        current.next = new_node


# ლექციაზე დაწერილ LinkedList კლასში დაამატეთ prepend მეთოდი რომელიც სიის დასაწყისში დაამატებს ახალ ელემენტს.
    
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        
        self.head = new_node


# ლექციაზე დაწერილ LinkedList კლასში დაამატეთ delete მეთოდი რომელიც გადაცემული მნიშვნელობის მიხედვით წაშლის ელემენტს LinkedList-დან.

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        
        while current is not None and current.data != data:
            prev = current
            current = current.next
        
        prev.next = current.next

    def display(self):
        """
        ყველაზე მარტივი გზა linked list-ის მონაცემების გამოსახატად.
        """
        current = self.head
    
        while current is not None:
        # დაბეჭდე მონაცემები და შემდეგი ელემენტის მისამართი
            print(current.data, end=" -> ")
            current = current.next
        # გადაიტანე ფოინთერი შემდეგ ელემენტზე
        
        
    # დაბეჭდე None, რათა გამოიხატოს, რომ სიის ბოლო ელემენტის შემდეგ არაფერი მოდის.
        print("None")



l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.display()

l1.prepend(9)
l1.prepend(7)
l1.display()

#ვშლი ბოლოს
l1.delete(30)
l1.display()

#ვშლი პირველს
l1.delete(7)
l1.display()

#ვშლი შუა ელემენტს
l1.delete(10)
l1.display()