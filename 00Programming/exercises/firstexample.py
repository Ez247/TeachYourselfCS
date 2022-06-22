# Load functionality for acessing data on the internet.
from urllib.request import urlopen

#Access the shakespeare text from the URL below
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

#Read, decode and split the text into words and place them in a set.
words = set(shakespeare.read().decode().split())

w = {w for w in words if len(w) == 6 and w[::-1] in words}
print(w)
