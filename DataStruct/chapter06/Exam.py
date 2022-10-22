#6.3 성공
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg='LinkedStack :'):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end='')
            node = node.link
        print()

    def getNode(self, pos):
        if pos < 0: return None
        node = self.head;
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None: node.data = elem

    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link


class Term:
    def __init__(self, expo, coef):
        self.expo = expo
        self.coef = coef


class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()

    def degree(self):
        if self.head == None:
            return 0
        else:
            return self.head.data.expo

    def display(self, msg=""):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data.coef, end='')
            if node.link != None: print("x^", end='')
            print(node.data.expo, end='')
            if node.link != None: print("+ ", end='')
            node = node.link
        print()

    def read(self):
        self.clear()
        token = input("입력(계수 지수 계수 지수 ...[enter]) : ").split(" ")
        for i in range(len(token) // 2):
            self.insert(self.size(), Term(int(token[i * 2 + 1]), float(token[i * 2])))

    def add(self, b):
        r = SparsePoly()
        node = self.head
        node1 = b.head
        i = 0
        while node != None and node1 != None:
            if (node.data.expo == node1.data.expo):  # 지수가 같으면 계수를 더해서 넣어줌
                r.insert(i, Term(node.data.expo, (node.data.coef + node1.data.coef)))
                node = node.link  # 다음 노드로 넘겨줌
                node1 = node1.link
            elif (node.data.expo > node1.data.expo):  # 지수가 더 크면 그 node의 지수와 계수를 넣어줌
                r.insert(i, Term(node.data.expo, node.data.coef))
                node = node.link  # 그 node만 다음 노드로 넘겨줌
            elif (node.data.expo < node1.data.expo):
                r.insert(i, Term(node1.data.expo, node1.data.coef))
                node1 = node1.link
            i += 1  # r의 다음 연결 자리로 넘겨줌
        if (node != None and node1 == None):  # 만약 data가 아직 남아있으면
            r.insert(i, Term(node.data.expo, node.data.coef))  # 다음 node에 넣어줌
            node = node.link
        elif (node == None and node1 != None):
            r.insert(i, Term(node1.data.expo, node1.data.coef))
            node1 = node1.link
        i += 1

        return r  # r반환

    def neg(self):
        tmp = SparsePoly()
        node = self.head
        while not node == None:
            for i in range(self.size()):
                tmp.insert(i, Term(node.data.expo, -node.data.coef))  # node의 계수를 - 해서 넣어줌
                node = node.link

        return tmp

    def sub(self, b):
        return self.add(b.neg())  # neg한 것를 add에 넣어주면 sub가 된다.

    def mult(self, b):
        m = SparsePoly()
        k = SparsePoly()
        node = self.head
        node1 = b.head
        f = 0  # 두번째 항까지 곱했을 때부터 더하기를 진행하기 위함.
        i = 0
        while node1 != None:
            while node != None:  # node에 node1의 각 항을 차례로 곱해준다.
                if (f == 0):  # node1의 첫번째 항과 곱한 것은 m에 넣어준다.
                    m.insert(i, Term(node.data.expo + node1.data.expo, (node.data.coef * node1.data.coef)))
                elif (f > 0):  # 나머지 항과 곱한 것은 k에 넣어준다.
                    k.insert(i, Term(node.data.expo + node1.data.expo, (node.data.coef * node1.data.coef)))
                node = node.link  # 곱하기를 했으면 node다음 항으로 넘겨준다.
                i += 1  # m과 k에 넣어줄 때도 다음 자리로 넘겨서 넣어준다.
            if (f > 0):  # 2번째 항과 곱하기를 진행한 다음부터는
                m = m.add(k)  # m(첫번째 항과 곱한 것)에 k(두번째 항과 곱한 것)을 더해서 m에 다시 넣어준다.
                k.clear()  # k는 초기화를 해서 다음 항(세번째, 네번째 ..)과 곱한 것을 넣어줄 수 있게 한다.
            node1 = node1.link
            node = self.head  # node1이 다음 항으로 넘어갈 때마다 node에 다시 처음부터 넣어서 while문이 돌아가도록 한다.
            f += 1
            i = 0  # node1이 다음 항으로 넘어갈 때마다 i도 초기화를 해준다.

        return m


a = SparsePoly()
b = SparsePoly()
a.read()
b.read()
a.display("A = ")
b.display("B = ")
c = a.add(b)
c.display("A+B = ")
d = a.sub(b)
d.display("A-B = ")
e = a.mult(b)
e.display("A*B = ")
