import sys


def dump(mode, msg=''):
  if mode == 'debug':
    print('Performing Debug Memory Dump')
  else:
    print(f'{msg}. Performing Memory Dump.')
  write = open(f'{mode}dump.pt.txt', "w")
  write.write(str(data))
  write.close()
  sys.exit()


if '-c' in sys.argv:
  codeint = sys.argv.index("-c") + 1
  code = sys.argv[codeint]
else:
  read = open("code.pt", "r")
  code = read.readline()
  read.close()

print(type(code))

dataPointer = 0
codePointer = 0
selected_reg = 8
reg = [0] * 8
data = [0] * 1024

while codePointer < len(code):
  char = code[codePointer]
  # This is the main interpret loop
  if char == '!':
    data[dataPointer] = 255 - data[dataPointer]
  elif char == '&':
    if selected_reg == 8:
      dump('mem', 'Error: No Register Selected')
    data[dataPointer] = reg[selected_reg] & data[dataPointer]
  elif char == '^':
    if selected_reg == 8:
      dump('mem', 'Error: No Register Selected')
    data[dataPointer] = reg[selected_reg] ^ data[dataPointer]
  elif char == ',':
    reg[0] = data[dataPointer]
    selected_reg = 0
  elif char == '$':
    data[dataPointer] = reg[0]
  elif char == '.':
    reg[1] = data[dataPointer]
    selected_reg = 1
  elif char == '*':
    data[dataPointer] = reg[1]
    reg[1] = 0
  elif char == '/':
    reg[2] = data[dataPointer]
    selected_reg = 2
  elif char == '?':
    data[dataPointer] = reg[2]
    reg[2] = 0
  elif char == ';':
    reg[3] = data[dataPointer]
    selected_reg = 3
  elif char == ':':
    data[dataPointer] = reg[3]
    reg[3] = 0
  elif char == '@':
    reg[4] = data[dataPointer]
    selected_reg = 4
  elif char == '#':
    data[dataPointer] = reg[4]
    reg[4] = 0
  elif char == '[':
    reg[5] = data[dataPointer]
    selected_reg = 5
  elif char == '{':
    data[dataPointer] = reg[5]
    reg[5] = 0
  elif char == ']':
    reg[6] = data[dataPointer]
    selected_reg = 6
  elif char == '}':
    data[dataPointer] = reg[6]
    reg[6] = 0
  elif char == '\\':
    reg[7] = data[dataPointer]
    selected_reg = 7
  elif char == '|':
    data[dataPointer] = reg[7]
    reg[7] = 0
  elif char == '>':
    dataPointer += 1
    if dataPointer > len(data):
      dump('mem', 'dataPointer out of bounds')
  elif char == '<':
    dataPointer -= 1
  elif char == '+':
    data[dataPointer] = (data[dataPointer] + 1) % 256
  elif char == '-':
    data[dataPointer] = (data[dataPointer] - 1) % 256
  elif char == '~':
    if '-a' in sys.argv:
      print(chr(data[dataPointer]))
    else:
      print(data[dataPointer])
  elif char == '%':
    data[dataPointer] = data[dataPointer] << 1
  elif char == '_':
    data[dataPointer] = data[dataPointer] >> 1
  elif char != '`':
    dump('mem', f'{code[codePointer]} is not a valid command')
  codePointer += 1

if '-d' in sys.argv  or '--debug' in sys.argv:
  dump('debug')
