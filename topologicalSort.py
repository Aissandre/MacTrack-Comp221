from collections import deque
# implementing a BFS topological sort (Kahn's Algo)

class TopologicalSort:

    # Method returns a list of nodes
    def sort(self, graph):
        queue = deque()
        output = []

        # Add nodes with no edges going into them to the queue
        # while queue is empty
            # node u = q.pop
            # output.add(u)
            # for each neighbor of node u
                # delete edge u -> v
                # if v has no incoming edge
                    # add v to queue

        return output
