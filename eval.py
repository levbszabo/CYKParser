from cykparser import *

def parse(grammar_filename, filename):
    rules = read_rules(grammar_filename)
    grammar = Grammar(rules)
    cnf_grammar = grammar.get_cnf()

    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        cnf_grammar.parse(line)
        
        #cnf_grammar.print_parse_result(line, log_probs, backpointer, length):
        
def test_arith():
    parse('data/arith.gr', 'data/arith.sen')

def test_wallstreet():
    parse('data/wallstreet.gr', 'data/wallstreet.sen')

if __name__ == '__main__':
    test_arith()
    #test_arith()
    test_wallstreet()
