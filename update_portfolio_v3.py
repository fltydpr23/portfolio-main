import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Update Dates in Feature Blocks and Project List
# Ripples -> 2023
html = html.replace('Project 01 — 2026', 'Project 01 — 2023')
html = re.sub(r'(<h3 class="project-name">Ripples 3</h3>.*?<span class="project-year">)2026(</span>)', r'\g<1>2023\g<2>', html, flags=re.DOTALL)

# Mileage Mafia -> 2025
html = html.replace('Project 02 — 2026', 'Project 02 — 2025')
html = re.sub(r'(<h3 class="project-name">Mileage Mafia</h3>.*?<span class="project-year">)2026(</span>)', r'\g<1>2025\g<2>', html, flags=re.DOTALL)

# Kemon -> 2024
html = html.replace('Project 03 — 2026', 'Project 03 — 2024')
html = re.sub(r'(<h3 class="project-name">Kemon Socks</h3>.*?<span class="project-year">)2026(</span>)', r'\g<1>2024\g<2>', html, flags=re.DOTALL)

# Dr Gayathri -> 2025
html = html.replace('Project 04 — 2026', 'Project 04 — 2025')
html = re.sub(r'(<h3 class="project-name">Dr. Gayathri</h3>.*?<span class="project-year">)2026(</span>)', r'\g<1>2025\g<2>', html, flags=re.DOTALL)

# Lune -> 2026
html = html.replace('Project 05 — 2025', 'Project 05 — 2026')
html = re.sub(r'(<h3 class="project-name">Lune Studio</h3>.*?<span class="project-year">)2025(</span>)', r'\g<1>2026\g<2>', html, flags=re.DOTALL)

# 2. Fix the Hero Graphics (Remove cheap noise and blurry bubbles)
html = html.replace('<div id="noise"></div>', '')  # global noise
html = html.replace('<div class="hero-noise-overlay"></div>', '')  # local hero noise
html = html.replace('filter: blur(15px);', '')  # canvas blur remove

# Make particle animation beautiful, gigantic, and slow (Premium fluid look)
old_particles = """      for(let i=0; i<40; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          vx: (Math.random() - 0.5) * 1.5,
          vy: (Math.random() - 0.5) * 1.5,
          radius: Math.random() * 120 + 40,
          color: colorPalettes[Math.floor(Math.random() * colorPalettes.length)]
        });
      }"""

new_particles = """      for(let i=0; i<8; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          vx: (Math.random() - 0.5) * 0.5,
          vy: (Math.random() - 0.5) * 0.5,
          radius: Math.random() * 400 + 300,
          color: colorPalettes[Math.floor(Math.random() * colorPalettes.length)]
        });
      }"""
html = html.replace(old_particles, new_particles)

html = html.replace('ctx.globalCompositeOperation = \'screen\';', 'ctx.globalCompositeOperation = \'lighter\';')
html = html.replace('ctx.fillStyle = \'rgba(5, 5, 5, 0.15)\';', 'ctx.fillStyle = \'rgba(5, 5, 5, 0.08)\';')
html = html.replace('grad.addColorStop(0, p.color + \'30\');', 'grad.addColorStop(0, p.color + \'10\');')

# 3. Fix the footer
old_footer = r'<footer class="footer">.*?</footer>'
new_footer = """<footer class="footer" style="flex-direction:row; justify-content:space-between; align-items:center; padding: 4rem;">
    <a href="https://github.com/fltydpr23" target="_blank" class="footer-link" style="color:var(--text); text-decoration:none; font-family:var(--font-ui); text-transform:uppercase; font-size:0.8rem; letter-spacing:0.1em; transition:color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--text)'">github.com/fltydpr23 ↗</a>
    <a href="#" onclick="window.scrollTo({top:0, behavior:'smooth'}); return false;" class="footer-link" style="color:var(--text); text-decoration:none; font-family:var(--font-ui); text-transform:uppercase; font-size:0.8rem; letter-spacing:0.1em; transition:color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='var(--text)'">Back to Top ↑</a>
  </footer>"""
html = re.sub(old_footer, new_footer, html, flags=re.DOTALL)

# 4. Fix Password Button Interaction
# We must ensure inner elements don't steal clicks and the tag intercepts it properly.
old_pw = r"""<span class="project-tag" style="cursor:pointer; display:inline-flex; align-items:center; transition: color 0.3s;" onclick="this.innerHTML='<span style=\\'color:var(--accent)\\'>mafia2026</span>';">🔒 Password Protected</span>"""

new_pw = """<span class="project-tag password-reveal-btn" style="position:relative; z-index:99; cursor:pointer;" onclick="event.preventDefault(); event.stopPropagation(); this.innerHTML='🔒 <span style=\\'color:var(--accent)\\'>mafia2026</span>';">🔒 Password Protected</span>"""

html = html.replace(old_pw, new_pw)

# We also need to add pointer-events: auto to the project-info if it was blocked
css_pointers = """    .project-tag {
      position: relative;
      z-index: 10;
      pointer-events: auto;
    }"""
html = html.replace('</style>', css_pointers + '\n  </style>')

with open("index.html", "w") as f:
    f.write(html)
print("UPDATED")
