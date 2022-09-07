import random

test_seed = int(input('crate a seed number:'))

random.seed(test_seed)

random_silde = random.randint(0, 1)

if random_silde == 1:
  print('heads')
else:
  print('tails')