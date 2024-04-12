from jinja2 import Environment, FileSystemLoader
import markdown
import yaml
import os
from datetime import datetime

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('employee-nda.md')

# Load data from the YAML file
with open('info.yml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Get the current date
current_date = datetime.now()

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

# Render the template with the data
rendered_content = template.render(data)

# Convert the rendered content from Markdown to HTML
html_content = markdown.markdown(rendered_content)

# Create the dist directory if it doesn't exist
if not os.path.exists('dist'):
    os.makedirs('dist')

# Save the HTML content to a file in the dist folder
with open('dist/output.html', 'w') as html_file:
    html_file.write(html_content)