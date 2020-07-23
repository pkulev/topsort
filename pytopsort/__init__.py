"""Topological sort implementation."""

from collections import deque
from typing import Any, Callable, Iterable


def topsort(nodes: Iterable, deptest: Callable[[Any, Any], bool]) -> deque:
    """Topological sorting routine based on depth-first search.

    Applicable only for directed acyclic graphs. Error will be raised if graph
    has cycles.

    :param nodes: collection of graph nodes to sort
    :param deptest: callable to determine if there are any dependencies
    """

    result: deque = deque()

    # pylint: disable=too-few-public-methods
    class Node:
        """Internal node wrapper for convinient node marking."""

        def __init__(self, data):
            self.data = data

            self.inprogress = False
            self.done = False

        def visit(self):
            """Recursively visit node and sort it's dependencies."""

            if self.done:
                return

            if self.inprogress:
                raise ValueError("Dependency graph has a cycle")

            self.inprogress = True

            for dep in filter(lambda it: deptest(self.data, it.data), nodes):
                dep.visit()

            self.inprogress = False
            self.done = True
            result.appendleft(self.data)

    nodes = list(map(Node, nodes))

    for node in nodes:
        node.visit()

    return result
