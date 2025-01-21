# 📚 Quiz Clash

Ett textbaserat äventyrsspel med en 2D-överbild där du slåss mot lärare genom att svara rätt på deras frågor – eller möta konsekvenserna!

---

## 🎮 Om spelet

I **Quiz Clash** måste du använda dina kunskaper och strategi för att besegra skolans lärare. Utforska en enkel 2D-vy av skolan, där varje lärare väntar med frågor. Spelet är turn-baserat och fylld med val som leder till olika utfall.

- 💰 **Belöning:** Varje vinst ger dig coins som kan användas för att låsa upp speciallådor med överraskningar.  
- 🏆 **Mål:** Upplev 4 olika slut baserade på dina val och prestationer.  
- 👑 **Utmaning:** Ta dig hela vägen till bossläraren Lars och visa att du är den smartaste i skolan!

---

## 🔑 Funktioner

- **Textbaserad spelmekanik:** Läs och svara på lärares frågor direkt i spelets textgränssnitt.  
- **2D-överbild:** Utforska skolan med en enkel 2D-karta där du möter olika lärare.  
- **Turn-based fighting:** Turas om att attackera och försvara i strid mot lärare om du svarar fel.  
- **Frågor och svar:** 5 unika frågor från lärare – rätt svar hjälper dig undvika strid!  
- **Flera lärare:** Möte med 6 olika lärare, alla med olika teman och styrkor.  
- **Bossfight:** Stå öga mot öga mot Lars, den tuffaste läraren av dem alla.  
- **Flera slut:** Upplev 3–4 olika slut baserade på dina prestationer.  
- **Samla coins:** Tjäna pengar genom att vinna och lås upp lådor med överraskningar.

---

## 🛠️ Installation

Så här öppnar du och kör spelet "Quiz_clash":

1. **Ladda ner spelet**
   - Besök projektets GitHub-sida.
   - Leta upp och klicka på knappen **"Code"** (ofta grön och finns längst upp till höger).
   - Välj alternativet **"Download ZIP"** för att ladda ner hela projektet som en zip-fil.
   - Packa upp den nedladdade filen till en mapp på din dator.

2. **Kontrollera att du har Python installerat**
   - Öppna en terminal eller kommandoprompt.
   - Skriv följande kommando:
     ```bash
     python --version
     ```
     eller
     ```bash
     python3 --version
     ```
   - Om du inte får en version av Python (exempel: Python 3.x.x), behöver du ladda ner och installera Python 3 från [python.org](https://www.python.org).

3. **Installera beroenden**
   - Öppna terminalen och navigera till mappen där du packade upp spelet. Exempel:
     ```bash
     cd /sökväg/till/Quiz_clash
     ```
   - Kör sedan följande kommando för att installera det nödvändiga paketet:
     ```bash
     pip install windows-curses
     ```

4. **Starta spelet**
   - I samma terminal, kör följande kommando:
     ```bash
     python spel.py
     ```
   - Spelet kommer nu att startas och du kan börja spela! 🎮

### Vanliga problem och lösningar:
- **Python-kommandot fungerar inte:**
  - Använd `python3` istället för `python`.
  - Kontrollera att Python finns i din PATH.

- **Felmeddelande om beroenden:**
  - Se till att du kör `pip install windows-curses` innan du startar spelet.

- **Spelet startar inte:**
  - Kontrollera att du befinner dig i samma mapp som filen `spel.py` när du kör kommandot.
  - Om allt är förberett som det ska, Zooma ut i terminalen. Om terminalen är FÖR inzoomad kan inte spelet fungera.

Lycka till! 🚀
