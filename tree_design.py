
from __future__ import annotations
from typing import List, Tuple, Any, Optional
from abc import abstractmethod, ABC


#------------------------ COMPOSITE ------------------------#

class Node(ABC):
    @abstractmethod
    def predict(self,x):
        pass

    # required method for Visitor pattern implementation!
    @abstractmethod
    def accept(self,visitor: Visitor):
        pass

    @property
    def children(self):
        return []

class LeafNode(Node):
    """
    Leaf of the Composite tree that simulates classification and accepts Visitors
    """
    def __init__(self,labels_dict,leaf_name):
        self.labels_dict = labels_dict
        self.leaf_name = leaf_name

    def predict(self,x):
        print(f"[Composite] ({self.leaf_name}) At Leaf x={x} -> returning {self.labels_dict[x]}")
        return self.labels_dict[x]
    
    def accept(self,visitor):
        return visitor.visit_leaf(self)

class DecisionNode(Node):
    """
    Composite node that  decides using a threshold (decision) for traversal
    """
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
    
    def accept(self,visitor):
        return visitor.visit_decision(self)
    
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
    """
    Concrete State for the phase of splitting the tree and transitions to StoppingState
    """
    def run(self):
        print("[State] SplittingState...")
        self.context.transition_to(StoppingState())

class StoppingState(State):
    """
    Concrete State for the phase stopping criterion phase and transitions to PruningState
    """
    def run(self):
        print("[State] StoppingState...")
        self.context.transition_to(PruningState())

class PruningState(State):
    """
    Concrete State for  pruning  and it is final state of the process
    """
    def run(self):
        print("[State] PruningState...")


class TreeBuilder:
    """
    Context of the State pattern that maintains the current state and executes it
    """
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
    """
    Iterator that traverses a Composite tree in pre-order using stack
    """
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

    @abstractmethod
    def visit_leaf(self,leaf_node):
        pass

    @abstractmethod
    def visit_decision(self, decision_node):
        pass

class DepthVisitor(Visitor):
    """
    Concrete Visitor that calculates depth during tree traversal
    """
    def __init__(self):
        self.current_depth = 0
        self.max_depth = 0

    def visit_leaf(self, leaf_node: LeafNode):
        print(f"[Visitor-Depth] Visiting leaf {leaf_node.leaf_name} at depth {self.current_depth}")
        if self.current_depth > self.max_depth:
            self.max_depth = self.current_depth

    def visit_decision(self, decision_node: DecisionNode):
        print(f"[Visitor-Depth] Visiting decisiion node with threshold={decision_node.threshold} at depth {self.current_depth}")

class CountLeavesVisitor(Visitor):
    """
    Concrete Visitor that counts the number of LeafNodes during tree traversal
    """
    def __init__(self):
        self.count = 0

    def visit_leaf(self, leaf_node: LeafNode):
        self.count += 1
        print(f"[Visitor-CountLeaves] Counting leafs {leaf_node.leaf_name}. Total until now is: {self.count}")

    def visit_decision(self, decision_node: DecisionNode):
        print(f"[Visitor-CountLeaves] Visiting decision node threshold={decision_node.threshold}")