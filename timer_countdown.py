

def countdown(t):
    import time
    print('Countdown in', t,"seconds")
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('Blastoff! \n \n \n \n \n')


countdown(5)
