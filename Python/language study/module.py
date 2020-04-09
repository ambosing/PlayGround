import math as m

print(m.pi)
print(m.sqrt(4.0))
print(m.sqrt(2.0))

from math import pi, sqrt

print(pi)
print(sqrt(4.0))
print(sqrt(2.0))

from math import sqrt as s, pi as p

print(p)
print(s(4.0))
print(s(2.0))

import urllib.request as r

response = r.urlopen('http://www.google.co.kr')
print(response.status)

from urllib.request import Request, urlopen

req = Request('http://www.google.co.kr')
response = urlopen(req)
print(response.status)

from urllib.request import Request as r, urlopen as u

req = r('http://www.naver.com')
response = u(req)
print(response.status)

from math import pi

r = float(input())
print(pi * r ** 2)