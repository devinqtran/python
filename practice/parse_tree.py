import operator

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_parse_tree(expression_str):
    # Split tokens securely, ensuring spaces around parentheses and operators
    tokens = expression_str.replace('(', ' ( ').replace(')', ' ) ').split()
    
    root = TreeNode('')
    stack = []
    current_node = root
    
    for token in tokens:
        if token == '(':
            # Rule 1: Descend left for a new sub-expression
            current_node.left = TreeNode('')
            stack.append(current_node)
            current_node = current_node.left
            
        elif token in ['+', '-', '*', '/']:
            # Rule 2: Current node becomes the operator, then descend right
            current_node.value = token
            current_node.right = TreeNode('')
            stack.append(current_node)
            current_node = current_node.right
            
        elif token == ')':
            # Rule 3: Sub-expression complete, move up to parent
            if stack:
                current_node = stack.pop()
                
        else:
            # Rule 4: Token is a number (operand). Assign value and return to parent.
            current_node.value = int(token)
            if stack:
                current_node = stack.pop()
                
    return root

def evaluate(node):
    # Mapping operators to actual Python functions
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    
    # Base case: Leaf node (operand)
    if node.left is None and node.right is None:
        return node.value
    
    # Recursive case: Internal node (operator)
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    return ops[node.value](left_val, right_val)

# --- Example Usage ---
expr = "((10 + 5) * 3)"
tree_root = build_parse_tree(expr)

print(f"Expression: {expr}")
print(f"Evaluated Result: {evaluate(tree_root)}")  # Output: 45