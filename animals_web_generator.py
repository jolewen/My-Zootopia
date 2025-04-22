import json


def load_json(filepath):
    """Load data from .json file"""
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def generate_animals_string(animals_data: list) -> str:
    """Generate a structured string as one html list item per animal."""
    output_str = ""
    for animal in animals_data:
        _name = animal["name"]
        _diet = animal.get('characteristics').get('diet')
        _location = animal.get('locations')[0]
        _type = animal.get('characteristics').get('type')

        output_str += (f'<li class="cards__item">\n'
                       f'<div class="card__title">{_name}</div>\n'
                       f'<p class="card__text">\n')

        if _diet:
            output_str += f"<strong>Diet</strong>: {_diet}<br/>\n"
        if _location:
            output_str += f"<strong>Location</strong>: {_location}<br/>\n"
        if _type:
            output_str += f"<strong>Type</strong>: {_type}<br/>\n"
        output_str += '</p></li>\n'
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


def main():
    animal_data = load_json('animals-data.json')
    animal_str = generate_animals_string(animal_data)
    update_html(filepath='animals_template.html', str_input=animal_str)


if __name__ == '__main__':
    main()