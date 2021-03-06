def initial_transform(data):
    for item in list(data):
        if type(item) is dict:
            for key in item:
                data[key] = item[key]

    return data


def final_transform(tfd_data):
    tfd_data['address'] = str.format(
        '{0}\n{1}, {2} {3}', tfd_data['street'],
        tfd_data['state'], tfd_data['city'],
        tfd_data['zip']
    )

    return tfd_data


def print_person(person_data):
    parents = "and".join(person_data['parents'])
    siblings = "and".join(person_data['siblings'])
    person_string = str.format(
        "Hello, my name is {0}, my siblings are {1}, "
        "my parents are {2}, and my mailing"
        "address is: \n{3}", person_data['name'],
        parents, siblings, person_data['address']
    )
    print(person_string)


JOHN_DATA = {
    'name': 'John Q. Public',
    'street': '123 Main St.',
    'city': 'Anytown',
    'state': 'FL',
    'zip': 99999,
    'relationships': {
        'siblings': ['Michael R. Public', 'Suzy Q. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
    }
}

SUZY_DATA = {
    'name': 'Suzy Q. Public',
    'street': '456 Broadway',
    'apt': '333',
    'city': 'Miami',
    'state': 'FL',
    'zip': 33333,
    'relationships': {
        'siblings': ['John Q. Public', 'Michael R. Public',
                     'Thomas Z. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
    }
}

inputs = [JOHN_DATA, SUZY_DATA]

for input_struc in inputs:
    initial_transformed = initial_transform(input_struc)
    final_transformed = final_transform(initial_transformed)
    print_person(final_transformed)
