import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Update emails
html = html.replace('mailto:hello@adhi.dev', 'mailto:adhityan2310@icloud.com')

# 2. Update projects count
html = html.replace('<span class="section-count">05 Projects</span>', '<span class="section-count">06 Projects</span>')

# 3. Add Ripples 3 to project list and update indices
# We need to find the start of the project list and insert Ripples 3
mm_target = '      <!-- 01 — Mileage Mafia -->'
ripples_html = """      <!-- 01 — Ripples 3 -->
      <article class="project-item" role="listitem" data-index="0">
        <div class="project-item-inner">
          <span class="project-num">01</span>
          <div class="project-info">
            <h3 class="project-name">Ripples 3</h3>
            <div class="project-tags">
              <span class="project-tag">Creative Coding</span>
              <span class="project-tag">Collaboration</span>
              <span class="project-tag">WebGL</span>
              <span class="project-tag">Interactive</span>
            </div>
          </div>
          <div class="project-meta">
            <span class="project-year">2026</span>
            <a href="https://nicopowa.github.io/ripples3/" target="_blank" rel="noopener" class="project-cta">
              View Site <span class="project-cta-arrow">↗</span>
            </a>
          </div>
        </div>
      </article>

"""

# Increment project numbers and data-indices
def inc_projects(match):
    idx = int(match.group(1)) + 1
    return f'data-index="{idx}"'

def inc_num(match):
    num = int(match.group(1)) + 1
    return f'<span class="project-num">0{num}</span>'

# Actually it's easier to just do simple replacements since there's only 5 existing projects
if mm_target in html:
    html = html.replace(mm_target, ripples_html + mm_target)
    
    html = html.replace('<span class="project-num">01</span>\n          <div class="project-info">\n            <h3 class="project-name">Mileage Mafia</h3>', '<span class="project-num">02</span>\n          <div class="project-info">\n            <h3 class="project-name">Mileage Mafia</h3>')
    html = html.replace('<span class="project-num">02</span>\n          <div class="project-info">\n            <h3 class="project-name">Kemon Socks</h3>', '<span class="project-num">03</span>\n          <div class="project-info">\n            <h3 class="project-name">Kemon Socks</h3>')
    html = html.replace('<span class="project-num">03</span>\n          <div class="project-info">\n            <h3 class="project-name">Dr. Gayathri</h3>', '<span class="project-num">04</span>\n          <div class="project-info">\n            <h3 class="project-name">Dr. Gayathri</h3>')
    html = html.replace('<span class="project-num">04</span>\n          <div class="project-info">\n            <h3 class="project-name">Lune Studio</h3>', '<span class="project-num">05</span>\n          <div class="project-info">\n            <h3 class="project-name">Lune Studio</h3>')
    html = html.replace('<span class="project-num">05</span>\n          <div class="project-info">\n            <h3 class="project-name">Michael Laffoley</h3>', '<span class="project-num">06</span>\n          <div class="project-info">\n            <h3 class="project-name">Michael Laffoley</h3>')

    # Update data indices for those 5 items explicitly by their position after Ripples 3 which takes data-index 0
    # A bit crude, but safe:
    html = html.replace('<!-- 01 — Mileage Mafia -->\n      <article class="project-item" role="listitem" data-index="0">', '<!-- 02 — Mileage Mafia -->\n      <article class="project-item" role="listitem" data-index="1">')
    html = html.replace('<!-- 02 — Kemon -->\n      <article class="project-item" role="listitem" data-index="1">', '<!-- 03 — Kemon -->\n      <article class="project-item" role="listitem" data-index="2">')
    html = html.replace('<!-- 03 — Gayathri Skin -->\n      <article class="project-item" role="listitem" data-index="2">', '<!-- 04 — Gayathri Skin -->\n      <article class="project-item" role="listitem" data-index="3">')
    html = html.replace('<!-- 04 — Lune Studio -->\n      <article class="project-item" role="listitem" data-index="3">', '<!-- 05 — Lune Studio -->\n      <article class="project-item" role="listitem" data-index="4">')
    html = html.replace('<!-- 05 — Michael Laffoley -->\n      <article class="project-item" role="listitem" data-index="4">', '<!-- 06 — Michael Laffoley -->\n      <article class="project-item" role="listitem" data-index="5">')

