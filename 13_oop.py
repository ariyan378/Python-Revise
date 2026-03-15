class Introduction:
    
    def __init__(self, name , id , batch):
        self.name = name
        self.id = id
        self.batch=batch
        
    def __str__(self):
        return "My name {} Id {} and Batch {} ".format(self.name, self.batch,self.id)
    def university(self,university):
        return "My name is [{}] Id [{}]  Batch [{}] and University [{}] ".format(self.name, self.id,self.batch,university)
        
    
intro = Introduction("Hridoy",123456,1)

print(intro)
print(intro.university('Daffodil International University'))
        