from jinja2 import Environment, FileSystemLoader
import markdown
import yaml

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('employee-nda.md')

# Load data from the YAML file
with open('info.yml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Render the template with the data
rendered_content = template.render(data)

# Convert the rendered content from Markdown to HTML
html_content = markdown.markdown(rendered_content)

print(html_content)