from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"""
Coping from {from_file} to {to_file}
{open(from_file.read())}
The input file is {len(from_file)} bytes long.
Does the ouput file exist? {exist(to_file)}
Ready, hit the RETURN to continue, CTRL-C to abort
?""")
