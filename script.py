def generate_md_file(data):
    md_content = "### Things I code with\n\n<p>\n"
    
    for item in data:
        alt_text = item['alt_text']
        name = item['name']
        color = item['color']
        logo = item['logo']
        logo_color = item['logo_color']
        
        md_content += f'  <img alt="{alt_text}" src="https://img.shields.io/badge/{name}-{color}?style=flat-square&logo={logo}&logoColor={logo_color}" />\n'

    md_content += "</p>\n\n"

    with open("CONTENT.md", "r") as base_file:
        existing_content = base_file.read()

    md_content += existing_content

    with open("README.md", "w") as file:
        file.write(md_content)

data = [
    {
        "alt_text": "JavaScript",
        "name": "JavaScript",
        "color": "FFE825",
        "logo": "javascript",
        "logo_color": "black"
    },
    {
        "alt_text": "TypeScript",
        "name": "TypeScript",
        "color": "007ACC",
        "logo": "typescript",
        "logo_color": "white"
    },
]

generate_md_file(data)
