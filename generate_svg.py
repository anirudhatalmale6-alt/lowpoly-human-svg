#!/usr/bin/env python3
"""
Generate a premium low-poly female human body SVG (front view).
Uses separate contour strips for each body part to ensure proper separation.
"""
import random
random.seed(42)

def color_for_position(cx, cy, region, tri=None):
    palette_highlight = ['#F5D7C0', '#F2D4BC', '#F0D0B8', '#EDD0B6', '#F4D2B8']
    palette_mid = ['#E8C4A0', '#E5C19E', '#EBC9AE', '#E8C5A8', '#E2C0A0']
    palette_shadow = ['#DDB892', '#DAB58E', '#D4A574', '#D1A270', '#D8B48C']
    palette_deep = ['#C9976A', '#C69470', '#C19068', '#BE8E65', '#B88C62']
    palette_hair = ['#3D2B1F', '#42301E', '#4A3528', '#352518', '#4E3A2C', '#45332A', '#3A2A1C', '#5C4033']

    # Facial feature colors - subtle, not dramatic
    palette_eye = ['#A07860', '#956E58', '#B08870', '#9A7462']
    palette_lip = ['#CC8E82', '#C48878', '#D49A8E', '#C89080']
    palette_brow = ['#B8977E', '#AD8C74', '#C0A088']

    if region == 'hair':
        return random.choice(palette_hair)

    # Facial features detection for head region
    if region == 'head' and tri:
        # Eye regions - small, subtle
        if 66 <= cy <= 76:
            if (176 <= cx <= 186) or (214 <= cx <= 224):
                return random.choice(palette_eye)
        # Eyebrow hint
        if 60 <= cy <= 66:
            if (176 <= cx <= 186) or (214 <= cx <= 224):
                return random.choice(palette_brow)
        # Nose bridge shadow
        if 80 <= cy <= 94 and 196 <= cx <= 204:
            return random.choice(palette_shadow)
        # Lip region
        if 100 <= cy <= 108 and 194 <= cx <= 206:
            return random.choice(palette_lip)

    body_cx = 200
    dist = abs(cx - body_cx) / 60
    y_factor = (cy - 30) / 600

    # More dramatic random variation for visible faceting
    shade = dist * 0.45 + y_factor * 0.15 + random.uniform(-0.25, 0.25)

    if shade < 0.2:
        return random.choice(palette_highlight)
    elif shade < 0.45:
        return random.choice(palette_mid)
    elif shade < 0.7:
        return random.choice(palette_shadow)
    else:
        return random.choice(palette_deep)

def triangulate_strip(slices):
    """Connect adjacent slices into triangles. Each slice is (y, [x_values])."""
    triangles = []
    for i in range(len(slices) - 1):
        y1, xs1 = slices[i]
        y2, xs2 = slices[i + 1]
        j1, j2 = 0, 0
        while j1 < len(xs1) - 1 or j2 < len(xs2) - 1:
            if j1 >= len(xs1) - 1:
                triangles.append(((xs2[j2], y2), (xs2[j2+1], y2), (xs1[j1], y1)))
                j2 += 1
            elif j2 >= len(xs2) - 1:
                triangles.append(((xs1[j1], y1), (xs1[j1+1], y1), (xs2[j2], y2)))
                j1 += 1
            else:
                m1 = (xs1[j1] + xs1[j1+1]) / 2
                m2 = (xs2[j2] + xs2[j2+1]) / 2
                if m1 <= m2:
                    triangles.append(((xs1[j1], y1), (xs1[j1+1], y1), (xs2[j2], y2)))
                    j1 += 1
                else:
                    triangles.append(((xs2[j2], y2), (xs2[j2+1], y2), (xs1[j1], y1)))
                    j2 += 1
    return triangles

# ============================================================
# BODY PART DEFINITIONS
# Each part: list of (y, [x_values left to right])
# ============================================================

# HAIR (shoulder-length, drapes around head)
hair_left = [
    (22, [188, 195]),
    (30, [172, 182]),
    (40, [164, 174]),
    (52, [158, 168]),
    (65, [154, 165]),
    (80, [152, 162]),
    (95, [150, 160]),
    (110, [150, 160]),
    (125, [152, 162]),
    (140, [154, 164]),
    (155, [158, 168]),
]