# 4. Insert Ripples 3 into previewContent
preview_target = "    const previewContent = ["
ripples_preview = "      { bg: '#000', color: '#fff', label: 'RIPPLES 3', sub: 'Interactive Fluid Simulation' },"
html = html.replace(preview_target, preview_target + "\n" + ripples_preview)

# 5. Replace Hero HTML
hero_target_regex = r'<!-- ══════════════════ HERO ══════════════════ -->.*?<!-- ══════════════════ MARQUEE ══════════════════ -->'

new_hero = """<!-- ══════════════════ HERO ══════════════════ -->
  <section class="hero minimalist-hero" id="hero" aria-label="Hero">
    <div class="hero-content-minimal">
      <div class="hero-photo-wrapper reveal-feature d1">
        <img src="file:///Users/Adhi/Downloads/xna1fs2q1e751.jpg" alt="Adhityan" class="hero-photo" />
      </div>
      <div class="hero-text-minimal reveal-feature d2">
        <h1 class="hero-headline-minimal">I'm Adhityan.</h1>
        <p class="hero-desc-minimal">
          I'm a designer and developer. I build websites, interactive interfaces, and bold identities. 
          I focus on consumer and high-end projects because I care about the emotional resonance of the web. 
          In my free time, I collaborate on visual experiments like <a href="https://nicopowa.github.io/ripples3/" target="_blank" class="hero-inline-link">Ripples 3</a>. 
          I love minimal typography, immersive interactions, and well-curated aesthetics. 
          I live on the internet, so <a href="mailto:adhityan2310@icloud.com" class="hero-inline-link">say hi.</a>
        </p>
        <div class="hero-links-minimal">
          <a href="#projects" class="hero-sublink">View Selected Work ↓</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ══════════════════ MARQUEE ══════════════════ -->"""

html = re.sub(hero_target_regex, new_hero, html, flags=re.DOTALL)

# Add minimal hero CSS
css_insertion = """    /* ═══════════════════════════════════════════
       MINIMALIST HERO
    ═══════════════════════════════════════════ */
    .minimalist-hero {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6rem 3rem 4rem;
      background: var(--bg);
    }
    .hero-content-minimal {
      display: flex;
      align-items: center;
      gap: 6rem;
      max-width: 1100px;
      margin: 0 auto;
    }
    .hero-photo-wrapper {
      flex-shrink: 0;
      width: 280px;
      height: 380px;
      border-radius: 4px;
      overflow: hidden;
      filter: grayscale(100%) contrast(1.1);
      border: 1px solid rgba(255,255,255,0.05);
    }
    .hero-photo {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .hero-text-minimal {
      flex: 1;
    }
    .hero-headline-minimal {
      font-family: var(--font-display);
      font-size: clamp(3rem, 5vw, 5rem);
      color: var(--text);
      line-height: 1;
      margin-bottom: 2rem;
    }
    .hero-desc-minimal {
      font-family: var(--font-body);
      font-size: 1.1rem;
      font-weight: 300;
      color: var(--text-dim);
      line-height: 1.8;
      max-width: 45ch;
      margin-bottom: 2.5rem;
    }
    .hero-inline-link {
      color: var(--accent);
      text-decoration: none;
      position: relative;
      display: inline-block;
      transition: color 0.3s;
    }
    .hero-inline-link::after {
      content: '';
      position: absolute;
      bottom: -2px; left: 0; right: 0;
      height: 1px;
      background: var(--accent);
      opacity: 0.5;
      transition: opacity 0.3s;
    }
    .hero-inline-link:hover { color: var(--text); }
    .hero-inline-link:hover::after { opacity: 1; background: var(--text); }
    
    .hero-links-minimal {
      display: flex;
      gap: 1.5rem;
    }
    .hero-sublink {
      font-family: var(--font-ui);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--text-muted);
      transition: color 0.2s;
    }
    .hero-sublink:hover { color: var(--accent); }

    @media (max-width: 900px) {
      .hero-content-minimal {
        flex-direction: column;
        gap: 3rem;
        text-align: left;
      }
      .minimalist-hero { padding: 8rem 1.5rem 4rem; }
    }
"""

style_tag = "</style>"
html = html.replace(style_tag, css_insertion + "\n" + style_tag)

with open("index.html", "w") as f:
    f.write(html)
