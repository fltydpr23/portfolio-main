import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Accent Color Theme
old_accent = """      --accent:     #c8ff57;       /* electric lime — portfolio signature */
      --accent-dim: rgba(200,255,87,0.12);
      --accent-glow:rgba(200,255,87,0.25);"""
new_accent = """      --accent:     #EAEAEA;       /* liquid chrome — portfolio signature */
      --accent-dim: rgba(234,234,234,0.12);
      --accent-glow:rgba(234,234,234,0.25);"""
html = html.replace(old_accent, new_accent)

# 2. Fix Canvas Styling
old_css = """    .hero-canvas-bg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      filter: blur(25px);
      opacity: 0.2; /* Dramatically reduce brightness so text remains legible */
    }"""
new_css = """    .hero-canvas-bg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      filter: blur(20px);
      opacity: 0.4;
    }"""
html = html.replace(old_css, new_css)

# 3. Canvas JS Overhaul to make extremely dark, slow grayscale gradients
js_target = r"      const colorPalettes = \['#5ab0e5', '#a3c75b', '#b180ff', '#1f242d'\];.*?requestAnimationFrame\(draw\);\n      }"
new_js = """      const colorPalettes = ['#202022', '#18181A', '#2A2C30', '#121214'];
      
      for(let i=0; i<8; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          vx: (Math.random() - 0.5) * 0.4,
          vy: (Math.random() - 0.5) * 0.4,
          radius: Math.random() * 400 + 400,
          color: colorPalettes[Math.floor(Math.random() * colorPalettes.length)]
        });
      }

      function draw() {
        ctx.fillStyle = 'rgba(7, 7, 7, 0.2)'; // Darker, stronger fade
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.globalCompositeOperation = 'screen'; 
        
        particles.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          
          if(p.x < -300) p.x = canvas.width + 300;
          if(p.x > canvas.width + 300) p.x = -300;
          if(p.y < -300) p.y = canvas.height + 300;
          if(p.y > canvas.height + 300) p.y = -300;
          
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius);
          // Extremely subtle alpha for the monochrome particles
          grad.addColorStop(0, p.color + '40'); 
          grad.addColorStop(1, '#00000000');
          ctx.fillStyle = grad;
          ctx.fill();
        });
        
        ctx.globalCompositeOperation = 'source-over';
        requestAnimationFrame(draw);
      }"""
html = re.sub(js_target, new_js, html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(html)
print("FIXED")
