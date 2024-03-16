class Concate:

    def stringListConcate(list1):

        sep = input("enter seperator:")
        s = sep.join(i for i in list1)
        print(s)

o = Concate
o.stringListConcate(["a","b","c"])