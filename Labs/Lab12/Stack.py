class Stack:

    def __init__(self):
        self.s = []
    

    def pop(self):
        """
        TODO
        """
        if self.s == []:
            return None
        else:
            return self.s.pop()
    

    def push(self, item):
        """
        Pushes an item on to a stack
        """
        self.s.append(item)
    

    def isEmpty(self):
        """
        Returns True is stack is empty, False otherwise
        """
        return self.s == []
    
    def peek(self):
        item = self.pop()
        self.push(item)
        return item
    
    def __str__(self):
        return self.s