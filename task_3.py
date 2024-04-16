def create_file_system(file_system):
    tree = {}
    for path in sorted(file_system):
        parts = path.split('/')
        node = tree
        for part in parts:
            node = node.setdefault(part, {})

    def print_tree(node, prefix=""):
        for name, children in sorted(node.items()):
            print(prefix + name)
            print_tree(children, prefix + "  ")

    print_tree(tree)


n = int(input())
file_system = [input() for _ in range(n)]
create_file_system(file_system)
