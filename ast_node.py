"""
"""


class ASTNode(object):
    """Abstract syntax tree node
    
    Attributes:
        type: the type of the node
        childs: the child nodes
    """

    def __init__(self, type, *child):
        """init the AST node
        
        Args:
            type: the type of the node
            childs: the child nodes
        """
        self.type = type
        self.childs = list(child)

    def __str__(self):
        """return the string representation of the AST"""
        if self != None:
            return str(self.type)
    
    def __repr__(self):
        """return the string representation of the AST"""
        if self.childs:
            return str(self.type) + "(" + ", ".join([repr(child) for child in self.childs]) + ")"
        else:
            return str(self.type)
    
    def print(self, indent=1, output_file=None):
        """print the AST
        
        Args:
            indent: the indent of the current node
        """
        out = " " * (indent - 1) * 4 + "└──" + " " + str(self)
        print(out)
        if output_file:
            output_file.write(out)
            output_file.write("\r")
        for child in self.childs:
            try:
                child.print(indent + 1, output_file)
            except AttributeError:
                print(" " * indent * 4 + "└──" + " " + str(child))