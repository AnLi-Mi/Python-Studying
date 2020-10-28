def search_element(sequence, expected_element):
    for element in sequence:
        if element == expected_element:
            return print(element)
    #raise RuntimeError('element not found')


friends = ("Bob", "Martha", "Alice", "Steven", "Julia", "Martin")


try:
    search_element(expected_element = "Julia", sequence = friends)
except RuntimeError:
    print ('element not found')

