def is_valid_identifier(input_string):
    # 1. Helper function to categorize our "alphabet"
    def get_char_type(char):
        if char.isalpha():
            return 'LETTER'
        elif char.isdigit():
            return 'DIGIT'
        else:
            return 'OTHER'

    # 2. The Transition Table
    # Maps (current_state, input_category) -> next_state
    transitions = {
        ('START', 'LETTER'): 'IDENTIFIER',
        ('START', 'DIGIT'): 'ERROR',
        ('START', 'OTHER'): 'ERROR',
        
        ('IDENTIFIER', 'LETTER'): 'IDENTIFIER',
        ('IDENTIFIER', 'DIGIT'): 'IDENTIFIER',
        ('IDENTIFIER', 'OTHER'): 'ERROR',
        
        # Once in the ERROR state, you can never leave (a "dead" state)
        ('ERROR', 'LETTER'): 'ERROR',
        ('ERROR', 'DIGIT'): 'ERROR',
        ('ERROR', 'OTHER'): 'ERROR',
    }

    # 3. Setup the machine
    current_state = 'START'
    accept_states = {'IDENTIFIER'}

    # 4. Run the machine over the input
    for char in input_string:
        char_type = get_char_type(char)
        
        # Look up the next state in our dictionary.
        # If the exact transition is missing, default to 'ERROR'.
        current_state = transitions.get((current_state, char_type), 'ERROR')

    # 5. Did we end up in an accepting state?
    return current_state in accept_states

# --- Testing the FSA ---
test_strings = ["Query1", "1stQuery", "Data_Set", "x", "Devin67"]

for test in test_strings:
    result = is_valid_identifier(test)
    print(f"'{test}': {result}")