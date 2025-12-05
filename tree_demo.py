from tree_design import LeafNode,DecisionNode

print("------------------[COMPOSITE MOCK]------------------")
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