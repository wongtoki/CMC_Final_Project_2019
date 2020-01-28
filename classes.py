import pandas as pd
import uuid
import random

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


class _Message:  # this upper class is only used for Post and Reply
    def __init__(self, content, likes, date, creator):
        self.content = content
        self.likes = likes
        self.date = date
        self.creator = creator


class Reply(_Message):
    pass  # for now, Reply is just the same as _Message


class Post(_Message):
    def __init__(self, Microblog, MicroblogLikes, Created, Door):
        _Message.__init__(self, Microblog, MicroblogLikes, Created, Door)
        self.Reacties = []  # [Reply, Reply, ...]
        self.repliedUsers = []  # [User, User, ...]

    def addReaction(self, reply):
        self.Reacties.append(reply)
        self.repliedUsers.append(reply.creator)

    def getCreator(self):
        return self.creator

    def getRepliers(self):
        return self.repliedUsers

    @staticmethod
    def getConnections(bloglist):
        edgeList = []
        for blog in bloglist:  # original Post
            for replier in blog.getRepliers():  # Reply
                edgeList.append((blog.getCreator(), replier))
        return edgeList


class Poll(Post):
    def __init__(self, Microblog, MicroblogLikes, Created, Door, choices=[]):
        Post.__init__(self, Microblog, MicroblogLikes, Created, Door)
        self.choices = choices


class User:
    def __init__(self, FullName, Function='', LastLogin='', IsExternal='', ManagerLevel='', IsAccountManager='',
                 HasAvatar='', HasPhonenumber='', Summary='', DateOfBirth='', EmployeeSince='', Organization='',
                 posts=[], replies=[]):

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
        self.replies = replies

        # Some values for path finding
        self.id = str(uuid.uuid4())
        self.interactivity = 0
        self.parent = None
        self.connections = []
        self.fscore = 0
        self.hscore = 0
        self.gscore = 0

    def __str__(self):  # Added because networkx graphs wants to print the userobject and we want to have it print a readable name
        return(self.FullName.split()[0])

    def addPost(self, postobject):
        self.posts.append(postobject)

    def addReply(self, replyobject):
        self.replies.append(replyobject)
