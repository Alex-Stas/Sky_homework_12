def filter_by_currency(list_of_transactions, currency):
    for i in list_of_transactions:
        if i['operationAmount']['currency']['code'] == currency:
            yield i
    yield 'End of Data'


def transaction_descriptions(list_of_transactions):
    for i in list_of_transactions:
        yield i['description']
    yield 'End of Data'




def card_number_generator(start, stop):
    for i in range(start, stop + 1):
        i_str = str(i)
        block_1, block_2, block_3, block_4 = '0000', '0000', '0000', '0000'

        if len(i_str) < 5:
            block_4 = '0' * (4 - len(i_str)) + i_str
        if 4 < len(i_str) < 9:
            block_4 = i_str[-4:]
            block_3 = '0' * (8 - len(i_str)) + i_str[:-4]
        if 8 < len(i_str) < 13:
            block_4 = i_str[-4:]
            block_3 = i_str[-8:-4]
            block_2 = '0' * (12 - len(i_str)) + i_str[:-8]
        if 12 < len(i_str) < 17:
            block_4 = i_str[-4:]
            block_3 = i_str[-8:-4]
            block_2 = i_str[-12:-8]
            block_1 = '0' * (16 - len(i_str)) + i_str[:-12]

        yield f'{block_1} {block_2} {block_3} {block_4}'
