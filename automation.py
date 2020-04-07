#!/usr/bin/env python3
import sys
import os
import re
pattern=r"x                   &           ([\w]+)\\"
line="x                   &           5\\"

def get_value(input_file):
  value=[]
  with open(input_file, 'r') as f:
    for line in f.readlines():
        #print(line)
        result=re.search(pattern,line)
        if result is not None:
            #print(result[1])
            value.append(result[1])
  return value[0]

def main():
    input_file="{}".format(file)
    output_file=output
    value_output=get_value(input_file)
    def write_output(output_file):
       with open(output_file, 'w+') as output_file:
         output_file.write(value_output)
         output_file.close()
    write_output(output_file)



from pathlib import Path



text_dir = Path(sys.argv[1]).glob('**/*.tex')

i=0
for path in text_dir:
     i = i+1
     # because path is object not string
     file = str(path)
     output = "{}\out_{}.txt".format(str(Path(sys.argv[2])),i)
     main()
