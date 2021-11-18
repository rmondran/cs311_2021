import random
import string

NODE_COUNT_PER_LAYER = [4,3,2]

class Node:
  def __init__(self):
    self.children = [] #connects to children nodes
    self.weight = [] #gives weight to each connection to children nodes

    self.node_name = ''.join([random.choice(string.ascii_letters) for i in range(3)])

  def make_children(self,current_layer_number,node_per_layer_map):
    #when to end recursion
    if current_layer_number >= len(node_per_layer_map):
      return

    for i in range(node_per_layer_map[current_layer_number]):
      self.children.append(Node())

    #self.children are all children node for this level
    self.children[0].make_children(current_layer_number+1,node_per_layer_map)

    #copy all children nodes from [0] to all the other children nodes
    for i in range(0,len(self.children)):
      self.children[i].children = self.children[0].children[:]

  def output_children(self,current_layer_number,node_per_layer_map):
    indent = '    ' * current_layer_number 

    #when to stop Recursion
    if current_layer_number >= len(node_per_layer_map):
      print(f"{indent} {self.node_name}")
      return

    print(f"{indent} {self.node_name} is connected to:")
    for i in range(len(self.children)):
        try:
          print(f"{indent} Weight of {self.weight[i]}")
        except:
          pass

        self.children[i].output_children(current_layer_number+1,node_per_layer_map)

    return

  def adjust_children_weights(self,current_layer_number,node_per_layer_map):
    #when to stop recursion
    if current_layer_number >= len(node_per_layer_map):
      return
    self.weight = [0.0] * len(self.children)
    for i in range(len(self.children)):
      self.weight[i] = random.uniform(0,1)
      self.children[i].adjust_children_weights(current_layer_number+1,node_per_layer_map)

    return 

new_node = Node()
new_node.make_children(0,NODE_COUNT_PER_LAYER)
new_node.output_children(0,NODE_COUNT_PER_LAYER)
print("\nAFTER ADJUSTING CHILDREN WEIGHTS:\n")
new_node.adjust_children_weights(0,NODE_COUNT_PER_LAYER)
new_node.output_children(0,NODE_COUNT_PER_LAYER)
