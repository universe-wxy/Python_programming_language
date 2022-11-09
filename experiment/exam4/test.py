from circle import circle
from cylinder import cylinder

a=circle(5)
b=cylinder(5,7)
a.show()
b.show()

print("---------")
a.setR(7)
b.setR(7)
b.setH(20)
a.show()
b.show()

