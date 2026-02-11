"""
=============================================================================
CHAMPION PORTFOLIO - Flask Backend
=============================================================================
Author: Satyam Kumar
"""

import os
from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# SITE CONFIGURATION
# =============================================================================

SITE_CONFIG = {
    "intro_name": "Satyam Kumar",
    "full_name": "Satyam Kumar",
    "title": "Student & Developer",
    "location": "Delhi, India",
    "username": "ggsatyam",
    "intro_text": """Welcome to my portfolio! I am a passionate Student and Developer 
    dedicated to building elegant digital experiences. I specialize in backend development 
    and enjoy exploring the intersection of design and technology.""",
    "page_title": "Satyam Kumar | Portfolio",
    "meta_description": "Portfolio of Satyam Kumar - Student and Developer based in Delhi, India",
    "tagline": "Crafting Digital Experiences",
}

# =============================================================================
# SOCIAL LINKS
# =============================================================================

SOCIAL_LINKS = {
    "instagram": {
        "url": "https://instagram.com/ggsatyam",
        "icon": "fa-brands fa-instagram",
        "label": "Instagram"
    },
    "github": {
        "url": "https://github.com/ggsatyam",
        "icon": "fa-brands fa-github",
        "label": "GitHub"
    },
    "linkedin": {
        "url": "https://linkedin.com/in/ggsatyam",
        "icon": "fa-brands fa-linkedin",
        "label": "LinkedIn"
    },
    "email": {
        "url": "mailto:your.email@gmail.com",
        "icon": "fa-solid fa-envelope",
        "label": "Email"
    },
}

# =============================================================================
# PROFICIENCY / SKILLS
# =============================================================================

PROFICIENCY = [
    {"name": "Python", "stars": 4},
    {"name": "Flask", "stars": 4},
    {"name": "JavaScript", "stars": 3},
    {"name": "VibeCoding", "stars": 5},
    {"name": "Web Design", "stars": 4},
]

# =============================================================================
# PROJECTS
# =============================================================================

PROJECTS = [
    {
        "title": "Workflewai",
        "category": "Web App",
        "year": "2024",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAECKo7HUP0tU2nO5oLe1A8iq6DT-VEEpluqQjSvEmqDzzTceqY1fPOxJN9PxBa6aq4bguFfxE2tdTkhVUqc9vE94MY0sIpe7ddOz5JVSNprpoiC46pXtebmJaroWpKsFrQFUKO7md7efHFX2-oz7UrivofD0_mDoz9_5b3VUN2_k-mDMIAPZPZ-uPIfbEAnb_rEcfNcA9MaSsIQfyhBPIX63P1KFJ0BOnvctZM1uVt6gsBB3NUhpAYVcPD6PxIMfOh5_k_LRDooKI",
        "link": "https://workflewai.vercel.app",
        "description": "AI-powered workflow automation tool"
    },
    {
        "title": "Aether Interface",
        "category": "UI Design",
        "year": "2023",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuBIdrXNHPWt9W_ExymxZG4AJ3_X2pRe5Yu8sm3Je9F2svIRnvKHHsnEfUhdhKpHgnMnzXWsJksov0wSFv4RVXt_DbmNv4JORE-rTPVb1aXENr4_N6t2o6XEPqkxV9xC9QQDN-aLyXvLlScBW7RSfwtBn0fjlbDeyoN-vOpxLiaAGikHKyM5t31lZ_TzCxDBtxXt8c8RQHt4FNneDeeq3nVI4ztvyNWnIeOZgOVM4qRZGbYB2CE5IN1r31Gnq3Lrqp-Ug-L0glq4_ak",
        "link": "https://example.com/aether",
        "description": "Futuristic interface design concept"
    },
]

# =============================================================================
# MUSIC TRACKS
# =============================================================================

MUSIC_TRACKS = [
    "music/track1.mp3",
    "music/track2.mp3",
]

# =============================================================================
# CHERRY BLOSSOM CONFIG
# =============================================================================

BLOSSOM_CONFIG = {
    "enabled_by_default": True,
    "count": 50,
    "colors": ["#ffb7c5", "#ff91a4", "#ffc0cb", "#fff0f2", "#f8c8d8"],
}

# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def index():
    return render_template('index.html',
        site=SITE_CONFIG,
        proficiency=PROFICIENCY,
        projects=PROJECTS,
        social_links=SOCIAL_LINKS,
        blossom_config=BLOSSOM_CONFIG,
        music_tracks=MUSIC_TRACKS,
    )

@app.route('/vault')
def vault():
    return render_template('vault.html', site=SITE_CONFIG)

@app.route('/photography')
def photography():
    return render_template('photography.html', site=SITE_CONFIG)

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
