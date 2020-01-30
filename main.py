from readdata import *
from createGraph import *
from classes import *
from network import Pathfinder
import random
'''
Order of the program:
Classes:
main.py
│
├─ readdata.py
│  │
│  └─ readscv()
│     ├─ readUsers() # from the csv and make objects of them
│     ├─ readBlogs() # from the csv and make objects of them
│     └─ return userDict and blogsDict, two dictionaries with their correponding objects
│
└─ creategraph.py # with the help of [User1, User2, ...] and [Post1, Post2, ...]
   └─ TODO
'''


def main():
    # first read the csv into objects
    # users, blogs = readcsv(usercsv='persons.csv',
    #                       postcsv='microblogs.csv', pollcsv='polls.csv')

    # now, create a graph
    # createGraph(users, blogs)

    import time

    userdict, blogdict = readcsv(
        usercsv='persons.csv', postcsv='microblogs.csv', pollcsv='polls.csv')

    # Add the connections for a*
    for blog in list(blogdict.values()):
        for replier in blog.getRepliers():
            if replier not in blog.getCreator().connections:
                blog.getCreator().connections.append(replier)
                if blog.getCreator() not in replier.connections:
                    replier.connections.append(blog.getCreator())

    interDict = {"Username": [],
                 "Interactivity": [],
                 "Avg.AssentWords": [],
                 "Avg.Tokens": [],
                 "Avg.FirstPersonPronouns": [],
                 "Avg.DefArticles": [],
                 "Posts": []}

    for user in userdict.values():
        score = user.calcInteractivity()
        interDict["Username"].append(user.FullName)
        interDict["Interactivity"].append(score)
        interDict["Avg.AssentWords"].append(user.avgAssentWords)
        interDict["Avg.Tokens"].append(user.avgTokens)
        interDict["Avg.FirstPersonPronouns"].append(user.avgFPPs)
        interDict["Avg.DefArticles"].append(user.avgdefs)
        interDict["Posts"].append(len(user.posts))

    import pandas

    data = pandas.DataFrame(interDict)
    data.to_csv("interactivity_results.csv")
    print("Successfully exported results.")

    pathfinder = Pathfinder()

    user_a = random.choice(list(userdict.keys()))
    user_b = random.choice(list(userdict.keys()))
    while user_b == user_a:
        user_b = random.choice(list(userdict.keys()))

    print(f"Finding path from {user_a} to {user_b}")
    path = pathfinder.find_path(
        userdict[user_a], userdict[user_b])

    createGraph(userdict.values(), path)

    path.pop()
    for user in path:
        print(user.FullName, end=" -> ")

    print(user_b)


if __name__ == "__main__":
    main()
