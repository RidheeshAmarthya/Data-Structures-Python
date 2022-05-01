class Node:
    data = 0
    link = None

    def __init__(self, data):
        self.data = data

class Linklist:

    def __init__(self, data):
        self.Flink = Node(data)
        self.root_node = self.Flink

    def addLink(self, data):
        newlink = Node(data)
        self.Flink.link = newlink
        self.Flink = newlink

    def printList(self):
        templist = self.root_node
        while templist.link != None:
            print(templist.data)
            templist = templist.link
        print(templist.data)

    # probably does not get rid of data from memory...
    def deleteList(self):
        templist = self.root_node
        while templist.link.link != None:
            templist = templist.link
        self.Flink = templist
        self.Flink.link = None

    def deleteElement(self, data):
        templist = self.root_node
        while templist.link.data != data:

            if templist.link.link == None:
                print("DATA not in LinkList")
                return None

            templist = templist.link

        templist.link = templist.link.link

x = Linklist(101)
x.addLink(120)
x.addLink(1289)
x.addLink(180)
x.addLink(1200)

x.deleteList()
x.deleteElement(180)

x.printList()