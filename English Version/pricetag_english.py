while True:
    try:
        print('\nPlease input number only')

        price = input('The price of the product: ')

        while True:
            a = input('If this product include multiple packages, please input a to provide more information, '
                      'else press enter to continue. ')
            if a == 'a':
                net_each = input('  The net content of each package：')
                quantity = input('  Quantity: ')
                net = float(net_each) * float(quantity)
                print('The overall net content of this product is：' + str(net) + ' g/ml')
                break
            else:
                net = input('The net content of this product：')
                break

        x = float(price) / float(net) * 500
        print('This product is: \n' + str(round(x, 4)) + ' £/$/€/¥ per 500 g/ml.')

    except Exception:
        print('\nSorry, please input number only. Or an unknown error occurred.')
    keep_running = input('Input any keys to continue or input b to exit the program ')
    if keep_running == 'b':
        print('')
        break
