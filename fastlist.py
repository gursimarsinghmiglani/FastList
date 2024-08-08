class AVLTree:
    def __init__(self, initval=None):
        self.value = initval
        if self.value:
            self.left = AVLTree()
            self.right = AVLTree()
            self.height = 1
            self.size = 1
        else:
            self.left = None
            self.right = None
            self.height = 0
            self.size = 0

    def isempty(self):
        return self.value is None

    def leftrotate(self):
        v = self.value
        vr = self.right.value
        tl = self.left
        trl = self.right.left
        trr = self.right.right
        newleft = AVLTree(v)
        newleft.left = tl
        newleft.right = trl
        self.value = vr
        self.right = trr
        self.left = newleft
        newleft.height = 1 + max(newleft.left.height, newleft.right.height)
        newleft.size = 1 + newleft.left.size + newleft.right.size
        self.height = 1 + max(self.left.height, self.right.height)
        self.size = 1 + self.left.size + self.right.size
        return

    def rightrotate(self):
        v = self.value
        vl = self.left.value
        tll = self.left.left
        tlr = self.left.right
        tr = self.right
        newright = AVLTree(v)
        newright.left = tlr
        newright.right = tr
        self.right = newright
        self.value = vl
        self.left = tll
        newright.height = 1 + max(newright.left.height, newright.right.height)
        newright.size = 1 + newright.left.size + newright.right.size
        self.height = 1 + max(self.left.height, self.right.height)
        self.size = 1 + self.left.size + self.right.size
        return

    def rebalance(self):
        hl = self.left.height if self.left else 0
        hr = self.right.height if self.right else 0
        if hl - hr > 1:
            if self.left.left.height >= self.left.right.height:
                self.rightrotate()
            else:
                self.left.leftrotate()
                self.rightrotate()
        if hl - hr < -1:
            if self.right.left.height <= self.right.right.height:
                self.leftrotate()
            else:
                self.right.rightrotate()
                self.leftrotate()

    def insert(self, index, v):
        if index < 0 or index > self.size:
            raise IndexError
        self.size += 1
        if self.isempty():
            self.value = v
            self.left = AVLTree()
            self.right = AVLTree()
            self.height = 1
            return
        if index <= self.left.size:
            self.left.insert(index, v)
            self.rebalance()
            self.height = 1 + max(self.left.height, self.right.height)
        else:
            self.right.insert(index - self.left.size - 1, v)
            self.rebalance()
            self.height = 1 + max(self.left.height, self.right.height)

    def get(self, index):
        if 0 > index or index >= self.size:
            raise IndexError
        if index < self.left.size:
            return self.left.get(index)
        if index == self.left.size:
            return self.value
        return self.right.get(index - self.left.size - 1)

    def set(self, index, v):
        if 0 > index or index >= self.size:
            raise IndexError
        if index < self.left.size:
            self.left.set(index, v)
        elif index == self.left.size:
            self.value = v
        else:
            self.right.set(index - self.left.size - 1, v)

    def delete(self, index):
        if 0 > index or index >= self.size:
            raise IndexError
        self.size -= 1
        if index < self.left.size:
            self.left.delete(index)
            self.rebalance()
            self.height = 1 + max(self.left.height, self.right.height)
        elif index > self.left.size:
            self.right.delete(index - self.left.size - 1)
            self.rebalance()
            self.height = 1 + max(self.left.height, self.right.height)
        else:
            if self.left.isempty():
                if self.right.isempty():
                    self.value = None
                    self.height = 0
                    return
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                self.height = 1 + self.right.height
                return
            if self.right.isempty():
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                self.height = 1 + self.left.height
                return
            minval = self.right.get(0)
            self.value = minval
            self.right.delete(0)
            self.rebalance()
            self.height = 1 + max(self.left.height, self.right.height)


class FastList:
    def __init__(self):
        self.tree = AVLTree()

    def __len__(self):
        return self.tree.size

    def __getitem__(self, index):
        return self.tree.get(index)

    def __setitem__(self, index, value):
        self.tree.set(index, value)

    def __delitem__(self, index):
        self.tree.delete(index)

    def insert(self, index, value):
        self.tree.insert(index, value)

    def append(self, value):
        self.tree.insert(len(self), value)

    def pop(self, index):
        value = self.tree.get(index)
        self.tree.delete(index)
        return value
