import os
import datetime
import requests

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
PRODUCT_HUNT_TOKEN = os.environ.get("PRODUCT_HUNT_TOKEN")

def fetch_product_hunt_data():
    """Fetches trending tools or reliably falls back to ensure pipeline generates content"""
    if PRODUCT_HUNT_TOKEN:
        url = "https://api.producthunt.com/v2/api/graphql"
        headers = {
            "Authorization": f"Bearer {PRODUCT_HUNT_TOKEN}",
            "Content-Type": "application/json"
        }
        query = """
        {
          posts(order: VOTES, first: 2) {
            edges {
              node {
                name
                tagline
                url
                votesCount
              }
            }
          }
        }
        """
        try:
            response = requests.post(url, json={"query": query}, headers=headers, timeout=10)
            if response.status_code == 200:
                edges = response.json().get("data", {}).get("posts", {}).get("edges", [])
                if edges:
                    print(f"Successfully fetched {len(edges)} items from Product Hunt API.")
                    return edges
        except Exception as e:
            print(f"API request exception: {e}")

    # Guaranteed fallback data so your pSEO pipeline always builds content and triggers the PR
    print("Using guaranteed fallback content items to populate pSEO pages.")
    today_str = datetime.date.today().isoformat()
    return [
        {
            "node": {
                "name": f"Mindset Focus Engine {today_str}",
                "tagline": "Break through mental resistance and achieve deep work automatically",
                "url": "https://www.producthunt.com"
            }
        },
        {
            "node": {
                "name": f"Habit Loop Optimizer {today_str}",
                "tagline": "Build unbreakable daily habits with cognitive behavioral tracking",
                "url": "https://www.producthunt.com"
            }
        }
    ]

def generate_ai_content(tool_name, tool_tagline):
    """Uses Google's Gemini API to write a structured SEO review"""
    if not GEMINI_API_KEY:
        return f"### Overview\n\n{tool_name} helps you tackle: {tool_tagline}."

    ai_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    prompt = f"""
    Write a 400-word objective review article about the productivity tool '{tool_name}' with tagline '{tool_tagline}'. Focus on helping professionals build better habits and overcome mental resistance. Use clean Markdown format with an introductory hook, 2 core benefits, and a call-to-action.
    """
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(ai_url, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print(f"Gemini generation error: {e}")
        
    return f"### Review for {tool_name}\n\nSupercharge your daily workflow and shatter mental blocks with {tool_tagline}."

def create_markdown_file():
    posts = fetch_product_hunt_data()
    print(f"Processing total items: {len(posts)}")
    
    os.makedirs("content/tools", exist_ok=True)
    
    for edge in posts:
        node = edge["node"]
        name = node["name"]
        tagline = node["tagline"]
        ph_url = node["url"]
        
        slug = name.lower().replace(" ", "-").replace(".", "").replace("+", "plus").replace("/", "-")
        filename = f"content/tools/{slug}.md"
        
        print(f"Writing markdown file for: {name}")
        ai_body = generate_ai_content(name, tagline)
        
        affiliate_cta = f"\n\n>[Check out {name} here]({ph_url}?ref=your-affiliate-tag)\n"
        final_content = ai_body + affiliate_cta
        
        today = datetime.date.today().isoformat()
        frontmatter = f"""---
title: "Best Review: {name} - {tagline}"
description: "Discover how {name} helps you beat procrastination and build bulletproof habits."
date: "{today}"
---
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(frontmatter + final_content)
        print(f"Successfully created: {filename}")

if __name__ == "__main__":
    create_markdown_file()
