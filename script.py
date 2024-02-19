from data import tech

def generate_md_file(data):
    md_content = "### What I Work With\n\n<p>\n"

    # [flat, flat-square, plastic, for-the-badge, social]
    tech_style = "flat-square"

    for index, item in enumerate(data):
        alt_text = item['alt_text']
        name = item['name']
        logo = item['logo']
        color = item['color'][1:]
        logo_color = item['logo_color'][1:]

        md_content += f'  <img alt="{alt_text}" src="https://img.shields.io/badge/{name}-{color}?style={tech_style}&logo={logo}&logoColor={logo_color}" />\n'
        
        if "insert_br" in item and index != len(data) - 1:
            md_content += "  <br>\n"
        if "insert_2br" in item and index != len(data) - 1:
            md_content += "  <br>\n"
            md_content += "  <br>\n"

    md_content += "</p>\n\n"

    with open("CONTENT.md", "r") as base_file:
        existing_content = base_file.read()

    md_content += existing_content

    with open("README.md", "w") as file:
        file.write(md_content)

generate_md_file(tech)