# import pickle
#
# from entity import nosprite_entity
#
# a = nosprite_entity("blue")
# a = pickle.dumps(a)
# a.__init__()
# print(pickle.loads(a).color)
#
#
# b = nosprite_entity("blue")


class parent() :
    def __init__(self) -> None:
        self.a = "a"

class child(parent) :
    def __init__(self ) -> None:
        super().__init__()
        self.a = "A"

a = parent()
a.a = "1"


# c = child(parent)
c = child()
# c.__init__()
print(a.a)
a.__init__()
print(a.a)
print(c.a)
