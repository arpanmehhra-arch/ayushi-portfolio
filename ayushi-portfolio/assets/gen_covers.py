#!/usr/bin/env python3
"""
Generates editorial-style SVG placeholder imagery for the portfolio,
in the site's own paper/ink/maroon/gold/sage palette. These are meant
to be swapped for real photography (from Ayushi's PDF exports) later —
file names and dimensions are kept stable so replacement is a drop-in.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

PAPER = "#F7F3EC"
PAPER_DIM = "#EFE9DD"
INK = "#1C1A17"
MAROON = "#7C2A2A"
MAROON_DEEP = "#5A1E1E"
GOLD = "#B8912E"
GOLD_SOFT = "#D9C48A"
SAGE = "#5B6B4F"
SAGE_SOFT = "#8A9A7C"
LINE = "rgba(28,26,23,0.16)"

def stitch_pattern(id_, color, opacity=0.5):
    return f'''
    <pattern id="{id_}" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="14" stroke="{color}" stroke-width="1.4" stroke-dasharray="4 4" opacity="{opacity}"/>
    </pattern>'''

def wrap(w, h, body, bg=PAPER):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
  <defs>{stitch_pattern('stitch', INK, 0.12)}</defs>
  <rect width="{w}" height="{h}" fill="{bg}"/>
  {body}
</svg>'''

def cover_card(filename, w, h, accent, label, sublabel, motif="arch"):
    """4:3-ish editorial cover card with a motif silhouette + type."""
    cx, cy = w/2, h/2
    motifs = {
        "arch": f'''
        <path d="M {w*0.30} {h*0.78} L {w*0.30} {h*0.42} A {w*0.20} {w*0.20} 0 0 1 {w*0.70} {h*0.42} L {w*0.70} {h*0.78}"
              fill="none" stroke="{accent}" stroke-width="2" opacity="0.55"/>
        <path d="M {w*0.38} {h*0.78} L {w*0.38} {h*0.50} A {w*0.12} {w*0.12} 0 0 1 {w*0.62} {h*0.50} L {w*0.62} {h*0.78}"
              fill="none" stroke="{accent}" stroke-width="1.4" opacity="0.35"/>''',
        "garment": f'''
        <path d="M {w*0.42} {h*0.30} L {w*0.36} {h*0.40} L {w*0.38} {h*0.82} L {w*0.62} {h*0.82} L {w*0.64} {h*0.40} L {w*0.58} {h*0.30}
                  Q {w*0.5} {h*0.24} {w*0.42} {h*0.30} Z" fill="none" stroke="{accent}" stroke-width="2" opacity="0.5"/>
        <line x1="{w*0.5}" y1="{h*0.30}" x2="{w*0.5}" y2="{h*0.82}" stroke="{accent}" stroke-width="1" opacity="0.3"/>''',
        "leaf": f'''
        <path d="M {w*0.5} {h*0.24} C {w*0.28} {h*0.34} {w*0.28} {h*0.66} {w*0.5} {h*0.82} C {w*0.72} {h*0.66} {w*0.72} {h*0.34} {w*0.5} {h*0.24} Z"
              fill="none" stroke="{accent}" stroke-width="2" opacity="0.5"/>
        <line x1="{w*0.5}" y1="{h*0.26}" x2="{w*0.5}" y2="{h*0.80}" stroke="{accent}" stroke-width="1" opacity="0.35"/>''',
        "pattern": f'''
        <rect x="{w*0.32}" y="{h*0.28}" width="{w*0.36}" height="{h*0.5}" fill="none" stroke="{accent}" stroke-width="2" opacity="0.5"/>
        <line x1="{w*0.32}" y1="{h*0.53}" x2="{w*0.68}" y2="{h*0.53}" stroke="{accent}" stroke-width="1" opacity="0.35"/>
        <line x1="{w*0.5}" y1="{h*0.28}" x2="{w*0.5}" y2="{h*0.78}" stroke="{accent}" stroke-width="1" opacity="0.35"/>''',
        "sword": f'''
        <line x1="{w*0.32}" y1="{h*0.72}" x2="{w*0.68}" y2="{h*0.32}" stroke="{accent}" stroke-width="3" opacity="0.5" stroke-linecap="round"/>
        <line x1="{w*0.40}" y1="{h*0.56}" x2="{w*0.50}" y2="{h*0.46}" stroke="{accent}" stroke-width="2" opacity="0.4"/>''',
        "denim": f'''
        <rect x="{w*0.30}" y="{h*0.30}" width="{w*0.4}" height="{h*0.46}" fill="none" stroke="{accent}" stroke-width="2" opacity="0.5"/>
        <line x1="{w*0.42}" y1="{h*0.30}" x2="{w*0.42}" y2="{h*0.76}" stroke="{accent}" stroke-width="1" stroke-dasharray="3 3" opacity="0.4"/>
        <line x1="{w*0.58}" y1="{h*0.30}" x2="{w*0.58}" y2="{h*0.76}" stroke="{accent}" stroke-width="1" stroke-dasharray="3 3" opacity="0.4"/>''',
    }
    body = f'''
    <rect x="0" y="0" width="{w}" height="{h}" fill="url(#stitch)"/>
    <rect x="14" y="14" width="{w-28}" height="{h-28}" fill="none" stroke="{INK}" stroke-width="1" opacity="0.18"/>
    {motifs.get(motif, motifs["arch"])}
    <text x="{w*0.5}" y="{h*0.9}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="{max(10,w*0.028)}" letter-spacing="2" fill="{INK}" opacity="0.55">{sublabel}</text>
    <text x="{w*0.5}" y="{h*0.14}" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="{max(13,w*0.04)}" fill="{accent}">{label}</text>
  '''
    svg = wrap(w, h, body)
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(svg)
    print("wrote", filename)


# ---- Work grid cover cards (4:3 @ 640x480) ----
cover_card("roots-cover.svg", 640, 480, MAROON, "Roots", "MENSWEAR — EMBROIDERED SHIRTING", "garment")
cover_card("pantaloons-cover.svg", 640, 480, GOLD, "Peregrine · 7alt · Ajile", "VISUAL MERCHANDISING", "arch")
cover_card("saree-cover.svg", 640, 480, SAGE, "Sustainable Saree", "UPCYCLED WOMENSWEAR", "leaf")
cover_card("clo3d-cover.svg", 640, 480, MAROON, "The Rathore Court", "CLO 3D COLLECTION", "pattern")
cover_card("costume-cover.svg", 640, 480, MAROON_DEEP, "Romeo & Juliet", "THEATRE COSTUME DESIGN", "sword")
cover_card("denim-cover.svg", 640, 480, "#3B4A63", "Inter — Wines Tradition", "SUSTAINABLE DENIM", "denim")

print("done")
