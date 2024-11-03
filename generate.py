import argparse
import os
from datetime import datetime

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

# Get the current date
current_date = datetime.now()

def get_formatted_githash():
    # Get the Git hash of the current commit
    git_hash = os.popen('git rev-parse HEAD').read().strip()
    return git_hash[:19]
def generate_document(template_file_path):
    # the info file is called info.yml and is in the same dir as the template_file_path
    info_file_path = os.path.join(os.path.dirname(template_file_path), 'info.yml')

    # Load data from the YAML file
    with open(info_file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    # format dates from the date list if there are any dates in the yml
    if 'dates' in data:
        for date in data['dates']:
            # get date key
            date_key = list(date.keys())[0]
            data[date_key] = datetime.fromisoformat(date[date_key].replace("Z", "+00:00"))

    # use the githash to track document verison
    data['githash'] = get_formatted_githash()

    # format text-based dates
    # Format the day
    day = current_date.strftime('%d')
    if day.endswith('1') and day != '11':
        day += 'st'
    elif day.endswith('2') and day != '12':
        day += 'nd'
    elif day.endswith('3') and day != '13':
        day += 'rd'
    else:
        day += 'th'

    # Format the month
    month = current_date.strftime('%B')

    # Format the year
    year = current_date.strftime('%Y')

    # Add the formatted date data to the existing YAML data
    data['day'] = day
    data['month'] = month
    data['year'] = year

    # load the template into jinja
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file_path)
    # Render the template with the data
    rendered_content = template.render(data)
    return rendered_content


def main():
    parser = argparse.ArgumentParser(description="Generate document from info.yml")

    parser.add_argument(
        'file_paths',
        nargs='+',
        help='List of file paths to be merged into contract.',
        type=str,
        default=None
    )

    args = parser.parse_args()

    # create an empty string to store the contract in
    rendered_contract = ""
    for file_path in args.file_paths:
        # render the document and add it to the contract
        rendered_contract += generate_document(file_path) + "\n"

    # convert the string to md object and save as md html
    html_content = markdown.markdown(rendered_contract)

    # Create the dist directory if it doesn't exist
    if not os.path.exists('dist'):
        os.makedirs('dist')

    # Save the HTML content to a file in the dist folder
    with open('dist/output.html', 'w') as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    main()
