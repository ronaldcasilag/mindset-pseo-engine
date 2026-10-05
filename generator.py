import os
import json

os.makedirs("content/tools", exist_ok=True)

# Load data from external JSON file for effortless scaling
with open("tools_data.json", "r", encoding="utf-8") as f:
    tools_data = json.load(f)

catalog_items = []

for tool in tools_data:
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tool['title']} | Mindset pSEO Engine</title>
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
        <span class="badge">{tool['category']}</span>
        <h1>{tool['title']}</h1>
        <p style="color: #4b5563; font-size: 18px; margin-bottom: 0;">{tool['subtitle']}</p>
    </header>
    <div class="content">
        {tool['content']}
    </div>
    <footer>
        &copy; 2026 Mindset pSEO Engine. All rights reserved.
    </footer>
</body>
</html>
"""
    
    file_path = f"content/tools/{tool['slug']}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    catalog_items.append(f"""
        <div style="background: #fff; padding: 24px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 20px;">
            <span style="background: #e0e7ff; color: #3730a3; padding: 4px 10px; border-radius: 10px; font-size: 11px; font-weight: 600; text-transform: uppercase;">{tool['category']}</span>
            <h2 style="margin: 10px 0 8px 0; font-size: 20px;"><a href="{tool['slug']}.html" style="color: #4f46e5; text-decoration: none;">{tool['title']}</a></h2>
            <p style="color: #4b5563; margin: 0; font-size: 15px;">{tool['subtitle']}</p>
        </div>
    """)

catalog_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Programmatic Tools | Mindset pSEO Engine</title>
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
        <h1>Programmatic Tool Directory</h1>
        <p style="color: #4b5563; margin-bottom: 0;">Explore our complete directory of automated mindset frameworks and focus systems.</p>
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

print(f"Successfully compiled {len(tools_data)} pages from JSON data.")
