import string
import random

class Keyboard(object):
    
    def __init__(self, leftright, updown):
        self.updown =updown
        self.leftright = leftright
        self.p_lr = 0.7

    def pickOne(self, randomer = None):
        if (randomer is None):
            randomer = random.Random()
        if randomer.random() > self.p_lr:
            idx = randomer.choice(range(len(self.updown)))
            return self.updown[idx]
        else:
            idx = randomer.choice(range(len(self.leftright)))
            return self.leftright[idx]

KBMatrix = {
    'q' : Keyboard("w", "as"),
    'w' : Keyboard("qe","asd"),
    'e' : Keyboard("wr","sdf"),
    'r' : Keyboard("et","dfg"),
    't' : Keyboard("ry","fgh"),
    'y' : Keyboard("tu","ghj"),
    'u' : Keyboard("yi","hjk"),
    'i' : Keyboard("uo","jkl"),
    'o' : Keyboard("ip","kl"),
    'p' : Keyboard("o","l"),

    'a' : Keyboard("s","qwzx"), 
    's' : Keyboard("ad","qwezxc"),
    'd' : Keyboard("sf","werxcv"),
    'f' : Keyboard("dg","ertcvb"),
    'g' : Keyboard("fh","rtyvbn"),
    'h' : Keyboard("gj","tyubnm"),
    'j' : Keyboard("hk","yuinm"),
    'k' : Keyboard("jl","uiom"),
    'l' : Keyboard("k","iop"),

    'z' : Keyboard("x","as"),
    'x' : Keyboard("zc","asd"),
    'c' : Keyboard("xv","sdf"),
    'v' : Keyboard("cb","dfg"),
    'b' : Keyboard("vn","fgh"),
    'n' : Keyboard("bm","ghj"),
    'm' : Keyboard("n","hjk")
}

class TypingMesser(object):
    """
    add character-level typing errors

    insertion
    deletion
    substitution
    transposition
    duplication

    alphabatic/numeric
    """
    def __init__(self, probability, randomer = None):
        self.probability = probability
        self.numerics = range(9)
        self.randomer = randomer
        if (self.randomer is None):
            self.randomer = random.Random()
        

    def insertion(self, word):
        idx = self.randomer.choice(range(len(word))) + 1
        if word[idx-1].lower() in KBMatrix:
            c = KBMatrix[word[idx-1].lower()].pickOne()
            return word[:idx] + c + word[idx:]
        elif word[idx-1].isdigit():
            c = str(self.randomer.choice(self.numerics))
            return word[:idx] + c + word[idx:]
        else:
            return word[:]
    
    def deletion(self, word):
        idx = self.randomer.choice(range(len(word)-1)) + 1
        return word[:idx] + word[idx+1:]
    
    def substitution(self, word):
        idx = self.randomer.choice(range(len(word)-1)) + 1
        if word[idx].isalpha():
            c = KBMatrix[word[idx].lower()].pickOne()
            return word[:idx] + c + word[idx+1:]
        elif word[idx].isdigit():
            c = str(self.randomer.choice(self.numerics))
            return word[:idx] + c + word[idx+1:]
        else:
            return word[:]

    def transposition(self,word):
        idx = self.randomer.choice(range(len(word)-2)) + 1
        return word[:idx] + word[idx+1] + word[idx] + word[idx+2:]
    
    def duplication(self, word):
        idx = self.randomer.choice(range(len(word)-1)) + 1
        return word[:idx] + word[idx] + word[idx:]

    def addTypingError(self, word):
        if (len(word) < 3 or self.randomer.random() > self.probability):
            return word[:]
            
        if self.randomer.random() < 0.2:
            return self.insertion(word)
        elif self.randomer.random() < 0.4:
            return self.deletion(word)
        elif self.randomer.random() < 0.6:
            return self.substitution(word)
        elif self.randomer.random() < 0.8:
            return self.transposition(word)
        else:
            return self.duplication(word)
        
if __name__ == '__main__':
    messer = TypingMesser(1.0)
    words = ["haha", "the", "quick", "brown", "fox", "1312321", "q23.02", "===", "100%"]
    for word in words:
        print(word)
        print(messer.addTypingError(word))
