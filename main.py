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
└─ creategraph.py # with the help of userDict (and maybe blogsDict)
   └─ TODO
'''

def main():
    # first read the csv into objects
    userDict, blogsDict = readcsv(usercsv='persons.csv', postcsv='microblogs.csv', pollcsv='polls.csv')
    # now, create a graph
    # creategraph(userDict, blogsDict)

if __name__ == "__main__":
    main()
