import pandas as pd

class Reply:
    def __init__(self, Reactie, ReactieLikes, ReactieDatum, ReactieDoor):
        self.Reactie = Reactie
        self.ReactieLikes = ReactieLikes
        self.ReactieDatum = ReactieDatum
        self.ReactieDoor = ReactieDoor


class Post:
    def __init__(self, Microblog, MicroblogLikes, Created, Door, isPoll):
        self.Microblog = Microblog
        self.MicroblogLikes = MicroblogLikes
        self.Created = Created
        self.Door = Door
        self.isPoll = isPoll
        self.Reacties = []

    #def __str__(self):
    #    return("Post:", self.Microblog,
    #    "\n of User: ", self.Door.getName())

    def addReaction(self, Reactie, ReactieLikes, ReactieDatum, ReactieDoor):
        self.Reacties.append(Reply(Reactie, ReactieLikes, ReactieDatum, ReactieDoor))
           
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

    #def __str__(self):
    #    return("Full Name:", self.FullName,
    #    "\n Posts: ", self.posts)
    
    def getName(self):
        return(self.FullName)
