
class JSONFilter(object):
    def compare_json(self,variablea=None, variableb=None, argslist=None):
        flag = False
        vara = dict([('a', 1), ('b', 2)])
        varb = {'a': 1, 'b': 2}

        list = ['a', 'b']
#        variablea = vara
#        variableb = varb
        args = list
        for element in argslist:
            if variablea[element] == variableb[element]:
                flag = True

        return flag

    def main(self):
        return "something"







