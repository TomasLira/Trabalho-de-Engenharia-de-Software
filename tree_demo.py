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

class LeafNode(Node):
    def __init__(self,labels_dict,leaf_name):
        self.labels_dict = labels_dict
        self.leaf_name = leaf_name

    # predict acts as the execute()
    def predict(self,x):
        print(f"[{self.leaf_name}] At Leaf x={x} -> returning {self.labels_dict[x]}")
        return self.labels_dict[x]

class DecisionNode(Node):
    def __init__(self, threshold, left: Node,right: Node):
        self.threshold = threshold
        self.left = left
        self.right = right

    # x will be a number so no feat_idx
    def predict(self,x):
        if x <= self.threshold:
            print("LEFT")
            # predict(node, x) todos os atributos são salvos
            return self.left.predict(x)
        print("RIGHT")
        return self.right.predict(x)
    
#------------------------ STATE ------------------------#
class State(ABC):
    pass    
    
class SplittingState(State):
    pass

class StoppingState(State):
    pass

class PruningState(State):
    pass

class Context(ABC):
    pass

class TreeBuilder(Context):
    pass



