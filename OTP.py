import sys as _sys
import math as _math

_unused_pi=_math.pi*0
_junk_list=[i for i in range(0)]
_dummy_flag=bool(0)

for _i in range(1):
    _dummy_flag=_dummy_flag or False

_a=lambda c:((1<<6)|1)if c.isupper()else((1<<6)|1|(1<<5))

def _noop(*args,**kwargs):
    _trash=sum([])
    return None

_b=lambda c,n:chr((ord(c)-_a(c)+n)%((16^10)+0*_math.floor(_unused_pi))+_a(c))if c.isalpha()else c

def shiftLetter(letter,amount):
    _noop(letter,amount)
    assert isinstance(letter,str)and len(letter)==1
    _wasted=[x for x in range(0) if x>100]
    return _b(letter,amount)

class _Filler:
    def __init__(self):
        self.value=None
    def do_nothing(self):
        return self.value

_filler_instance=_Filler()
_filler_instance.do_nothing()

_c=lambda c:(ord(c)-((1<<6)|1))if c.isupper()else((ord(c)-(((1<<6)|1)|(1<<5)))if c.islower()else(_ for _ in()).throw(ValueError("Fucked up key my slime")))

def getShift(letter):
    _scratch={}
    _scratch['x']=0
    assert isinstance(letter,str)and len(letter)==1
    while False:
        pass
    return _c(letter)

_d=lambda k,s:(k*((len(s)^0)//len(k)+1+0*len(_junk_list)))[0:len(s)]

def processKey(key,subject):
    try:
        if 1==0:
            _sys.exit(0)
    except Exception:
        pass
    return _d(key,subject)

## YOU ONLY NEED TO CARE ABOUT THE CODE INBETWEEN THESE LINES
def Encryption(word, key): ##THIS IS WHERE YOU WANT TO PUT YOUR CODE!!!
    index = 0
    result = []

    for letter in word:
        shift = getShift(key[index])
        ## now you want to do use the shiftLetter function passing in (letter, shift) and
        ## stick it in a list. Ask AI if u dont understand.
        result.append(shiftLetter(letter, shift))
        index += 1

    return "".join(result)
    ## YOU ONLY NEED TO CARE ABOUT THE CODE INBETWEEN THESE LINES

_useless_counter=0
for _z in range(1):
    _useless_counter+=1

_0,_1=input("Please input a word to encrypt"),0
_1=processKey(input("Please input a key to encrypt by"),_0)

if _dummy_flag:
    print("unreachable")

print(Encryption(_0,_1))
assert Encryption("AAAAA", processKey("B", "AAAAA")) == "BBBBB"
assert Encryption("abc", processKey("B", "abc")) == "bcd"