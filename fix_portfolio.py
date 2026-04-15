import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Fix the Hero Animation (CSS)
hero_css_old = r"""    /\* Smooth animated fluid orbs \*/
    .hero-bg-orbs \{
      position: absolute;
      inset: 0;
      z-index: 0;
      overflow: hidden;
      filter: blur\(80px\);
      opacity: 0\.6;
    \}
    \.fluid-orb \{
      position: absolute;
      border-radius: 50%;
      mix-blend-mode: screen;
      animation: fluidRotate 20s infinite linear;
    \}
    \.fluid-orb-1 \{
      width: 600px; height: 600px;
      background: radial-gradient\(circle, rgba\(160, 200, 255, 0\.4\) 0%, transparent 60%\);
      top: -10%; left: 10%;
      animation-duration: 25s;
    \}
    \.fluid-orb-2 \{
      width: 700px; height: 700px;
      background: radial-gradient\(circle, rgba\(200, 255, 87, 0\.25\) 0%, transparent 60%\);
      bottom: -20%; right: -10%;
      animation-duration: 30s;
      animation-direction: reverse;
    \}
    \.fluid-orb-3 \{
      width: 500px; height: 500px;
      background: radial-gradient\(circle, rgba\(177, 128, 255, 0\.3\) 0%, transparent 60%\);
      top: 30%; left: 40%;
      animation-duration: 40s;
    \}
    @keyframes fluidRotate \{
      0% \{ transform: rotate\(0deg\) translate\(50px\) rotate\(0deg\); \}
      100% \{ transform: rotate\(360deg\) translate\(50px\) rotate\(-360deg\); \}
    \}"""

hero_css_new = """    /* Sharp fractal-like floating glow meshes (performant) */
    .hero-bg-orbs {
      position: absolute;
      inset: 0;
      z-index: 0;
      overflow: hidden;
      opacity: 0.8;
    }
    .fluid-orb {
      position: absolute;
      border-radius: 50%;
      mix-blend-mode: screen;
      filter: blur(60px);
    }
    .fluid-orb-1 {
      width: 600px; height: 600px;
      background: radial-gradient(circle, rgba(160, 200, 255, 0.4) 0%, transparent 70%);
      top: 0%; left: 20%;
      animation: orbMove1 15s infinite alternate ease-in-out;
    }
    .fluid-orb-2 {
      width: 750px; height: 750px;
      background: radial-gradient(circle, rgba(200, 255, 87, 0.25) 0%, transparent 70%);
      bottom: 0%; right: 10%;
      animation: orbMove2 18s infinite alternate ease-in-out;
    }
    .fluid-orb-3 {
      width: 550px; height: 550px;
      background: radial-gradient(circle, rgba(177, 128, 255, 0.3) 0%, transparent 70%);
      top: 40%; left: 40%;
      animation: orbMove3 20s infinite alternate ease-in-out;
    }
    @keyframes orbMove1 {
      0% { transform: translate3d(0, 0, 0) scale(1); }
      50% { transform: translate3d(80px, -60px, 0) scale(1.1); }
      100% { transform: translate3d(-40px, 50px, 0) scale(0.9); }
    }
    @keyframes orbMove2 {
      0% { transform: translate3d(0, 0, 0) scale(1); }
      50% { transform: translate3d(-100px, 80px, 0) scale(1.05); }
      100% { transform: translate3d(50px, -40px, 0) scale(0.95); }
    }
    @keyframes orbMove3 {
      0% { transform: translate3d(0, 0, 0) scale(1.1); }
      50% { transform: translate3d(-60px, -60px, 0) scale(0.9); }
      100% { transform: translate3d(60px, 60px, 0) scale(1.2); }
    }"""

html = re.sub(hero_css_old, hero_css_new, html, flags=re.DOTALL)


# 2. Fix the Ripples 3 feature-thumb-body
ripples_old = r'<div class="feature-thumb-body" style="background:radial-gradient\(ellipse at center, rgba\(100,200,255,0\.15\) 0%, transparent 80%\); display:flex; align-items:center; justify-content:center;">\n             <div style="width: 200px; height: 200px; border-radius: 50%; border: 1px solid rgba\(100,200,255,0\.3\); position: absolute; animation: scrollPulse 3s infinite;"></div>\n             <div style="width: 140px; height: 140px; border-radius: 50%; border: 1px solid rgba\(100,200,255,0\.6\); position: absolute; animation: scrollPulse 3s infinite 0\.5s;"></div>\n             <div style="width: 80px; height: 80px; border-radius: 50%; border: 1px solid rgba\(100,200,255,1\); position: absolute;"></div>\n          </div>'

ripples_new = """<div class="feature-thumb-body" style="background:#0a0c10; position:relative; overflow:hidden; display:flex; align-items:center; justify-content:center;">
             <!-- Concentric Ripples matching screenshot -->
             <div style="width:280px; height:280px; border-radius:50%; border:1px solid rgba(90,176,229,0.05); position:absolute;"></div>
             <div style="width:180px; height:180px; border-radius:50%; border:1px solid rgba(90,176,229,0.2); position:absolute;"></div>
             <div style="width:90px; height:90px; border-radius:50%; border:1.5px solid rgba(90,176,229,0.8); position:absolute;"></div>
             <!-- Green Object matching screenshot -->
             <div style="position:absolute; left: 10%; top: 50%; transform:translateY(-50%); width:36px; height:36px; border-radius:50%; border:1.5px solid #a3c75b; display:flex; align-items:center; justify-content:center;">
               <div style="width:10px; height:10px; background:#a3c75b; border-radius:50%;"></div>
             </div>
          </div>"""

html = re.sub(ripples_old, ripples_new, html, flags=re.DOTALL)

# 3. Handle Password Reveal for Mileage Mafia
mm_tags_old = r"""            <div class="project-tags">
              <span class="project-tag">Cyberpunk Design</span>
              <span class="project-tag">Interactive Leaderboard</span>
              <span class="project-tag">Motion UI</span>
              <span class="project-tag">WebGL</span>
            </div>"""

mm_tags_new = """            <div class="project-tags">
              <span class="project-tag">Cyberpunk Design</span>
              <span class="project-tag">Interactive Leaderboard</span>
              <span class="project-tag">Motion UI</span>
              <span class="project-tag" style="cursor:pointer; display:inline-flex; align-items:center; transition: color 0.3s;" onclick="this.innerHTML='<span style=\\'color:var(--accent)\\'>mafia2026</span>';">🔒 Password Protected</span>
            </div>"""

html = html.replace(mm_tags_old, mm_tags_new)

with open("index.html", "w") as f:
    f.write(html)

print("SUCCESS")
