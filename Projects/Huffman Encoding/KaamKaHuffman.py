def find_encoding(root, key):
    if root < len(chars):  # if the root node is a character
        encoding[chars[root]] = key  # set its encoding
        return  # return

    lkey = key + '0'  # key of left subtree will be the current key with 0 appended to it
    rkey = key + '1'  # similarly for right subtree
    find_encoding(nodes[root][0], lkey)  # find the encoding of the two subtrees
    find_encoding(nodes[root][1], rkey)


f = open("huffman_uncompressed.txt", "r")
raw = f.read()  # reading raw text
f.close()

chars = list(set(raw))  # list of all distinct characters in file
freq = {}  # frequency distribution

for i in range(len(chars)):
    freq[i] = raw.count(chars[i])  # assigning frequencies, with each letter mapped to its index in chars

nodes_freq = freq.copy()  # copy of frequencies we can edit
nodes = {}  # mapping of int to (left, right, total_freq)

free_node_ind = len(chars)  # an index with no node, so we can create a new node here
while len(nodes_freq) > 1:  # while we haven't compressed all the letters
    sorted_keys = sorted(nodes_freq.items(), key=lambda x: x[1])  # get the list of keys sorted by their values
    min1 = sorted_keys[0][0]  # the two keys with the minimum value
    min2 = sorted_keys[1][0]
    # create a node with these two minimum keys as its children, and value being the sum of frequencies of children
    nodes[free_node_ind] = (min2, min1, nodes_freq[min1] + nodes_freq[min2])
    del nodes_freq[min1]  # we have combined these two keys into one node, so we remove them from our dictionary
    del nodes_freq[min2]
    nodes_freq[free_node_ind] = nodes[free_node_ind][2]  # and we add the combined node
    free_node_ind += 1  # increment the next node index we can assign to

root = free_node_ind - 1  # root node is the last node assigned

encoding = {}  # mapping of char to its binary encoding
find_encoding(root, '')  # finding encoding of all characters
print(encoding)