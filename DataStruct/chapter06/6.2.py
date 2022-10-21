class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def clear(self):
        self.top = None

    def push(self, item):
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):
        if self.isEmpty():
            return self.top.data

    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedStack: "):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()


def checkBrackets(lines):
    stack = LinkedStack()
    for line in lines:
        for ch in line:
            if ch in ('{', '[', '('):
                stack.push(ch)
            elif ch in ('}', ']', ')'):
                if stack.isEmpty():
                    return False
                else:
                    left = stack.pop()
                    if (ch == '}' and left != '{') or (ch == ']' and left != '[') or (ch == ')' and left != '('):
                        return False
    return stack.isEmpty()

filename = "LinkedStack.h"
infile = open(filename, 'r')
lines = infile.readlines()
infile.close

result = checkBrackets(lines)
print(filename, ' ---> ', result)

