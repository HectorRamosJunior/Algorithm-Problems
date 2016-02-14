"""
Hash Table Implementation
Hector Ramos, 12/7/2015
"""

class StringBuilder(object):
    def __init__(self, string = None):
        self.stringList = []

        if string:
            self.stringList.append(string)

    def add(self, string):
        self.stringList.append(str(string))

    def build(self):
        output = ""

        return output.join(self.stringList)


s = StringBuilder()

[s.add(x+1) for x in xrange(100)]

print s.build()

