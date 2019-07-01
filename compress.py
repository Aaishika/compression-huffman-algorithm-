import sys
class Letter:
    def __init__(self, letter, freq):
        self.letter = letter
        self.freq = freq
        self.bitstring = ""
    def __repr__(self):
        return f'{self.letter}:{self.freq}'
class TreeNode:
    def __init__(self, freq, left, right):
        self.freq = freq
        self.left = left
        self.right = right
def parse_file(file_path):
    chars = {}
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars.keys() else 1
    return sorted([Letter(c, f) for c, f in chars.items()], key=lambda l: l.freq)
def build_tree(letters):
    while len(letters) > 1:
        left = letters.pop(0)
        right = letters.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        letters.append(node)
        letters.sort(key=lambda l: l.freq)
    return letters[0]
def traverse_tree(root, bitstring):
    if type(root) is Letter:
        root.bitstring = bitstring
        return [root]
    letters = []
    letters += traverse_tree(root.left, bitstring + "0")
    letters += traverse_tree(root.right, bitstring + "1")
    return letters
def huffman(file_path):
    letters_list = parse_file(file_path)
    root = build_tree(letters_list)
    letters = traverse_tree(root, "")
    print(f'Huffman Coding of {file_path}: ')
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            le = list(filter(lambda l: l.letter == c, letters))[0]
            print(le.bitstring, end=" ")
    print()
if __name__ == "__main__":
    huffman(sys.argv[1])
