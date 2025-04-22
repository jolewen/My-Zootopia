import json


def load_json(filepath: str) -> list | dict:
    """Load data from .json file"""
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def extract_single_animal_display_info(animal: dict) -> tuple[str, str, str, str]:
    """Extract information to display in the html about a single animal."""
    _name: str = animal["name"]
    _diet: str = animal.get('characteristics').get('diet')
    _location: str = animal.get('locations')[0]
    _type: str = animal.get('characteristics').get('type')
    return _name, _diet, _location, _type


def serialize_animal_info(animals_data_list: list) -> str:
    """Serialize animals data into html list items.
    Each animal gets its own card item.
    Add some \n and tabs for readability of the html code."""
    output_str = ''
    for animal_dict in animals_data_list:
        _name, _diet, _location, _type = extract_single_animal_display_info(animal_dict)

        output_str += (f'<li class="cards__item">\n'
                       f'\t<div class="card__title">{_name}</div>\n'
                       f'\t<p class="card__text">\n')
        for label, value in [("Diet", _diet), ("Location", _location), ("Type", _type)]:
            if value:
                output_str += f"\t\t<strong>{label}</strong>: {value}<br/>\n"
        output_str += '\t</p>\n</li>\n'

    return output_str


def update_html(filepath: str,
                str_pattern: str = '__REPLACE_ANIMALS_INFO__',
                str_input: str = '',
                output_html: str = 'animals.html') -> None:
    """Read html file at the provided filepath
    and update the given str_pattern with new string input (str_input)"""
    with open(filepath, 'r') as html_file:
        html_content = html_file.read()
    html_content = html_content.replace(str_pattern, str_input)
    with open(output_html, 'w') as html_file:
        html_file.write(html_content)


def main():
    animal_data: list = load_json('animals-data.json')
    animal_str: str = serialize_animal_info(animal_data)
    update_html(filepath='animals_template.html', str_input=animal_str)


if __name__ == '__main__':
    main()