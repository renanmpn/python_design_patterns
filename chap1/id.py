# codding=utf-8
#
# Renan Monteiro Pinto Neto 06/10/16

class A(object):
    pass

if __name__ == '__main__':
    a = A()
    b = A()

    print(id(a) == id(b))
    print(a, b)
