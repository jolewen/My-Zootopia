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


def generate_animals_string(animals_data: list) -> str:
    output_str = ""
    for animal in animals_data:
        output_str += f"Name: {animal.get('name')}\n"
        if animal.get('characteristics').get('diet'):
            output_str += f"Diet: {animal.get('characteristics').get('diet')}\n"
        if animal.get('locations'):
            output_str += f"Location: {animal.get('locations')[0]}\n"
        if animal.get('characteristics').get('type'):
            output_str += f"Type: {animal.get('characteristics').get('type')}\n"
        output_str += '\n'
    return output_str


def update_html(filepath: str,
                str_pattern: str = '__REPLACE_ANIMALS_INFO__',
                str_input: str = '',):
    """Read html file at the provided filepath
    and update the given pattern with new string input"""
    with open(filepath, 'r') as html_file:
        html_content = html_file.read()
    html_content = html_content.replace(str_pattern, str_input)
    with open('animals.html', 'w') as html_file:
        html_file.write(html_content)
    return html_content


def main():
    animal_data = load_json('animals-data.json')
    print_data(animal_data)


if __name__ == '__main__':
    animal_data = load_json('animals-data.json')
    animal_str = generate_animals_string(animal_data)
    print(update_html(filepath='animals_template.html', str_input=animal_str))