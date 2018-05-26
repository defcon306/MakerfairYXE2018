#!/usr/bin/python

print "Hello DCG306"

dinoLetters=['g','w','r','a','o','e']
englishLetters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
englishExtras=['1','2','3','4','5','6','7','8','9','0',' ']
englishAll=englishLetters+englishExtras

#or valid ranges
#letters 97->122 (inclusive)
#numbers 48->57 (inclusive)
#space 20

class DinoCrypt():
  def __init__(self):
    self.dinoLookup=self.createDinoLookup()
    self.englishLookup = dict((v,k) for k,v in self.dinoLookup.iteritems())
    
    print
    print "Dino -> English lookup Table"
    print
    print self.dinoLookup
    print
    print "English -> Dino lookup Table"
    print
    print self.englishLookup

  def createDinoLookup(self):
    lookupDict={}
    letter_idx=0;
    letter2_idx=0;

    for letter in dinoLetters: #outter loop
      for letter2 in dinoLetters: #inner loop
        lookupDict[letter+letter2]=englishAll[letter_idx*6+letter2_idx]
        letter2_idx=letter2_idx+1
      #end inner
      letter_idx=letter_idx+1
      letter2_idx=0
    #end outter
    return lookupDict

  def english2Dino(self, string):
    #for letter in the string create full string
    dinofied=""
    for c in string:
      cl=c.lower()
      if cl in self.englishLookup:
        dinofied=dinofied+self.englishLookup[cl]
      else:
        dinofied=dinofied+cl
    return dinofied
      

  def dino2English(self, string):
    i=0
    oldc=''
    newc=''
    englishfied=""
    for c in string:
      newc=c.lower()
      if newc in self.englishLookup:
        if i==1:
          englishfied=englishfied+self.dinoLookup[oldc+newc]
          i=0
        else:
          oldc=newc
          i=1
      else:
        englishfied=englishfied+newc 

    return englishfied
    #for pair of letters in string create full string

if __name__ == "__main__":
  Dino = DinoCrypt();
  crypted = Dino.english2Dino("Welcome to the Defcon306 group table. Enjoy your stay!")
  decrypted = Dino.dino2English(crypted)

  print
  print "Encrypted message:"
  print crypted
  print
  print "Decrypted message:"
  #print decrypted
  
        
