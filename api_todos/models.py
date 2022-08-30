import uuid
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Tag(models.Model): 
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255,unique=True)

    def __repr__ (self): 
        return f'Tag({self.name})'
    
    def __str__(self):
        return f'Tag({self.name})'
    

class Todo(models.Model) :
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    isDated = models.BooleanField(default=False)
    deadline = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    isDone = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

    def __str__(self) -> str:
        return f"Todo({self.title[:20]} : {self.isDone})"
    
    def __repr__(self) -> str:
        return f"Todo({self.title[:20]} : {self.isDone})"