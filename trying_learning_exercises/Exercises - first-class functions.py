def search_element(sequence, expected_element):
    for element in sequence:
        if element == expected_element:
            return print(element)
    raise RuntimeError('element not found')


friends = [{"name":"Bob", "age":34}, {"name":"Martha", "age":34}, {"name":"Alice", "age":29}, {"name":"Steven", "age":33}, {"name":"Julia", "age":30}, {"name":"Martin", "age":24}]

friends_names = []
for friend in friends:
    friends_names.append(friend["name"])
    

try:
    search_element(expected_element = "Julia", sequence = friends_names)
except RuntimeError:
    print ('element not found')

