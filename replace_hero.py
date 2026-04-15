import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Update the HTML layer
hero_target_regex = r'<!-- ══════════════════ HERO ══════════════════ -->.*?<!-- ══════════════════ MARQUEE ══════════════════ -->'

new_hero = """<!-- ══════════════════ HERO ══════════════════ -->
  <section class="hero minimalist-hero" id="hero" aria-label="Hero">
    <div class="hero-bg-orbs" aria-hidden="true">
      <div class="fluid-orb fluid-orb-1"></div>
      <div class="fluid-orb fluid-orb-2"></div>
      <div class="fluid-orb fluid-orb-3"></div>
    </div>
    <div class="hero-noise-overlay"></div>
    
    <div class="hero-content-minimal">
      <div class="hero-text-minimal reveal-feature d1">
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

# 2. Update the CSS for the Minimalist Hero
css_target_regex = r'/\* ═══════════════════════════════════════════\n       MINIMALIST HERO\n    ═══════════════════════════════════════════ \*/.*?</style>'

new_css = """/* ═══════════════════════════════════════════
       MINIMALIST HERO (ORB/FRACTAL VIBE)
    ═══════════════════════════════════════════ */
    .minimalist-hero {
      position: relative;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6rem 3rem 4rem;
      background: #050505; /* Deep dark background */
      overflow: hidden;
    }
    
    /* Smooth animated fluid orbs */
    .hero-bg-orbs {
      position: absolute;
      inset: 0;
      z-index: 0;
      overflow: hidden;
      filter: blur(80px);
      opacity: 0.6;
    }
    .fluid-orb {
      position: absolute;
      border-radius: 50%;
      mix-blend-mode: screen;
      animation: fluidRotate 20s infinite linear;
    }
    .fluid-orb-1 {
      width: 600px; height: 600px;
      background: radial-gradient(circle, rgba(160, 200, 255, 0.4) 0%, transparent 60%);
      top: -10%; left: 10%;
      animation-duration: 25s;
    }
    .fluid-orb-2 {
      width: 700px; height: 700px;
      background: radial-gradient(circle, rgba(200, 255, 87, 0.25) 0%, transparent 60%);
      bottom: -20%; right: -10%;
      animation-duration: 30s;
      animation-direction: reverse;
    }
    .fluid-orb-3 {
      width: 500px; height: 500px;
      background: radial-gradient(circle, rgba(177, 128, 255, 0.3) 0%, transparent 60%);
      top: 30%; left: 40%;
      animation-duration: 40s;
    }
    @keyframes fluidRotate {
      0% { transform: rotate(0deg) translate(50px) rotate(0deg); }
      100% { transform: rotate(360deg) translate(50px) rotate(-360deg); }
    }
    
    /* Grain overlay just for the hero to give texture */
    .hero-noise-overlay {
      position: absolute;
      inset: 0;
      z-index: 1;
      opacity: 0.25;
      pointer-events: none;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    }

    .hero-content-minimal {
      position: relative;
      z-index: 10;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      max-width: 850px;
      margin: 0 auto;
    }
    .hero-text-minimal {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .hero-headline-minimal {
      font-family: var(--font-display);
      font-size: clamp(3.5rem, 8vw, 7rem);
      color: var(--text);
      line-height: 1.1;
      margin-bottom: 2rem;
      letter-spacing: -0.02em;
    }
    .hero-desc-minimal {
      font-family: var(--font-body);
      font-size: 1.1rem;
      font-weight: 300;
      color: var(--text-dim);
      line-height: 1.8;
      max-width: 55ch;
      margin-bottom: 3rem;
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
      color: var(--text);
      padding: 1rem 2rem;
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 4px;
      transition: all 0.3s ease;
      background: rgba(255,255,255,0.03);
      backdrop-filter: blur(10px);
    }
    .hero-sublink:hover { 
      border-color: var(--accent); 
      color: var(--accent); 
      background: rgba(200,255,87,0.05);
      transform: translateY(-2px);
    }

    @media (max-width: 900px) {
      .minimalist-hero { padding: 8rem 1.5rem 4rem; }
      .hero-content-minimal { text-align: left; align-items: flex-start; }
      .hero-text-minimal { align-items: flex-start; }
    }
</style>"""

html = re.sub(css_target_regex, new_css, html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(html)
