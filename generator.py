import os

# Ensure the output directory exists
os.makedirs("content/tools", exist_ok=True)

# Define your programmatic data sets (mindset, resistance, and productivity tools)
tools_data = [
    {
        "slug": "unmotivated-running-on-empty",
        "title": "You’re Not Unmotivated — You’re Running on Empty",
        "subtitle": "A deep dive into burnout recovery, cognitive fatigue, and resetting your baseline energy.",
        "category": "Mindset & Recovery",
        "content": """
            <p>Most high-performers label themselves as 'lazy' or 'unmotivated' when they hit a wall. In reality, motivation is a finite emotional resource that burns out when your physical and mental recovery deficit crosses a critical threshold.</p>
            <h2>The Core Symptoms of Running on Empty</h2>
            <ul>
                <li>Chronic decision fatigue over simple, everyday tasks.</li>
                <li>Numbness toward goals that previously sparked excitement.</li>
                <li>Physical lethargy that doesn't resolve with standard sleep.</li>
            </ul>
            <h2>Actionable Recovery Framework</h2>
            <p>To reverse this state, you must pivot from forcing output to intentional systemic restoration. Cut your daily cognitive load by 50% for 3 days, audit your sleep hygiene, and eliminate micro-stressors before attempting to rebuild momentum.</p>
        """
    },
    {
        "slug": "breaking-the-resistance-loop",
        "title": "Breaking the Resistance Loop in Deep Work",
        "subtitle": "How to bypass psychological friction and step into frictionless execution.",
        "category": "Productivity",
        "content": """
            <p>The greater the resistance you feel toward a task, the more important that task is for your long-term growth. Resistance isn't a sign to stop; it's a compass pointing directly at the work that matters.</p>
            <h2>Why Resistance Manifests</h2>
            <p>Your brain is biologically wired to conserve energy and avoid uncertainty. When you approach high-leverage deep work, your amygdala triggers resistance to protect you from perceived failure or cognitive strain.</p>
            <h2>The 5-Minute Rule</h2>
            <p>Commit to working on the task for just five minutes with zero expectations of finishing. Once friction is broken, momentum takes over naturally.</p>
        """
    },
    {
        "slug": "dopamine-detox-for-creators",
        "title": "The Creator's Dopamine Reset: Reclaiming Focus",
        "subtitle": "Reclaim your attention span from endless feeds and shallow distraction loops.",
        "category": "Focus & Habits",
        "content": """
            <p>Modern creators struggle not with a lack of ideas, but with a fractured attention span caused by constant micro-dopamine hits from notifications, analytics dashboards, and social feeds.</p>
            <h2>Signs Your Baseline is Hijacked</h2>
            <ul>
                <li>The compulsive urge to check your phone every 3 minutes.</li>
                <li>Inability to read a book or watch a video longer than 5 minutes without skipping.</li>
            </ul>
            <h2>Executing a Clean Reset</h2>
            <p>Designate strict offline blocks in your daily calendar. Treat your attention as your most valuable financial asset—because in the digital economy, it literally is.</p>
        """
    }
]

# Generate individual HTML pages for each tool
index_links = []

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
    <a class="back" href="../../index.html">&larr; Back to Home</a>
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
    
    index_links.append(f'<li><a href="content/tools/{tool["slug"]}.html"><strong>{tool["title"]}</strong></a> — <span style="color: #6b7280;">{tool["subtitle"]}</span></li>')

print(f"Successfully generated {len(tools_data)} programmatic HTML pages.")
