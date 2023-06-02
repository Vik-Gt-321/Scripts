import numpy as np
import math


def print_donut(output, screen_height, screen_width):
  print("\x1b[H")  # Move cursor to the top-left corner
  for i in range(screen_height):
    for j in range(screen_width):
      print(output[i, j], end='')
    print()


def render(A, B, screen_width, screen_height, theta_spacing, phi_spacing, R1,
           R2, K1, K2):
  cosa = math.cos(A)
  sina = math.sin(A)
  cosb = math.cos(B)
  sinb = math.sin(B)

  output = np.empty((screen_width, screen_height), dtype=np.dtype('U1'))
  output.fill(' ')
  z_inv = np.zeros((screen_width, screen_height))

  for theta in np.arange(0, 2 * math.pi, theta_spacing):
    cost = math.cos(theta)
    sint = math.sin(theta)

    for phi in np.arange(0, 2 * math.pi, phi_spacing):
      cosp = math.cos(phi)
      sinp = math.sin(phi)

      circlex = R2 + R1 * cost
      circley = R1 * sint

      x = circlex * (cosb * cosp + sina * sinb * sinp) - circley * cosa * sinb
      y = circlex * (sinb * cosp - sina * cosb * sinp) + circley * cosa * cosb
      z = K2 + cosa * circlex * sinp + circley * sina
      ooz = 1 / z

      xp = int(screen_width / 2 + K1 * ooz * x)
      yp = int(screen_height / 2 - K1 * ooz * y)

      L = cosp * cost * sinb - cosa * cost * sinp - sina * sint + cosb * (
        cosa * sint - cost * sina * sinp)

      if L > 0:
        if ooz > z_inv[xp, yp]:
          z_inv[xp, yp] = ooz
          luminance_index = int(L * 8)
          output[xp, yp] = ".,-~:;=!*#$@"[luminance_index]
  print('\x1b[?25l')
  # sys.stdout.flush()
  print_donut(output, screen_height, screen_width)


def main(theta_spacing=0.07,
         phi_spacing=0.02,
         R1=1,
         R2=2,
         K2=5,
         screen_width=35,
         screen_height=35):

  K1 = screen_width * K2 * 3 / (8 * (R1 + R2))

  A = 1.0
  B = 1.0
  print('\x1b[2J')

  for i in range(250):
    render(A, B, screen_width, screen_height, theta_spacing, phi_spacing, R1,
           R2, K1, K2)
    A += 0.08
    B += 0.03


main()
