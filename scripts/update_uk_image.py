import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_svg_block = '''                   <!-- UK Outline SVG -->
                   <svg viewBox="0 0 100 150" class="w-full h-full opacity-30 drop-shadow-md">
                     <!-- Great Britain Silhouette -->
                     <path d="M 40 140 C 50 140, 60 135, 65 125 C 70 115, 65 110, 60 100 C 70 95, 75 90, 75 80 C 75 70, 70 65, 65 60 C 65 50, 75 40, 70 30 C 65 20, 60 15, 55 10 C 50 5, 45 5, 40 15 C 35 25, 40 35, 45 45 C 50 55, 45 65, 40 70 C 35 75, 45 80, 45 90 C 45 100, 35 110, 40 120 C 45 130, 35 135, 40 140 Z" fill="#94a3b8" />
                     <!-- Northern Ireland Silhouette -->
                     <path d="M 25 70 C 30 70, 35 65, 30 60 C 25 55, 20 60, 20 65 C 20 70, 25 70, 25 70 Z" fill="#94a3b8" />
                   </svg>'''

new_image_block = '''                   <!-- UK Detailed SVG -->
                   <img src="images/uk.svg" alt="UK Map" class="w-full h-full object-contain opacity-50 drop-shadow-md" />'''

if old_svg_block in html:
    html = html.replace(old_svg_block, new_image_block)

# Let's adjust the heatmap blur layers slightly so they align better with a real UK map
old_heatmap = '''                   <!-- Abstract regions color overlays -->
                   <div class="absolute top-[20%] left-[45%] w-14 h-14 bg-green-500/60 rounded-full blur-xl"></div>
                   <div class="absolute top-[40%] left-[35%] w-16 h-12 bg-green-500/60 rounded-full blur-xl"></div>
                   <div class="absolute top-[55%] left-[40%] w-16 h-16 bg-yellow-500/60 rounded-full blur-xl"></div>
                   <div class="absolute top-[65%] left-[30%] w-12 h-10 bg-red-500/60 rounded-full blur-xl"></div>
                   <div class="absolute bottom-[15%] left-[45%] w-20 h-16 bg-red-500/60 rounded-full blur-xl"></div>'''

new_heatmap = '''                   <!-- Abstract regions color overlays (Heatmap) -->
                   <!-- Scotland -->
                   <div class="absolute top-[20%] left-[35%] w-24 h-24 bg-green-500/70 rounded-full blur-2xl"></div>
                   <div class="absolute top-[35%] left-[40%] w-20 h-16 bg-green-500/60 rounded-full blur-2xl"></div>
                   <!-- North -->
                   <div class="absolute top-[50%] left-[45%] w-20 h-20 bg-green-500/60 rounded-full blur-2xl"></div>
                   <!-- Midlands -->
                   <div class="absolute top-[65%] left-[55%] w-20 h-20 bg-yellow-500/60 rounded-full blur-2xl"></div>
                   <!-- Wales -->
                   <div class="absolute top-[70%] left-[35%] w-16 h-16 bg-red-500/60 rounded-full blur-2xl"></div>
                   <!-- South -->
                   <div class="absolute bottom-[10%] left-[55%] w-32 h-20 bg-red-500/70 rounded-full blur-2xl"></div>'''

if old_heatmap in html:
    html = html.replace(old_heatmap, new_heatmap)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modified index.html successfully")