hair_right = [
    (22, [205, 212]),
    (30, [218, 228]),
    (40, [226, 236]),
    (52, [232, 242]),
    (65, [235, 246]),
    (80, [238, 248]),
    (95, [240, 250]),
    (110, [240, 250]),
    (125, [238, 248]),
    (140, [236, 246]),
    (155, [232, 242]),
]

hair_top = [
    (18, [190, 200, 210]),
    (22, [180, 190, 200, 210, 220]),
    (28, [172, 183, 194, 200, 206, 217, 228]),
    (36, [166, 178, 190, 200, 210, 222, 234]),
    (45, [162, 175, 188, 200, 212, 225, 238]),
]

# HEAD (face)
head = [
    (45, [168, 180, 190, 200, 210, 220, 232]),
    (54, [166, 178, 188, 200, 212, 222, 234]),
    (62, [164, 176, 186, 194, 200, 206, 214, 224, 236]),
    (70, [164, 175, 184, 192, 200, 208, 216, 225, 236]),
    (78, [165, 176, 184, 192, 200, 208, 216, 224, 235]),
    (86, [166, 177, 186, 194, 200, 206, 214, 223, 234]),
    (94, [168, 178, 188, 196, 200, 204, 212, 222, 232]),
    (102, [170, 180, 190, 197, 200, 203, 210, 220, 230]),
    (110, [174, 183, 192, 198, 200, 202, 208, 217, 226]),
    (118, [178, 186, 194, 200, 206, 214, 222]),
    (126, [182, 190, 196, 200, 204, 210, 218]),
]

# NECK
neck = [
    (126, [184, 192, 200, 208, 216]),
    (133, [184, 192, 200, 208, 216]),
    (140, [182, 190, 200, 210, 218]),
    (148, [180, 190, 200, 210, 220]),
]

# TORSO (shoulders down to groin)
torso = [
    (148, [178, 188, 196, 200, 204, 212, 222]),
    (155, [166, 178, 190, 200, 210, 222, 234]),
    (162, [156, 168, 180, 192, 200, 208, 220, 232, 244]),
    (170, [150, 162, 176, 188, 200, 212, 224, 238, 250]),
    # Chest
    (180, [152, 164, 176, 188, 200, 212, 224, 236, 248]),
    (190, [154, 166, 178, 188, 200, 212, 222, 234, 246]),
    (200, [156, 168, 178, 190, 200, 210, 222, 232, 244]),
    (212, [158, 168, 178, 190, 200, 210, 222, 232, 242]),
    # Ribcage narrowing
    (224, [160, 170, 180, 190, 200, 210, 220, 230, 240]),
    (236, [162, 172, 182, 192, 200, 208, 218, 228, 238]),
    # Waist (narrowest)
    (250, [166, 175, 184, 192, 200, 208, 216, 225, 234]),
    (262, [164, 174, 184, 192, 200, 208, 216, 226, 236]),
    # Lower abdomen
    (275, [162, 172, 182, 192, 200, 208, 218, 228, 238]),
    (288, [160, 170, 180, 192, 200, 208, 220, 230, 240]),
    # Hips (wider)
    (300, [158, 168, 180, 192, 200, 208, 220, 232, 242]),
    (312, [158, 168, 180, 192, 200, 208, 220, 232, 242]),
    (322, [160, 170, 182, 194, 200, 206, 218, 230, 240]),
    # Groin area - start narrowing to leg split
    (332, [164, 174, 184, 194, 200, 206, 216, 226, 236]),
    (340, [168, 178, 188, 196, 200, 204, 212, 222, 232]),
]

