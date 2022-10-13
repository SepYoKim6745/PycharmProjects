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
        if not self.isEmpty():
            return self.top.data

    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg='LinkedStack'):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

def checkBrackets(statement):
    stack = LinkedStack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if(ch == '}' and left != '{') or\
                  (ch == ']' and left != '[') or\
                  (ch == ')' and left != '('):
                    return False
        return stack.isEmpty()

if __name__ == '__main__':
    str = ("{ A[(i+1)] = 0;", "if( ( i == 0) && (j == 0)", "A[(i+1]) = 0;")
    for s in str:
        m = checkBrackets(s)
        print(s, '--->', m)
















    # odd = LinkedStack()
    # even = LinkedStack()
    # for i in range(10):
    #     if i % 2 == 0:
    #         even.push(i)
    #     else:
    #         odd.push(i)
    # even.display('LinkedStack_Even : ')
    # odd.display('LinkedStack_Odd : ')
    # print('스택 even peek :', even.peek())
    # print('스택 odd peek :', odd.peek())
    #
    # for _ in range(2): even.pop()
    # for _ in range(3): odd.pop()
    # even.display('LinkedStack_Even : ')
    # odd.display('LinkedStack_Odd : ')