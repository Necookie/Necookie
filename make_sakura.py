import random
import os

num_petals = 200
width = 900
height = 150  # Made it taller for a bigger effect

css = []
petals = []

colors = ['url(#pink)', 'url(#light)', 'url(#green)']

for i in range(num_petals):
    duration = round(random.uniform(2.5, 6.0), 1)
    delay = round(random.uniform(0.0, 5.0), 1)
    
    start_x = random.randint(-100, width + 100)
    start_y = random.randint(-50, 10)
    start_rot = random.randint(-45, 45)
    
    end_x_offset = random.randint(-100, 100)
    end_y_offset = random.randint(160, 250)
    end_rot = start_rot + random.randint(300, 700) * random.choice([-1, 1])
    
    css.append(f'''    @keyframes f{i}{{
      0%{{transform:translate(0px,-10px) rotate({start_rot}deg);opacity:0}}
      10%{{opacity:{round(random.uniform(0.8, 1.0),2)}}}
      85%{{opacity:{round(random.uniform(0.5, 0.7),2)}}}
      100%{{transform:translate({end_x_offset}px,{end_y_offset}px) rotate({end_rot}deg);opacity:0}}
    }}
    .p{i}{{animation:f{i} {duration}s ease-in-out infinite {delay}s}}''')
    
    color = random.choice(colors)
    rx = round(random.uniform(4.5, 9.5), 1)
    ry = round(rx * 0.55, 1)
    
    petals.append(f'''  <g class="p{i}"><ellipse cx="{start_x}" cy="{start_y}" rx="{rx}" ry="{ry}" fill="{color}" transform="rotate({start_rot} {start_x} {start_y})"/></g>''')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <style>
{chr(10).join(css)}
  </style>
  <defs>
    <radialGradient id="pink" cx="40%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#ffb7c5"/>
      <stop offset="100%" stop-color="#ff7b9c"/>
    </radialGradient>
    <radialGradient id="light" cx="35%" cy="25%" r="75%">
      <stop offset="0%" stop-color="#ffe4ec"/>
      <stop offset="100%" stop-color="#ffadc0"/>
    </radialGradient>
    <radialGradient id="green" cx="40%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#a8f0b0"/>
      <stop offset="100%" stop-color="#6dcf7a"/>
    </radialGradient>
  </defs>
{chr(10).join(petals)}
</svg>'''

with open('c:/Users/dheyn/Documents/02_Dev/necookienecookie/Necookie/.github/assets/sakura.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
