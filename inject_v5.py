import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Canvas JS Overhaul to Dotted Wave
canvas_js_target = r"    // ════════════════════════════════════════\n    // HERO CANVAS ANIMATION\n    // ════════════════════════════════════════.*?if \(canvas\) \{.*?\n      \}\n    \}"

new_canvas_js = """    // ════════════════════════════════════════
    // HERO CANVAS ANIMATION - ANTIGRAVITY DOT GRID
    // ════════════════════════════════════════
    const canvas = document.getElementById('hero-canvas');
    if (canvas) {
      const ctx = canvas.getContext('2d');
      let width, height;
      function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
      }
      resize();
      window.addEventListener('resize', resize);
      
      const spacing = 35;
      let mouse = { x: -1000, y: -1000 };
      
      document.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
      });
      
      let time = 0;
      function draw() {
        ctx.clearRect(0, 0, width, height);
        time += 0.03; // Wave speed
        
        const cols = Math.floor(width / spacing) + 3;
        const rows = Math.floor(height / spacing) + 3;
        
        for (let i = -1; i < cols; i++) {
          for (let j = -1; j < rows; j++) {
            let cx = i * spacing;
            let cy = j * spacing;
            
            // Standard sine wave displacement (Liquid feel)
            const waveX = Math.sin(time + j * 0.4) * 8;
            const waveY = Math.cos(time + i * 0.4) * 8;
            cx += waveX;
            cy += waveY;
            
            // Mouse gravity/repulsion
            const dx = cx - mouse.x;
            const dy = cy - mouse.y;
            const dist = Math.sqrt(dx*dx + dy*dy);
            
            let radius = 1.0;
            let alpha = 0.15;
            
            if (dist < 250) {
              const force = (250 - dist) / 250;
              // Repulse away from cursor
              cx += (dx / dist) * force * 45;
              cy += (dy / dist) * force * 45;
              radius += force * 1.5;
              alpha += force * 0.35;
            }
            
            ctx.fillStyle = `rgba(234, 234, 234, ${alpha})`;
            ctx.beginPath();
            ctx.arc(cx, cy, radius, 0, Math.PI * 2);
            ctx.fill();
          }
        }
        requestAnimationFrame(draw);
      }
      draw();
    }"""

html = re.sub(canvas_js_target, new_canvas_js, html, flags=re.DOTALL)

# Remove blur from CSS
css_canvas_old = r"""    .hero-canvas-bg \{
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      filter: blur\(20px\);
      opacity: 0.4;
    \}"""
css_canvas_new = """    .hero-canvas-bg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
      opacity: 1.0;
    }"""
html = re.sub(css_canvas_old, css_canvas_new, html, flags=re.DOTALL)

# 2. Append new behaviors
new_behaviors_js = """
    // ════════════════════════════════════════
    // MAGNETIC BUTTONS
    // ════════════════════════════════════════
    const magnetics = document.querySelectorAll('.feature-link, .project-cta, .about-link');
    magnetics.forEach(btn => {
      btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        const h = rect.width / 2;
        const v = rect.height / 2;
        const x = e.clientX - rect.left - h;
        const y = e.clientY - rect.top - v;
        btn.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px)`;
        btn.style.transition = 'none';
      });
      btn.addEventListener('mouseleave', () => {
        btn.style.transform = `translate(0px, 0px)`;
        btn.style.transition = 'transform 0.4s var(--ease-out)';
      });
    });

    // ════════════════════════════════════════
    // SCROLL VELOCITY SKEW
    // ════════════════════════════════════════
    let scrollVelocity = 0;
    let lastScroll = window.scrollY;
    const skewElements = document.querySelectorAll('.feature-visual');
    function renderScroll() {
      const currentScroll = window.scrollY;
      scrollVelocity = currentScroll - lastScroll;
      lastScroll = currentScroll;
      
      // Clamp the skew
      let skew = scrollVelocity * 0.03;
      if (skew > 4) skew = 4;
      if (skew < -4) skew = -4;
      
      skewElements.forEach(el => {
        el.style.transform = `skewY(${-skew}deg)`;
        el.style.transition = 'transform 0.1s linear';
      });
      requestAnimationFrame(renderScroll);
    }
    renderScroll();

    // ════════════════════════════════════════
    // TEXT SCRAMBLE REVEAL
    // ════════════════════════════════════════
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
    const scrambleElements = document.querySelectorAll('.feature-title');
    
    const scrambleObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.scrambled) {
          entry.target.dataset.scrambled = "true";
          const originalHTML = entry.target.innerHTML;
          const originalText = entry.target.innerText;
          
          let iterations = 0;
          const maxIterations = 14;
          
          const interval = setInterval(() => {
            entry.target.innerText = originalText.split("").map((char, index) => {
              if (index < iterations) return originalText[index];
              return letters[Math.floor(Math.random() * letters.length)];
            }).join("");
            
            iterations += 1;
            
            if (iterations >= originalText.length || iterations >= maxIterations) {
              clearInterval(interval);
              entry.target.innerHTML = originalHTML;
            }
          }, 35);
        }
      });
    }, { threshold: 0.25, rootMargin: '0px' });
    
    scrambleElements.forEach(el => scrambleObserver.observe(el));
"""

html = html.replace('</script>', new_behaviors_js + '\n  </script>')

with open('index.html', 'w') as f:
    f.write(html)
print("INJECTED")
