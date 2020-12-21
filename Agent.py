
from typing import Any, List, Tuple, Dict, Set

import networkx as nx
from networkx.algorithms import tree
import AgentBase
from AgentBase import Message, MatchingSolution, AgentID
import Settings


def find_path_to_first(agent_idx, center_idx, connectivity_graph: nx.Graph):
    return nx.shortest_path(connectivity_graph, source=agent_idx, target=center_idx)

class Data:
    def __init__(self, subgraph_to_pass: nx.Graph, path: List[int], is_solution: bool, id, involved: List[int]):
        self.subgraph_to_pass = subgraph_to_pass
        self.path = path
        self.is_solution = is_solution
        self.id = id
        self.involved = involved

def find_optimal_matching(matching_graph: nx.Graph):
    return nx.algorithms.matching.max_weight_matching(matching_graph)
def new_compose(graph1, graph2):
    new_graph = graph1.copy()
    for u, v, data in graph2.edges(data=True):
        if data['weight'] > 0:
            new_graph[u][v]['weight'] = data['weight']
    return new_graph
# Definition: Let G be a graph on finitely many vertices v_1,...,v_n. Let x_1,...,x_n be a maximal path in the graph.
# Then, x_(floor(n/2)) is (one of) the graph's center(s).
# This function returns one of a graph's centers.
# Hmm, would I prefer a different definition of a center? Perhaps one that by definition minimizes the message expenditure?
def measure_center(graph):
    longest_distance = 0
    current_path = []
    for i in range(0, Settings.NUM_AGENTS):
        for j in range(0, Settings.NUM_AGENTS):
            path = nx.shortest_path(graph, source=i, target=j)
            if len(path) > longest_distance:
                longest_distance = len(path)
                current_path = path
    return current_path[longest_distance//2 - 1]

def measure_distance_sum(graph, node):
    current_sum = 0
    list_going_through = []
    for i in range(0, Settings.NUM_AGENTS):
        if i == node:
            continue
        path = nx.shortest_path(graph, source=node, target=i)
        if len(path) < 2:
            continue
        del path[0]
        del path[len(path) - 1]
        list_going_through.extend(path)
    for i in range(0, Settings.NUM_AGENTS):
        if i in list_going_through:
            continue
        current_sum += len(nx.shortest_path(graph, source=node, target = i))
    return current_sum
def measure_center_for_minimizing_expenditure(graph):
    current_minimizer = 0
    current_minimum = 999 # /shrug
    for node in graph.nodes():
        if measure_distance_sum(graph, node) < current_minimum:
            current_minimum = measure_distance_sum(graph, node)
            current_minimizer = node
    return current_minimizer

def calculate_paths(graph, center):
    paths = []
    for node in graph.nodes():
        if node == center:
            continue
        paths.append(nx.shortest_path(graph, source=node, target=center)) 
    paths.sort(key=len)
    return list(reversed(paths))

PORTION_SKIP_GETTING = 24 / 29 
PORTION_SKIP_SENDING = 0 / 29
def get_skip(graph, center, param):
    paths = calculate_paths(graph, center)
    number_to_skip = len(paths) * param
    to_skip = []
    if number_to_skip <= 0:
        return set()
    for i in range(int(number_to_skip)):
        to_skip.append(paths[i][0])
    return set(to_skip)

class SolutionPacket:
    def __init__(self, solution: MatchingSolution, source, pings):
        self.solution = solution
        self.source = source
        self.pings = pings

DEBUG = False
ROUNDS_DEBUG = True
class Agent:
    def __init__(self,
                 agent_idx: int,
                 matching_subgraph: nx.Graph,
                 connectivity_graph: nx.Graph):
        self._agent_idx = agent_idx
        self._matching_subgraph = matching_subgraph
        self._connectivity_graph = connectivity_graph
        self.index_center = measure_center_for_minimizing_expenditure(connectivity_graph) # measure_center(connectivity_graph) # 
        self.spanning_connections_graph = nx.algorithms.tree.mst.minimum_spanning_tree(connectivity_graph, algorithm='prim')
        self.to_skip = get_skip(connectivity_graph, self.index_center, PORTION_SKIP_GETTING)
        self.to_skip_sending = get_skip(self.spanning_connections_graph, self.index_center, PORTION_SKIP_SENDING)
        if self._agent_idx == 0 and DEBUG:
            print("Skipped recieving: " + str(self.to_skip))
            print("Skipped sending: " + str(self.to_skip_sending))
            print("Center at: " + str(self.index_center) + ". Center of graph  for min. messages at " + str(measure_center_for_minimizing_expenditure(connectivity_graph)))
        if agent_idx == self.index_center:
            self.path_to_first = None
        else:
            self.path_to_first = find_path_to_first(agent_idx, self.index_center,   connectivity_graph)
        self.solution = None
        self.passed_graph = False
        self.passed = set([agent_idx])
        self.count = 0
        self.is_done_override = False
        if DEBUG or ROUNDS_DEBUG:
            self.rounds = 0
        

    @property
    def agent_idx(self) -> AgentID:
        return self._agent_idx

    def __eq__(self, other):
        return isinstance(other, Agent) and self.agent_idx == other.agent_idx

    def _count_weighted_edges(self, graph):
        count = 0

        for edge in graph.edges(data=True):
            count += (edge[2]['weight'] > 0)

        return count


    
    def step(self, message_budget, messages: List[Message]) -> Dict[AgentID, Message]:
        ret = {}
        #if Settings.EASY_DIFFICULTY - message_budget > 33:
        #    self.is_done_override = True
        if DEBUG or ROUNDS_DEBUG:
            self.rounds += 1
            if self.rounds >= 100:
                print("Over 100 rounds!!!")
            elif self.rounds == 1:
                pass
        if DEBUG:
            print("ID: " + str(self._agent_idx) + " messages length: " + str(len(messages)) + " passed: " + str(self.passed_graph) + " and solved: " + str(self.is_done()))
    
        if self._agent_idx == self.index_center:
            if DEBUG:
                print("Passed: " + str(len(self.passed)))
            for message in messages:
                self._matching_subgraph = new_compose(message.data.subgraph_to_pass, self._matching_subgraph)
                self.passed = self.passed.union(message.data.involved)
            if len(self.passed) == Settings.NUM_AGENTS - len(self.to_skip) and not self.passed_graph:
                self.passed_graph = True
                self.solution = find_optimal_matching(self._matching_subgraph)
                for i in range(0, Settings.NUM_AGENTS):
                    if i == self._agent_idx or not self.spanning_connections_graph.has_edge(self._agent_idx, i):
                        continue
                    if DEBUG:
                        print("Sending from " + str(self._agent_idx) + " to " + str(i))
                    ret[i] = Message(SolutionPacket(self.solution, self._agent_idx, 1))
                
            return ret
        elif not self.passed_graph:
            self.passed_graph = True
            list_going_through = []
            for i in range(0, Settings.NUM_AGENTS):
                if i == self._agent_idx or i in self.to_skip:
                    continue
                path = nx.shortest_path(self._connectivity_graph, source=self.index_center, target=i)
                if len(path) < 2:
                    continue
                del path[0]
                del path[len(path) - 1]
                list_going_through.extend(path)
            del self.path_to_first[0]
            if not (self.agent_idx in list_going_through) and not (self.agent_idx in self.to_skip):
                ret[self.path_to_first[0]] = Message(Data(self._matching_subgraph, self.path_to_first, False, str(self._agent_idx) + "_" + str(self.count), set([self._agent_idx])))
                self.count = self.count + 1
                if DEBUG:
                    print("Sending from " + str(self._agent_idx) + " to " + str(self.index_center) + " by " + str(self.path_to_first) + " with the first being " + str(self.path_to_first[0]))
        for message in messages:
            if isinstance(message.data, SolutionPacket):
                self.solution = message.data.solution
                for i in range(Settings.NUM_AGENTS):
                    if i == message.data.source or i == self._agent_idx or not self.spanning_connections_graph.has_edge(self._agent_idx, i) or i in self.to_skip_sending:
                        continue
                    ret[i] = Message(SolutionPacket(message.data.solution, self._agent_idx, message.data.pings + 1))
                    if DEBUG:
                        print("Sending from " + str(self._agent_idx) + " to " + str(i))
            else:
                path = message.data.path
                del path[0]
                if DEBUG:
                    print("Path: " + str(path) + " first: " + str(path[0]))
                if not (path[0] in ret):
                    self._matching_subgraph = new_compose(message.data.subgraph_to_pass, self._matching_subgraph)
                    ret[path[0]] = Message(Data(new_compose(message.data.subgraph_to_pass, self._matching_subgraph),
                     path, message.data.is_solution,
                      str(self._agent_idx) + "_" + str(self.count), message.data.involved.union([self._agent_idx])))
                else:
                    self._matching_subgraph = new_compose(self._matching_subgraph, new_compose(ret[path[0]].data.subgraph_to_pass, message.data.subgraph_to_pass))
                    obj = Message(Data(new_compose(self._matching_subgraph, new_compose(ret[path[0]].data.subgraph_to_pass, message.data.subgraph_to_pass)),
                    path, message.data.is_solution,
                    str(self._agent_idx) + "_" + str(self.count),
                        ret[path[0]].data.involved.union(message.data.involved)))
                    ret[path[0]] = obj
                self.count = self.count + 1
        return ret

    def is_done(self) -> bool:
        return self.solution != None or self._agent_idx in self.to_skip_sending or self.is_done_override

    def get_solution(self) -> MatchingSolution:
        if self.solution == None:
            return find_optimal_matching(self._matching_subgraph)
        return self.solution

