import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Add favicon
head_end = "</head>"
favicon_link = '  <link rel="icon" href="file:///Users/Adhi/Downloads/xna1fs2q1e751.jpg" type="image/jpeg">\n</head>'
html = html.replace(head_end, favicon_link)

# 2. Add Ripples 3 to featured section
feature_start = '<section class="features" id="featured" aria-label="Featured Projects">'
ripples_feature = """<section class="features" id="featured" aria-label="Featured Projects">

    <!-- ── Feature 0: Ripples 3 ── -->
    <div class="feature-block reverse">
      <div class="feature-visual">
        <div class="feature-thumb mm-bg" style="background:#050505;">
          <div class="feature-thumb-header">
            <div class="dot dot-r"></div><div class="dot dot-y"></div><div class="dot dot-g"></div>
            <div class="feature-thumb-url"><span>nicopowa.github.io/ripples3</span></div>
          </div>
          <div class="feature-thumb-body" style="background:radial-gradient(ellipse at center, rgba(100,200,255,0.15) 0%, transparent 80%); display:flex; align-items:center; justify-content:center;">
             <div style="width: 200px; height: 200px; border-radius: 50%; border: 1px solid rgba(100,200,255,0.3); position: absolute; animation: scrollPulse 3s infinite;"></div>
             <div style="width: 140px; height: 140px; border-radius: 50%; border: 1px solid rgba(100,200,255,0.6); position: absolute; animation: scrollPulse 3s infinite 0.5s;"></div>
             <div style="width: 80px; height: 80px; border-radius: 50%; border: 1px solid rgba(100,200,255,1); position: absolute;"></div>
          </div>
        </div>
      </div>
      <div class="feature-info">
        <p class="feature-num reveal-feature d1">Project 01 — 2026</p>
        <h3 class="feature-title reveal-feature d2">Ripples<br /><em>Three</em></h3>
        <p class="feature-desc reveal-feature d3">
          A hypnotic, interactive fluid and ripple simulator built as a collaboration. Move your cursor across the screen to generate realistic, physics-based liquid ripples that bounce and reflect in real-time. It's built heavily on WebGL constraints for maximum performance and visual impact.
        </p>
        <div class="feature-details reveal-feature d4">
          <div class="feature-detail"><div class="feature-detail-dot"></div><span>Physics-Based Fluid Sim</span></div>
          <div class="feature-detail"><div class="feature-detail-dot"></div><span>High-Performance WebGL</span></div>
          <div class="feature-detail"><div class="feature-detail-dot"></div><span>Creative Collaboration</span></div>
          <div class="feature-detail"><div class="feature-detail-dot"></div><span>Interactive UI/UX Art</span></div>
        </div>
        <a href="https://nicopowa.github.io/ripples3/" target="_blank" rel="noopener" class="feature-link reveal-feature d5">
          Play With Ripples <span class="feature-link-arrow">↗</span>
        </a>
      </div>
    </div>"""

html = html.replace(feature_start, ripples_feature)

# Update feature numbers for the rest
html = html.replace('<p class="feature-num reveal-feature d1">Project 01 — 2026</p>\n        <h3 class="feature-title reveal-feature d2">Mileage', '<p class="feature-num reveal-feature d1">Project 02 — 2026</p>\n        <h3 class="feature-title reveal-feature d2">Mileage')
html = html.replace('<p class="feature-num reveal-feature d1">Project 02 — 2026</p>\n        <h3 class="feature-title reveal-feature d2">Kemon', '<p class="feature-num reveal-feature d1">Project 03 — 2026</p>\n        <h3 class="feature-title reveal-feature d2">Kemon')
html = html.replace('<p class="feature-num reveal-feature d1">Project 03 — 2026</p>\n        <h3 class="feature-title reveal-feature d2">Dr.', '<p class="feature-num reveal-feature d1">Project 04 — 2026</p>\n        <h3 class="feature-title reveal-feature d2">Dr.')
html = html.replace('<p class="feature-num reveal-feature d1">Project 04 — 2025</p>\n        <h3 class="feature-title reveal-feature d2">Lune', '<p class="feature-num reveal-feature d1">Project 05 — 2025</p>\n        <h3 class="feature-title reveal-feature d2">Lune')

with open("index.html", "w") as f:
    f.write(html)
