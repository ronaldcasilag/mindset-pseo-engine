import os
import datetime

def create_markdown_file():
    today_str = datetime.date.today().isoformat()
    
    # Static guaranteed items to test PR creation immediately
    posts = [
        {
            "name": f"DeepWork Focus Engine {today_str}",
            "tagline": "Destroy distractions and hyper-focus on high-leverage tasks",
            "url": "https://www.producthunt.com"
        },
        {
            "name": f"Habit Loop Tracker {today_str}",
            "tagline": "Build unbreakable daily routines using behavioral science",
            "url": "https://www.producthunt.com"
        }
    ]
    
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
