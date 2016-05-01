# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.traverse_inOrder(0)
    return self.result

  def traverse_inOrder(self, i):
      if i == -1 or i >= self.n:
          return
      self.traverse_inOrder(self.left[i])
      self.result.append(self.key[i])
      self.traverse_inOrder(self.right[i])

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.traverse_preOrder(0)
    return self.result

  def traverse_preOrder(self, i):
      if i == -1 or i >= self.n:
          return
      self.result.append(self.key[i])
      self.traverse_preOrder(self.left[i])
      self.traverse_preOrder(self.right[i])

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.traverse_postOrder(0)
    return self.result

  def traverse_postOrder(self, i):
      if i == -1 or i >= self.n:
          return
      self.traverse_postOrder(self.left[i])
      self.traverse_postOrder(self.right[i])
      self.result.append(self.key[i])


def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
