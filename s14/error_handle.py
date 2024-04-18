try:
    print('1) add new record')
    print('2) remove a record')
    print('3) search for a record')
    print('4) show all record')
    while True:
        try:
            c = int(input('enter your choice: '))
            if not (0 < c < 5):
                raise ValueError('your number is not in range')
            break
        except ValueError as e:
            print('----------------------')
            print('Value error')
            print(e)
            print('please enter a valid number.')
            print('----------------------')

except KeyboardInterrupt:
    print('\ngoodbye:)')
