"""Markdown -> HTML -> PDF via headless Chrome.

Chrome is used rather than a Python PDF library because the source contains
mermaid diagrams and raw HTML page-break divs: only a real browser renders
both correctly, and it gets CJK text and vector output for free.
"""
import re, sys, subprocess, pathlib, shutil, os

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2]).resolve()   # Chrome needs an absolute path
HTML = OUT.with_suffix(".html")

text = SRC.read_text(encoding="utf-8")

# ---- pull mermaid blocks out so the markdown parser cannot mangle them -----
blocks = []
def stash(m):
    blocks.append(m.group(1))
    return f"\n@@MERMAID{len(blocks)-1}@@\n"
text = re.sub(r"```mermaid\n(.*?)```", stash, text, flags=re.S)

# The source opens <div style="zoom: 0.85;"> and never closes it. python-markdown
# treats everything inside a block-level raw HTML element as raw HTML, so nothing
# after that line gets parsed as markdown. Strip the wrapper (zoom is applied via
# CSS on body instead) and turn the page-break divs into markers.
text = re.sub(r'<div style="zoom:[^"]*">', "", text)
text = re.sub(r'<div style="page-break-after:[^"]*"></div>', "\n\n@@PAGEBREAK@@\n\n", text)

# The English half writes sub-items as "* ..." at column 0 straight after a
# numbered item, with no blank line. Markdown reads those as a lazy paragraph
# continuation, so the asterisk prints literally. Indent them so they nest,
# which is how the Chinese half of the same document is already written.
lines, out, in_ol = text.split("\n"), [], False
for ln in lines:
    if re.match(r"^\d+\.\s", ln):
        in_ol = True
    elif in_ol and re.match(r"^\*\s+\S", ln):
        ln = "   - " + ln[2:].lstrip()
    elif in_ol and not ln.strip():
        pass                       # blank lines do not end the list here
    elif in_ol and not re.match(r"^[\s*\-]", ln):
        in_ol = False
    out.append(ln)
text = "\n".join(out)

# Insert the blank line markdown needs before a nested list that was written
# directly under a list item. This replaces the nl2br extension, which turned
# EVERY newline into a <br> and so broke prose lines wherever the source
# happened to wrap.
# python-markdown nests a sub-list only at 4-space indent; these documents use
# 3. Re-indent to multiples of 4 so sub-items nest under their parent instead
# of being swallowed into its paragraph. (This is why nl2br was needed before —
# it papered over the same problem while breaking every prose line.)
out = []
for ln in text.split("\n"):
    m = re.match(r"^( +)([-*+])(\s+)(\S.*)$", ln)
    if m:
        level = max(1, round(len(m.group(1)) / 3))
        ln = "    " * level + m.group(2) + " " + m.group(4)
    out.append(ln)
text = "\n".join(out)

import markdown
body = markdown.markdown(text, extensions=["extra", "sane_lists"])

for i, b in enumerate(blocks):
    # mermaid wants <br/> for line breaks; a literal \n inside a quoted label
    # is NOT a break and would print as the characters "\n"
    fixed = re.sub(r'(?<=")([^"]*?)\s*\\n\s*', lambda m: m.group(1) + "<br/>", b)
    holder = f"<pre class=\"mermaid\">{fixed.strip()}</pre>"
    body = body.replace(f"<p>@@MERMAID{i}@@</p>", holder).replace(f"@@MERMAID{i}@@", holder)

body = body.replace("<p>@@PAGEBREAK@@</p>", '<div class="pagebreak"></div>')
body = body.replace("@@PAGEBREAK@@", '<div class="pagebreak"></div>')

CJK = ('"Microsoft JhengHei", "Microsoft YaHei", "Noto Sans CJK TC", '
       '"PingFang TC", "Segoe UI Emoji"')     # emoji font for the callout marks
