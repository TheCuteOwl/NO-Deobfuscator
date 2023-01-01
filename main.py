import base64
import re
infile = "obfuscated.txt"
outfile = "deobfuscated.txt"

delete_list = ["NO", "__", '"', '+', '=']
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)



# Open the file
with open(outfile, 'r') as file:
    # Read the lines of the file
    lines = file.readlines()

# Open the file for writing
with open(outfile, 'w') as file:
    # Write each line to the file, with no line breaks
    for line in lines:
        file.write(line.strip())
        file.write(' ')

with open(outfile, 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Remove all spaces from the contents
contents = contents.replace(' ', '')

# Open the file for writing
with open(outfile, 'w') as file:
    # Write the modified contents back to the file
    file.write(contents)


print("Done!")
with open(outfile, 'r') as f:
    obfuscated_string = f.readline()

print(obfuscated_string)
import re

def unescape(s):
    
    s = re.sub(r'\\x([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)

    return s


deobfuscated = unescape(obfuscated_string)

deobfuscated = base64.b64decode(deobfuscated)
deobfuscated = deobfuscated.decode("utf-8")
print(deobfuscated)
with open(outfile, 'w+') as f:
    print('test3')

    f.write(deobfuscated)
    print('Deobfuscated version in deobfuscated.txt)
    input('Successfully Deobfuscated Press Enter to Quit')



