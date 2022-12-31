import ast
# creating class for syntax tree
class SyntaxTree():
    def __init__(self,expression):
        self.expression = expression

    # creating syntax tree  
    def generate_syntax_tree(self):
        tree = ast.parse(self.expression)
        return tree

    # displaying table output
    def Table(self,node):  
        print(f"{node.__class__.__name__}: {ast.dump(node,indent = 3)}")

if __name__ == "__main__":
    expression = "2 + 3 * 4"
    obj = SyntaxTree(expression)
    tree = obj.generate_syntax_tree()
    obj.Table(tree)