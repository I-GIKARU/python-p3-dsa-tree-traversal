class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def _search(node):
            if node is None:
                return None
            # Check current node
            if node.get('id') == id:
                return node
            # Search children recursively
            for child in node.get('children', []):
                result = _search(child)
                if result is not None:
                    return result
            return None

        return _search(self.root)
