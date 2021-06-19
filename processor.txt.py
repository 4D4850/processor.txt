import sys

read = open("code.pt", "r")
if '-c' in sys.argv:
  codeint = sys.argv.index("-c") + 1
  code = sys.argv[codeint]
else:
  code = read.readline()
read.close()

print(type(code))

dataPointer = 0
codePointer = 0
data = []
selected_reg = 8
reg = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1000):
  data.append(0)

for i in range(len(code)):
  # This is the main interpret loop
  if code[codePointer] == '!':
    data[dataPointer] = 255 - data[dataPointer]
  elif code[codePointer] == '&':
    if selected_reg == 8:
      print("Error: No Register Selected. Performing Memory Dump.")
      write = open("memdump.pt.txt", "w")
      write.write(str(data))
      write.close()
      sys.exit()
    data[dataPointer] = reg[selected_reg] & data[dataPointer]
  elif code[codePointer] == '^':
    if selected_reg == 8:
      print("Error: No Register Selected. Performing Memory Dump.")
      write = open("memdump.pt.txt", "w")
      write.write(str(data))
      write.close()
      sys.exit()
    data[dataPointer] = reg[selected_reg] ^ data[dataPointer]
  elif code[codePointer] == ',':
    reg[0] = data[dataPointer]
    selected_reg = 0
  elif code[codePointer] == '$':
    data[dataPointer] = reg[0]
  elif code[codePointer] == '.':
    reg[1] = data[dataPointer]
    selected_reg = 1
  elif code[codePointer] == '*':
    data[dataPointer] = reg[1]
    reg[1] = 0
  elif code[codePointer] == '/':
    reg[2] = data[dataPointer]
    selected_reg = 2
  elif code[codePointer] == '?':
    data[dataPointer] = reg[2]
    reg[2] = 0
  elif code[codePointer] == ';':
    reg[3] = data[dataPointer]
    selected_reg = 3
  elif code[codePointer] == ':':
    data[dataPointer] = reg[3]
    reg[3] = 0
  elif code[codePointer] == '@':
    reg[4] = data[dataPointer]
    selected_reg = 4
  elif code[codePointer] == '#':
    data[dataPointer] = reg[4]
    reg[4] = 0
  elif code[codePointer] == '[':
    reg[5] = data[dataPointer]
    selected_reg = 5
  elif code[codePointer] == '{':
    data[dataPointer] = reg[5]
    reg[5] = 0
  elif code[codePointer] == ']':
    reg[6] = data[dataPointer]
    selected_reg = 6
  elif code[codePointer] == '}':
    data[dataPointer] = reg[6]
    reg[6] = 0
  elif code[codePointer] == '\\':
    reg[7] = data[dataPointer]
    selected_reg = 7
  elif code[codePointer] == '|':
    data[dataPointer] = reg[7]
    reg[7] = 0
  elif code[codePointer] == '>':
    dataPointer += 1
  elif code[codePointer] == '<':
    dataPointer -= 1
  elif code[codePointer] == '+':
    data[dataPointer] = (data[dataPointer] + 1)%256
  elif code[codePointer] == '-':
    data[dataPointer] = (data[dataPointer] - 1)%256
  elif code[codePointer] == '~':
    if '-a' in sys.argv:
      print(chr(data[dataPointer]))
    else:
      print(data[dataPointer])
  elif code[codePointer] == '`':
    pass
  else:
    print(f"{code[codePointer]} is not a valid command. Performing Memory Dump.")
    write = open("memdump.pt.txt", "w")
    write.write(str(data))
    write.close()
    sys.exit()
  codePointer += 1

if '-d' in sys.argv  or '--debug' in sys.argv:
  print("Performing Debug Memory Dump")
  write = open("debugdump.pt.txt", "w")
  write.write(str(data))
  write.close()
sys.exit()
