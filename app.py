import streamlit as st
import streamlit.components.v1 as components

# 1. Layout wide
st.set_page_config(page_title="Kalkulator Born to Brand", layout="wide")

# 2. CSS Hack
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

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

        body { font-family: 'Poppins', sans-serif; background: transparent; color: var(--dark); margin: 0; padding: 0; box-sizing: border-box; }

        .container { 
            background: white; 
            padding: 20px 15px; 
            border-radius: 12px; 
            box-shadow: var(--shadow); 
            width: 100%; 
            max-width: 600px; 
            margin: auto; 
            position: relative; 
            padding-bottom: 50px; 
        }

        h1 { text-align: center; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; font-size: 24px; line-height: 1.2; }
        h1 span { color: var(--primary); }
        
        .cennik-label { text-align: center; font-size: 16px; font-weight: 600; text-transform: uppercase; margin-bottom: 20px; color: #333; letter-spacing: 1px;}
        .subtitle { text-align: center; font-size: 14px; color: #555; margin-bottom: 20px; font-weight: 500; }

        .section-box { border: 1px solid #eee; border-radius: 12px; margin-bottom: 12px; overflow: hidden; transition: 0.3s; }
        
        summary { padding: 15px; background: #fff; cursor: pointer; font-weight: 600; display: flex; justify-content: space-between; align-items: center; list-style: none; user-select: none; font-size: 14px; }
        summary::-webkit-details-marker { display: none; }
        summary::after { content: '+'; font-size: 20px; color: var(--primary); transition: 0.3s; }
        details[open] summary::after { transform: rotate(45deg); }
        details[open] summary { border-bottom: 1px solid #f0f0f0; background: #fafafa; }

        .content { padding: 15px; background: #fff; }

        /* Pakiety Social Media */
        .presets-container { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 10px; }
        
        .btn-preset {
            background: #fff; border: 2px solid #eee; padding: 12px 5px; border-radius: 10px;
            cursor: pointer; transition: 0.3s; text-align: center; position: relative;
        }
        .btn-preset:hover { border-color: #ddd; background: #fafafa; }
        .btn-preset.active { border-color: var(--primary); background: #fffdf5; box-shadow: 0 4px 12px rgba(255, 194, 0, 0.15); }
        
        .btn-preset strong { display: block; font-size: 13px; margin-bottom: 5px; text-transform: uppercase; }
        .btn-preset.full-width { grid-column: span 2; }

        .preset-list { font-size: 10px; color: #555; line-height: 1.5; margin: 0; padding: 0; list-style: none; }
        .preset-list li { border-bottom: 1px solid #f0f0f0; padding: 2px 0; }
        .preset-list li:last-child { border-bottom: none; }

        /* Inputy */
        label { display: block; margin-bottom: 4px; font-weight: 500; font-size: 13px; }
        input[type="number"], select, input[type="text"], input[type="email"], textarea {
            width: 100%; padding: 12px; border: 2px solid #eee; border-radius: 8px; 
            font-family: inherit; font-size: 14px; transition: 0.3s; box-sizing: border-box;
        }
        input:focus, select:focus, textarea:focus { border-color: var(--primary); outline: none; }
        textarea { resize: vertical; min-height: 80px; }

        /* Checkboxy */
        .checkbox-group { display: flex; flex-direction: column; gap: 5px; margin-top: 20px; background: #fffdf5; padding: 15px; border-radius: 10px; border: 1px solid #ffeeba; }
        .checkbox-row { display: flex; align-items: center; gap: 10px; cursor: pointer; font-weight: 500; font-size: 13px; margin: 0; }
        .checkbox-row input { width: 18px; height: 18px; accent-color: var(--primary); cursor: pointer; flex-shrink: 0; }
        .checkbox-hint { font-size: 10px; color: #999; margin-left: 30px; margin-bottom: 8px; line-height: 1.2; }

        .hint-text { font-size: 11px; color: #666; margin-top: 15px; font-style: italic; line-height: 1.4; background: #f9f9f9; padding: 10px; border-radius: 6px; border-left: 3px solid var(--primary); }

        /* Custom Hints (ukryte domyślnie) */
        .custom-hint-box {
            display: none;
            font-size: 11px; color: #555; background: #fff3cd; 
            padding: 10px; border-radius: 6px; margin-top: 10px; line-height: 1.4; border: 1px solid #ffeeba;
        }

        /* Stylizacja listy dodanych elementów */
        .added-items-list { margin-top: 15px; border-top: 1px solid #eee; padding-top: 10px; }
        .added-item { 
            display: flex; justify-content: space-between; align-items: center; 
            background: #f8f9fa; padding: 8px 12px; border-radius: 6px; margin-bottom: 6px; font-size: 13px;
        }
        .added-item .remove-btn { color: red; cursor: pointer; font-weight: bold; margin-left: 10px; font-size: 16px; }
        
        /* Przycisk Dodaj Pozycję */
        .btn-add-item {
            background: #333; color: #fff; border: none; padding: 10px; width: 100%;
            border-radius: 8px; margin-top: 10px; cursor: pointer; font-size: 13px; text-transform: uppercase;
        }
        .btn-add-item:hover { background: #555; }

        .btn-calc {
            width: 100%; background: transparent; color: var(--dark); border: 2px solid var(--primary); padding: 15px;
            font-size: 15px; font-weight: 700; border-radius: 10px; cursor: pointer;
            text-transform: uppercase; letter-spacing: 0.5px; transition: 0.3s;
            margin-top: 20px;
        }
        .btn-calc:hover { background: var(--primary); color: #000; }

        #result-section { 
            display: none; 
            margin-top: 30px; 
            padding-top: 20px; 
            border-top: 2px dashed #eee;
            animation: slideDown 0.5s ease-out;
        }
        @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

        .price-box {
            background: var(--dark); color: white; padding: 20px; border-radius: 12px;
            text-align: center; margin-bottom: 20px;
        }
        .price-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.8; }
        .price-val { font-size: 24px; font-weight: 700; color: var(--primary); display: block; margin-top: 5px; line-height: 1.2; }

        .contact-box {
            text-align: center; margin-bottom: 20px; padding: 15px; border: 2px solid #000; border-radius: 10px;
            font-weight: 700; font-size: 15px; text-transform: uppercase;
        }
        .phone-link { color: var(--primary); text-decoration: none; display: block; font-size: 18px; margin-top: 5px; }

        .form-header { text-align: center; font-weight: 600; margin-bottom: 15px; font-size: 13px; color: #333; line-height: 1.4; }

        .btn-send {
            width: 100%; background: var(--primary); color: #000; border: none; padding: 16px;
            font-size: 16px; font-weight: 700; border-radius: 8px; cursor: pointer;
            text-transform: uppercase; transition: 0.3s; margin-top: 5px;
            box-shadow: 0 4px 10px rgba(255, 194, 0, 0.3);
        }
        .btn-send:hover { background: #e0aa00; transform: translateY(-2px); }
        .info-text { font-size: 10px; color: #999; margin-top: 10px; text-align: center; }
        
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
                <div class="btn-preset full-width" onclick="selectPackage(this, 0, 'INNE', 'Wycena indywidualna')">
                    <strong>INNE</strong>
                </div>
            </div>

            <div id="sm-custom-hint" class="custom-hint-box">
                Twoje oczekiwania nie spełnia żaden z pakietów? Zaznacz tę opcję, na dole strony kliknij <b>OBLICZ SZACUNKOWY KOSZT</b> oraz w formularzu napisz co oczekujesz, a my odeślemy wycenę na maila i smsem!
            </div>

            <div class="hint-text">
                W cenie miesięcznego pakietu: prowadzimy Twoje social media od A do Z. W tym: wykorzystujemy profesjonalny sprzęt foto/wideo, jesteśmy w stałym kontakcie ze zleceniodawcą, przygotowujemy comiesięczne raporty z wynikami, odpisujemy na komentarze i wiadomości.
            </div>
        </div>
    </details>

    <details class="section-box">
        <summary>Projektowanie Graficzne</summary>
        <div class="content">
            <label>Dodaj pozycję do wyceny:</label>
            <select id="gfx_type" onchange="checkGfxOther()">
                <option value="0">Wybierz...</option>
                <option value="150">Baner</option>
                <option value="150">Ulotka</option>
                <option value="100">Wizytówka</option>
                <option value="100">Grafika Social Media</option>
                <option value="0">Inne</option>
            </select>

            <div id="gfx-custom-hint" class="custom-hint-box">
                Twoje oczekiwania nie spełnia żaden z podpunktów? Zaznacz tę opcję, na dole strony kliknij <b>OBLICZ SZACUNKOWY KOSZT</b> oraz w formularzu napisz co oczekujesz, a my odeślemy wycenę na maila i smsem!
            </div>

            <label style="margin-top:10px">Ilość sztuk</label>
            <input type="number" id="gfx_qty" min="0" placeholder="0" oninput="validity.valid||(value='');">
            
            <button class="btn-add-item" onclick="addGfxItem()">+ Dodaj kolejną pozycję</button>

            <div id="gfx-list" class="added-items-list" style="display:none;"></div>
            
            <label class="checkbox-row" style="margin-top:15px; border-top: 1px dashed #eee; padding-top:10px;">
                <input type="checkbox" id="gfx_print">
                <span>Zlecam również druk</span>
            </label>
        </div>
    </details>

    <details class="section-box">
        <summary>Tworzenie Filmów</summary>
        <div class="content">
            <label>Dodaj pozycję do wyceny:</label>
            <select id="vid_type" onchange="checkVidOther()">
                <option value="0">Wybierz...</option>
                <option value="200">Rolka do 30s</option>
                <option value="350">Rolka 30s-60s</option>
                <option value="450">Film 1-2 min</option>
                <option value="550">Film > 2 min</option>
                <option value="0">Inne</option>
            </select>

            <div id="vid-custom-hint" class="custom-hint-box">
                Twoje oczekiwania nie spełnia żaden z podpunktów? Zaznacz tę opcję, na dole strony kliknij <b>OBLICZ SZACUNKOWY KOSZT</b> oraz w formularzu napisz co oczekujesz, a my odeślemy wycenę na maila i smsem!
            </div>

            <label style="margin-top:10px">Ilość filmów</label>
            <input type="number" id="vid_qty" min="0" placeholder="0" oninput="validity.valid||(value='');">
            
            <button class="btn-add-item" onclick="addVidItem()">+ Dodaj kolejną pozycję</button>

            <div id="vid-list" class="added-items-list" style="display:none;"></div>
            
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
                var p1 = "515";
                var p2 = "478";
                var p3 = "736";
                var el = document.getElementById('secure-contact');
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
    // --- VARIABLES TO STORE MULTI-SELECT ITEMS ---
    let graphicsList = [];
    let videoList = [];

    function resizeStreamlit() {
        const height = document.body.scrollHeight;
        const frame = window.frameElement;
        if (frame) { frame.style.height = height + 'px'; }
    }
    new ResizeObserver(resizeStreamlit).observe(document.body);

    // --- SOCIAL MEDIA LOGIC (Toggle functionality) ---
    function selectPackage(element, price, name, details) {
        // Sprawdź czy ten element jest już aktywny
        if (element.classList.contains('active')) {
            // ODZNACZ (Deselect)
            element.classList.remove('active');
            document.getElementById('sm_price_val').value = 0;
            document.getElementById('sm_desc').value = "";
            document.getElementById('sm-custom-hint').style.display = 'none';
        } else {
            // ZAZNACZ (Select new)
            // Najpierw usuń klasę active ze wszystkich
            document.querySelectorAll('.btn-preset').forEach(el => el.classList.remove('active'));
            
            // Dodaj do klikniętego
            element.classList.add('active');
            document.getElementById('sm_price_val').value = price;
            
            // Obsługa INNE
            let hintBox = document.getElementById('sm-custom-hint');
            if (name === 'INNE') {
                 document.getElementById('sm_desc').value = "Social Media: Wycena Indywidualna (INNE)";
                 hintBox.style.display = 'block';
            } else {
                 document.getElementById('sm_desc').value = `Pakiet ${name} (${details})`;
                 hintBox.style.display = 'none';
            }
        }
        resizeStreamlit();
    }

    // --- GRAPHICS LOGIC ---
    function checkGfxOther() {
        let sel = document.getElementById('gfx_type');
        let text = sel.options[sel.selectedIndex].text;
        let hint = document.getElementById('gfx-custom-hint');
        
        if (text === "Inne") {
            hint.style.display = 'block';
        } else {
            hint.style.display = 'none';
        }
        resizeStreamlit();
    }

    function addGfxItem() {
        let sel = document.getElementById('gfx_type');
        let qtyInput = document.getElementById('gfx_qty');
        let price = parseFloat(sel.value);
        let name = sel.options[sel.selectedIndex].text;
        let qty = parseInt(qtyInput.value);

        if (sel.value === "0" && name !== "Inne") {
            alert("Wybierz rodzaj projektu!"); 
            return;
        }
        if ((!qty || qty <= 0) && name !== "Inne") {
            alert("Podaj ilość!"); 
            return;
        }
        if (name === "Inne") qty = 1;

        graphicsList.push({ name: name, price: price, qty: qty, isOther: (name === "Inne") });
        
        // Reset
        sel.value = "0";
        qtyInput.value = "";
        checkGfxOther(); // ukryj hint po dodaniu
        renderList('gfx');
    }

    // --- VIDEO LOGIC ---
    function checkVidOther() {
        let sel = document.getElementById('vid_type');
        let text = sel.options[sel.selectedIndex].text;
        let hint = document.getElementById('vid-custom-hint');
        
        if (text === "Inne") {
            hint.style.display = 'block';
        } else {
            hint.style.display = 'none';
        }
        resizeStreamlit();
    }

    function addVidItem() {
        let sel = document.getElementById('vid_type');
        let qtyInput = document.getElementById('vid_qty');
        let price = parseFloat(sel.value);
        let name = sel.options[sel.selectedIndex].text;
        let qty = parseInt(qtyInput.value);

        if (sel.value === "0" && name !== "Inne") {
             alert("Wybierz rodzaj filmu!"); 
             return;
        }
        if ((!qty || qty <= 0) && name !== "Inne") {
             alert("Podaj ilość!"); 
             return;
        }
        if (name === "Inne") qty = 1;

        videoList.push({ name: name, price: price, qty: qty, isOther: (name === "Inne") });
        
        // Reset
        sel.value = "0";
        qtyInput.value = "";
        checkVidOther(); // ukryj hint po dodaniu
        renderList('vid');
    }

    function removeItem(type, index) {
        if (type === 'gfx') graphicsList.splice(index, 1);
        if (type === 'vid') videoList.splice(index, 1);
        renderList(type);
    }

    function renderList(type) {
        let listArr = (type === 'gfx') ? graphicsList : videoList;
        let container = document.getElementById(type + '-list');
        
        if (listArr.length === 0) {
            container.style.display = 'none';
            container.innerHTML = '';
        } else {
            container.style.display = 'block';
            let html = "";
            listArr.forEach((item, index) => {
                let desc = item.isOther ? "Inne (Wycena Indywidualna)" : `${item.name} x${item.qty}`;
                html += `<div class="added-item">
                            <span>${desc}</span>
                            <span class="remove-btn" onclick="removeItem('${type}', ${index})">&times;</span>
                         </div>`;
            });
            container.innerHTML = html;
        }
        resizeStreamlit();
    }

    // --- CALCULATION LOGIC ---
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
        let isSmCustom = smDesc.includes("INNE");

        // GRAFIKA
        let gfxTotal = 0;
        let isGfxCustom = false;
        let gfxDescArr = [];
        
        graphicsList.forEach(item => {
            if (item.isOther) {
                isGfxCustom = true;
                gfxDescArr.push("Grafika: INNE");
            } else {
                let itemTotal = item.price * item.qty;
                if (item.qty > 1) itemTotal *= 0.9; 
                gfxTotal += itemTotal;
                gfxDescArr.push(`${item.name} x${item.qty}`);
            }
        });

        // WIDEO
        let vidTotal = 0;
        let isVidCustom = false;
        let vidDescArr = [];
        videoList.forEach(item => {
            if (item.isOther) {
                isVidCustom = true;
                vidDescArr.push("Wideo: INNE");
            } else {
                vidTotal += (item.price * item.qty);
                vidDescArr.push(`${item.name} x${item.qty}`);
            }
        });

        // DODATKI
        let useDrone = document.getElementById('drone').checked;
        let useTravel = document.getElementById('travel').checked;
        let usePrint = document.getElementById('gfx_print').checked; 

        // Dron
        let droneBase = gfxTotal + vidTotal;
        let droneCost = 0;
        if (useDrone && droneBase > 0) {
            if (droneBase <= 1000) {
                droneCost = droneBase * 0.20;
            } else {
                droneCost = 200;
            }
        }

        // Dojazd
        let travelBase = smPrice + vidTotal;
        let travelCost = 0;
        if (useTravel && travelBase > 0) {
            travelCost = travelBase * 0.15; 
        }

        let total = Math.round(smPrice + gfxTotal + vidTotal + droneCost + travelCost);
        let displayTotal = total + " zł";
        
        // Logika wyświetlania "Wycena Indywidualna"
        let forceCustom = false;
        if (isSmCustom) forceCustom = true;
        if (isGfxCustom) forceCustom = true;
        if (isVidCustom) forceCustom = true;

        if (forceCustom) {
            if (total > 0) {
                 displayTotal = total + " zł + Wycena Indywidualna";
            } else {
                 displayTotal = "Wycena Indywidualna";
            }
        }
        
        if (usePrint) {
            displayTotal += " + Druk (napisz w formularzu poniżej szczegóły)";
        }

        document.getElementById('total-display').innerText = displayTotal;
        document.getElementById('hidden-total').value = displayTotal;

        // Opis do formularza
        let desc = [];
        if (smDesc !== "") desc.push(smDesc);
        if (gfxDescArr.length > 0) desc.push("GRAFIKA: " + gfxDescArr.join(", "));
        if (usePrint) desc.push("+ DRUK (do wyceny)");
        if (vidDescArr.length > 0) desc.push("WIDEO: " + vidDescArr.join(", "));
        
        if (useDrone) desc.push("+ Dron");
        if (useTravel) desc.push("+ Dojazd");
        
        document.getElementById('hidden-details').value = desc.join(" | ");
    }
</script>

</body>
</html>
"""

components.html(calc_code, height=1500, scrolling=False)
