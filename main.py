import random, sys
try:
    password_length = int(sys.argv[1])
    print(''.join(random.choice("abcdefghjkmnpqrstuvwxyz123456789ABCDEFGHJKLMNPQRSTUVWXYZ!?#$%&*()") for _ in range(password_length)))
except IndexError as ie:
    print(''.join(random.choice("abcdefghjkmnpqrstuvwxyz123456789ABCDEFGHJKLMNPQRSTUVWXYZ!?#$%&*()") for _ in range(12)))
