import os
import json
import datetime
import requests

# 1. Configuration & Free API Keys loaded from GitHub Secrets
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
PRODUCT_HUNT_TOKEN = os.environ.get("PRODUCT_HUNT_TOKEN")

def fetch_product_hunt_data():
    """Fetches trending productivity/habit tools from Product Hunt via GraphQL"""
    url = "https://api.producthunt.com/v2/api/graphql"
    headers = {
        "Authorization": f"Bearer {PRODUCT_HUNT_TOKEN}",
        "Content-Type": "application/json"
    }
    query = """
    {
      posts(order: VOTES, first: 3) {
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
    if response.status_code == 200:
        return response.json().get("data", {}).get("posts", {}).get("edges", [])
    return []

def generate_ai_content(tool_name, tool_tagline):
    """Uses Google's Gemini API free tier to write a structured SEO guide"""
    ai_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    prompt = f"""
    Write a 400-word objective review article about the productivity tool '{tool_name}' which has the tagline: '{tool_tagline}'. Focus on how it helps professionals build better habits and overcome mental resistance. Format the output cleanly in Markdown. Include an introductory hook, 2 core benefits, and a call-to-action to try the tool.
    """
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(ai_url, json=payload, headers=headers)
    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "Content generation failed parsing response."
    return "API Error generating content."

def create_markdown_file():
    posts = fetch_product_hunt_data()
    for edge in posts:
        node = edge["node"]
        name = node["name"]
        tagline = node["tagline"]
        ph_url = node["url"]
        
        # Format slug-friendly filename
        slug = name.lower().replace(" ", "-").replace(".", "")
        filename = f"content/tools/{slug}.md"
        
        print(f"Processing content for: {name}")
        ai_body = generate_ai_content(name, tagline)
        
        # Inject Affiliate Link or fallback to Product Hunt landing page
        affiliate_cta = f"\n\n>[Check out {name} here]({ph_url}?ref=your-affiliate-tag)\n"
        final_content = ai_body + affiliate_cta
        
        # Build Frontmatter metadata for SEO
        today = datetime.date.today().isoformat()
        frontmatter = f"""---
title: "Best Review: {name} - {tagline}"
description: "Discover how {name} helps you beat procrastination and build bulletproof habits."
date: "{today}"
---
"""
        os.makedirs("content/tools", exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(frontmatter + final_content)
        print(f"Successfully generated: {filename}")

if __name__ == "__main__":
    create_markdown_file()
