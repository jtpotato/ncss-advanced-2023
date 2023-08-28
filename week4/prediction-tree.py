# Implement the following Node class API.
# If you delete something important, this code is copied in specification.py

class Node:
  def __init__(self, prefix, is_word=False):
    """
    Creates a Node with the given string prefix.
    The root node will be given prefix ''.
    You will need to track:
    - the prefix
    - whether this prefix is also a complete word
    - child nodes
    """

    self.prefix = prefix
    self.children = {}
    self.is_word_state = is_word
    pass
  
  def get_prefix(self):
    """
    Returns the string prefix for this node.
    """
    return self.prefix
  
  def get_children(self):
    """
    Returns a list of child Node objects, in any order.
    """
    return list(self.children.values())
  
  def is_word(self):
    """
    Returns True if this node prefix is also a complete word.
    """
    return self.is_word_state
  
  def add_word(self, word):
    """
    Adds the complete word into the trie, causing child nodes to be created as needed.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> root.add_word('cheese')
    """
    def add_word_helper(node, word):
      if word == '':
        node.is_word_state = True
        return
      if word[0] not in node.children:
        node.children[word[0]] = Node(node.prefix + word[0])
      add_word_helper(node.children[word[0]], word[1:])
  
    add_word_helper(self, word)
  
  def find(self, prefix):
    """
    Returns the node that matches the given prefix, or None if not found.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> node = root.find('te')
    """
    # needs to look in subchildren too
    def find_helper(node, prefix):
      if prefix == '':
        return node
      if prefix[0] not in node.children:
        return None
      return find_helper(node.children[prefix[0]], prefix[1:])
    
    return find_helper(self, prefix)
  
  def words(self):
    """
    Returns a list of complete words that start with my prefix.
    The list should be in lexicographical order.
    """
    def words_helper(node):
      result = []
      if node.is_word_state:
        result.append(node.prefix)
      for child in node.children.values():
        result += words_helper(child)
      return result
    
    words = words_helper(self)
    words.sort()
    return words


if __name__ == '__main__':
  # Write your test code here. This code will not be run by the marker.

  # The first example in the question.
  root = Node('')
  for word in ['tea', 'ted', 'ten']:
    root.add_word(word)
  node = root.find('te')
  print(node.get_prefix())
  print(node.is_word())
  print(node.words())

  # The second example in the question.
  root = Node('')
  for word in ['inn', 'in', 'into', 'idle']:
    root.add_word(word)
  node = root.find('in')
  print(node.get_prefix())
  children = node.get_children()
  print(sorted([n.get_prefix() for n in children]))
  print(node.is_word())
  print(node.words())

  # The third example in the question.
  with open('the-man-from-snowy-river.txt') as f:
    words = f.read().split()
  root = Node('')
  for word in words:
    root.add_word(word)
  print(root.find('th').words())

  root = Node('')
  for word in ['dog', 'dog-house', 'dogged']:
    root.add_word(word)
  node = root.find('dog')
  print(node.get_prefix())
  child_nodes = node.get_children()
  print(sorted([n.get_prefix() for n in child_nodes]))
  leaf_node = root.find('dog-house')
  leaf_children = None if leaf_node is None else leaf_node.get_children()
  print(leaf_children == [])

  root = Node('')
  for word in ['teapot', 'teacup']:
    root.add_word(word)
  node = root.find('tea')
  print(node.is_word())
  print(node.words())
  root.add_word('tea')
  node = root.find('tea')
  print(node.is_word())
  print(node.words())
  for word in ['cup', 'pot', 'water']:
    root.add_word(word)
  print(root.words())
  node = root.find('tea')
  print(node.words())