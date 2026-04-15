import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Fix the Password Capitalization
old_pw = r"""onclick="this.innerHTML='Entry Code: <span style=\\'color:var(--accent)\\'>mafia2026</span>'\""""
new_pw = """onclick="this.innerHTML='Entry Code: <span style=\\'color:var(--accent); text-transform:none; letter-spacing:0;\\'>mafia2026</span>'\""""
html = html.replace(old_pw, new_pw)

# 2. Fix the Hero Canvas Brightness
old_canvas_css = """    .hero-canvas-bg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      /* Add slight blur on the canvas itself to smooth out particles without relying on expensive SVG container filters */
      filter: blur(15px);
    }"""
new_canvas_css = """    .hero-canvas-bg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      filter: blur(25px);
      opacity: 0.2; /* Dramatically reduce brightness so text remains legible */
    }"""
html = html.replace(old_canvas_css, new_canvas_css)

with open("index.html", "w") as f:
    f.write(html)
print("UPDATED")