# LEFT ARM (upper + forearm + hand) - wider for better visibility
left_arm = [
    (170, [136, 144, 152]),
    (180, [132, 140, 148, 154]),
    (192, [130, 138, 146, 154]),
    (205, [128, 136, 144, 152]),
    (218, [126, 134, 142, 150]),
    (232, [124, 132, 140, 148]),
    (246, [122, 130, 138, 146]),
    (260, [122, 130, 138, 146]),
    (274, [122, 130, 138, 146]),
    (288, [122, 130, 138, 146]),
    (302, [124, 132, 140]),
    (316, [124, 132, 140]),
    (330, [126, 134, 140]),
    (344, [128, 135, 142]),
    (356, [130, 136, 142]),
    (366, [130, 136, 142]),
    (376, [132, 138, 144]),
    (386, [134, 140, 146]),
    (394, [136, 142, 148]),
]

# RIGHT ARM
right_arm = [
    (170, [248, 256, 264]),
    (180, [246, 252, 260, 268]),
    (192, [246, 254, 262, 270]),
    (205, [248, 256, 264, 272]),
    (218, [250, 258, 266, 274]),
    (232, [252, 260, 268, 276]),
    (246, [254, 262, 270, 278]),
    (260, [254, 262, 270, 278]),
    (274, [254, 262, 270, 278]),
    (288, [254, 262, 270, 278]),
    (302, [260, 268, 276]),
    (316, [260, 268, 276]),
    (330, [260, 266, 274]),
    (344, [258, 265, 272]),
    (356, [258, 264, 270]),
    (366, [258, 264, 270]),
    (376, [256, 262, 268]),
    (386, [254, 260, 266]),
    (394, [252, 258, 264]),
]

# LEFT LEG (thigh + calf + foot)
left_leg = [
    (340, [168, 178, 188, 196]),
    (350, [166, 176, 186, 196]),
    (362, [164, 174, 184, 194]),
    (376, [162, 172, 182, 194]),
    (390, [162, 172, 182, 194]),
    (405, [162, 172, 182, 192]),
    (420, [164, 172, 182, 192]),
    (435, [164, 173, 182, 190]),
    # Knee
    (448, [166, 174, 182, 190]),
    (458, [166, 174, 182, 190]),
    # Calf
    (472, [168, 175, 182, 190]),
    (488, [168, 176, 183, 190]),
    (504, [170, 176, 183, 190]),
    (520, [170, 177, 184, 190]),
    (538, [172, 178, 184, 190]),
    (555, [172, 178, 184, 190]),
    (572, [174, 179, 184, 190]),
    (586, [174, 180, 185, 190]),
    # Ankle
    (598, [174, 180, 186, 192]),
    # Foot
    (606, [170, 178, 186, 194]),
    (614, [166, 176, 186, 196]),
    (622, [162, 174, 186, 196]),
    (628, [160, 172, 184, 196]),
]

# RIGHT LEG
right_leg = [
    (340, [204, 212, 222, 232]),
    (350, [204, 214, 224, 234]),
    (362, [206, 216, 226, 236]),
    (376, [206, 218, 228, 238]),
    (390, [206, 218, 228, 238]),
    (405, [208, 218, 228, 238]),
    (420, [208, 218, 228, 236]),
    (435, [210, 218, 227, 236]),
    # Knee
    (448, [210, 218, 226, 234]),
    (458, [210, 218, 226, 234]),
    # Calf
    (472, [210, 218, 225, 232]),
    (488, [210, 217, 224, 232]),
    (504, [210, 217, 224, 230]),
    (520, [210, 216, 223, 230]),
    (538, [210, 216, 222, 228]),
    (555, [210, 216, 222, 228]),
    (572, [210, 216, 221, 226]),
    (586, [210, 215, 220, 226]),
    # Ankle
    (598, [208, 214, 220, 226]),
    # Foot
    (606, [206, 214, 222, 230]),
    (614, [204, 214, 224, 234]),
    (622, [204, 216, 226, 238]),
    (628, [204, 216, 228, 240]),
]

# ============================================================
# Build SVG
# ============================================================

parts = {
    'hair': [
        ('hair-top', hair_top, 'hair'),
        ('hair-left', hair_left, 'hair'),
        ('hair-right', hair_right, 'hair'),
    ],
    'head': [('head', head, 'head')],
    'neck': [('neck', neck, 'neck')],
    'torso': [('torso', torso, 'torso')],
    'arm-left': [('arm-left', left_arm, 'left-arm')],
    'arm-right': [('arm-right', right_arm, 'right-arm')],
    'leg-left': [('leg-left', left_leg, 'left-leg')],
    'leg-right': [('leg-right', right_leg, 'right-leg')],
}

