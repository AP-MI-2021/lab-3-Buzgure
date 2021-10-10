from typing import List


def show_menu():
    print('1.Citire Date')
    print('2.Cea mai lunga subsecventa in care toate numerele au semne alternative')
    print('3...')
    print('x.Exit')
def read_list() -> List[int]:
    list = []
    list_str = input('Dati numerele separate prin spatiu')
    list_str_split = list_str.split(' ')
    for num_str in list_str_split:
        list.append(int(num_str))
    return list


def different_signs(a, b):
    if a <= 0 and b >=0:
        return True
    elif a >= 0 and b <= 0:
        return True
    else:
        return False

def test_different_signs():
    assert different_signs(-1, 1) == True
    assert different_signs(-1, -1) == False
    assert different_signs(1, 1) == False
    assert different_signs(1, -1) == True

def get_longest_alternating_signs(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga secventa de intregi care au semne diferite
    :param lst: lista de intregi
    :return: result - lista ce contine secventa ceruta
    '''
    n = len(lst)
    max_len = 1
    end_ind = 0
    current_len = 1
    for i in range(1, n):
        if different_signs(lst[i], lst[i - 1]):
            current_len += 1
            if current_len > max_len:
                max_len = current_len
                end_ind = i
        else:
            current_len = 1
    if max_len == 1:
        return None
    result = lst[end_ind - max_len + 1: end_ind + 1]
    return result
def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1, -1, 1]) == [1, -1, 1]
    assert get_longest_alternating_signs([1, 1, 1]) == None
    assert get_longest_alternating_signs([1, -1, 1, -1, -1]) == [1, -1, 1, -1]
    assert get_longest_alternating_signs([1, -1, 1, 2, 3, 4, 5, 6, -1, 2, -3, 4, -5, 6]) == [6, -1, 2, -3, 4, -5, 6]
    assert get_longest_alternating_signs([-1, -1, 1]) == [-1, 1]

def convert_number(n):
    '''
    Converteste un numar dat din baza 10 in baza 2
    Input:
    -n: intreg
    Output:
    -base2Number: lista de string-uri
    '''
    base2Number = []
    while n:
        base2Number.append(str(n%2))
        n = n // 2
    base2Number.reverse()
    return ''.join(base2Number)
def test_convert_number():
    assert convert_number(12) == "1100"





def same_bit(a, b):
    pass
test_convert_number()
def main():
    while True:
        show_menu()
        option = input('Introduceti optiunea: ')
        if option == '1':
            lst = read_list()
        elif option == '2':
            print(get_longest_alternating_signs(lst))
        elif option == '3':
            pass
        elif option == 'x':
            break
        else:
            print('Optiune invalida')
if __name__ == '__main__':
    main()
    test_different_signs()
    test_get_longest_alternating_signs()


