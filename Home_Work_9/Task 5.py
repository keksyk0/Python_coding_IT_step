def process_list (input_list):

    try:
        assert len(input_list) >= 3
        print(f'List consist of {len(input_list)} elements.')
    except AssertionError:
        print("List have to consist of minimum 3 elements!")


input_list_1 = [input('Enter first element:'),
                  input('Enter second element:'),
                  input('Enter third element:')]

process_list(input_list_1)


input_list_2 = [input('Enter first element:'),
                  input('Enter second element:')]

process_list(input_list_2)