
import sys
import re

def convert(s):
    s = re.sub(r"\[",r"{",s)
    s = re.sub(r"\]",r"}",s)
    s = re.sub(r"\s*",r"", s)
    return s
def stringify(s):
    s = convert(s)
    s = re.sub(r"\'", r"\"", s)
    return s
def charify(s):
    s = convert(s)
    s = re.sub(r"\"", r"'", s)
    s = re.sub(r",", r"','", s)
    s = re.sub(r"{", r"{'", s)
    s = re.sub(r"}", r"'}", s)
    s = re.sub(r"{'{", r"{{", s)
    s = re.sub(r"}'}", r"}}", s)
    s = re.sub(r"}','{", r"},{", s)
    
    return s
def tostring(s):
    s = convert(s)
    s = re.sub(r"{", r'{"', s)
    s = re.sub(r"}", r'"}', s)
    s = re.sub(r",", r'","', s)
    s = re.sub(r'{"{', r'{{', s)
    s = re.sub(r'}"}', r'}}', s)
    s = re.sub(r'}","{', r'},{', s)
    return s
if __name__ == "__main__":
	
    arg = sys.argv
    s = arg[2]
    s = "".join(s.split('\n'))
    if arg[1] == 'stringify':
        print(stringify(s))        
    elif arg[1] == 'charify':
        print(charify(s))
    elif arg[1] == 'string':
        print(tostring(s))   
    else:
        print(convert(s))
