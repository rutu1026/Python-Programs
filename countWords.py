class count:

    def countWords(string):

        dict = {}
        c = 0

        for i in string:

            c = string.count(i)
            dict[i] = c

        return dict

s = input("ENter a string:")
obj = count
print(obj.countWords(s))

