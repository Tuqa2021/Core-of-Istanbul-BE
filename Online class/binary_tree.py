class TreeNode:
    def __init__(self,value=0 ,left= None,right=None):
        self.value=value
        self.left=left
        self.right=right
def cal_branch_sum(node,current_sum,sums):
        if node is None:
            return
        current_sum += node.value
        if  node.left is None and node.right is None:
            sums.append(current_sum)
        else:
             cal_branch_sum(node.left,current_sum,sums)
             cal_branch_sum(node.right,current_sum,sums)
def branch_sums(root):
     sums=[]
     cal_branch_sum(root,0,sums)
     return sums

def findMax(node):
    if node is None:
        return 
    max_node = node
    if node.left:
        lres =findMax(node.left)
        max_node=max(max_node,lres,key=lambda x: x.value)
    if node.right:
        rres =findMax(node.right)
        max_node=max(max_node,rres,key=lambda x: x.value)
    return max_node

def findMin(node):
    if node is None:
        return 
    min_node = node
    if node.left:
        lres =findMin(node.left)
        min_node=min(min_node,lres,key=lambda x: x.value)
    if node.right:
        rres =findMin(node.right)
        min_node=min(min_node,rres,key=lambda x: x.value)
    return min_node

def ifNodeExists(node, key):
 
    if (node == None): 
        return False
 
    if (node.value == key): 
        return True
    res1 = ifNodeExists(node.left, key) 
    if res1:
        return True
    res2 = ifNodeExists(node.right, key) 
 
    return res2

def parent(node, val):
    if node:
        if (node.left and node.left.value==val) or (node.right and node.right.value==val):
            return node.value or parent(node.left, val) or parent(node.right, val)
        else:
            return parent(node.left, val) or parent(node.right, val)



root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
result=branch_sums(root)
print(result)
max_node=findMax(root)
print("Maximum Node:",max_node.value)
min_node=findMin(root)
print("Minimum Node:",min_node.value)
key=int(input())
if (ifNodeExists(root, key)): 
        print("YES" )
else:
        print("NO")
print(f"The parent of node 3 is {parent(root, 3)}.")
        