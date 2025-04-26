import json


def load_json(filepath: str) -> list | dict:
    """Load data from .json file"""
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def _get_available_skin_types(animal_data:list) -> set:
    """Private method to get available skin types from the animal data."""
    skin_types = set()
    for animal in animal_data:
        if animal['characteristics'].get('skin_type'):
            skin_types.add(animal['characteristics'].get('skin_type'))
    return skin_types

def extract_single_animal_display_info(animal: dict) -> tuple[str, dict]:
    """Extract information to display in the html about a single animal.
    The animal must have a name and the categories 'characteristics', 'locations',
    and 'taxonomy', which can have additional information to be displayed."""
    name: str = animal['name']
    _diet: str = animal['characteristics'].get('diet')
    _location: str = animal['locations'][0]
    _type: str = animal['characteristics'].get('type')
    _scientific_name: str = animal['taxonomy'].get('scientific_name')
    _skin_type: str = animal['characteristics'].get('skin_type')

    displayed_animal_info = {'Diet': _diet,
                             'Location': _location,
                             'Type': _type,
                             'Skin Type': _skin_type,
                             'Scientific Name': _scientific_name}

    return name, displayed_animal_info


def serialize_animal_info(animals_data_list: list) -> str:
    """Serialize animals data into html list items.
    Each animal gets its own card item.
    Add some \n and tabs for readability of the html code."""
    output_str = ''
    skin_type_filter = input(f'Filter animals for skin type '
                             f'{_get_available_skin_types(animals_data_list)} '
                             f'or press ENTER: ').lower()
    for animal_dict in animals_data_list:
        _name, _animal_info = extract_single_animal_display_info(animal_dict)
        if (skin_type_filter!= ''
                and _animal_info['Skin Type'].lower() != skin_type_filter):
            continue
        output_str += (f'<li class="cards__item">\n'
                       f'\t<div class="card__title">{_name}</div>\n'
                       f'\t<div class="card__text">\n'
                       f'\t\t<ul>\n')
        for label, value in _animal_info.items():
            if value:
                output_str += f"\t\t\t<li><strong>{label}</strong>: {value}</li>\n"
        output_str += '\t\t</ul>\n\t</div>\n</li>\n'

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
