# Baut eine einzige, eigenständige HTML-Datei (Logo, Speisekarte, Rechtsseiten eingebettet).
import re, base64, sys, os
PUB = os.path.join(os.path.dirname(__file__), "..", "public")
out = sys.argv[1]
r = lambda f: open(os.path.join(PUB, f)).read()
b64 = lambda f: 'data:image/png;base64,' + base64.b64encode(open(os.path.join(PUB, f), 'rb').read()).decode()
s = open(sys.argv[2]).read() if len(sys.argv) > 2 else r('index.html')
s = s.replace('src="logo.png"', 'src="' + b64('logo.png') + '"').replace('url(logo.png)', 'url(' + b64('logo.png') + ')')
s = s.replace('src="logo-mark.png"', 'src="' + b64('logo-mark.png') + '"').replace('href="logo-mark.png"', 'href="' + b64('logo-mark.png') + '"')
MT = {'mp4': 'video/mp4', 'jpg': 'image/jpeg', 'webp': 'image/webp'}
s = re.sub(r'"((?:video|img)/[\w-]+\.(mp4|jpg|webp))"', lambda m: '"data:' + MT[m.group(2)] + ';base64,' + base64.b64encode(open(os.path.join(PUB, m.group(1)), 'rb').read()).decode() + '"', s)
s = s.replace('<script src="menu.js"></script>', '<script>\n' + r('menu.js') + '\n</script>')
pages = {f: re.search(r'<main class="wrap">(.*?)</main>', r(f + '.html'), re.S).group(1) for f in ['impressum', 'datenschutz', 'agb', 'allergene']}
tpl = ''.join(f'<template id="pg-{k}">{v}</template>' for k, v in pages.items())
overlay = '''<div id="pgOverlay" class="pg-ov" hidden role="dialog" aria-modal="true" aria-label="Information"><div class="pg-box"><button class="x pg-x" aria-label="Schließen">✕</button><div class="pg-body"></div></div></div>
''' + tpl + '''
<style>
.pg-ov{position:fixed;inset:0;z-index:95;background:rgba(0,0,0,.75);display:flex;justify-content:center;align-items:flex-start;overflow-y:auto;padding:calc(20px + env(safe-area-inset-top,0px)) 12px 40px}
.pg-ov[hidden]{display:none!important}
.pg-box{position:relative;width:min(820px,100%);background:#231e17;border:1px solid var(--line);border-radius:18px;padding:28px max(18px,4vw) 36px}
.pg-x{position:absolute;top:14px;right:14px;background:transparent;color:var(--cream)}
.pg-body h1{font-family:var(--f-display);font-weight:500;font-size:clamp(2rem,6vw,3rem);margin:0 0 8px;padding-right:44px}
.pg-body h2{font-family:var(--f-display);font-weight:500;font-size:1.35rem;margin:32px 0 6px;color:var(--gold-hi)}
.pg-body p,.pg-body li{color:var(--muted);max-width:68ch}
.pg-body .lead{color:var(--cream)}
.pg-body .todo{background:rgba(217,167,80,.12);border:1px dashed var(--gold);border-radius:12px;padding:12px 14px;color:var(--gold-hi);font-size:.9rem}
.pg-body mark{background:rgba(217,167,80,.22);color:var(--gold-hi);padding:0 .25em;border-radius:4px}
.pg-body a{color:var(--gold-hi)}
.pg-body table{width:100%;border-collapse:collapse;font-size:.92rem}
.pg-body .tw{overflow-x:auto}
.pg-body th,.pg-body td{text-align:left;padding:10px 8px 10px 0;border-bottom:1px solid var(--line);vertical-align:top}
.pg-body th{font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:500}
.pg-body td:first-child{color:var(--gold);width:3em}
</style>
<script>
(function(){
  var ov=document.getElementById("pgOverlay"),body=ov.querySelector(".pg-body");
  function allergens(){var h="";WIESN.cats.forEach(function(c){h+='<h2>'+c.name+'</h2><div class="tw"><table><thead><tr><th>Nr.</th><th>Gericht</th><th>Allergene</th></tr></thead><tbody>';c.items.forEach(function(i){h+='<tr><td>'+i[0]+'</td><td>'+i[1]+'</td><td>'+(i[4]||'keine Hauptallergene')+'</td></tr>'});h+='</tbody></table></div>'});return h}
  function show(name,hash){var t=document.getElementById("pg-"+name);if(!t)return false;body.innerHTML=t.innerHTML;var l=body.querySelector("#list");if(l)l.innerHTML=allergens();ov.hidden=false;document.body.style.overflow="hidden";ov.scrollTop=0;if(hash){var el=body.querySelector("#"+hash);if(el)el.scrollIntoView()}ov.querySelector(".pg-x").focus();return true}
  function close(){ov.hidden=true;document.body.style.overflow=""}
  ov.querySelector(".pg-x").onclick=close;ov.addEventListener("click",function(e){if(e.target===ov)close()});
  addEventListener("keydown",function(e){if(e.key==="Escape"&&!ov.hidden)close()});
  document.addEventListener("click",function(e){var a=e.target.closest("a[href]");if(!a)return;var h=a.getAttribute("href"),m=h.match(/^(impressum|datenschutz|agb|allergene)\\.html(?:#(\\w+))?$/);if(m&&show(m[1],m[2])){e.preventDefault()}else if(a.closest(".pg-body")&&/^index\\.html/.test(h)){e.preventDefault();close()}});
})();
</script>
'''
s = s.replace('\n</body>', overlay + '\n</body>') if '\n</body>' in s else s + overlay
assert not re.search(r'(src|href)="(logo|logo-mark)\.png"', s)
open(out, 'w').write(s)
print('single ok', len(s))
