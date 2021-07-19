# input example
sentence = input("Masukan Kalimat: ")
tokens = sentence.lower().split()
for i in range(len(tokens)-1):
    if tokens[i] == "les" or tokens[i] == "la" or tokens[i] == "des":
        tokens[i] = tokens[i] + " " + tokens[i+1]
        j = i
        while j < i-1:
            tokens[j] = tokens[j+1]
            j += 1
        del tokens[j+1]

print(tokens)
tokens.append('EOS')

# sumbols definition
non_terminals = ['S', 'SB', 'VB', 'OB']
terminals = ['je', 'il', 'ils', 'manger', 'aimer', 'porter', 'jouer', 'des oeuf', 'la table', 'les toilettes']

# symbols table definition
parse_table = {}

parse_table[('S', 'je')] = ['SB', 'VB', 'OB']
parse_table[('S', 'il')] = ['SB', 'VB', 'OB']
parse_table[('S', 'ils')] = ['SB', 'VB', 'OB']
parse_table[('S', 'manger')] = ['error']
parse_table[('S', 'aimer')] = ['error']
parse_table[('S', 'porter')] = ['error']
parse_table[('S', 'jouer')] = ['error']
parse_table[('S', 'des oeuf')] = ['error']
parse_table[('S', 'la table')] = ['error']
parse_table[('S', 'les toilettes')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('SB', 'je')] = ['je']
parse_table[('SB', 'il')] = ['il']
parse_table[('SB', 'ils')] = ['ils']
parse_table[('SB', 'manger')] = ['error']
parse_table[('SB', 'aimer')] = ['error']
parse_table[('SB', 'porter')] = ['error']
parse_table[('SB', 'jouer')] = ['error']
parse_table[('SB', 'des oeuf')] = ['error']
parse_table[('SB', 'la table')] = ['error']
parse_table[('SB', 'les toilettes')] = ['error']
parse_table[('SB', 'EOS')] = ['error']

parse_table[('VB', 'je')] = ['error']
parse_table[('VB', 'il')] = ['error']
parse_table[('VB', 'ils')] = ['error']
parse_table[('VB', 'manger')] = ['manger']
parse_table[('VB', 'aimer')] = ['aimer']
parse_table[('VB', 'porter')] = ['porter']
parse_table[('VB', 'jouer')] = ['jouer']
parse_table[('VB', 'des oeuf')] = ['error']
parse_table[('VB', 'la table')] = ['error']
parse_table[('VB', 'les toilettes')] = ['error']
parse_table[('VB', 'EOS')] = ['error']

parse_table[('OB', 'je')] = ['error']
parse_table[('OB', 'il')] = ['error']
parse_table[('OB', 'ils')] = ['error']
parse_table[('OB', 'manger')] = ['error']
parse_table[('OB', 'aimer')] = ['error']
parse_table[('OB', 'porter')] = ['error']
parse_table[('OB', 'jouer')] = ['error']
parse_table[('OB', 'des oeuf')] = ['des oeuf']
parse_table[('OB', 'la table')] = ['la table']
parse_table[('OB', 'les toilettes')] = ['les toilettes']
parse_table[('OB', 'EOS')] = ['error']

# stack initialization
stack = []
stack.append('#')
stack.append('S')

# input reading initialization
idx_token = 0
symbol = tokens[idx_token]

# parsing process
while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top = ', top)
    print('symbol = ', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                print('isi stack:', stack)
                stack.pop()
        else:
            print('error')
            break;
    elif top in non_terminals:
        print('top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('error')
            break;
    else:
        print('error')
        break;
    print('isi stack:', stack)
    print()

# conclusion
print()
if symbol == 'EOS' and len(stack) == 0:
    print('Input string ', sentence, ' diterima,  sesuai Grammar')
else:
    print('Error, input string:', sentence, ', tidak diterima, tidak sesuai Grammar')

