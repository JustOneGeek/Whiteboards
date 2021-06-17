#Given a string after every y add an ! and after every s add a peroid and make every w and g capital
#Make a Function that takes a string as input and returns the adjusted string.
s="Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"
#output= Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!
def fix_string(s):
    new_sentence=""
    for letter in s:
        if letter.lower()=='y':
            new_sentence+=letter+"!"
        elif letter.lower()=='s':
            new_sentence+=letter+"."
        elif letter.lower()=='w' or letter.lower()=='g':
            new_sentence+=letter.upper()
        else:
            new_sentence+=letter
    return new_sentence

print(fix_string(s))

def fix_string_lc(s):
    return "".join([letter+"!" if letter.lower()=='y' else letter+"." if letter.lower()=='s' else letter.upper() if letter.lower()=='w' or letter.lower()=='g' else letter for letter in s])

print(fix_string_lc(s))


def fix_string_replace(s):
    return s.replace('y',"y!").replace('s','s.').replace('w','W').replace('g','G')

print(fix_string_replace(s))