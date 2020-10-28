
def friend_name(friend: dir):
    return (friend["name"])


def search_element(sequence, expected_element, function):
    for element in sequence:
        name = function(element)
        if name == expected_element:
            return print(name)
    raise RuntimeError('element not found')


friends = [{"name":"Bob", "age":34}, {"name":"Martha", "age":34}, {"name":"Alice", "age":29}, {"name":"Steven", "age":33}, {"name":"Julia", "age":30}, {"name":"Martin", "age":24}]

#for friend in friends:
   # friend_name(friend)


try:
    search_element(expected_element = "Anna",
                   sequence = friends,
                   function=friend_name)
except RuntimeError:
    print ('element not found')

