'''
This module generates the HTML and CSS files based on the categorized data.
'''
from jinja2 import Environment, FileSystemLoader
import datetime
def generate_html_css(categorized_data):
    # Load the template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    # Render the template with the categorized data
    output = template.render(categorized_data=categorized_data)
    # Write the output to a file
    with open(f'output_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.html', 'w') as f:
        f.write(output)