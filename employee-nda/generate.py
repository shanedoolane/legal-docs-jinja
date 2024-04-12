from jinja2 import Environment, FileSystemLoader
import markdown
import yaml
import os

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('employee-nda.md')

# Load data from the YAML file
with open('info.yml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

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