from tree_demo import LeafNode,DecisionNode

labels = {idx: (True if idx % 2 == 1 else False) for idx in range(1, 11)}

l1 = LeafNode(labels,"l1")
l2 = LeafNode(labels, 'l2')
r2 = LeafNode(labels, 'r2')

d1 = DecisionNode(8,l2,r2)
root = DecisionNode(5,l1,d1)

print(root.predict(2))
print('\n\n')
print(root.predict(9))
print('\n\n')
print(root.predict(6))