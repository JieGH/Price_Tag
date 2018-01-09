while True:
    try:
        print('\n请输入纯数字')

        price = input('商品售价：')

        while True:
            a = input('如果这个商品为组合商品，请输入 a 进行下一步计算；如果不是请按任意键 ')
            if a == 'a':
                net_each = input('  单个含量（以克或者毫升为单位）：')
                quantity = input('  个数')
                net = float(net_each) * float(quantity)
                print('此商品总含量为：' + str(net) + ' 克/毫升')
                break
            else:
                net = input('含量（以克或者毫升为单位）：')
                break

        x = float(price) / float(net) * 500
        print('此商品，每 500 克/毫升：' + str(round(x, 4)) + '元')

    except Exception :
        print('抱歉！你输入的价钱或者含量不为纯数字，或者其他未知错误。')
    keep_running = input('\n请按任意键重新开始，或者输入 b 停止程序。')
    if keep_running == 'b':
        print('程序结束。')
        break
