# -*- coding: utf-8 -*-
from dictionary import Dictionary
from noun import Noun
from verb import Verb
from person import Person
from case import Case
from prev import Prev
from adjective import Adjective
from exceptions import Exceptions
from next_ import Next


def story():
    """runs all the classes with the help of for loops and
    spits out the translation"""
    d = Dictionary("testengwords.txt", "testfiwords.txt")
    res = d.res
    strip = d.stripped
    rest = dict(res)
    strip1 = strip[0]
    strip2 = strip[1]
    strip3 = strip[2]
    strip4 = strip[3]
    strip5 = strip[4]
    strip6 = strip[5]
    translist = []

    print("Stripped form:     " + strip1.lower(), strip2.lower(), strip3.lower(), strip4.lower(), strip5.lower(), strip6.lower())
    sentence = " ".join([strip1.lower(), strip2.lower(), strip3.lower(), strip4.lower(), strip5.lower(), strip6.lower()])

    for i in strip:
            if rest[i].startswith("VB"):
                pr = Prev(sentence, strip1, strip2, strip3, strip4, strip5, strip6)
                p = Person(pr)
                v = Verb(rest, d, p, i)
                nx = Next(sentence, strip1, strip2, strip3, strip4, strip5, strip6)
                nx.nextie()
                v.verb()
                v.pers()
                ex = Exceptions(pr, nx, v.trans)
                ex.exes()
                translist.append(ex.trans)
            elif rest[i].startswith("NN") or rest[i].startswith("PR"):
                pr = Prev(i, strip1, strip2, strip3, strip4, strip5, strip6)
                p = Person(pr)
                c = Case(pr)
                n = Noun(rest, d, c, i)
                nx = Next(sentence, strip1, strip2, strip3, strip4, strip5, strip6)
                n.noun()
                ex = Exceptions(pr, nx, n.trans)
                translist.append(ex.trans)
            elif rest[i].startswith("JJ"):
                a = Adjective(d, i)
                a.adj()
                translist.append(a.trans)
            else:
                t = d.dictionary.get(i)
                try:
                    translist.append(t[2])
                except IndexError:
                    translist.append(t[0])
                except TypeError:
                    translist.append("-")

    translations = " ".join(translist).replace("-", "")

    print("Translation:       " + translations, "\n")

###############################################################################
####################### RUN ###################################################
###############################################################################
    
def main():
    print("\n")
    print("Welcome to the demo version of the english-finnish translator!")
    print("\n")
    print("Let's get started:")
    print("\n")
    story()
    start = input("Would you like another story? y/n:     ")
    while start != "n":
        print("\n")
        story()
        start = input("Would you like another story? y/n:     ")
        print("\n")
        
    
    print("Okay, have a great day!")

main()

