import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kalkulator Born to Brand", layout="centered")

# Kod HTML/CSS/JS
calc_code = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root { --primary: #ffc200; --dark: #1a1a1a; --light: #f8f9fa; --shadow: 0 4px 20px rgba(0,0,0,0.08); }

        body { font-family: 'Poppins', sans-serif; background: transparent; color: var(--dark); margin: 0; padding: 10px; box-sizing: border-box; }

        .container { background: white; padding: 30px; border-radius: 16px; box-shadow: var(--shadow); max-width: 600px; margin: auto; position: relative; padding-bottom: 50px; }

        /* Nagłówki */
        h1 { text-align: center; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; font-size: 26px; line-height: 1.2; }
        h1 span { color: var(--primary); }
        
        .cennik-label { text-align: center; font-size: 18px; font-weight: 600; text-transform: uppercase; margin-bottom: 25px; color: #333; letter-spacing: 1px;}
        .subtitle { text-align: center; font-size: 15px; color: #555; margin-bottom: 20px; font-weight: 500; }

        /* Sekcje rozwijane (Accordions) */
        .section-box { border: 1px solid #eee; border-radius: 12px; margin-bottom: 15px; overflow: hidden; transition: 0.3s; }
        .section-box:hover { border-color: #ddd; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }

        summary { padding: 18px; background: #fff; cursor: pointer; font-weight: 600; display: flex; justify-content: space-between; align-items: center; list-style: none; user-select: none; font-size: 15px; }
        summary::-webkit-details-marker { display: none; }
        summary::after { content: '+'; font-size: 22px; color: var(--primary); transition: 0.3s; }
        details[open] summary::after { transform: rotate(45deg); }
        details[open] summary { border-bottom: 1px solid #f0f0f0; background: #fafafa; }

        .content { padding: 20px; background: #fff; }

        /* Pakiety Social Media */
        .presets-container { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px; }
        
        .btn-preset {
            background: #fff; border: 2px solid #eee; padding: 15px; border-radius: 12px;
            cursor: pointer; transition: 0.3s; text-align: center; position: relative;
        }
        .btn-preset:hover { border-color: #ddd; background: #fafafa; }
        .btn-preset.active { border-color: var(--primary); background: #fffdf5; box-shadow: 0 4px 12px rgba(255, 194, 0, 0.15); }
        
        .btn-preset strong { display: block; font-size: 14px; margin-bottom: 8px; text-transform: uppercase; }
        .btn-preset.full-width { grid-column: span 2; }

        .preset-list { font-size: 11px; color: #555; line-height: 1.6; margin: 0; padding: 0; list-style: none; }
        .preset-list li { border-bottom: 1px solid #f0f0f0; padding: 3px 0; }
        .preset-list li:last-child { border-bottom: none; }

        /* Inputy */
        label { display: block; margin-bottom: 6px; font-weight: 500; font-size: 13px; }
        input[type="number"], select, input[type="text"], input[type="email"], textarea {
            width: 100%; padding: 12px; border: 2px solid #eee; border-radius: 8px; 
            font-family: inherit; font-size: 14px; transition: 0.3s; box-sizing: border-box;
        }
        input:focus, select:focus, textarea:focus { border-color: var(--primary); outline: none; }
        textarea { resize: vertical; min-height: 80px; }

        /* Checkboxy */
        .checkbox-group { display: flex; flex-direction: column; gap: 5px; margin-top: 20px; background: #fffdf5; padding: 15px; border-radius: 10px; border: 1px solid #ffeeba; }
        .checkbox-row { display: flex; align-items: center; gap: 12px; cursor: pointer; font-weight: 500; font-size: 14px; margin: 0; }
        .checkbox-row input { width: 18px; height: 18px; accent-color: var(--primary); cursor: pointer; }
        .checkbox-hint { font-size: 10px; color: #999; margin-left: 34px; margin-bottom: 8px; }

        /* Mały druczek / Hinty */
        .hint-text { font-size: 11px; color: #666; margin-top: 15px; font-style: italic; line-height: 1.5; background: #f9f9f9; padding: 10px; border-radius: 6px; border-left: 3px solid var(--primary); }

        /* Przycisk Oblicz */
        .btn-calc {
            width: 100%; background: transparent; color: var(--dark); border: 2px solid var(--primary); padding: 16px;
            font-size: 16px; font-weight: 700; border-radius: 10px; cursor: pointer;
            text-transform: uppercase; letter-spacing: 0.5px; transition: 0.3s;
            margin-top: 20px;
        }
        .btn-calc:hover { background: var(--primary); color: #000; }

        /* Wynik */
        #result-section { 
            display: none; 
            margin-top: 40px; 
            padding-top: 20px; 
            border-top: 2px dashed #eee;
            animation: slideDown 0.5s ease-out;
        }
        @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

        .price-box {
            background: var(--dark); color: white; padding: 25px; border-radius: 12px;
            text-align: center; margin-bottom: 25px;
        }
        .price-label { font-size: 12px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.8; }
        .price-val { font-size: 32px; font-weight: 700; color: var(--primary); display: block; margin-top: 5px; }

        /* Kontakt i Formularz */
        .contact-box {
            text-align: center; margin-bottom: 25px; padding: 15px; border: 2px solid #000; border-radius: 10px;
            font-weight: 700; font-size: 16px; text-transform: uppercase;
        }
        /* Styl dla linku generowanego przez JS */
        .phone-link { color: var(--primary); text-decoration: none; display: block; font-size: 20px; margin-top: 5px; }

        .form-header { text-align: center; font-weight: 600; margin-bottom: 15px; font-size: 14px; color: #333; line-height: 1.5; }

        .btn-send {
            width: 100%; background: var(--primary); color: #000; border: none; padding: 16px;
            font-size: 16px; font-weight: 700; border-radius: 8px; cursor: pointer;
            text-transform: uppercase; transition: 0.3s; margin-top: 10px;
            box-shadow: 0 4px 10px rgba(255, 194, 0, 0.3);
        }
        .btn-send:hover { background: #e0aa00; transform: translateY(-2px); }
        .info-text { font-size: 11px; color: #999; margin-top: 10px; text-align: center; }
        
        input[type=number]::-webkit-inner-spin-button, 
        input[type=number]::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
    </style>
</head>
<body>

<div class="container">
    <h1>Born to <span>Brand</span></h1>
    <div class="cennik-label">Cennik usług</div>
    <div class="subtitle">Co potrzebujesz?</div>

    <input type="hidden" id="sm_price_val" value="0">
    <input type="hidden" id="sm_desc" value="">

    <details class="section-box" open>
        <summary>Prowadzenie Social Media</summary>
        <div class="content">
            <div class="presets-container">
                <div class="btn-preset" onclick="selectPackage(this, 400, 'Minimum', '2 Rolki, 2 Grafiki, 2 Relacje')">
                    <strong>Pakiet Minimum</strong>
                    <ul class="preset-list">
                        <li>2x Rolki (Reels)</li>
                        <li>2x Grafiki</li>
                        <li>2x Relacje (Stories)</li>
                    </ul>
                </div>
                <div class="btn-preset" onclick="selectPackage(this, 1000, 'Niski', '4 Rolki, 4 Grafiki, 4 Relacje')">
                    <strong>Pakiet Niski</strong>
                    <ul class="preset-list">
                        <li>4x Rolki (Reels)</li>
                        <li>4x Grafiki</li>
                        <li>4x Relacje (Stories)</li>
                    </ul>
                </div>
                <div class="btn-preset" onclick="selectPackage(this, 1500, 'Polecany', '8 Rolek, 4 Grafiki, 8 Relacji')">
                    <strong>Pakiet Polecany</strong>
                    <ul class="preset-list">
                        <li>8x Rolek (Reels)</li>
                        <li>4x Grafiki</li>
                        <li>8x Relacji (Stories)</li>
                    </ul>
                </div>
                <div class="btn-preset" onclick="selectPackage(this, 2000, 'Wysoki', '10 Rolek, 8 Grafik, 10 Relacji')">
                    <strong>Pakiet Wysoki</strong>
                    <ul class="preset-list">
                        <li>10x Rolek (Reels)</li>
                        <li>8x Grafik</li>
                        <li>10x Relacji (Stories)</li>
                    </ul>
                </div>
                <div class="btn-preset full-width" onclick="selectPackage(this, 0, 'Indywidualna', 'Wycena indywidualna')">
                    <strong>Inne - Wycena Indywidualna</strong>
                    <span style="font-size:11px; color:#555">Kliknij, aby poprosić o niestandardową ofertę</span>
                </div>
            </div>

            <div class="hint-text">
                W cenie miesięcznego pakietu: prowadzimy Twoje social media od A do Z. W tym: wykorzystujemy profesjonalny sprzęt foto/wideo, jesteśmy w stałym kontakcie ze zleceniodawcą, przygotowujemy comiesięczne raporty z wynikami, odpisujemy na komentarze i wiadomości.
            </div>
        </div>
    </details>

    <details class="section-box">
        <summary>Projektowanie Graficzne</summary>
        <div class="content">
            <label>Rodzaj projektu</label>
            <select id="gfx_type">
                <option value="0">Wybierz...</option>
                <option value="150">Baner / Ulotka</option>
                <option value="100">Wizytówka</option>
                <option value="100">Post Social Media (pojedynczy)</option>
            </select>
            <label style="margin-top:10px">Ilość sztuk</label>
            <input type="number" id="gfx_qty" min="0" placeholder="0" oninput="validity.valid||(value='');">
            
            <div class="hint-text">
                * Istnieje możliwość zlecenia druku (wycena indywidualna).
            </div>
        </div>
    </details>

    <details class="section-box">
        <summary>Tworzenie Filmów</summary>
        <div class="content">
            <label>Rodzaj filmu</label>
            <select id="vid_type">
                <option value="0">Wybierz...</option>
                <option value="200">Rolka do 30s</option>
                <option value="350">Rolka 30s-60s</option>
                <option value="450">Film 1-2 min</option>
                <option value="550">Film > 2 min</option>
            </select>
            <label style="margin-top:10px">Ilość filmów</label>
            <input type="number" id="vid_qty" min="0" placeholder="0" oninput="validity.valid||(value='');">
            
            <div class="hint-text">
                * Cena obejmuje nagranie wideo oraz profesjonalny montaż.
            </div>
        </div>
    </details>

    <div class="checkbox-group">
        <label class="checkbox-row">
            <input type="checkbox" id="drone"> 
            <span>Ujęcie z drona</span>
        </label>
        
        <label class="checkbox-row" style="margin-top:10px">
            <input type="checkbox" id="travel"> 
            <span>Zlecenie powyżej 60 km od Oświęcimia</span>
        </label>
        <div class="checkbox-hint">(dotyczy to realizacji na miejscu u klienta)</div>
    </div>

    <button class="btn-calc" onclick="showCalculation()">Oblicz szacunkowy koszt</button>

    <div id="result-section">

        <div class="price-box">
            <span class="price-label">Szacowana kwota zlecenia</span>
            <span class="price-val" id="total-display">0 zł</span>
        </div>

        <div class="contact-box">
            Masz pytania? Zadzwoń!
            <span id="secure-contact"></span>
        </div>
        
        <script>
            (function() {
                // Numer podzielony na części
                var p1 = "515";
                var p2 = "478";
                var p3 = "736";
                var el = document.getElementById('secure-contact');
                // Sklejenie i wstawienie linku
                el.innerHTML = '<a href="tel:+48' + p1 + p2 + p3 + '" class="phone-link">' + p1 + ' ' + p2 + ' ' + p3 + '</a>';
            })();
        </script>

        <div class="form-header">
            Wyślij zapytanie, a odezwiemy się do Ciebie jak najszybciej SMS-em oraz mailem.
        </div>

        <form action="https://formsubmit.co/eb22f98293c64af2624298419c9477ac" method="POST" target="_blank">
            <input type="hidden" name="_subject" value="Nowe Zapytanie - Born to Brand">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_template" value="table">
            
            <input type="hidden" name="Szczegóły_Zlecenia" id="hidden-details">
            <input type="hidden" name="Szacowana_Kwota" id="hidden-total">

            <div style="margin-bottom:10px"><input type="text" name="Klient" placeholder="Imię i Nazwisko / Firma" required></div>
            <div style="margin-bottom:10px"><input type="text" name="Telefon" placeholder="Telefon" required></div>
            <div style="margin-bottom:10px"><input type="email" name="Email" placeholder="E-mail" required></div>
            <div style="margin-bottom:15px"><textarea name="Wiadomosc" placeholder="Dodatkowe pytania / spostrzeżenia..."></textarea></div>

            <button type="submit" class="btn-send">Wyślij Zapytanie</button>
            <p class="info-text">Kliknięcie otworzy potwierdzenie w nowej karcie.</p>
        </form>
    </div>

</div>

<script>
    function resizeStreamlit() {
        const height = document.body.scrollHeight;
        const frame = window.frameElement;
        if (frame) { frame.style.height = height + 'px'; }
    }
    new ResizeObserver(resizeStreamlit).observe(document.body);

    function selectPackage(element, price, name, details) {
        document.querySelectorAll('.btn-preset').forEach(el => el.classList.remove('active'));
        
        let currentDesc = document.getElementById('sm_desc').value;
        let isSame = element.innerText.includes(name) && document.getElementById('sm_price_val').value == price;

        if(isSame && name !== 'Indywidualna') {
            document.getElementById('sm_price_val').value = 0;
            document.getElementById('sm_desc').value = "";
        } else {
            element.classList.add('active');
            document.getElementById('sm_price_val').value = price;
            if (name === 'Indywidualna') {
                 document.getElementById('sm_desc').value = "Social Media: Wycena Indywidualna";
            } else {
                 document.getElementById('sm_desc').value = `Pakiet ${name} (${details})`;
            }
        }
    }

    function showCalculation() {
        calculateLogic();
        document.getElementById('result-section').style.display = 'block';
        document.getElementById('result-section').scrollIntoView({ behavior: 'smooth' });
        resizeStreamlit();
    }

    function calculateLogic() {
        // SOCIAL MEDIA
        let smPrice = parseInt(document.getElementById('sm_price_val').value) || 0;
        let smDesc = document.getElementById('sm_desc').value;
        let isSmCustom = smDesc.includes("Indywidualna");

        // GRAFIKA
        let gfxBase = parseFloat(document.getElementById('gfx_type').value);
        let gfxName = document.getElementById('gfx_type').options[document.getElementById('gfx_type').selectedIndex].text;
        let gfxQty = parseInt(document.getElementById('gfx_qty').value) || 0;
        let gfxTotal = gfxBase * gfxQty;
        if(gfxQty > 1) gfxTotal *= 0.9; 

        // WIDEO
        let vidBase = parseFloat(document.getElementById('vid_type').value);
        let vidName = document.getElementById('vid_type').options[document.getElementById('vid_type').selectedIndex].text;
        let vidQty = parseInt(document.getElementById('vid_qty').value) || 0;
        let vidTotal = vidBase * vidQty;

        // DODATKI
        let useDrone = document.getElementById('drone').checked;
        let useTravel = document.getElementById('travel').checked;

        // Dron: tylko przy Grafikach i Wideo
        let droneBase = gfxTotal + vidTotal;
        let droneCost = 0;
        if (useDrone && droneBase > 0) {
            if (droneBase <= 1000) {
                droneCost = droneBase * 0.20;
            } else {
                droneCost = 200;
            }
        }

        // Dojazd: tylko przy Social Media i Wideo
        let travelBase = smPrice + vidTotal;
        let travelCost = 0;
        if (useTravel && travelBase > 0) {
            travelCost = travelBase * 0.15; 
        }

        let total = Math.round(smPrice + gfxTotal + vidTotal + droneCost + travelCost);
        let displayTotal = total + " zł";
        
        if (isSmCustom) {
            if (total > 0) {
                 displayTotal = total + " zł + Wycena SM";
            } else {
                 displayTotal = "Wycena Indywidualna";
            }
        }

        document.getElementById('total-display').innerText = displayTotal;
        document.getElementById('hidden-total').value = displayTotal;

        // Opis do formularza
        let desc = [];
        if (smDesc !== "") desc.push(smDesc);
        if (gfxQty > 0) desc.push(`${gfxName} x${gfxQty}`);
        if (vidQty > 0) desc.push(`${vidName} x${vidQty}`);
        if (useDrone) desc.push("+ Dron");
        if (useTravel) desc.push("+ Dojazd");
        document.getElementById('hidden-details').value = desc.join(" | ");
    }
</script>

</body>
</html>
"""

components.html(calc_code, height=1400, scrolling=False)
