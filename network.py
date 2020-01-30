from classes import *
import random
import time


class Pathfinder(object):
    def __init__(self):
        pass

    def find_path(self, user_a: User, user_b: User):

        self.target: User = user_b
        self.start: User = user_a

        open_set = [user_a]
        closed_set = []

        while len(open_set) != 0:
            # Find the user with the lowest fscore in open set
            current: User = min(open_set, key=lambda x: x.fscore)
            open_set.remove(current)
            closed_set.append(current)

            if current == self.target:
                print("Path found!")
                return self._construct_path(current)

            for neighbour in current.connections:
                if neighbour in closed_set:
                    continue

                tentative_gscore = current.gscore + \
                    1 / (current.interactivity + neighbour.interactivity)
                if neighbour not in open_set or tentative_gscore < neighbour.gscore:

                    neighbour.hscore = 1 / \
                        (self.target.interactivity + neighbour.interactivity)
                    neighbour.fscore = neighbour.gscore + neighbour.hscore

                    neighbour.parent = current
                    if neighbour not in open_set:
                        open_set.append(neighbour)

        print("Cannot find path.")
        return None

    def _construct_path(self, current):

        waypoints = []

        while True:
            if current == self.start:
                waypoints.append(self.start.FullName)
                break

            waypoints.append(current.FullName)
            current = current.parent

        waypoints.reverse()
        return waypoints