html = f"""<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<title>{SRC.stem}</title>
<style>
  @page {{ size: A4; margin: 16mm 15mm 14mm 15mm; }}
  html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  body {{ font-family: {CJK}, "Segoe UI", Arial, sans-serif;
         font-size: 11pt; line-height: 1.62; color: #15282D; margin: 0; }}
  h1, h2, h3 {{ break-inside: avoid; break-after: avoid; }}
  h1 {{ font-size: 19pt; margin: 0 0 .45em; padding-bottom: .28em;
       border-bottom: 2px solid #0E6A74; color: #0E6A74; }}
  h2 {{ font-size: 14.5pt; margin: 1em 0 .45em; color: #15282D; }}
  h3 {{ font-size: 12pt; margin: 1em 0 .4em; }}
  p  {{ margin: .45em 0; }}
  ol, ul {{ margin: .4em 0 .7em; padding-left: 1.5em; }}
  li {{ margin: .22em 0; }}
  ol > li {{ padding-left: .15em; }}
  li > ul, li > ol {{ margin: .25em 0 .35em; }}
  strong {{ color: #0E6A74; }}
  code {{ background: #F2F7F7; padding: .1em .35em; border-radius: 3px;
         font-family: Consolas, monospace; font-size: .92em; }}

  /* Tables: markdown gives no borders of its own, so they must be styled here
     or they print as bare floating text. */
  table {{ border-collapse: collapse; width: 100%; margin: .7em 0 1em;
          font-size: 9.6pt; break-inside: auto; }}
  thead {{ display: table-header-group; }}      /* repeat header across pages */
  tr {{ break-inside: avoid; }}
  th, td {{ border: .8px solid #C3D6D8; padding: .38em .55em;
           text-align: left; vertical-align: top; line-height: 1.45; }}
  th {{ background: #0E6A74; color: #fff; font-weight: 700; border-color: #0E6A74; }}
  /* CJK breaks between any two characters, so a narrow label column splits
     words like 納入 down the middle. Keep the label column on one line. */
  th:first-child, td:first-child {{ white-space: nowrap; }}
  tbody tr:nth-child(even) td {{ background: #F6FAFA; }}
  td code {{ background: #E9F1F1; }}

  blockquote {{ margin: .7em 0; padding: .5em .8em; background: #F2F7F7;
               border-radius: 4px; break-inside: avoid; }}
  blockquote p {{ margin: .25em 0; }}
  hr {{ border: none; border-top: 1px solid #D6E2E3; margin: 1.1em 0; }}
  pre.mermaid {{ background: none; text-align: center; margin: .6em 0 .8em;
                break-inside: avoid; }}
  /* A4 content box is 267mm tall; leave room for the heading above so the
     diagram never gets bumped onto a page of its own. */
  pre.mermaid svg {{ max-width: 100% !important; width: auto !important;
                    max-height: 190mm; height: auto; }}
  .pagebreak {{ break-after: page; }}
  /* NB: no CSS `zoom` anywhere. Zoom desyncs mermaid's text measurement from
     its layout, which clips every node label. The source's zoom:0.85 is
     honoured by using smaller type instead. */
</style></head><body>
{body}
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({{ startOnLoad: false, theme: 'base', securityLevel: 'loose',
    fontFamily: '{CJK}, Segoe UI, Arial, sans-serif',
    flowchart: {{ useMaxWidth: true, padding: 12 }},
    themeVariables: {{ fontSize: '15px', primaryColor: '#E3F0F1',
      primaryBorderColor: '#0E6A74', primaryTextColor: '#15282D',
      lineColor: '#4A8F97', clusterBkg: '#F7FAFA', clusterBorder: '#C3D6D8' }} }});
  await mermaid.run({{ querySelector: 'pre.mermaid' }});
  document.title = 'RENDER_DONE';
</script></body></html>"""

HTML.write_text(html, encoding="utf-8")
print("html ->", HTML)

# ---- print to PDF -----------------------------------------------------------
chrome = next((p for p in [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
] if os.path.exists(p)), None)
if not chrome:
    sys.exit("no Chrome or Edge found")

cmd = [chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
       "--allow-file-access-from-files",
       "--virtual-time-budget=25000",          # let mermaid + the CDN finish
       "--no-pdf-header-footer",
       f"--print-to-pdf={OUT}", HTML.resolve().as_uri()]
r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
if r.returncode != 0 and r.stderr.strip():
    print(r.stderr.strip()[-600:])

if OUT.exists():
    print(f"OK  {OUT}  ({OUT.stat().st_size/1024:.0f} KB)")
    if "--keep-html" not in sys.argv:
        HTML.unlink(missing_ok=True)      # intermediate file, not a deliverable
else:
    sys.exit("FAILED: no PDF produced (chrome exit %d)" % r.returncode)
