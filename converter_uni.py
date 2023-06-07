import argparse
from termcolor import colored
# Dicionário de substituições
substitutions = {
    '<': '\\u{0:04x}'.format(ord('<')),
    '>': '\\u{0:04x}'.format(ord('>')),
    '/': '\\u{0:04x}'.format(ord('/')),
    '[': '\\u{0:04x}'.format(ord('[')),
    ']': '\\u{0:04x}'.format(ord(']')),
    '^': '\\u{0:04x}'.format(ord('^')),
    '?': '\\u{0:04x}'.format(ord('?')),
    ':': '\\u{0:04x}'.format(ord(':')),
    ';': '\\u{0:04x}'.format(ord(';')),
    '.': '\\u{0:04x}'.format(ord('.')),
    ',': '\\u{0:04x}'.format(ord(',')),
    '`': '\\u{0:04x}'.format(ord('`')),
    '´': '\\u{0:04x}'.format(ord('´')),
    '~': '\\u{0:04x}'.format(ord('~')),
    '-': '\\u{0:04x}'.format(ord('-')),
    '+': '\\u{0:04x}'.format(ord('+')),
    '=': '\\u{0:04x}'.format(ord('=')),
    '_': '\\u{0:04x}'.format(ord('_')),
    ')': '\\u{0:04x}'.format(ord(')')),
    '(': '\\u{0:04x}'.format(ord('(')),
    '*': '\\u{0:04x}'.format(ord('*')),
    '&': '\\u{0:04x}'.format(ord('&')),
    '¨': '\\u{0:04x}'.format(ord('¨')),
    '%': '\\u{0:04x}'.format(ord('%')),
    '$': '\\u{0:04x}'.format(ord('$')),
    '#': '\\u{0:04x}'.format(ord('#')),
    '@': '\\u{0:04x}'.format(ord('@')),
    '!': '\\u{0:04x}'.format(ord('!')),
    '\"': '\\u{0:04x}'.format(ord('\"')),
    '\'': '\\u{0:04x}'.format(ord('\'')),
    '|': '\\u{0:04x}'.format(ord('|')),
    '\\': '\\u{0:04x}'.format(ord('\\'))
    
    
}

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--string', help='String para codificar em Unicode')
group.add_argument('-w', '--file', help='Nome do arquivo para codificar em Unicode')
args = parser.parse_args()

if args.string:
    input_string = args.string
else:
    try:
        with open(args.file, 'r') as file:
            input_string = file.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        exit()

unicode_string = ''
for char in input_string:
    if char in substitutions:
        unicode_string += substitutions[char]
    else:
        unicode_string += char


print(colored(f"[+]String em Unicode[+] ","red",attrs=["bold"]))
print(colored(f"{unicode_string}","green",attrs=["bold"]))
