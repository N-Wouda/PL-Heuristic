from copy import deepcopy

from heuristic.classes import Problem
from heuristic.functions import learners_to_remove


def random_learners(current, rnd_state):
    destroyed = deepcopy(current)
    problem = Problem()

    while len(destroyed.unassigned) < learners_to_remove():
        pass

    return destroyed
