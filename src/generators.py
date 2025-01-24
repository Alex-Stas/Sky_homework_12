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
    pass
