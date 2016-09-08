class Dependence:

    def __init__(self, x, p):
        self.x = x  # integer
        self.p = set(p)  # set

    def __repr__(self):
        s = str(x) + " <-";
        for item in p:
            s += " " + str(item)

        return s

    def __eq__(self, obj):
        if (obj is None):
            return False
        return self.x == obj.x and self.p.symmetric_difference(set(obj.p)) == set()

    def __hash__(self):
        myHash = 0
        for item in p:
            myHash += item * item

        return myHash + self.x * 7117

