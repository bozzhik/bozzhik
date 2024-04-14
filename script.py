# script.py
from data import tech

def generate_md_file(data):
    md_content = "### What I Work With\n\n<p>\n"

    # [flat, flat-square, plastic, for-the-badge, social]
    tech_style = "flat-square"

    for index, item in enumerate(data):
        name = item[0]
        logo = item[1]
        color = item[2][1:]
        logo_color = item[3][1:]

        md_content += f'  <img alt="{name}" src="https://img.shields.io/badge/{name}-{color}?style={tech_style}&logo={logo}&logoColor={logo_color}" />\n'
        
        if len(item) > 4 and item[4]:
            md_content += "  <br>\n"
        if len(item) > 5 and item[5]:
            md_content += "  <br>\n"

    md_content += "</p>\n\n"

    with open("CONTENT.md", "r") as base_file:
        existing_content = base_file.read()

    md_content += existing_content

    with open("README.md", "w") as file:
        file.write(md_content)

generate_md_file(tech)
