# Erzeugt Impressum, Datenschutz, AGB und Allergene als eigene Seiten.
# Platzhalter in <mark>…</mark> muss der Inhaber ausfüllen.
import sys, os
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "public")

def page(fname, title, body, extra=""):
    html = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · WIESN Lounge &amp; Bar</title>
<link rel="icon" href="logo-mark.png">
<link rel="stylesheet" href="seite.css">
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="index.html"><img src="logo-mark.png" alt="">WIESN</a><a class="back" href="index.html">← Zur Startseite</a></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap"><a href="index.html#menue">Speisekarte</a><a href="allergene.html">Allergene</a><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a><a href="agb.html">AGB &amp; Widerruf</a><span>Lindwurmstraße 139a · 80337 München</span></div></footer>
{extra}
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w").write(html)

M = lambda t: f"<mark>{t}</mark>"

page("impressum.html", "Impressum", f'''
<h1>Impressum</h1>
<p class="todo">Bitte die markierten Felder mit den echten Angaben des Betreibers ausfüllen. Diese Vorlage ersetzt keine Rechtsberatung.</p>
<h2>Angaben gemäß § 5 DDG</h2>
<p class="lead">WIESN Lounge &amp; Bar<br>Inhaber: Ghazi Hafiz<br>Lindwurmstraße 139a<br>80337 München</p>
<h2>Kontakt</h2>
<p>Telefon: +49 89 57877700<br>E-Mail: <a href="mailto:ghazihafiz@yahoo.com">ghazihafiz@yahoo.com</a></p>
<h2>Umsatzsteuer</h2>
<p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: {M("DE…")}</p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
<p>Ghazi Hafiz, Lindwurmstraße 139a, 80337 München</p>
<h2>Verbraucherstreitbeilegung</h2>
<p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Bild- und Videonachweis</h2>
<p>Fotos: Unsplash (Unsplash-Lizenz). Videos: Pexels (Pexels-Lizenz) und Mixkit (Mixkit Stock Video Free License). Logo: WIESN Lounge &amp; Bar.</p>
''')

page("datenschutz.html", "Datenschutz", f'''
<h1>Datenschutzerklärung</h1>
<p class="todo">Vorlage, abgestimmt auf die Technik dieser Website (Hosting, Stripe, Telegram/E-Mail an die Küche). Bitte Platzhalter ausfüllen und von einer fachkundigen Stelle prüfen lassen.</p>
<h2>1. Verantwortlicher</h2>
<p>WIESN Lounge &amp; Bar, Inhaber Ghazi Hafiz, Lindwurmstraße 139a, 80337 München, E-Mail: <a href="mailto:ghazihafiz@yahoo.com">ghazihafiz@yahoo.com</a>, Telefon: +49 89 57877700</p>
<h2>2. Aufruf der Website</h2>
<p>Beim Besuch verarbeitet unser Hosting-Anbieter {M("Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, USA")} technisch notwendige Daten (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browser). Das ist nötig, um die Website sicher auszuliefern (Art. 6 Abs. 1 lit. f DSGVO). Die Übermittlung in die USA erfolgt auf Grundlage des EU-US Data Privacy Framework bzw. von Standardvertragsklauseln.</p>
<h2>3. Bestellungen</h2>
<p>Wenn du bestellst, verarbeiten wir Name, Telefonnummer, bei Lieferung deine Adresse, optional deine E-Mail-Adresse, deine Hinweise und die bestellten Gerichte. Wir brauchen diese Daten, um deine Bestellung zuzubereiten, zu liefern und bei Rückfragen anzurufen (Art. 6 Abs. 1 lit. b DSGVO). Rechnungsrelevante Daten bewahren wir nach den gesetzlichen Fristen auf (Art. 6 Abs. 1 lit. c DSGVO, § 147 AO).</p>
<p>Damit die Bestellung sofort in der Küche ankommt, speichern wir sie für 3 Tage in unserem Bestellsystem bei Upstash Inc. (Serverstandort {M("Frankfurt am Main, EU")}) und zeigen sie auf dem Küchen-Bildschirm an bzw. drucken sie als Küchenbon aus. Zusätzlich wird sie übermittelt über {M("Telegram (Telegram Messenger Inc.) und/oder per E-Mail über Resend (Resend Inc., USA)")}. Nach 3 Tagen wird sie dort automatisch gelöscht.</p>
<h2>4. Online-Zahlung mit Stripe</h2>
<p>Bei Online-Zahlung wirst du zu Stripe weitergeleitet (Stripe Payments Europe Ltd., 1 Grand Canal Street Lower, Dublin 2, Irland). Stripe verarbeitet deine Zahlungsdaten selbst; wir erhalten keine Kartendaten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO. Mehr dazu: <a href="https://stripe.com/de/privacy" target="_blank" rel="noopener">stripe.com/de/privacy</a>.</p>
<h2 id="cookies">5. Cookies und lokale Speicherung</h2>
<p>Wir setzen keine Werbe- oder Analyse-Cookies. Dein Warenkorb und auf Wunsch deine Lieferadresse werden nur in deinem eigenen Browser gespeichert (lokaler Speicher), damit sie beim nächsten Besuch noch da sind. Das ist für den Bestellvorgang erforderlich (§ 25 Abs. 2 TDDDG). Du kannst diese Daten jederzeit löschen, indem du die Website-Daten in deinem Browser entfernst.</p>
<h2>6. Schriftarten</h2>
<p>{M("Die Schriftarten werden lokal von unserem Server geladen. (Falls noch Google Fonts eingebunden ist: vor dem Livegang lokal einbinden, siehe Anleitung.)")}</p>
<h2>7. Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO). Schreib uns dafür einfach an <a href="mailto:ghazihafiz@yahoo.com">ghazihafiz@yahoo.com</a>. Außerdem kannst du dich bei einer Datenschutz-Aufsichtsbehörde beschweren, zum Beispiel beim Bayerischen Landesamt für Datenschutzaufsicht.</p>
<p>Stand: {M("Monat Jahr")}</p>
''')