region_labels = {
    'hair': 'Hair', 'head': 'Head', 'neck': 'Neck',
    'torso': 'Torso', 'left-arm': 'Left Arm', 'right-arm': 'Right Arm',
    'left-leg': 'Left Leg', 'right-leg': 'Right Leg',
}

def torso_region(cy):
    if cy < 170: return 'Shoulder'
    if cy < 225: return 'Upper Torso'
    if cy < 280: return 'Lower Torso'
    return 'Hips'

def arm_region(cy, side):
    if cy < 260: return f'{side} Upper Arm'
    if cy < 350: return f'{side} Forearm'
    return f'{side} Hand'

def leg_region(cy, side):
    if cy < 460: return f'{side} Thigh'
    if cy < 600: return f'{side} Calf'
    return f'{side} Foot'

def get_label(cx, cy, part_type):
    if part_type == 'hair': return 'Hair'
    if part_type == 'head': return 'Head'
    if part_type == 'neck': return 'Neck'
    if part_type == 'torso': return torso_region(cy)
    if part_type == 'left-arm': return arm_region(cy, 'Left')
    if part_type == 'right-arm': return arm_region(cy, 'Right')
    if part_type == 'left-leg': return leg_region(cy, 'Left')
    if part_type == 'right-leg': return leg_region(cy, 'Right')
    return part_type

svg_lines = []
svg_lines.append('    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 650" fill="none">')

total_count = 0

for group_id, strips in parts.items():
    svg_lines.append(f'      <g id="{group_id}">')
    for strip_id, slices, part_type in strips:
        tris = triangulate_strip(slices)
        total_count += len(tris)
        for tri in tris:
            cx = (tri[0][0] + tri[1][0] + tri[2][0]) / 3
            cy = (tri[0][1] + tri[1][1] + tri[2][1]) / 3
            region_for_color = 'hair' if part_type == 'hair' else part_type
            fill = color_for_position(cx, cy, region_for_color, tri)
            label = get_label(cx, cy, part_type)
            pts = ' '.join(f'{p[0]},{p[1]}' for p in tri)
            svg_lines.append(f'        <polygon class="facet" data-region="{label}" points="{pts}" fill="{fill}"/>')
    svg_lines.append('      </g>')

svg_lines.append('    </svg>')
svg_content = '\n'.join(svg_lines)

