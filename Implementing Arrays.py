class MyArray():
    def __init__(self):
        self.length = 0 #We initialize the array's length to be zero
        self.data = {} 
    
     #When we print the instance of the class, the built-in __str__ method is called. So we can modify the __str__ method inside the class
    #To suit our needs.
    def __str__(self):
         return str(self.data)

    def get(self,index):
        return (self.data[index])
    
    def push(self, num):
        self.data[self.length] = num
        self.length += 1

    def pop(self):
        a = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return a

    def insert(self,index,num):
        self.length+=1
        for i in range(index,self.length-1):
            self.data[i+1] = self.data[i]
        self.data[index] = num                
    
    def delete(self,index):
        for i in range(self.length-1,index,-1):
            self.data[i-1] =self.data[i]
        del self.data[index]     
        self.length-=1
    
arr = MyArray()


arr.push(6)
arr.push (7)
arr.push (10)
arr.push(8)
arr.get(0)
arr.insert(2,9)
print(arr)
arr.delete(3)
print(arr)
