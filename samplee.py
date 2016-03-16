class Gitest(object):
    name = "Gitest"
    glass = 199

    def __init__(self):
        print self.name

    def get_glass(self):
        return self.glass


if __name__ == "__main__":
    gitest = Gitest()
    print gitest.get_glass()


    print 'Done.'
