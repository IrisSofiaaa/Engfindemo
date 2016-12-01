import random
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import brown


# -*- coding: utf-8 -*-

class Dictionary:
    """represents the dictionary and making of it"""
    def __init__(self, english, finnish):
        enl = open(english, mode="r", encoding="utf-8")
        self.english = enl.readlines()
        fil = open(finnish, mode="r", encoding="utf-8")
        self.dictionary = {}
        self.stripped = []
        self.res = []
        self.fixed = ""
        self.finnish = fil.readlines()
        self.create_dictionary(self.english, self.finnish) ##############
        self.runwords()                                    ######RUN#####
        self.tokenize()                                    ##############

    def create_dictionary(self, enl, fil):
        """creates a dictionary from testeng and testfi, replaces characters
         that didn't get replaced with utf-8 encoding"""

        keys = []
        values = []

        for i in enl:
            out = "".join(c for c in i if c not in ('!', '.', ':', ",", "\n", "?", "'", '"')).replace("\\u201c", "").replace(
                "\\u201d", "").replace("\\u2019", "'").replace("\\u2026", "").replace('"', "") 
            keys.append(out)

        for j in fil:
            out = "".join(c for c in j if c not in ('!', '.', ':', ",",  '"', "\n"))
            values.append(out)

        for k, v in zip(keys, values):
            self.dictionary.setdefault(k, [])
            self.dictionary[k].append(v)

    def first_words(self, words):
        """opens the story file, pulls out a random story and processes it
        so that I can work with just the six words and that's it (not the
        usernames of the authors or other unimportant stuff"""
        
        f = open("testcorpus.txt", "r")
        linelist = f.readlines()

        random_index = random.randint(0, 225)
        story = linelist[random_index]
        print("Original text:     " + story)
        for i in range(0, len(story)):
            if story[i] == ' ':
                words -= 1
            if words == 0:
                return story[0:i]
        return ""

    def runwords(self):
        """fixes the words in to a list that I can use in another class"""
        result = self.first_words(6)
        self.fixed = ''.join(result.split("'", 1))

        # print(fixed)

        for word in self.fixed.split():
            striped = "".join(c for c in word if c not in ('!', '.', ':', ",", "\n", "?", "'", ";")).replace("\\u201c",
                                                                                                    "").replace('"', "").replace("\\u201d", "").replace("\\u2019", "").replace("\\u2026", "").replace("\u201c", "").replace("\u201d", "")

            self.stripped.append(striped)

        return self.fixed
        return self.stripped

    def tokenize(self):
        """tokenize the words and tag them according to part of speech"""
        strip = " ".join(self.stripped)
        tokens = word_tokenize(strip)
        self.res = nltk.pos_tag(tokens)
