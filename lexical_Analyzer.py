import re
def lexical_analyzer(exp):
    # Define regular expressions for identifiers, constants, operators, punctuator and special character
    identifier_regex =  r'[A-Z]|[a-z]'
    operator_regex = r'[+-/*=<>!%&|^~]'
    constants_regex = r'[0-9]'
    punctuator_regex = r'[,;:.()\[\]{}]'
    special_characters_regex = r'[$#@!%^&*<>?/\'\"|~`]'

    # passing expression to text vaiable
    text = exp
    
    # matching expression with regexs  using re library
    print("\n*********** Lexical Analyzer ***************")
    for c in text:
        if re.match(identifier_regex, c):
            print(f'{c} = Identifier')
        elif re.match(operator_regex, c):
            print(f'{c} = Operator')
        elif re.match(constants_regex, c):
            print(f'{c} = Constant')
        elif re.match(punctuator_regex, c):
            print(f'{c} = Punctuators')
        elif re.match(special_characters_regex, c):
            print(f'{c} = Special charater')
        else:
            pass
    print("********************************************\n")


if __name__ == "__main__":
    exp = "a+(b*c  )"
    lexical_analyzer(exp)



