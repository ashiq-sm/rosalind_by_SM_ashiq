d={
  
}
# for itr in range(5):
#   a,b = input(), input()
  
#   c = a.count('G') + a.count('C')
#   d[a]=c/100.0

# print(max(d, key=d.get))
o=open('rosalind_gc.txt','r')
# n=open('input.txt', 'w')
content = o.read().replace('\n','').replace('>Rosalind_' , '')

import re

def split_string(string):
    global pairs 
    pairs = re.findall(r"(\d+)([a-zA-Z]+)", string)
    for p in pairs:
      digit = p[0]
      text = p[1]
      d[digit]=text
      

# Example usage:
split_string(content) # Output: ('foofo', '21')
gcdict = {}# d.get(max(d.keys()))
# print('Rosalind_'+max(d.keys()))
for key, value in d.items():
  c= value.count('G') + value.count('C')
  gcdict[key]=c/len(value)*100.0
# print(c)
# print(gcdict)
print('Rosalind_'+max(gcdict, key=gcdict.get))
print(max(gcdict.values()))
o.close()