from tree_design import LeafNode,DecisionNode,PreOrderIterator,CountLeavesVisitor,DepthVisitor, SplittingState,PruningState, TreeBuilder

print("\n------------------[COMPOSITE]------------------")
labels = {idx: (True if idx % 2 == 1 else False) for idx in range(1, 11)}

l1 = LeafNode(labels,"l1")
l2 = LeafNode(labels, 'l2')
r2 = LeafNode(labels, 'r2')

d1 = DecisionNode(8,l2,r2)
root = DecisionNode(5,l1,d1)

print('\n')
print("                root : DecisionNode(threshold=5)")
print("               /                                \\")
print("      l1 : LeafNode('l1')            d1 : DecisionNode(threshold=8)")
print("                                         /                         \\")
print("                           l2 : LeafNode('l2')             r2 : LeafNode('r2')")

print("\n\n")
print('PREDICTING VALUE:',2)
print(root.predict(2))
print('\n')

print('PREDICTING VALUE:',9)
print(root.predict(9))
print('\n')

print('PREDICTING VALUE:',6)
print(root.predict(6))
print('\n')

print("\n------------------[ITERATOR]------------------")
it = PreOrderIterator(root)
for node in it:
    if isinstance(node, LeafNode):
        print(f"Found LeafNode: {node.leaf_name}")
    elif isinstance(node, DecisionNode):
        print(f"Found DecisionNode with threshold={node.threshold}")

print("\n------------------[STATE]------------------")

# Using the same tree as above
initial_state = SplittingState()
builder = TreeBuilder(initial_state)
print('\n')
print("Phase 1: Splitting (tree expansion)...")
builder.execute()
print('\n')
print("Phase 2: Stopping (stop growing the tree)...")
builder.execute() 
print('\n')
print("Phase 3: Pruning (simplifying the tree)...")
builder.execute()
print('\n')
print("State cycles finished")


print("\n------------------[VISITOR]------------------")

count_visitor = CountLeavesVisitor()

print("Applying CountLeavesVisitor using PreOrderIterator...")

for node in PreOrderIterator(root):
    node.accept(count_visitor)

print('\n')
print(f"Total number of leaves = {count_visitor.count}")

print('\n')

depth_visitor = DepthVisitor()
print("Applying DepthVisitor using PreOrderIterator...")
print('\n')

for node in PreOrderIterator(root):
    node.accept(depth_visitor)

