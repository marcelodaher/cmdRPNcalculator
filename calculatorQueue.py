class CalculatorQueue:
    """A LIFO Queue to keep number data"""
    q = [] #where we will keep our numbers
    
    def __init__(self):
        self.q = []
    
    def __str__(self):
        """A method to print the queue"""
        if self.empty():
            return "Queue is empty"
        s = "Queue:"
        for element in self.q:
            s += '\n' + str(element)
        return s
    
    def push(self, number):
        """Method to add elements to the top of the queue"""
        self.q.append(number)
    
    def get (self):
        """Method to pop and return first element"""
        return self.q.pop();
    
    def clear(self):
        """Method to empty the queue"""
        self.q = []
    
    def empty(self):
        return 0 == len(self.q)
    
