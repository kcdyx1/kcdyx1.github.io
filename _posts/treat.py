import sys
import re
import readline

url = ''
fr = open('./1.txt', 'r')
for line in fr:
    url = re.search('[a-zA-z]+://[^\s]*', line)
    if url:       
        line = line[:-len(url.group(0)) - 1] + '[' + url.group(0) + '](' + url.group(0) + ')'
        print(line)
    else:
        print(line)

fr.close()
