from urllib.request import urlopen
import ssl
context = ssl._create_unverified_context()
req = urlopen('https://j5a203.p.ssafy.io/static/airlines/npl/stopwords.txt', context=context)
data=req.read().decode('utf8')
print(data)


# file.readlines()
# stopwords = stopwords.split('\n')
# print(stopwords)