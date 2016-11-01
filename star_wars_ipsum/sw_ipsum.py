import re
from random import randint
import pkgutil
import os
import sys

class sw_ipsum(object):
    def __init__(self):
        self.sentance = {}
        self.key = 0
        script_text = ''
        IS = False


        f=pkgutil.get_data('star_wars_ipsum','/data/Movie4.txt')
        f=f.decode('utf-8')
        #ofp=open('t.t','wt')
        #ofp.write(f)
        #ofp.close()


        #print('file is %s'%f)

        #with open(f, 'r') as ifp:
        for line in f.split('\n'):
            if re.match(r'^[A-Z]+[:][ ][A-Z][a-z]+', line):
                script_text = script_text + ' '.join(line.split(' ')[1:])
                script_text = script_text.strip('\n')
                IS = True
            elif IS == True and len(line) > 2:
                script_text = script_text + ' '.join(line.split(' '))
                script_text = script_text.strip('\n')

            if line == '' and len(script_text) > 2:
                self.sentance[self.key] = script_text
                IS = False
                script_text = ''
                self.key = self.key + 1
        #print("Imported %d"%self.key)


    def __iter__(self):
        return self.sen(self)

    def gen_sentances(self, n):
        for i in range(0, n - 1):
            yield (self.sentance[randint(0,self.key-1)])

if __name__ == "__main__":
    jedi = sw_ipsum()
    for i in jedi.gen_sentances(20):
        print('%s' % i)
