poem_file = open('hwpoem.txt', encoding='utf-8')
content = poem_file.read()
print(content)
poem_file.close()


print('I have read this poem:')
print()
poem_file = open('hwpoem.txt', encoding='utf-8')
for line in poem_file:
    print('    ' + line)
poem_file.close()
print()
print('Is this poem lovely. How do you like it?')


def last_line():
    """Return the last line in the poem."""

    poem_file = open('hwpoem.txt', encoding='utf-8')
    try:
        content = poem_file.read()
        return content[0]
    finally:
        poem_file.close()

print(last_line())


def last_line():
    """Return the last line in the poem."""

    with open('hwpoem.txt', encoding='utf-8') as poem_file:
        content = poem_file.read()
        return content[0]

print(last_line())


with open('second-hwpoem.txt', mode='w', encoding='utf-8') as poem_file:
    poem_file.write('Filled with pines and electronics\n')
    poem_file.write("Where deer stroll peacefully\n")
    poem_file.write('As if they were flowers\n')
    poem_file.write("With spinning blossoms\n")


with open('second-hwpoem.txt', mode='w', encoding='utf-8') as poem_file:
        print('Filled with pines and electronics', file=poem_file)
        print("Where deer stroll peacefully", file=poem_file)
        print('As if they were flowers', file=poem_file)
        print("With spinning blossoms", file=poem_file)


        string = "But I have promises to keep"
new_string = string.replace("have", "great")
 
print(new_string)


# Python program to replace text in the file
s = input("I am a peaceful animal:")
f = open("second-hwpoem.txt", "r+")
 
# r+ mode opens the file in read and write mode
f.truncate(0)
f.write(s)
f.close()
print("I am a peaceful animal")


import argparse

parser = argparse.ArgumentParser(description='replace')
parser.add_argument("character", help='a character to replace')
parser.add_argument("count", help='how many times', type=int)
parser.add_argument("--indent", action="store_true", help=("character will be replaced by 5 times"))
                    
def replace(count, character, indent=False):
     string = "I am a peaceful animal"
new_string = string.replace("a", "z")
"""Simple program that replaces 'character' for a total of 'count' times and optionally indents."""
for _ in range('count'):
        if 'indent':
            print("    ", end="")
        print(f"second-hwpoem {'character'}!")                    
                    
