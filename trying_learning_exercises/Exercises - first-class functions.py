
def friend_name(friend: dir)-> str:
    return (friend["name"])


def search_element(sequence, expected_element, function)-> str:
    for element in sequence:
        if function(element) == expected_element:
            return print(f'{element} is in the given sequence')
    raise RuntimeError('element not found')


friends = [{"name":"Bob", "age":34}, {"name":"Martha", "age":34}, {"name":"Alice", "age":29}, {"name":"Steven", "age":33}, {"name":"Julia", "age":30}, {"name":"Martin", "age":24}]

#for friend in friends:
   # friend_name(friend)


try:
    search_element(expected_element = "Alice",
                   sequence = friends,
                   function=friend_name)
except RuntimeError:
    print ('element not found')

# ----------using lambda as the function argument -----

try:
    search_element(expected_element = "Steven",
                   sequence = friends,
                   function = lambda friend: friend["name"])
except RuntimeError:
    print ('element not found')

