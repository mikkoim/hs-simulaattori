# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:14:45 2017

@author: Mikko
"""

import txtfile_processing as tp
import random
#path = "C:\\Users\\Mikko\\Google Drive\\koodia\\"
#path = "D:\\Libraries\\Documents\\Mikko\\HS_otsikot\\data2\\"

#h, headers = tp.read_headers(path)

class TitleGenerator:
    
    def __init__(self, headers = None, n = 2):
        """Params: headers: an array containing the headers in a list"""
        
        self.__o = headers
        self.__n = n
        self.__firsts = []
        self.__lasts = []
        self.__ngrams = []
        self.__dic = {}
        
        if headers != None:
            self.process()
            
    def train(self, headers, n = 2):
        
        self.__o = headers
        self.__n = n
        
        self.process()
        
    def process(self):
        self.__firsts = []
        self.__lasts = []
        self.__ngrams = []
        self.__dic = {}
        
        n = self.__n
        
        for i in self.__o:
            i.strip()
            words = i.split(' ')
            self.__firsts.append( words[0:n] )
            self.__lasts.append( words[len(words)-1] )
            
            for i in range(len(words) - n + 1):
                gram = words[i : i + n]
                self.__ngrams.append(gram)
                
                txt = ''
                for j in gram:
                    txt = txt + j + ' '
                    
                if i < len(words) - n:
                    following_word = words[i + n]
                else:
                    following_word = None
                    
                if txt in self.__dic:
                    self.__dic[txt].append(following_word)
                else:
                    self.__dic[txt] = [following_word]
                
    def generate(self):
        try:
            #choose first gram
            first_int = random.randint(0,len(self.__firsts)-1)
            first_gram = self.__firsts[first_int]
            first_gram_txt = ' '.join(first_gram)
            
            title = first_gram_txt
            
            next_gram = first_gram[1:]
            next_gram_txt = ' '.join(next_gram)
            
            #second gram
            nextlist = self.__dic[first_gram_txt + ' ']
    
            next_int = random.randint(0,len(nextlist)-1)
            next_word = nextlist[next_int]
            
            title = title + ' ' + next_word
            
    
            while next_word != None:
                
                next_gram.append(next_word)
                next_gram_txt = ' '.join(next_gram)
                
                nextlist = self.__dic[next_gram_txt + ' ']
                next_int = random.randint(0,len(nextlist)-1)
                next_word = nextlist[next_int]
    
                if next_word != None:
                    
                    title = title + ' ' + next_word
        
                    next_gram = next_gram[1:]
                    
            if (title == self.find_original(title)) or (len(title) >= 140 
                or len(title) < 50):
                title = self.generate()
                
            self.__title = title
            
            return title
        except TypeError:
            self.generate()
            
    def print_headers(self):
        
        if self.has_headers() == True:
            for i in self.__o:
                print(i)
        else:
            raise ValueError("No headers assigned to object")
        
    def has_headers(self):
        if self.__o != None:
            return True
        else: 
            return False
        
    def find_original(self, string):
        index = self.find_indx(string)
        if index != None:
            return self.__o[index]
    
    def find_indx(self, string):
        l = 0
        for i in self.__o:
            if i.find(string) != -1:
                return l
            else:
                l += 1
        return None
    def find_headers(self, string):
        for i in self.__o:
            if i.find(string) != -1:
                print(i)
                
    def title(self):
        return self.__title
        
    def firsts(self):
        return self.__firsts
    
    def lasts(self):
        return self.__lasts
        
    def n(self):
        return self.__n
    
    def ngrams(self):
        return self.__ngrams
    
    def dic(self):
        return self.__dic

"""
gen = TitleGenerator()
print(gen.has_headers())
gen.train(h, 2)
print(gen.has_headers(), gen.n())

ngrams = gen.ngrams()
n = gen.n()
firsts = gen.firsts()
lasts = gen.lasts()

dic = gen.dic()

print(gen.generate())
"""
#a = []
#
#for header in h:
#    length = len(header)
#    a.append(length)
#    
#from scipy import stats
#import numpy as np
#mean, sigma = np.mean(a), np.std(a)
#
#conf_int = stats.norm.interval(0.95, loc=mean, scale=sigma)


def find_indx(string,  h):
    l = 0
    for i in h:
        if i.find(string) != -1:
            return l
        else:
            l += 1

            
