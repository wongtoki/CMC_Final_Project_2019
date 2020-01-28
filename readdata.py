import pandas as pd
from classes import *

VERBOSE = False


def readUsers(userCSV):
    # read csv with the users
    userDF = pd.read_csv(userCSV, encoding='utf-8')
    # create a dictionary of user-objects, e.g. John Johnsen <amazon.Use object>
    userDict = {u.FullName: User(
        u.FullName, u.Function, u.LastLogin, u.IsExternal, u.ManagerLevel, u.IsAccountManager,
        u.HasAvatar, u.HasPhonenumber, u.Summary, u.DateOfBirth, u.EmployeeSince, u.Organization
    ) for u in userDF.itertuples()}
    # Sandra Schuur was missing:
    userDict['Sandra Schuur'] = User('Sandra Schuur')
    # check if all users are there:
    if VERBOSE:
        print("\nUsers in dictionary:")
        for key, value in userDict.items():
            print(key, value)
    return userDict


def readBlogs(microblogs, polls, userDict):
    # read the csv with the microblogs
    blogsDF = pd.read_csv(microblogs, encoding='utf-8')
    # we use polls.csv to check whether a microblog is a 'post' or a 'poll'
    pollsDF = pd.read_csv(polls, encoding='utf-8')
    # making a 'list' of polls
    allPolls = set(pollsDF['Microblog'].tolist())

    # adding blogs to dictionary-objects
    blogsDict = {}
    for _, row in blogsDF.iterrows():
        Microblog = row['Microblog']
        if VERBOSE:
            print('\n', Microblog)

        # if the microblog DOES NOT EXIST in blogsdict, create a new object in the dictionary
        if Microblog not in blogsDict:

            # add blog to blogsDict
            if Microblog in allPolls:  # if the microblog exists in polls.csv it is a poll
                blogsDict[Microblog] = Poll(
                    Microblog, row['MicroblogLikes'], row['Created'], userDict[row['Door']])
            else:  # it is not a poll, but only a 'normal' Post
                blogsDict[Microblog] = Post(
                    Microblog, row['MicroblogLikes'], row['Created'], userDict[row['Door']])
            # now, also add reaction to userDict
            userDict[row['Door']].addPost(blogsDict[Microblog])

        # add reaction to blogsdict
        # only add if 'Reactie' and likes are not NULL
        if (not pd.isnull(row['Reactie'])) and (not pd.isnull(row['ReactieLikes'])):
            # add reaction to blogsdict
            currentReply = Reply(row['Reactie'], row['ReactieLikes'],
                                 row['ReactieDatum'], userDict[row['ReactieDoor']])
            blogsDict[Microblog].addReaction(currentReply)
            # now, also add reaction to userDict
            userDict[row['ReactieDoor']].addReply(currentReply)

        if VERBOSE:
            print(row['Reactie'])
    return blogsDict


def readcsv(usercsv='persons.csv', postcsv='microblogs.csv', pollcsv='polls.csv'):
    userDict = readUsers(usercsv)
    blogsDict = readBlogs(postcsv, pollcsv, userDict)

    # until now, we used the keys to prevent double entrances, from now on, we only need the .values()
    return set(userDict.values()), set(blogsDict.values())


if __name__ == "__main__":
    readcsv()
