#!/usr/bin/env python3
"""Draw the 26 November 2026 world-news front page as a 1024x1024 PNG.

The image is drawn entirely with Pillow from the story data below: no
downloaded or copied artwork. Run: python3 generate.py
Writes entry.png next to this file.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 36
PAPER = (247, 243, 234)
INK = (27, 27, 27)
CARD = (255, 253, 247)
BORDER = (216, 210, 196)
RED = (179, 38, 30)
NAVY = (31, 58, 95)
ORANGE = (194, 87, 11)
MAROON = (91, 35, 51)
TEAL = (47, 93, 80)
GOLD = (122, 92, 0)
GREY = (110, 105, 92)
BODY = (60, 58, 50)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(bold, size):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


# (tag, headline, summary, accent colour, icon kind)
STORIES = [
    ("MIDDLE EAST · OIL", "Houthis claim strikes on Saudi refinery",
     "Brent crude tops $94 as Yemen's Houthis say they hit Ras Tanura and Riyadh.",
     RED, "oil"),
    ("TRADE · USA", "US unveils sweeping new tariffs",
     "New duties on 14 partners, incl. China, the EU and Brazil; Taiwan faces up to 15%.",
     NAVY, "bars"),
    ("EGYPT", "Cairo ring-road inferno kills 30",
     "A fuel tanker crash ignites a huge fire on the highway around the capital.",
     ORANGE, "flame"),
    ("UKRAINE WAR", "Russia's own toll nears 500,000",
     "Russia's own figures put its Ukraine war dead at nearly 500,000.",
     MAROON, "poppy"),
    ("SPACE", "BepiColombo reaches Mercury",
     "Europe-Japan probe enters orbit after an eight-year voyage to the smallest planet.",
     TEAL, "planet"),
    ("SPORT", "15-year-old smashes cricket record",
     "Vaibhav Sooryavanshi hits 204 off 53 balls, the fastest List A double century.",
     GOLD, "ball"),
]

ALSO = ("Thanksgiving in the US  •  India: Constitution Day, 18 years since the 26/11 "
        "Mumbai attacks  •  Duran Duran guitarist Andy Taylor dies at 65  •  "
        "World Chess Championship, Game 2 ends in a draw")


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit in width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_icon(d, kind, x, y, s, color):
    cx, cy = x + s / 2, y + s / 2
    if kind == "oil":
        d.polygon([(cx, y + 2), (x + s - 3, y + s * 0.55), (x + 3, y + s * 0.55)],
                  fill=color)
        d.ellipse([x + 3, y + s * 0.40, x + s - 3, y + s - 2], fill=color)
        d.ellipse([x + s * 0.32, y + s * 0.55, x + s * 0.48, y + s * 0.75],
                  fill=(255, 255, 255))
    elif kind == "bars":
        bw = s * 0.22
        for i, hfrac in enumerate((0.45, 0.68, 1.0)):
            bx = x + i * (bw + 4)
            bh = s * hfrac
            d.rectangle([bx, y + s - bh, bx + bw, y + s],
                        fill=color if i < 2 else RED)
    elif kind == "flame":
        d.ellipse([x + 6, y + s * 0.30, x + s - 6, y + s - 2], fill=(232, 110, 20))
        d.polygon([(cx, y + 2), (x + s - 8, y + s * 0.62), (x + 8, y + s * 0.62)],
                  fill=(232, 110, 20))
        d.ellipse([x + s * 0.30, y + s * 0.52, x + s * 0.70, y + s - 6],
                  fill=(245, 196, 66))
    elif kind == "poppy":
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            d.ellipse([cx - 13 + dx * 13, cy - 13 + dy * 13,
                       cx + 13 + dx * 13, cy + 13 + dy * 13], fill=(200, 40, 40))
        d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(30, 30, 30))
    elif kind == "planet":
        d.ellipse([x + 4, y + 4, x + s - 4, y + s - 4], fill=(120, 130, 140))
        for ox, oy, r in ((-8, -6, 4), (8, 2, 5), (-2, 10, 3)):
            d.ellipse([cx + ox - r, cy + oy - r, cx + ox + r, cy + oy + r],
                      fill=(90, 100, 110))
        d.arc([x - 6, y - 2, x + s + 6, y + s + 2], start=200, end=340,
              fill=color, width=3)
    elif kind == "ball":
        d.ellipse([x + 4, y + 4, x + s - 4, y + s - 4], fill=(178, 34, 34))
        d.arc([x + 10, y + 2, x + s - 2, y + s - 10], start=300, end=120,
              fill=(255, 255, 255), width=3)
        d.arc([x + 2, y + 10, x + s - 10, y + s - 2], start=120, end=300,
              fill=(255, 255, 255), width=3)


def draw_card(d, x, y, w, h, story):
    tag, head, summ, color, icon = story
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                        outline=BORDER, width=2)
    px, py = x + 16, y + 14
    d.text((px, py), tag, font=font(True, 17), fill=color)
    draw_icon(d, icon, x + w - 16 - 52, y + 12, 52, color)
    headf = font(True, 28)
    lines = wrap(d, head, headf, w - 32 - 62)
    hy = py + 26
    for ln in lines[:2]:
        d.text((px, hy), ln, font=headf, fill=INK)
        hy += 33
    sumf = font(False, 20)
    slines = wrap(d, summ, sumf, w - 32)
    sy = hy + 6
    for ln in slines[:3]:
        d.text((px, sy), ln, font=sumf, fill=BODY)
        sy += 25


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead: the day it sums up, front and centre.
    titlef = font(True, 58)
    title = "THE WORLD IN ONE DAY"
    d.text(((W - d.textlength(title, font=titlef)) / 2, 30), title,
           font=titlef, fill=INK)
    d.rectangle([MARGIN, 104, W - MARGIN, 109], fill=RED)
    datef = font(True, 36)
    date = "THURSDAY 26 NOVEMBER 2026"
    d.text(((W - d.textlength(date, font=datef)) / 2, 118), date,
           font=datef, fill=RED)
    d.rectangle([MARGIN, 168, W - MARGIN, 170], fill=INK)

    # Six stories, two columns by three rows.
    cw, ch, gap = 468, 224, 16
    for i, story in enumerate(STORIES):
        cx = MARGIN + (i % 2) * (cw + gap)
        cy = 186 + (i // 2) * (ch + gap)
        draw_card(d, cx, cy, cw, ch, story)

    # Footer: more of the day, then a source note.
    fy = 906
    d.rectangle([MARGIN, fy, W - MARGIN, fy + 2], fill=INK)
    d.text((MARGIN, fy + 10), "ALSO TODAY", font=font(True, 20), fill=NAVY)
    items = wrap(d, ALSO, font(False, 19), W - 2 * MARGIN)
    yy = fy + 36
    for ln in items[:2]:
        d.text((MARGIN, yy), ln, font=font(False, 19), fill=BODY)
        yy += 24
    credit = "Drawn from wire and press reports of 26 November 2026"
    cf = font(False, 14)
    d.text(((W - d.textlength(credit, font=cf)) / 2, 1002), credit,
           font=cf, fill=GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote", out, os.path.getsize(out), "bytes", img.size)


if __name__ == "__main__":
    main()
