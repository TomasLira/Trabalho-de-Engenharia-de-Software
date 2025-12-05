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

```