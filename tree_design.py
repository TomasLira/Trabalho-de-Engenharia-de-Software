
from __future__ import annotations
from typing import List, Tuple, Any, Optional
from abc import abstractmethod, ABC

#--- eOBSe & eTODOe ---
    # Adding the inoput and output types specifications later 
    # Our tree will only work for numeric values!

#------------------------ COMPOSITE ------------------------#

class Node(ABC):
    @abstractmethod
    def predict(self,x):
        pass

    @property
    def children(self):
        return []

class LeafNode(Node):
    def __init__(self,labels_dict,leaf_name):
        self.labels_dict = labels_dict
        self.leaf_name = leaf_name

    def predict(self,x):
        print(f"[Composite] ({self.leaf_name}) At Leaf x={x} -> returning {self.labels_dict[x]}")
        return self.labels_dict[x]

class DecisionNode(Node):
    def __init__(self, threshold, left: Node,right: Node):
        self.threshold = threshold
        self.left = left
        self.right = right

    def predict(self,x):
        if x <= self.threshold:
            print("[Composite] LEFT")
            return self.left.predict(x)
        print("[Composite] RIGHT")
        return self.right.predict(x)
    
    @property
    def children(self):
        return [self.left, self.right]
    
#------------------------ STATE ------------------------#
class State(ABC):

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def run(self):
        pass
    
class SplittingState(State):
    def run(self):
        print("[State] SplittingState...")
        self.context.transition_to(StoppingState())

class StoppingState(State):
    def run(self):
        print("[State] StoppingState...")
        self.context.transition_to(PruningState())

class PruningState(State):
    def run(self):
        print("[State] PruningState...")


class TreeBuilder:

    def __init__(self, state: State):
        self.root = state
        self.transition_to(state)

    def transition_to(self, state: State):
        self._state = state
        self._state.context = self     

    def execute(self):
        return self._state.run()      

#------------------------ ITERATOR ------------------------#
class PreOrderIterator:
    def __init__(self, root: Node):
        self.stack = [root]
        print("[Iterator] Creating PreOrderIterator")

    def __iter__(self):
        print("[Iterator] __iter__ called")
        return self
    
    def __next__(self):
        if not self.stack:
            print("[Iterator] StopIteration")
            raise StopIteration

        node = self.stack.pop()
        print(f"[Iterator] Visiting: {node}")

        for child in reversed(node.children):
            self.stack.append(child)
        return node
    
#------------------------ VISITOR ------------------------#

class Visitor(ABC):
    
    def visit_leaf(self):
        pass

    def visit_decision(self):
        pass

class DepthVisitor(Visitor):
    pass

class CountLeavesVisitor(Visitor):
    pass



