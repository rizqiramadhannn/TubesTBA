import string
def lexical(sentence):
    print("=================== Lexical Analyzer ===================")
    input_string = sentence.lower()+'#'

    # initialization
    alphabet_list = list(string.ascii_lowercase)
    state_list = {
        'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9',
        'q10','q11','q12','q13','q14','q15','q16','q17','q18','q19',
        'q20','q21','q22','q23','q24','q25','q26','q27','q28','q29',
        'q30','q31','q32','q33','q34','q35','q36','q37','q38','q39',
        'q40','q41'
    }

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    # space before input string
    transition_table['q0', ' '] = 'q0'

    # update the transition table for the following token: il & ils
    transition_table['q0', 'i'] = 'q1'
    transition_table['q1', 'l'] = 'q2'
    transition_table['q2', ' '] = 'q41'
    transition_table['q2', '#'] = 'accept'
    transition_table['q2', 's'] = 'q40'
    transition_table['q40', ' '] = 'q41'
    transition_table['q40', '#'] = 'accept'
    transition_table['q41', ' '] = 'q41'
    transition_table['q41', '#'] = 'accept'

    # update the transition table for the following token: je
    transition_table['q0', 'j'] = 'q3'
    transition_table['q3', 'e'] = 'q40'

    # update the transition table for the following token: jouer
    transition_table['q3', 'o'] = 'q4'
    transition_table['q4', 'u'] = 'q13'
    transition_table['q13', 'e'] = 'q14'
    transition_table['q14', 'r'] = 'q40'

    # update the transition table for the following token: manger
    transition_table['q0', 'm'] = 'q5'
    transition_table['q5', 'a'] = 'q6'
    transition_table['q6', 'n'] = 'q7'
    transition_table['q7', 'g'] = 'q13'

    # update the transition table for the following token: aimer
    transition_table['q0', 'a'] = 'q8'
    transition_table['q8', 'i'] = 'q9'
    transition_table['q9', 'm'] = 'q13'

    # update the transition table for the following token: porter
    transition_table['q0', 'p'] = 'q10'
    transition_table['q10', 'o'] = 'q11'
    transition_table['q11', 'r'] = 'q12'
    transition_table['q12', 't'] = 'q13'

    # update the transition table for the following token: des oeuf
    transition_table['q0', 'd'] = 'q15'
    transition_table['q15', 'e'] = 'q16'
    transition_table['q16', 's'] = 'q17'
    transition_table['q17', ' '] = 'q18'
    transition_table['q18', 'o'] = 'q19'
    transition_table['q19', 'e'] = 'q20'
    transition_table['q20', 'u'] = 'q21'
    transition_table['q21', 'f'] = 'q40'

    # update the transition table for the following token: les toilettes
    transition_table['q0', 'l'] = 'q22'
    transition_table['q22', 'e'] = 'q23'
    transition_table['q23', 's'] = 'q24'
    transition_table['q24', ' '] = 'q25'
    transition_table['q25', 't'] = 'q26'
    transition_table['q26', 'o'] = 'q27'
    transition_table['q27', 'i'] = 'q28'
    transition_table['q28', 'l'] = 'q29'
    transition_table['q29', 'e'] = 'q30'
    transition_table['q30', 't'] = 'q31'
    transition_table['q31', 't'] = 'q32'
    transition_table['q32', 'e'] = 'q33'
    transition_table['q33', 's'] = 'q40'

    # update the transition table for the following token: la table
    transition_table['q22', 'a'] = 'q34'
    transition_table['q34', ' '] = 'q35'
    transition_table['q35', 't'] = 'q36'
    transition_table['q36', 'a'] = 'q37'
    transition_table['q37', 'b'] = 'q38'
    transition_table['q38', 'l'] = 'q39'
    transition_table['q39', 'e'] = 'q40'

    # transition for new token
    transition_table['q41', 'i'] = 'q1'
    transition_table['q41', 'j'] = 'q3'
    transition_table['q41', 'm'] = 'q5'
    transition_table['q41', 'a'] = 'q8'
    transition_table['q41', 'p'] = 'q10'
    transition_table['q41', 'd'] = 'q15'
    transition_table['q41', 'l'] = 'q22'

    # lexical analysis
    idx_char = 0
    state = 'q0'
    current_token = ' '
    final_state = ['q2', 'q40']
    
    result = []
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state in final_state:
            print('current token:', current_token,', valid')
            current_token = ''
        if state == 'error':
            print('error')
            break;
        idx_char = idx_char + 1
    # conclusion
    if state == 'accept':
        print('semua token di input: ', sentence, ', valid')
        return sentence
    else:
        return ""
    
def parser(sentence):
    print("======================== Parser ========================")
    print("Kalimat =", sentence)
    # input example
    tokens = sentence.lower().split()
    for i in range(len(tokens)-1):
        if (tokens[i] == "les" or tokens[i] == "la" or tokens[i] == "des"):
            tokens[i] = tokens[i] + " " + tokens[i+1]
            j = i
            while j < i-1:
                tokens[j] = tokens[j+1]
                j += 1
            del tokens[j+1]
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



sentence = input("masukan sebuah kalimat: ")
tokens = lexical(sentence)
if tokens != "":
    parser(tokens)
else:
    print("karena lexical error, parser tidak dapat dijalankan")