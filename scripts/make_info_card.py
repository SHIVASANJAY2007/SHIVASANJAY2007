import os
import html

def make_info_card(out_path):
    canvas_w = 490
    canvas_h = 387
    pad = 18
    titlebar_h = 28
    bg = "#0d1117"
    bg2 = "#111722"
    frame = "#30363d"
    title_text = "#7d8590"
    ink = "#c9d1d9"
    accent = "#58a6ff"

    content = [
        ("shiva@github", "-------------------------"),
        ("Role", "AI & Web Developer | Trainer | Sportsman"),
        ("Stack", "React, Node.js, Python, PostgreSQL, Prisma"),
        ("Now", "Building scalable full-stack & ERP systems"),
        ("Sport", "Kho-Kho Player & Team Captain"),
        ("Projects", "Zyvox AI, Fitlee, INGRES"),
        ("Education", "B.Tech @ Kongu Engineering College"),
    ]

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_w}" height="{canvas_h}" viewBox="0 0 {canvas_w} {canvas_h}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        f'<defs><linearGradient id="wbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{bg2}"/><stop offset="1" stop-color="{bg}"/></linearGradient></defs>',
        f'<rect width="{canvas_w}" height="{canvas_h}" rx="12" fill="url(#wbg)"/>',
        f'<rect x="0.5" y="0.5" width="{canvas_w-1}" height="{canvas_h-1}" rx="12" fill="none" stroke="{frame}" stroke-width="1"/>',
        f'<line x1="0" y1="{titlebar_h}" x2="{canvas_w}" y2="{titlebar_h}" stroke="{frame}"/>',
    ]

    for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        p.append(f'<circle cx="{pad + i*15}" cy="{titlebar_h/2}" r="4.5" fill="{dot}"/>')
    
    p.append(f'<text x="{canvas_w/2}" y="{titlebar_h/2 + 4}" fill="{title_text}" font-size="11.5" text-anchor="middle">shiva@github: ~$ neofetch</text>')
    
    y = titlebar_h + 40
    line_h = 24
    reveal = 1.6
    step = 0.2

    # Title
    p.append(f'<g opacity="0"><text x="{pad}" y="{y}" fill="{accent}" font-size="14" font-weight="bold">{content[0][0]}</text><set attributeName="opacity" to="1" begin="{reveal}s"/></g>')
    y += line_h
    p.append(f'<g opacity="0"><text x="{pad}" y="{y}" fill="{title_text}" font-size="14">{content[0][1]}</text><set attributeName="opacity" to="1" begin="{reveal + step}s"/></g>')
    y += line_h + 10

    # Key-Values
    delay = reveal + step * 2
    for k, v in content[1:]:
        p.append(f'<g opacity="0">')
        p.append(f'<text x="{pad}" y="{y}" fill="{accent}" font-size="14" font-weight="bold">{k}</text>')
        p.append(f'<text x="{pad + 90}" y="{y}" fill="{ink}" font-size="14">{html.escape(v)}</text>')
        p.append(f'<set attributeName="opacity" to="1" begin="{delay:.1f}s"/>')
        p.append(f'</g>')
        y += line_h
        delay += step

    p.append("</svg>")

    with open(out_path, "w") as f:
        f.write("".join(p))
    print(f"wrote {out_path}")

if __name__ == "__main__":
    make_info_card(os.path.join(os.path.dirname(__file__), "..", "info-card.svg"))
