def is_saddle(m, x, y):
  if (m[x][y] > m[x - 1][y] and m[x][y] > m[x + 1][y] and
      m[x][y] < m[x][y + 1] and m[x][y] < m[x][y - 1]
  ) or (
      m[x][y] < m[x - 1][y] and m[x][y] < m[x + 1][y] and
      m[x][y] > m[x][y + 1] and m[x][y] > m[x][y - 1]):
    return True
  else:
    return False


# Time complexity.
# Outer loop is executed n-1 times.
# Inner loop is executed n-1 times.
# TV = (n-2)*(n-2)*8 = O(n^2)
#
# Space complexity.
# S_max = maximum possible number of saddle points ∝ n^2 => S = O(n^2)
# S_min = 1 (0 saddle points -> 1 pointer to empty list)
# S_actual depends on matrix.
def get_saddle_points(m):
  saddles = []

  for i in range(1, len(m) - 1):
    for j in range(1, len(m[i]) - 1):
      if is_saddle(m, i, j):  # at most 8 comparisons in is_saddle
        saddles.append((i, j))

  return saddles


def main():
  m = [
    [1, 2, 3, 4, 5],
    [5, 3, 0, 1, 0],
    [6, 4, 2, 7, 8],
    [5, 7, 5, 4, 2],
    [4, 5, 1, 9, 1]
  ]

  saddle_points = get_saddle_points(m)

  for sdl in saddle_points:
    print(sdl)


main()
