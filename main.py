from typing import List


def show_menu():
    print('1.Citire Date')
    print('2.Cea mai lunga subsecventa in care toate numerele au semne alternative')
    print('3. Cea mai lunga subsecventa in care toate numerele au acelasi numar de biti de 1 in reprezentarea binara')
    print('4. Cea mai lunga subsecventa in care toate numerele sunt patrate perfecte')
    print('x.Exit')


def read_list() -> List[int]:
    '''
    Functia de citire a listei
    :return:lista citita
    '''
    list = []
    list_str = input('Dati numerele separate prin spatiu')
    list_str_split = list_str.split(' ')
    for num_str in list_str_split:
        list.append(int(num_str))
    return list


def different_signs(a, b):
    '''
    Determina daca doua numere au semne diferite
    :param a: primul numar
    :param b: al doilea numar
    :return: True daca numerele au semne diferite, respectiv False daca nu
    '''
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


def number_of_set_bits(num):
    '''
    Determina numarul de biti setati ai lui num
    :param num: numarul ai carui biti de 1 urmeaza a fi numarati
    :return: setBits : un counter care determina numarul de biti setati dintr-un numar
    '''
    setBits = 0
    while num:
        bit = num % 2
        num = num // 2
        if bit == 1:
            setBits += 1
    return setBits

def test_number_of_set_bits():
    assert number_of_set_bits(8) == 1
    assert number_of_set_bits(10) == 2
    assert number_of_set_bits(12) == 2
    assert number_of_set_bits(4) == 1


def get_longest_same_bit_counts(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa in care toate numerele au acelasi numar de biti de 1 in reprezentarea binara
    :param lst: lista de intregi pozitivi
    :return: result - lista ce contine subsecventa ceruta
    '''
    n = len(lst)
    max_len = 1
    end_ind = 0
    current_len = 1
    for i in range(1, n):
        if number_of_set_bits(lst[i]) == number_of_set_bits(lst[i - 1]):
            current_len += 1
            if current_len > max_len:
                max_len = current_len
                end_ind = i
        else:
            current_len = 1
    if max_len == 1:
        return lst[0]
    result = lst[end_ind - max_len + 1: end_ind + 1]
    return result

def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([10, 12, 14, 8]) == [10, 12]
    assert get_longest_same_bit_counts([10, 12, 1, 2, 4, 8, 16]) == [1, 2, 4, 8, 16]
    assert get_longest_same_bit_counts([1,10,121]) == 1

def perfect_square(number: int):
    sq = number ** 0.5
    if sq == (int)(sq):
        return True
    return False

def get_longest_all_perfect_squares(lst: List[int]) -> List[int]:
    """
    Determina cea mai lunga subsecventa in care toate numerele sunt oatrate perfecte
    :param lst: lista de intregi pozitivi
    :return: result - lista ce contine subsecventa ceruta
    '''
    """
    result = []
    for left in range(len(lst)):
        for right in range(left, len(lst)):
            all_squares = True
            for num in lst[left:right +1]:
                if perfect_square(num) == False:
                    all_squares = False
                    break
            if all_squares:
                if right - left + 1 > len(result):
                    result = lst[left:right + 1]
    return result

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([25, 36, 4, 1, 8, 7]) == [25, 36, 4, 1]
    assert get_longest_all_perfect_squares([25, 36, 4, 1, 8, 7, 25, 100, 25, 100, 36]) == [25, 100, 25, 100, 36]
    assert get_longest_all_perfect_squares([8, 7]) == []
def main():
    while True:
        show_menu()
        option = input('Introduceti optiunea: ')
        if option == '1':
            lst = read_list()
        elif option == '2':
            print(get_longest_alternating_signs(lst))
        elif option == '3':
            print(get_longest_same_bit_counts(lst))
        elif option == '4':
            print(get_longest_all_perfect_squares(lst))
        elif option == 'x':
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__':
    main()
    test_different_signs()
    test_get_longest_alternating_signs()
    test_number_of_set_bits()
    test_get_longest_same_bit_counts()
    test_get_longest_all_perfect_squares()