print(f"Total triangles: {total_count}")

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Low-Poly Female — Front View</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Outfit:wght@200;300;400&display=swap');

  *{{margin:0;padding:0;box-sizing:border-box}}

  body{{
    background:#07060e;
    min-height:100vh;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    overflow-x:hidden;
    position:relative;
    font-family:'Outfit',sans-serif;
    color:#e8ddd0;
  }}

  body::before{{
    content:'';
    position:fixed;
    inset:0;
    background:
      radial-gradient(ellipse 60% 50% at 50% 45%, rgba(180,140,110,0.06) 0%, transparent 70%),
      radial-gradient(ellipse 40% 30% at 30% 30%, rgba(120,80,60,0.04) 0%, transparent 60%),
      radial-gradient(ellipse 35% 40% at 70% 65%, rgba(100,70,50,0.03) 0%, transparent 60%);
    pointer-events:none;
    z-index:0;
  }}

  .page-wrapper{{
    position:relative;
    z-index:1;
    display:flex;
    flex-direction:column;
    align-items:center;
    padding:40px 20px 60px;
  }}

  .title-block{{
    text-align:center;
    margin-bottom:24px;
  }}

  .title-block h1{{
    font-family:'Cormorant Garamond',serif;
    font-weight:300;
    font-size:clamp(1.6rem,3.5vw,2.4rem);
    letter-spacing:0.15em;
    text-transform:uppercase;
    color:#d4bfa8;
    margin-bottom:6px;
  }}

  .title-block .subtitle{{
    font-family:'Outfit',sans-serif;
    font-weight:200;
    font-size:0.75rem;
    letter-spacing:0.35em;
    text-transform:uppercase;
    color:rgba(200,180,160,0.4);
  }}

  .svg-container{{
    position:relative;
    width:clamp(320px,55vw,500px);
    filter:drop-shadow(0 0 80px rgba(180,140,110,0.08));
    animation:breathe 6s ease-in-out infinite;
  }}

  @keyframes breathe{{
    0%,100%{{filter:drop-shadow(0 0 80px rgba(180,140,110,0.08))}}
    50%{{filter:drop-shadow(0 0 100px rgba(180,140,110,0.14))}}
  }}

  .svg-container svg{{
    width:100%;
    height:auto;
    display:block;
  }}

  .facet{{
    stroke:rgba(30,25,20,0.18);
    stroke-width:0.3;
    stroke-linejoin:round;
    transition:filter 0.25s ease, stroke 0.3s ease, stroke-width 0.3s ease;
    cursor:pointer;
  }}
  .facet:hover{{
    filter:brightness(1.2) saturate(1.1);
    stroke:rgba(220,200,180,0.4);
    stroke-width:0.6;
  }}
  .facet.active{{
    filter:brightness(1.3) saturate(1.15);
    stroke:rgba(240,210,180,0.65);
    stroke-width:1;
  }}

  .tooltip{{
    position:fixed;
    pointer-events:none;
    background:rgba(12,10,18,0.92);
    border:1px solid rgba(200,170,140,0.25);
    color:#d4bfa8;
    font-family:'Outfit',sans-serif;
    font-weight:300;
    font-size:0.7rem;
    letter-spacing:0.12em;
    text-transform:uppercase;
    padding:6px 14px;
    border-radius:2px;
    opacity:0;
    transition:opacity 0.2s ease;
    z-index:100;
    white-space:nowrap;
  }}
  .tooltip.visible{{opacity:1}}

  .region-label{{
    display:inline-block;
    color:rgba(200,180,160,0.3);
    font-size:0.6rem;
    letter-spacing:0.2em;
    text-transform:uppercase;
    margin-top:20px;
    font-weight:200;
  }}

  .stats{{
    margin-top:12px;
    color:rgba(200,180,160,0.2);
    font-size:0.55rem;
    letter-spacing:0.15em;
    text-transform:uppercase;
    font-weight:200;
  }}
</style>
</head>
<body>

<div class="page-wrapper">
  <div class="title-block">
    <h1>Low-Poly Female &mdash; Front View</h1>
    <div class="subtitle">Interactive SVG Topology &bull; Beauty-Tech Series</div>
  </div>

  <div class="svg-container">
{svg_content}
  </div>

  <span class="region-label">Hover to explore &bull; Click to select</span>
  <span class="stats">{total_count} polygons &bull; Pure vector &bull; Transparent background</span>
</div>

<div class="tooltip" id="tooltip"></div>

<script>
(function(){{
  const tooltip = document.getElementById('tooltip');
  let activeFacet = null;

  document.querySelectorAll('.facet').forEach(facet => {{
    facet.addEventListener('mouseenter', e => {{
      tooltip.textContent = facet.getAttribute('data-region');
      tooltip.classList.add('visible');
    }});

    facet.addEventListener('mousemove', e => {{
      tooltip.style.left = (e.clientX + 14) + 'px';
      tooltip.style.top = (e.clientY - 10) + 'px';
    }});

    facet.addEventListener('mouseleave', () => {{
      tooltip.classList.remove('visible');
    }});

    facet.addEventListener('click', e => {{
      e.stopPropagation();
      if(activeFacet) activeFacet.classList.remove('active');
      if(activeFacet === facet){{ activeFacet = null; return; }}
      facet.classList.add('active');
      activeFacet = facet;
    }});
  }});

  document.addEventListener('click', () => {{
    if(activeFacet){{ activeFacet.classList.remove('active'); activeFacet = null; }}
  }});
}})();
</script>
</body>
</html>'''

with open('/var/lib/freelancer/projects/40461616/demo.html', 'w') as f:
    f.write(html)

print("HTML written to demo.html")
