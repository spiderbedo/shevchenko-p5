import turtle as t

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

if (xc - x) ** 2 + (yc - y) ** 2 < r ** 2:
    print("Точка внутри окружности.")
elif (xc - x) ** 2 + (yc - y) ** 2 == r ** 2:
    print("Точка на окружности.")
else:
    print("Точка вне окружности.")

t.up()
t.setposition(xc, yc - r)
t.down()
t.circle(r)
t.up()
t.setposition(x, y)
t.down()
t.dot(10)
t.done()
print('\n')
