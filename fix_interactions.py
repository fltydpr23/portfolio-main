import re

with open('index.html', 'r') as f:
    html = f.read()


# 1. Fix CSS override
html = html.replace('.reveal-feature.in { opacity: 1 !important; transform: none !important; }', '.reveal-feature.in { opacity: 1; transform: none; }')


# 2. Scrambler speed
old_scramble = """          const interval = setInterval(() => {
            entry.target.innerText = originalText.split("").map((char, index) => {
              if (index < iterations) return originalText[index];
              return letters[Math.floor(Math.random() * letters.length)];
            }).join("");
            
            iterations += 1;
            
            if (iterations >= originalText.length || iterations >= maxIterations) {
              clearInterval(interval);
              entry.target.innerHTML = originalHTML;
            }
          }, 35);"""
new_scramble = """          const interval = setInterval(() => {
            entry.target.innerText = originalText.split("").map((char, index) => {
              if (index < iterations) return originalText[index];
              return letters[Math.floor(Math.random() * letters.length)];
            }).join("");
            
            iterations += 1;
            
            if (iterations >= originalText.length || iterations >= maxIterations) {
              clearInterval(interval);
              entry.target.innerHTML = originalHTML;
            }
          }, 75);"""
html = html.replace(old_scramble, new_scramble)


# 3. Canvas AntiGravity exact clone
canvas_js_target = r"      const spacing = 35;\n      let mouse = \{ x: -1000, y: -1000 \};.*?\n      draw\(\);\n    \}"

new_canvas_js = """      const spacing = 22; // Tight grid like antigravity
      let mouse = { x: -1000, y: -1000 };
      
      document.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
      });
      document.addEventListener('mouseleave', () => {
        mouse.x = -1000;
        mouse.y = -1000;
      });
      
      let dots = [];
      let cols, rows;
      
      function initGrid() {
        dots = [];
        cols = Math.floor(width / spacing) + 3;
        rows = Math.floor(height / spacing) + 3;
        for (let i = -1; i < cols; i++) {
          for (let j = -1; j < rows; j++) {
            dots.push({
              hx: i * spacing,
              hy: j * spacing,
              x: i * spacing,
              y: j * spacing
            });
          }
        }
      }
      initGrid();
      window.addEventListener('resize', initGrid);
      
      let time = 0;
      function draw() {
        ctx.clearRect(0, 0, width, height);
        time += 0.015; 
        
        dots.forEach(dot => {
          let dx = mouse.x - dot.hx;
          let dy = mouse.y - dot.hy;
          let dist = Math.sqrt(dx*dx + dy*dy);
          
          let repelX = 0;
          let repelY = 0;
          let force = 0;
          
          if (dist < 180) {
            force = (180 - dist) / 180;
            repelX = -(dx / dist) * force * 35; // Push away from cursor
            repelY = -(dy / dist) * force * 35;
          }
          
          // Subtle overarching wave motion
          let wave = Math.sin(time + dot.hx * 0.005 + dot.hy * 0.005) * 4;
          
          let tx = dot.hx + repelX;
          let ty = dot.hy + repelY + wave;
          
          // Spring physics
          dot.x += (tx - dot.x) * 0.15;
          dot.y += (ty - dot.y) * 0.15;
          
          let alpha = 0.15; // default faint dot
          if (force > 0) alpha += force * 0.35;
          let radius = 1.0;
          if (force > 0) radius += force * 1.5;
          
          ctx.fillStyle = `rgba(234, 234, 234, ${alpha})`;
          ctx.beginPath();
          ctx.arc(dot.x, dot.y, radius, 0, Math.PI * 2);
          ctx.fill();
        });
        
        requestAnimationFrame(draw);
      }
      draw();
    }"""
html = re.sub(canvas_js_target, new_canvas_js, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("FIXED")
