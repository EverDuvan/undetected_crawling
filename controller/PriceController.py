def clean_price_principal(price, symbol):
    final_price = '0.0'
    price = get_number_price(price, symbol).replace(',', '.').strip()
    if price == None or price == '' or price == '0.0':
        final_price = '0.0'
    else:
        price_aux = price.split('.')
        price_temporal = ''
        flag = False

        con = 0
        while con < len(price_aux):
            if len(price_aux[con]) != 2 or con == 0:
                price_temporal += price_aux[con]
            elif con != 0:
                price_temporal += "." + price_aux[con]
                if price_aux.pop() == '0' and price_aux[con] == '00':
                    flag = True
            con += 1
        final_price = symbol + ' ' + price_temporal
        # double p = Double.parseDouble(price_temporal)
        # DecimalFormat formato = new DecimalFormat("#,###.###")
        #final_value = formato.format(p)
        if flag:
            final_price += "0"
    return final_price


def clean_price(price, symbol):
    final_price = ''
    price = get_number_price(price, symbol)
    if price == None or price == '' or price == '0.0' or len(price) > 10:
        final_price = '0.0'
    else:
        centinel = False
        sub_price = ''
        point = 0

        symbol = symbol.strip()
        price = price.strip()

        if ',' in price:
            price = price.replace(',', '')
        if '.' in price:
            sub_price = "." + price.split('.')[1]
            price = price.split('.')[0]
            if sub_price == '.00' or sub_price == '.0':
                sub_price = ''
        price = price.strip()
        if len(price) == 4:
            point = 0
            centinel = True
        elif len(price) == 5:
            point = 1
            centinel = True
        elif len(price) == 6:
            point = 2
            centinel = True
        elif len(price) == 7:
            point = 3
            centinel = True
        for i in price:
            final_price += i
            if centinel and i == point:
                final_price += ','
        final_price = symbol + ' ' + final_price + sub_price
    return final_price


def get_number_price(price, symbol):
    print(price)
    if symbol in price:
        price = price.replace(symbol, '')
    new_price = "".join([ele for ele in price if ele.isdigit() or ',' or '.'])
    return new_price
