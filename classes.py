import pandas as pd

'''
Variables starting with a captital already existed in the csv-files (Door, Reacties, etc...)
Variables starting with a small letter we made up ourselfs (content, repliedUsers, etc...)

Classes:
_Message - 'private' upper class
│
├─ Post (subclass of _Message) 
│  └─ Poll (subclass of Post, since a Poll is a kind of Post) 
│
└─ Reply (subclass of _Message)

User: class for all Users
'''
class _Message: # this upper class is only used for Post and Reply
    def __init__(self, content, likes, date, creator):
        self.content = content
        self.likes = likes
        self.date = date
        self.creator = creator

class Reply(_Message):
    pass # for now, Reply is just the same as _Message

class Post(_Message):
    def __init__(self, Microblog, MicroblogLikes, Created, Door):
        _Message.__init__(self, Microblog, MicroblogLikes, Created, Door)
        self.Reacties = [] # [Reply, Reply, ...]
        self.repliedUsers = [] # [User, User, ...]

    def addReaction(self, Reactie, ReactieLikes, ReactieDatum, ReactieDoorObject):
        self.Reacties.append(Reply(Reactie, ReactieLikes, ReactieDatum, ReactieDoorObject))
        self.repliedUsers.append(ReactieDoorObject)

class Poll(Post):
    def __init__(self, Microblog, MicroblogLikes, Created, Door, choices=[]):
        Post.__init__(self, Microblog, MicroblogLikes, Created, Door)
        self.choices = choices

class User:
    def __init__(self, FullName, Function='', LastLogin='', IsExternal='', ManagerLevel='', IsAccountManager='',
    HasAvatar='', HasPhonenumber='', Summary='', DateOfBirth='', EmployeeSince='', Organization='', posts=[]):
        self.FullName = FullName
        self.Function = Function
        self.LastLogin = LastLogin
        self.IsExternal = IsExternal
        self.ManagerLevel = ManagerLevel
        self.IsAccountManager = IsAccountManager
        self.HasAvatar = HasAvatar
        self.HasPhonenumber = HasPhonenumber
        self.Summary = Summary
        self.DateOfBirth = DateOfBirth
        self.EmployeeSince = EmployeeSince
        self.Organization = Organization
        self.posts = posts

    def __str__(self): # Added because networkx graphs wants to print the userobject and we want to have it print a readable name
        return(self.FullName)
