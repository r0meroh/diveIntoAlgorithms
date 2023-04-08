import matplotlib.pyplot as plt

def ball_trajectory(x):
    location = 10*x - 5*(x**2)
    return location
xs = [x/100 for x in list (range(201))]
ys = [ball_trajectory(x) for x in xs]

plt.plot(xs, ys)
# plt.title('The trajectory of the ball thrown')
# plt.xlabel('Horizontal position of ball')
# plt.ylabel('Vertical position of ball')
# plt.axhline(y = 0)
# plt.show()

xs2 = [0.1, 2]
ys2 = [ball_trajectory(0.1), 0]

xs3 = [0.2, 2]
ys3 = [ball_trajectory(0.2), 0]

xs4 = [0.3, 2]
ys4 = [ball_trajectory(0.3), 0]

xs5 = [0.3, 0.3]
ys5 = [0, ball_trajectory(0.3)]

xs6 = [0.3, 2]
ys6 = [0, 0]

xs7 = [1.0, 2]
ys7 = [ball_trajectory(1.0), 0]

xs8 = [1.5, 2]
ys8 = [ball_trajectory(1.5), 0]

plt.title('The trajectory of the ball thrown - with lines of sight')
plt.xlabel('Horizontal position of ball')
plt.ylabel('Vertical position of ball')
plt.plot(xs,ys,xs2,ys2,xs3,ys3,xs4,ys4,xs5,ys5,xs6,ys6,xs7,ys7,xs8,ys8)
plt.show()


