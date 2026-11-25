"""Build es/index.html from index.html and i18n/es.json. Run after every change to index.html."""
import json, re, os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = json.load(open(os.path.join(ROOT, "i18n", "es.json")))
src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

def tr_text(m):
    raw = m.group(1); key = html.unescape(" ".join(raw.split()))
    if key in T:
        lead = raw[:len(raw) - len(raw.lstrip())]; trail = raw[len(raw.rstrip()):]
        return ">" + lead + T[key] + trail + "<"
    return m.group(0)

head, sep, rest = src.partition("<body>")
parts = re.split(r"(<script.*?</script>|<style.*?</style>)", rest, flags=re.S)
for i in range(0, len(parts), 2):
    parts[i] = re.sub(r">([^<>]+)<", tr_text, parts[i])
body = "".join(parts)
out = head + sep + body

def tr_attr(m):
    name, val = m.group(1), m.group(2)
    return f'{name}="{T.get(val, val)}"'
out = re.sub(r'\b(content|aria-label|alt|title)="([^"]*)"', tr_attr, out)
out = re.sub(r"<title>(.*?)</title>", lambda m: f"<title>{T.get(m.group(1), m.group(1))}</title>", out)

def fix_path(m):
    attr, val = m.group(1), m.group(2)
    if re.match(r"(https?:|#|/|mailto:|\.\./|data:)", val): return m.group(0)
    return f'{attr}="../{val}"'
out = re.sub(r'\b(href|src)="([^"]*)"', fix_path, out)
out = out.replace('<html lang="en"', '<html lang="es"', 1)
out = out.replace('href="https://vestival.es/" ', 'href="https://vestival.es/es/" ')
out = out.replace('<link rel="canonical" href="https://vestival.es/" />', '<link rel="canonical" href="https://vestival.es/es/" />')
out = out.replace('content="https://vestival.es/" />', 'content="https://vestival.es/es/" />')
out = out.replace('<a href="/" class="nav-logo">', '<a href="/es/" class="nav-logo">')
out = out.replace('<a class="lang-switch" href="/es/" hreflang="es" lang="es">ES</a>', '<a class="lang-switch" href="/" hreflang="en" lang="en">EN</a>')
os.makedirs(os.path.join(ROOT, "es"), exist_ok=True)
open(os.path.join(ROOT, "es", "index.html"), "w", encoding="utf-8").write(out)
srcbody = re.sub(r"<script.*?</script>|<style.*?</style>", "", src.partition("<body>")[2], flags=re.S)
left = [k for k in sorted(set(html.unescape(" ".join(x.split())) for x in re.findall(r">([^<>]+)<", srcbody))) if re.search(r"[a-z]{4}", k) and k not in T]
print("es/index.html written. Untranslated text nodes:", len(left))
for k in left: print("  ", k[:90])
