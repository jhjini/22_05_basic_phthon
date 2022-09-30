Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Turtle()

t.shape("turtle")
t.foward(100)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.foward(100)
AttributeError: 'Turtle' object has no attribute 'foward'. Did you mean: 'forward'?
t.fd(100)
t.rt(100)
t.fd(100)
t.rt(100)
t.fd(100)
t.rt(100)



t.fd(100)
