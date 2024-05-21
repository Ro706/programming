# python\frustum.py
# Calculate the volume of a frustum
# v = 1/3 * 3.14 * h * (r1**2 + r2**2 + r1 * r2)
r1 = float(input("r1:"))
r2 = float(input("r2:"))
h = float(input("h:"))
v = 1 / 3 * 3.14 * h * (r1 ** 2 + r2 ** 2 + r1 * r2)
print("volume =", v)
print("thank you")
