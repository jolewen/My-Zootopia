import json

def load_json(filepath):
    """Load data from .json file"""
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def print_data(animals):
    """Print data to console"""
    for animal in animals:
        print(f"Name: {animal.get('name')}")
        if animal.get('characteristics').get('diet'):
            print(f"Diet: {animal.get('characteristics').get('diet')}")
        if animal.get('locations'):
            print(f"Location: {animal.get('locations')[0]}")
        if animal.get('characteristics').get('type'):
            print(f"Type: {animal.get('characteristics').get('type')}")
        print()


if __name__ == '__main__':
    animal_data = load_json('animals-data.json')
    print_data(animal_data)
