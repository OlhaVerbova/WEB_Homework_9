from mongoengine import *

connect(host="mongodb+srv://userweb17:567234@cluster0.x8roo9r.mongodb.net/hw9_1", ssl=True)

class Authors(Document):
    fullname = StringField(required=True) 
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=100)
    description = StringField(max_length=5000)


class Qoutes(Document):
    tags = ListField(StringField(max_length=30)) 
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)    
    qoute = StringField(max_length=5000, required=True)
    
    meta = {'allow_inheritance': True}