page("agb.html", "AGB & Widerruf", f'''
<h1>AGB &amp; Widerruf</h1>
<p class="todo">Vorlage für einen Liefer- und Abholservice. Bitte vom Betreiber prüfen lassen und an die eigenen Abläufe anpassen.</p>
<h2>1. Geltungsbereich</h2>
<p>Diese Bedingungen gelten für alle Bestellungen über diese Website bei WIESN Lounge &amp; Bar, Inhaber Ghazi Hafiz, Lindwurmstraße 139a, 80337 München.</p>
<h2>2. Vertragsschluss</h2>
<p>Die Speisekarte auf der Website ist noch kein verbindliches Angebot. Mit dem Klick auf „Zahlungspflichtig bestellen“ gibst du eine verbindliche Bestellung ab. Der Vertrag kommt zustande, wenn wir die Bestellung annehmen. Das zeigen wir dir mit der Bestellbestätigung auf der Website an.</p>
<h2>3. Preise</h2>
<p>Alle Preise sind Endpreise in Euro inklusive der gesetzlichen Mehrwertsteuer. Je nach Lieferzone kommt eine Liefergebühr hinzu, die vor der Bestellung angezeigt wird.</p>
<h2>4. Lieferung und Abholung</h2>
<p>Wir liefern in die auf der Website genannten Lieferzonen. Angegebene Lieferzeiten sind Durchschnittswerte und können zu Stoßzeiten abweichen. Bei Abholung liegt die Bestellung zur angegebenen Zeit in der Lindwurmstraße 139a bereit.</p>
<h2>5. Zahlung</h2>
<p>Du kannst bar, mit Karte bei Lieferung bzw. im Restaurant oder online über Stripe bezahlen. Bei Online-Zahlung wird der Betrag mit Abschluss der Bestellung belastet.</p>
<h2>6. Widerrufsrecht</h2>
<p>Ein Widerrufsrecht besteht nicht bei Verträgen über die Lieferung von Waren, die schnell verderben können, und über Speisen und Getränke, die zur sofortigen Zubereitung bestimmt sind (§ 312g Abs. 2 Nr. 2 BGB). Für deine Bestellung besteht daher kein Widerrufsrecht. Bei Problemen mit einer Bestellung melde dich bitte direkt bei uns.</p>
<h2>7. Allergene</h2>
<p>Die enthaltenen Allergene stehen bei jedem Gericht und gesammelt auf der <a href="allergene.html">Allergen-Seite</a>. In unserer Küche werden alle Zutaten verarbeitet, Spuren können wir daher nicht ausschließen.</p>
<h2>8. Jugendschutz</h2>
<p>{M("Falls alkoholische Getränke verkauft werden: Abgabe nur an Personen ab 16 bzw. 18 Jahren, Ausweiskontrolle bei Übergabe.")}</p>
<p>Stand: {M("Monat Jahr")}</p>
''')

page("allergene.html", "Allergene", '''
<h1>Allergene</h1>
<p class="lead">Alle Gerichte mit den enthaltenen Allergenen auf einen Blick. Wenn du eine Allergie hast, schreib es gern in den Hinweis bei deiner Bestellung.</p>
<div id="list"></div>
<p style="margin-top:28px">In unserer Küche werden alle Zutaten verarbeitet. Spuren anderer Allergene können wir nicht ausschließen.</p>
''', extra='''<script src="menu.js"></script>
<script>
(function(){
  var W=window.WIESN,h="";
  W.cats.forEach(function(c){
    h+='<h2>'+c.name+'</h2><div class="tw"><table><thead><tr><th>Nr.</th><th>Gericht</th><th>Allergene</th></tr></thead><tbody>';
    c.items.forEach(function(i){h+='<tr><td>'+i[0]+'</td><td>'+i[1]+'</td><td>'+(i[4]||'keine Hauptallergene')+'</td></tr>'});
    h+='</tbody></table></div>';
  });
  document.getElementById("list").innerHTML=h;
})();
</script>''')
print("ok")
