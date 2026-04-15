import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Add CSS for .hero-content-minimal fade-in
css_target = r"    \.hero-content-minimal \{(.*?)\}"
# We just append to it or replace it. Actually, I can just inject new CSS at the end of the <style> block before </head>
css_injection = """
    /* Cinematic Intro */
    .hero-content-minimal {
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 2s cubic-bezier(0.16, 1, 0.3, 1), transform 2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .hero-content-minimal.show {
      opacity: 1;
      transform: translateY(0);
    }
"""
html = html.replace('</style>', css_injection + '\n  </style>')


# 2. Update the JS loader logic to include scrollRestoration and cinematic stagger
js_target = r"    window\.addEventListener\('load', \(\) => \{\n      setTimeout\(\(\) => \{\n        document\.getElementById\('loader'\)\.classList\.add\('hidden'\);\n      \}, 1600\);\n    \}\);"

new_js = """    if ('scrollRestoration' in history) {
      history.scrollRestoration = 'manual';
    }
    window.scrollTo(0,0);

    window.addEventListener('load', () => {
      window.scrollTo(0, 0);
      setTimeout(() => {
        document.getElementById('loader').classList.add('hidden');
        // Wait 1.2s for the wavetable to breathe, then fade in the text
        setTimeout(() => {
          const heroContent = document.querySelector('.hero-content-minimal');
          if (heroContent) heroContent.classList.add('show');
        }, 1200);
      }, 1600);
    });"""

html = re.sub(js_target, new_js, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("INJECTED")
