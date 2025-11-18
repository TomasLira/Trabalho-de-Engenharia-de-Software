from __future__ import annotations
from typing import List, Tuple, Any, Optional
from abc import abstractmethod, ABC

#--- eOBSe & eTODOe ---
    # Adding the inoput and output types specifications later 
    # Our tree will only work for numeric values!

class Node(ABC):
    @abstractmethod
    def predict(self,x):
        pass

class LeafNode:
    def __init__(self,labels_dict):
        self.labels_dict

    def predict(self,x):
        return self.labels_dict[x]

    

class DecisionNode(Node):
    def __init__(self,feature_idx, threshold, left: Node,right: Node):
        self.feature_idx = feature_idx
        self.threshold = threshold
        self.left = left
        self.right = right

    def predict(self,x):
        if x <= self.threshold:
            # predict(node, x) todos os atributos são salvos
            return self.left.predict(x)
        return self.right.predict(x)
    
