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
data = [0 for _ in range(1000)]
reg = [0 for _ in range(8)]

while codePointer < len(code):
  # This is the main interpret loop
  if (char := code[codePointer]) == '!':
    data[dataPointer] = 255 - data[dataPointer]
  elif char == '&':
    if selected_reg == 8:
      dump('mem', 'Error: No Register Selected')
    data[dataPointer] = reg[selected_reg] & data[dataPointer]
  elif char == '^':
    if selected_reg == 8:
      dump('mem', 'Error: No Register Selected')
    data[dataPointer] = reg[selected_reg] ^ data[dataPointer]
  elif char in (s := ',./;@[]\\'):
    ind = s.find(char)
    reg[ind] = data[dataPointer]
    selected_reg = ind
  elif char in (s := '$*?:#{}|'):
    ind = s.find(char)
    data[dataPointer] = reg[ind]
    if char != '$':
      reg[ind] = 0
  elif char == '>':
    dataPointer += 1
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
