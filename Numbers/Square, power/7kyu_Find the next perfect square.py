def is_square(num):
  x = num // 2
  seen = set([x])
  while x * x != num:
    x = (x + (num // x)) // 2
    if x in seen: 
        return False
    seen.add(x)
  return True




def find_next_square(num):
    print(num)
    x = num // 2
    seen = set([x])
    while x * x != num:
        x = (x + (num // x)) // 2
        if x in seen: 
            return -1
        seen.add(x)
    return (x + 1) ** 2




def find_next_square(sq):
    # a perfect square must be a sum of a arithmetic sequence by 2
    i = 1
    temp = sq
    while temp > 0: 
        temp -= i
        i += 2
    return sq + i if temp == 0 else -1
