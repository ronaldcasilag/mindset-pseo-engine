import os 
import json
from datetime import datetime

# Ensure directories exist
os.makedirs("content/tools", exist_ok=True)

# Base URL of your live GitHub Pages site
BASE_URL = "https://ronaldcasilag.github.io/mindset-pseo-engine"
today_date = datetime.now().strftime("%Y-%m-%d")

# Load structured matrix data from external JSON file
with open("tools_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

categories = data["categories"]
audiences = data["audiences"]

catalog_items = []
sitemap_urls = [
    f"{BASE_URL}/",
    f"{BASE_URL}/contact.html",
    f"{BASE_URL}/privacy.html",
    f"{BASE_URL}/content/tools/"
]

total_pages_generated = 0

for cat in categories:
    cat_name = cat["name"]
    for prob in cat["problems"]:
        # Generate the base problem page
        pages_to_build = [(prob["slug"], prob["title"], prob["subtitle"], cat_name)]
        
        # Matrix multiply with audiences to create long-tail pSEO pages
        for aud in audiences:
            long_tail_slug = f"{prob['slug']}-{aud['suffix']}"
            long_tail_title = f"{prob['title']} ({aud['label']})"
            long_tail_subtitle = f"{prob['subtitle']} Tailored specifically {aud['label'].lower()}."
            pages_to_build.append((long_tail_slug, long_tail_title, long_tail_subtitle, cat_name))

        for slug, title, subtitle, category in pages_to_build:
            total_pages_generated += 1
            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Mindset pSEO Engine</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 40px 20px; background: #f9fafb; }}
        header {{ background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 30px; }}
        h1 {{ color: #111; margin-top: 0; font-size: 28px; }}
        .badge {{ background: #e0e7ff; color: #3730a3; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600; text-transform: uppercase; }}
        .content {{ background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        .back {{ display: inline-block; margin-bottom: 20px; color: #4f46e5; text-decoration: none; font-weight: 500; }}
        .back:hover {{ text-decoration: underline; }}
        footer {{ margin-top: 40px; text-align: center; color: #6b7280; font-size: 14px; }}
    </style>
</head>
<body>
    <a class="back" href="../index.html">&larr; Back to Tools Catalog</a>
    <header>
        <span class="badge">{category}</span>
        <h1>{title}</h1>
        <p style="color: #4b5563; font-size: 18px; margin-bottom: 0;">{subtitle}</p>
    </header>
    <div class="content">
        <p>High-performers frequently encounter friction when trying to scale their output without burning out. This framework breaks down the exact mechanics required to solve this bottleneck.</p>
        <h2>Key Systems & Execution Steps</h2>
        <ul>
            <li>Audit your current cognitive drag and isolate friction points.</li>
            <li>Implement strict environment and boundary rules to safeguard deep blocks.</li>
            <li>Iterate through execution loops without falling into perfectionism traps.</li>
        </ul>
    </div>
    <footer>
        &copy; 2026 Mindset pSEO Engine. All rights reserved.
    </footer>
</body>
</html>
"""
            file_path = f"content/tools/{slug}.html"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            
            sitemap_urls.append(f"{BASE_URL}/content/tools/{slug}.html")
            
            catalog_items.append(f"""
                <div style="background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 20px;">
                    <span style="background: #e0e7ff; color: #3730a3; padding: 4px 10px; border-radius: 10px; font-size: 11px; font-weight: 600; text-transform: uppercase;">{category}</span>
                    <h2 style="margin: 10px 0 8px 0; font-size: 20px;"><a href="{slug}.html" style="color: #4f46e5; text-decoration: none;">{title}</a></h2>
                    <p style="color: #4b5563; margin: 0; font-size: 15px;">{subtitle}</p>
                </div>
            """)

# Generate catalog page (content/tools/index.html)
catalog_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Programmatic Tools ({total_pages_generated}) | Mindset pSEO Engine</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 40px 20px; background: #f9fafb; }}
        header {{ background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 30px; }}
        h1 {{ color: #111; margin-top: 0; font-size: 28px; }}
        .back {{ display: inline-block; margin-bottom: 20px; color: #4f46e5; text-decoration: none; font-weight: 500; }}
        .back:hover {{ text-decoration: underline; }}
        footer {{ margin-top: 40px; text-align: center; color: #6b7280; font-size: 14px; }}
    </style>
</head>
<body>
    <a class="back" href="../../index.html">&larr; Back to Home</a>
    <header>
        <h1>Programmatic Tool Directory ({total_pages_generated} Systems)</h1>
        <p style="color: #4b5563; margin-bottom: 0;">Explore our complete programmatic directory of automated mindset frameworks and focus systems.</p>
    </header>
    <main>
        {''.join(catalog_items)}
    </main>
    <footer>
        &copy; 2026 Mindset pSEO Engine. All rights reserved.
    </footer>
</body>
</html>
"""

with open("content/tools/index.html", "w", encoding="utf-8") as f:
    f.write(catalog_page)

# Automatically generate sitemap.xml at the repo root
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_xml += f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{today_date}</lastmod>\n  </url>\n"
sitemap_xml += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print(f"Successfully compiled {total_pages_generated} programmatic pSEO pages, catalog, and sitemap.xml.")
