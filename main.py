from application.check_sequence import is_balanced_sequence


def main(sequences):
    balanced = 'сбалансированная последовательность'
    unbalanced = 'несбалансированная последовательность'
    [print(f'{sequence} - {balanced}') if is_balanced_sequence(sequence)
     else print(f'{sequence} - {unbalanced}') for sequence in sequences]


if __name__ == '__main__':
    sequences_for_chek = ['(((([{}]))))',
                          '[([])((([[[]]])))]{()}',
                          '{{[()]}}',
                          '}{}',
                          '{{[(])]}}',
                          '[[{())}]']
    main(sequences_for_chek)
