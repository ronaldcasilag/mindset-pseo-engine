import os
import datetime
import requests

def fetch_live_tools():
    """
    Fetches real productivity and software tools from an open API.
    You can replace this endpoint later with the Product Hunt API or a custom list.
    """
    print("Fetching live tools from external source...")
    try:
        # Example: Fetching free public tech/software entries from a public API
        response = requests.get("https://api.github.com/repositories?q=topic:productivity&sort=stars", timeout=10)
        if response.status_code == 200:
            items = response.json().get("items", [])[:3] # Grab top 3 trending tools
            tools = []
            for item in items:
                tools.append({
                    "name": item.get("name", "Productivity Tool"),
                    "tagline": item.get("description") or "Boost your workflow and overcome daily resistance.",
                    "url": item.get("html_url", "https://github.com")
                })
            return tools
    except Exception as e:
        print(f"API fetch failed ({e}), falling back to curated dynamic list.")
        
    # Safe fallback if API rate limits or fails
    today_str = datetime.date.today().isoformat()
    return [
        {
            "name": f"DeepWork Focus Engine {today_str}",
            "tagline": "Destroy distractions and hyper-focus on high-leverage tasks",
            "url": "https://www.producthunt.com"
        }
    ]

def create_markdown_file():
    today_str = datetime.date.today().isoformat()
    posts = fetch_live_tools()
    
    # Explicitly build absolute path to content/tools directory
    target_dir = os.path.join(os.getcwd(), "content", "tools")
    os.makedirs(target_dir, exist_ok=True)
    print(f"Target directory resolved to: {target_dir}")
    
    for item in posts:
        name = item["name"]
        tagline = item["tagline"]
        ph_url = item["url"]
        
        slug = name.lower().replace(" ", "-").replace(".", "").replace("+", "plus").replace("/", "-")
        filename = os.path.join(target_dir, f"{slug}.md")
        
        print(f"Writing file for: {name}")
        
        content = f"""---
title: "Best Review: {name} - {tagline}"
description: "Discover how {name} helps you beat procrastination and build bulletproof habits."
date: "{today_str}"
---

### Overview

{name} is an incredible tool designed to help professionals tackle: {tagline}. 

### Key Benefits

1. **Overcome Resistance:** Streamlines your workflow so you can bypass daily procrastination.
2. **Build Lasting Habits:** Uses cognitive principles to keep you consistent.

> [Check out {name} here]({ph_url}?ref=your-affiliate-tag)
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated file: {filename}")

if __name__ == "__main__":
    create_markdown_file()
