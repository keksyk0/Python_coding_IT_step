def process_list (input_list):
    assert len(input_list) >= 3, \
        "List have to consist of minimum 3 elements!"
    print(f'List consist of {len(input_list)} elements.')


input_list_1 = [input('Enter first element:'),
                  input('Enter second element:'),
                  input('Enter third element:')]

process_list(input_list_1)


input_list_2 = [input('Enter first element:'),
                  input('Enter second element:')]

process_list(input_list_2)