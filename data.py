# data.py
colors = {
    "white": "#FFF",
    "black": "#000",
    "gray": "#333",
    "yellow": "#FFE825",
    "blue": "#007ACC",
    "html": "#FC613B",
    "redux": "#764ABC",
    "astro": "#2a233e",
    "node": "#43853d",
    "heroku": "#430098",
    "insomnia": "#5849BE",
    "graph": "#E10098",
    "sass": "#CC6699",
    "git": "#F05032",
    "npm": "#CB3837",
    "postgresql": "#316192",
}

default_logo_color = colors["white"]

tech = [
    ["JavaScript", "javascript", colors["yellow"], colors.get("black", default_logo_color)],
    ["TypeScript", "typescript", colors["blue"], default_logo_color],
    ["HTML", "html5", colors["html"], default_logo_color],
    ["CSS", "css3", colors["blue"], default_logo_color],
    ["SASS", "sass", colors["sass"], default_logo_color],
    ["Tailwind", "tailwindcss", colors["blue"], default_logo_color],
    ["Styled Components", "styled-components", colors["sass"], default_logo_color, True],

    ["React", "react", colors["blue"], default_logo_color],
    ["Redux", "redux", colors["redux"], default_logo_color],
    ["NextJS", "next.js", colors["gray"], default_logo_color],
    ["NodeJS", "node.js", colors["node"], default_logo_color],
    ["NestJS", "nestjs", colors["npm"], default_logo_color],
    ["Astro", "astro", colors["astro"], default_logo_color],
    ["npm", "npm", colors["npm"], default_logo_color],
    ["Three.js", "three.js", colors["yellow"], colors.get("black", default_logo_color)],
    ["Swiper.js", "swiper", colors["blue"], default_logo_color, True],

    ["Vite", "vite", colors["insomnia"], default_logo_color],
    ["Webpack", "webpack", colors["blue"], default_logo_color],
    ["Vercel", "vercel", colors["gray"], default_logo_color],
    ["Heroku", "heroku", colors["heroku"], default_logo_color],
    ["Docker", "docker", colors["blue"], default_logo_color, True, True],

    ["git", "git", colors["git"], default_logo_color],
    ["Github Actions", "github-actions", colors["heroku"], default_logo_color],
    ["PostgreSQL", "postgresql", colors["postgresql"], default_logo_color],
    ["SQLite", "sqlite", colors["blue"], default_logo_color],
    ["MongoDB", "mongodb", colors["node"], default_logo_color],
    ["SanityCMS", "sanity", colors["npm"], default_logo_color],
    ["Axios", "axios", colors["astro"], default_logo_color],
    ["GraphQL", "graphql", colors["graph"], default_logo_color, True],
    
    ["Python", "python", colors["blue"], default_logo_color],
    ["Ruby", "ruby", colors["npm"], default_logo_color],
    ["Ruby on Rails", "rubyonrails", colors["npm"], default_logo_color],
    ["gem", "rubygems", colors["npm"], default_logo_color],
]
