'''
This file contains the HTMLGenerator class which is responsible for generating the HTML file.
'''
class HTMLGenerator:
    def generate(self, data):
        # Generate the HTML file with efficient data display and appealing output
        html_content = "<html><head><title>Generated HTML</title></head><body>"
        # Add code here to process the data and generate the HTML content
        html_content += "</body></html>"
        # Generate the top menu
        top_menu = "<div class='top-menu'>...</div>"
        html_content = html_content.replace("<!--TOP_MENU-->", top_menu)
        return html_content
    def save_html(self, html_content):
        with open("output.html", "w") as file:
            file.write(html_content)