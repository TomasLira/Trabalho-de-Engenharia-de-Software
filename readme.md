```mermaid
classDiagram
    class Node {
        +predict(x)
        +children
    }
    class LeafNode {
        +predict(x)
        +labels_dict
        +leaf_name
    }
    class DecisionNode {
        +threshold
        +left
        +right
        +predict(x)
        +children
    }
    Node <|-- LeafNode
    Node <|-- DecisionNode
    DecisionNode o--> Node : compõe filhos

classDiagram
    class State {
        +context
        +run()
    }
    class SplittingState {
        +run()
    }
    class StoppingState {
        +run()
    }
    class PruningState {
        +run()
    }
    State <|-- SplittingState
    State <|-- StoppingState
    State <|-- PruningState

    class TreeBuilder {
        -_state
        +transition_to(state)
        +execute()
    }
    TreeBuilder --> State : mantém/avança
    State --> TreeBuilder : usa context

classDiagram
    class Node {
        +children
    }
    class PreOrderIterator {
        -stack
        +__iter__()
        +__next__()
    }
    PreOrderIterator --> Node : itera

classDiagram
    class Node {
        +accept(visitor)
    }
    class Visitor {
        +visit_leaf(leaf)
        +visit_decision(decision)
    }
    class DepthVisitor {
        -current_depth
        -max_depth
        +visit_leaf(leaf)
        +visit_decision(decision)
    }
    class CountLeavesVisitor {
        -count
        +visit_leaf(leaf)
        +visit_decision(decision)
    }
    Visitor <|-- DepthVisitor
    Visitor <|-- CountLeavesVisitor
    Node --> Visitor : accept(visitor)

```