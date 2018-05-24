from Tkinter import *

def fileparse(filename):

    fd = open(filename)

    root = Node()
    line = fd.readline().strip('\r\n')  # Remove newline characters \r\n

    while line != '':
        root.add_item(line) #build the trie tree
        line = fd.readline().strip('\r\n')

    return root

class Node:

    def __init__(self):
        self.next = {}
        self.boolean = False

    #This method to add a string the Trie data structure
    def add_item(self, string):

        if len(string) == 0:
            self.boolean = True
            return

        key = string[0]  # get first character from string

        string = string[1:]  # Create a string by removing first character

        # If the key character exists in the hash, call next pointing node's add_item() with
        # remaining string (re)

        if self.next.has_key(key):
            self.next[key].add_item(string)

        # Else create an empty node. Insert the key character to hash and point it to newly created node.
        # Call add_item() in new node with remaining string.
        else:
            node = Node()
            self.next[key] = node
            node.add_item(string)

    #Depth First Search Traversal
    def dfs(self,e1, sofar):


        if self.next.keys() == [] and self.boolean == True:
            print "Match:", sofar
            res = sofar +"\n"
            e1.insert(END, res)
            return

        # elif self.boolean == True:
        #     print "Match:", sofar
        #     res = sofar + "\n"
        #     e1.insert(END, res)

        # Recursively call dfs for all the nodes pointed by keys in the hash

        for key in self.next.keys():
            temp = sofar + key
            self.next[key].dfs(e1,temp)

    def search(self,e2, string, sofar=""):
        '''Perform auto completion search and print the autocomplete results'''
        # When the input characters becomes exhaused, perform dfs() so that the trie gets traversed upto leaves and print the state characters

        if len(string) > 0:
            key = string[0]
            string = string[1:]
            if self.next.has_key(key):
                sofar = sofar + key
                self.next[key].search(e2,string, sofar)

            else:
                print "No match"
                e2.insert(END, "No match")
        else:
            if self.boolean == True:
                print "Match:", sofar
                res = sofar + "\n"
                e2.insert(END, res)

            for key in self.next.keys():
              temp = sofar + key
              self.next[key].dfs(e2,temp)
#end class!!!
