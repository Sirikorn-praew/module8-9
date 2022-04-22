import math

pos = [200, 0, 20]
check = 0
oriz = 0
gram = 1
q = [0,0,0,0]
c2 = (((pos[0] * pos[0] + pos[1] * pos[1]) - 61504.0) - 170544.22090000001)/204724.0
s2 = 1.0 - c2 * c2
if s2 >= 0.0:
    check = 1
    s2 = gram * math.sqrt(s2)
    q2 = math.atan2(s2, c2)

    q[1] = q2
    s2 = math.atan2(pos[1], pos[0]) - math.atan2(412.97 * s2, 412.97 * c2 + 248.0)
    q[0] = s2
    q[2] = 217.04 - pos[2]
    q[3] = (oriz - s2) - q2
else:
    check = 0

print(check)
print(q)