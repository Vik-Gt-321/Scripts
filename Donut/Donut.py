import numpy as np
import math
R1 = 3
R2 = 1
screen_height = 10
screen_width = 10
def print_donut(output, screen_height, screen_width):
    print("\x1b[H")
    for i in range(screen_height):
        for j in range(screen_width):
            print(output[i, j])
        print('\n')

def render(A, B):

    output = np.zeros((screen_height, screen_width))
    for theta in np.arange(0, 2*math.pi, 0.01):
        x = R1 + R2*math.cos(theta)
        y = R2*math.sin(theta)
        z = 0
        coordinates = np.array([x, y, z])
        for phi in np.arange(0, 2*math.pi, 0.01):
            torus_matrix = np.array([[math.cos(phi), 0, math.sin(phi)], 
                                    [0, 1, 0], 
                                    [-math.sin(phi), 0, math.cos(phi)]])

            torus = np.dot(torus_matrix, coordinates)
            # A, B = 0, 0
            x_rot_matrix = np.array([[1, 0, 0], 
                                    [0, math.cos(A), math.sin(A)], 
                                    [0, -math.sin(A), math.cos(A)]])
            z_rot_matrix = np.array([[math.cos(B), math.sin(B), 0], 
                                    [-math.sin(B), math.cos(B), 0], 
                                    [0, 0, 1]])
            # print(x_rot_matrix, z_rot_matrix)
            final_coordinate = np.dot(z_rot_matrix, np.dot(x_rot_matrix, torus))
            # print(final_coordinate)

            lumin = np.dot(torus_matrix, np.array([math.cos(theta), math.sin(theta), 0]))
            lumin = np.dot(x_rot_matrix, lumin)
            lumin = np.dot(z_rot_matrix, lumin)
            lumin = np.dot(np.array([0, 1, -1]), lumin)
            print(int(lumin), "hello", ".,-~:;=!*#$@"[int(lumin)])
            output[x, y] = ".,-~:;=!*#$@"[int(lumin)]

    print_donut(output, screen_height, screen_width)

render(10, 10)