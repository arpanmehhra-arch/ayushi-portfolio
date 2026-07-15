#!/usr/bin/env python3
"""
Generates placeholder PDF documents for every document link used in the
portfolio, so the in-browser viewer never hits a dead link out of the box.
Ayushi should replace each file (same filename) with her real PDF export —
see README.md in the project root for exact steps.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

OUT = os.path.dirname(os.path.abspath(__file__))

INK = HexColor("#1C1A17")
MAROON = HexColor("#7C2A2A")
PAPER = HexColor("#F7F3EC")
GREY = HexColor("#4A443C")

def make_placeholder(filename, title, subtitle, note_lines):
    path = os.path.join(OUT, filename)
    c = canvas.Canvas(path, pagesize=A4)
    w, h = A4

    c.setFillColor(PAPER)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    # top rule
    c.setStrokeColor(INK)
    c.setLineWidth(1)
    c.line(25*mm, h-30*mm, w-25*mm, h-30*mm)

    c.setFillColor(MAROON)
    c.setFont("Helvetica", 9)
    c.drawString(25*mm, h-24*mm, "AYUSHI KANOJIYA — FASHION DESIGN PORTFOLIO")

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(25*mm, h-48*mm, title)

    c.setFillColor(GREY)
    c.setFont("Helvetica", 12)
    c.drawString(25*mm, h-58*mm, subtitle)

    c.setStrokeColor(INK)
    c.line(25*mm, h-66*mm, w-25*mm, h-66*mm)

    y = h - 82*mm
    c.setFont("Helvetica", 10.5)
    for line in note_lines:
        c.setFillColor(GREY)
        c.drawString(25*mm, y, line)
        y -= 7*mm

    c.setFillColor(MAROON)
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(25*mm, 30*mm, "Replace this file with the real PDF export — keep the exact filename shown above.")

    c.showPage()
    c.save()
    print("wrote", filename)


docs = [
    ("Ayushi_Kanojiya_Resume.pdf", "Resume", "Ayushi Kanojiya — Fashion Design Student", [
        "This is a placeholder for Ayushi's resume PDF.",
        "",
        "To replace: export the resume (Resume__2_.pdf) as a PDF and save it",
        "into the /pdfs folder with the exact filename:",
        "  Ayushi_Kanojiya_Resume.pdf",
    ]),
    ("Internship_report_Roots.pdf", "Internship Report — Roots", "Roots by Sujata Agrawal", [
        "Placeholder for the full Roots internship report PDF",
        "(offer letter, certificate, feedback & recommendation letters).",
        "",
        "Replace with: Internship_report_compressed.pdf",
        "Save as: Internship_report_Roots.pdf",
    ]),
    ("Pantaloons_Visual_Merchandising.pdf", "Visual Merchandising Portfolio", "Pantaloons — Six Brand Displays", [
        "Placeholder for the Pantaloons Visual Merchandising portfolio PDF.",
        "",
        "Replace with: pantaloons_work_as_a_Visual_Merchandiser_compressed.pdf",
        "Save as: Pantaloons_Visual_Merchandising.pdf",
    ]),
    ("Sustainable_Saree_Fashion.pdf", "Sustainable Saree Fashion", "Concept, Mood Board & Spec Sheet", [
        "Placeholder for the Sustainable Saree Fashion project PDF.",
        "",
        "Replace with: sustainable_saree_compressed.pdf",
        "Save as: Sustainable_Saree_Fashion.pdf",
    ]),
    ("CLO3D_Rathore_Court.pdf", "CLO 3D Collection Development", "Durbar — The Rathore Court", [
        "Placeholder for the CLO 3D collection development PDF.",
        "",
        "Replace with: clo_3d_compressed.pdf",
        "Save as: CLO3D_Rathore_Court.pdf",
    ]),
    ("Costume_Design_Romeo_Juliet.pdf", "Costume Design", "Romeo & Juliet — Theatre & Film Costume", [
        "Placeholder for the Romeo & Juliet costume design PDF.",
        "",
        "Replace with: Costume_makeing_compressed.pdf",
        "Save as: Costume_Design_Romeo_Juliet.pdf",
    ]),
    ("Sustainable_Denim_Collection.pdf", "Inter — Wines Tradition", "Sustainable Denim Collection", [
        "Placeholder for the Sustainable Denim Collection PDF.",
        "",
        "Replace with: DENIM_COLLECTION_compressed.pdf",
        "Save as: Sustainable_Denim_Collection.pdf",
    ]),
]

for fname, title, subtitle, notes in docs:
    make_placeholder(fname, title, subtitle, notes)

print("done —", len(docs), "placeholder PDFs written")
