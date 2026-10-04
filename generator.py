import os
import json
import datetime
import requests

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
PRODUCT_HUNT_TOKEN = os.environ.get("PRODUCT_HUNT_TOKEN")

def fetch_product_hunt_data():
    """Fetches trending productivity tools or falls back to demo data if token is missing"""
    if not PRODUCT_HUNT_TOKEN:
        print("Warning: PRODUCT_HUNT_TOKEN not found. Using fallback sample data.")
        return [
            {"node": {"name": "FocusFlow AI", "tagline": "AI-powered deep work session planner", "url": "https://producthunt.com"}},
            {"node": {"name": "HabitStack", "tagline": "Build bulletproof routines with micro-habits", "url": "https://producthunt.com"}}
        ]

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
    response = requests.post(url, json={"query": query}, headers=headers)
    print("PH API Status Code:", response.status_code)
    print("PH API Response:", response.text)
    
    if response.status_code == 200:
        data = response.json()
        edges = data.get("data", {}).get("posts", {}).get("edges", [])
        if edges:
            return edges
            
    # Fallback if API returns empty
    print("API returned no posts, falling back to sample data for pipeline test.")
    return [
        {"node": {"name": "MindLock Pro", "tagline": "Eliminate digital distractions instantly", "url": "https://producthunt.com"}}
    ]

def generate_ai_content(tool_name, tool_tagline):
    """Uses Google's Gemini API to write a structured SEO review"""
    if not GEMINI_API_KEY:
        return f"### Overview\n\n{tool_name} is an incredible tool designed to help you with: {tool_tagline}."

    ai_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    prompt = f"""
    Write a 400-word objective review article about the productivity tool '{tool_name}' with tagline '{tool_tagline}'. Focus on helping professionals build better habits and overcome mental resistance. Use clean Markdown format with an introductory hook, 2 core benefits, and a call-to-action.
    """
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(ai_url, json=payload, headers=headers)
    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            pass
    return f"### Review for {tool_name}\n\nEmpower your daily workflow with {tool_tagline}."

def create_markdown_file():
    posts = fetch_product_hunt_data()
    print(f"Total posts to process: {len(posts)}")
    
    os.makedirs("content/tools", exist_ok=True)
    
    for edge in posts:
        node = edge["node"]
        name = node["name"]
        tagline = node["tagline"]
        ph_url = node["url"]
        
        slug = name.lower().replace(" ", "-").replace(".", "").replace("+", "plus")
        filename = f"content/tools/{slug}.md"
        
        print(f"Processing content for: {name}")
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
        print(f"Successfully generated: {filename}")

if __name__ == "__main__":
    create_markdown_file()
