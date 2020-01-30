import pandas as pd
from classes import *
import time
import sys

def readUsers(userCSV):
    # read csv with the users
    userDF = pd.read_csv(userCSV, encoding='utf-8')
    # create a dictionary of user-objects, e.g. John Johnsen <classes.py-User>
    userDict = {u.FullName: User(
        u.FullName, u.Function, u.LastLogin, u.IsExternal, u.ManagerLevel, u.IsAccountManager,
        u.HasAvatar, u.HasPhonenumber, u.Summary, u.DateOfBirth, u.EmployeeSince, u.Organization
    ) for u in userDF.itertuples()}
    # Sandra Schuur was missing in persons.csv:
    userDict['Sandra Schuur'] = User('Sandra Schuur')
    return userDict


def readBlogs(microblogs, polls, userDict):
    # read the csv with the microblogs
    blogsDF = pd.read_csv(microblogs, encoding='utf-8')
    # we use polls.csv to check whether a microblog is a 'post' or a 'poll'
    pollsDF = pd.read_csv(polls, encoding='utf-8')
    # making a 'list' of polls
    allPolls = pollsDF['Microblog'].tolist()

    # adding blogs to userDict and blogsDict
    blogsDict = {}
    for _, row in blogsDF.iterrows(): # for every row in microblogs.csv:
        Microblog = row['Microblog']

        # if the microblog DOES NOT EXIST in blogsdict, create a new object in the dictionary,
        # (if the microblog DOES exist in blogsdict, we add only the Reply)
        if Microblog not in blogsDict:

            # add blog to blogsDict and to the User
            if Microblog in allPolls:  # if the microblog exists in polls.csv it is a poll
                currentblog = Poll(Microblog, row['MicroblogLikes'], row['Created'], userDict[row['Door']])
            else:  # not in polls.csv, so the current item is just a 'normal' Post
                currentblog = Post(Microblog, row['MicroblogLikes'], row['Created'], userDict[row['Door']])
            # add to the blogsdict
            blogsDict[Microblog] = currentblog
            # add to the User
            userDict[row['Door']].addPost(currentblog)
            # now, also add blog to the User

        # add THE REPLY to blogsdict and userdict
        # only add if 'Reactie' and likes are not NULL
        if (not pd.isnull(row['Reactie'])) and (not pd.isnull(row['ReactieLikes'])):
            # add reaction to the blogsdict
            currentReply = Reply(row['Reactie'], row['ReactieLikes'],
                                 row['ReactieDatum'], userDict[row['ReactieDoor']])
            blogsDict[Microblog].addReaction(currentReply)
            # now, also add reaction to the User
            userDict[row['ReactieDoor']].addReply(currentReply)
        
    return blogsDict


def readcsv(usercsv='persons.csv', postcsv='microblogs.csv', pollcsv='polls.csv'):
    userDict = readUsers(usercsv)
    blogsDict = readBlogs(postcsv, pollcsv, userDict)

    return userDict, blogsDict


if __name__ == "__main__":
    readcsv()
