class Introduction:
    
    def __init__(self, name , id , batch):
        self.__name = name
        self.__id = id  # now we cant acess these infomally and that is called encapsulation
        self.__batch=batch
        
    def __str__(self):
        return "My name {} Id {} and Batch {} ".format(self.__name, self.__batch,self.__id)
    def university(self,university):
        return "My name is [{}] Id [{}]  Batch [{}] and University [{}] ".format(self.__name, self.__id,self.__batch,university)
    
    def getname(self):
        return self.__name
        
    
intro = Introduction("Hridoy",123456,1)

print(intro)
print(intro.university('Daffodil International University'))
# print(intro.__name) will throw error
print(intro.getname())
        