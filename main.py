from readdata import *
from createGraph import *

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
    users, blogs = readcsv(usercsv='persons.csv', postcsv='microblogs.csv', pollcsv='polls.csv')
    # now, create a graph
    createGraph(users, blogs)

if __name__ == "__main__":
    main()
