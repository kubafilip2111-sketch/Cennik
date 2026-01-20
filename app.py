import streamlit as st
import streamlit.components.v1 as components

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Kalkulator Born to Brand",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS FIX DLA STREAMLIT ---
st.markdown("""
    <style>
        .block-container { padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        [data-testid="stToolbar"] {visibility: hidden;}
        .stDeployButton {display:none;}
        iframe { width: 100%; min-height: 100vh; }
    </style>
""", unsafe_allow_html=True)

# --- 3. GŁÓWNY KOD HTML/JS/CSS ---
html_content = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Kalkulator Born to Brand</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root { 
            --primary: #ffc200; 
            --primary-hover: #e0aa00;
            --dark: #1a1a1a; 
            --light: #f8f9fa; 
            --shadow: 0 8px 30px rgba(0,0,0,0.08); 
            --radius: 16px;
        }

        * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body { 
            font-family: 'Poppins', sans-serif; 
            background: #fff; 
            color: var(--dark); 
            margin: 0; padding: 20px 10px;
            width: 100%; overflow-x: hidden;
        }

        .container { 
            background: #fff; 
            max-width: 600px; 
            margin: 0 auto; 
            padding-bottom: 60px;
        }

        h1 { 
            text-align: center; font-weight: 800; text-transform: uppercase; 
            margin: 10px 0 5px 0; font-size: 38px; line-height: 1.1; letter-spacing: -1px;
        }
        h1 span { color: var(--primary); }
        .cennik-label { 
            text-align: center; font-size: 13px; font-weight: 600; text-transform: uppercase; 
            color: #999; letter-spacing: 4px; margin-bottom: 30px; 
        }

        details { 
            background: #fff; border: 1px solid #eee; border-radius: var(--radius); 
            margin-bottom: 12px; overflow: hidden; transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        }
        details[open] { border-color: var(--primary); box-shadow: 0 5px 15px rgba(255, 194, 0, 0.15); }
        
        summary { 
            padding: 20px; cursor: pointer; font-weight: 600; font-size: 16px;
            display: flex; justify-content: space-between; align-items: center; list-style: none; 
        }
        summary::-webkit-details-marker { display: none; }
        summary::after { content: '+'; font-size: 24px; color: var(--primary); font-weight: 300; }
        details[open] summary::after { content: '-'; transform: rotate(0deg); }
        details[open] summary { border-bottom: 1px solid #f0f0f0; background: #fafafa; }

        .content { padding: 20px; animation: fadeIn 0.4s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(-5px); } to { opacity: 1; transform: translateY(0); } }

        .presets-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        .btn-preset {
            background: #fff; border: 2px solid #eee; padding: 15px 10px; border-radius: 12px;
            cursor: pointer; transition: 0.2s; text-align: center; position: relative;
        }
        .btn-preset:hover { border-color: #ccc; }
        .btn-preset.active { 
            border-color: var(--primary); background: #fffdf5; 
            box-shadow: 0 0 0 1px var(--primary) inset; 
        }
        .btn-preset strong { display: block; font-size: 14px; margin-bottom: 6px; text-transform: uppercase; }
        .btn-preset ul { font-size: 11px; color: #666; padding: 0; margin: 0; list-style: none; line-height: 1.4; }
        .btn-preset.full-width { grid-column: span 2; padding: 12px; }

        label { display: block; margin-bottom: 8px; font-weight: 500; font-size: 13px; color: #555; }
        
        /* --- STYLE PÓL INPUT --- */
        input[type="text"], input[type="number"], input[type="tel"], input[type="email"], select, textarea {
            width: 100%; padding: 16px; border: 2px solid #eee; border-radius: 12px;
            font-family: inherit; font-size: 15px; transition: 0.3s; 
            appearance: none; 
            background-color: #fff;
            outline: none;
        }
        
        input:focus, select:focus, textarea:focus { 
            border-color: var(--primary) !important; 
            box-shadow: 0 0 0 3px rgba(255, 194, 0, 0.25) !important; 
        }
        
        input[type="checkbox"] {
            width: 24px; 
            height: 24px; 
            accent-color: var(--primary); 
            cursor: pointer; 
            margin: 0;
            appearance: auto; 
            -webkit-appearance: checkbox; 
        }

        .btn-add {
            background: #333; color: #fff; border: none; padding: 14px; width: 100%;
            border-radius: 12px; margin-top: 15px; cursor: pointer; font-size: 13px; 
            text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px;
        }
        .btn-add:hover { background: #000; }

        .btn-calc {
            width: 100%; background: #fff; color: var(--dark); border: 3px solid var(--primary); 
            padding: 20px; font-size: 18px; font-weight: 800; border-radius: 16px; cursor: pointer;
            text-transform: uppercase; margin-top: 40px; transition: 0.2s;
            box-shadow: 0 10px 20px rgba(255, 194, 0, 0.15);
        }
        .btn-calc:hover { background: var(--primary); color: #000; transform: translateY(-2px); }

        #result-section { display: none; margin-top: 40px; border-top: 2px dashed #eee; padding-top: 40px; }
        
        .price-box {
            background: var(--dark); color: #fff; padding: 30px 20px; border-radius: 20px;
            text-align: center; margin-bottom: 30px; position: relative; overflow: hidden;
        }
        .price-box::before {
            content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
            background: radial-gradient(circle, rgba(255,194,0,0.1) 0%, rgba(0,0,0,0) 70%);
        }
        .price-label { font-size: 12px; text-transform: uppercase; letter-spacing: 2px; opacity: 0.7; }
        .price-val { font-size: 36px; font-weight: 700; color: var(--primary); display: block; margin-top: 10px; }

        .form-box { background: #f9f9f9; padding: 25px; border-radius: 16px; }
        .btn-send {
            width: 100%; background: var(--primary); color: #000; border: none; padding: 18px;
            font-size: 16px; font-weight: 700; border-radius: 12px; cursor: pointer;
            text-transform: uppercase; margin-top: 15px; box-shadow: 0 4px 15px rgba(255, 194, 0, 0.4);
        }
        .btn-send:hover { background: var(--primary-hover); }

        .added-item { 
            display: flex; justify-content: space-between; align-items: center;
            background: #fff; border: 1px solid #eee; padding: 12px; border-radius: 8px; margin-bottom: 8px; font-size: 13px; 
        }
        .remove-btn { color: #ff4444; font-weight: bold; cursor: pointer; padding: 0 10px; font-size: 20px; }

        .checkbox-group { background: #fffdf5; padding: 20px; border-radius: 16px; border: 1px solid #ffeeba; margin-top: 20px; }
        .checkbox-row { display: flex; align-items: center; gap: 12px; cursor: pointer; margin-bottom: 10px; }
        .checkbox-row span { cursor: pointer; }
        
        .custom-hint { display: none; background: #fff8e1; color: #664d03; padding: 12px; font-size: 12px; border-radius: 8px; margin-top: 10px; border: 1px solid #ffecb5; }
        
        .info-desc { font-size: 12px; color: #666; margin-top: 20px; line-height: 1.5; border-top: 1px solid #eee; padding-top: 15px; }

        .auto-attach-info {
            font-size: 12px; 
            background: #e9f7ef; 
            color: #1e8449; 
            padding: 10px; 
            border-radius: 8px; 
            margin-bottom: 20px; 
            border: 1px solid #c3e6cb;
            display: flex;
            align-items: center;
            gap: 8px;
        }

    </style>
</head>
<body>

<div class="container">
    <h1>Born to <span>Brand</span></h1>
    <div class="cennik-label">Kalkulator Wyceny</div>

    <input type="hidden" id="sm_price_val" value="0">
    <input type="hidden" id="sm_desc" value="">

    <details>
        <summary>Prowadzenie Social Media</summary>
        <div class="content">
            <div class="presets-grid">
                <div class="btn-preset" onclick="selectPackage(this, 400, 'Minimum', '2 Rolki, 2 Grafiki, 2 Relacje')">
                    <strong>Minimum</strong>
                    <ul><li>2x Rolki</li><li>2x Grafiki</li><li>2x Relacje</li></ul>
                </div>
                <div class="btn-preset" onclick="selectPackage(this, 1000, 'Niski', '4 Rolki, 4 Grafiki, 4 Relacje')">
                    <strong>Niski</strong>
                    <ul><li>4x Rolki</li><li>4x Grafiki</li><li>4x Relacje</li></ul>
                </div>
                <div class="btn-preset" onclick="selectPackage(this, 1500, 'Polecany', '8 Rolek, 4 Grafiki, 8 Relacji')">
                    <strong>Polecany</strong>
                    <ul><li>8x Rolki</li><li>4x Grafiki</li><li>8x Relacje</li></ul>
                </div>
                <div class="btn-preset" onclick="selectPackage(this, 2000, 'Wysoki', '10 Rolek, 8 Grafik, 10 Relacji')">
                    <strong>Wysoki</strong>
                    <ul><li>10x Rolki</li><li>8x Grafiki</li><li>10x Relacje</li></ul>
                </div>
                <div class="btn-preset full-width" onclick="selectPackage(this, 0, 'INNE', 'Wycena indywidualna')">
                    <strong>Inne / Wycena Indywidualna</strong>
                </div>
            </div>
            
            <div id="sm-hint" class="custom-hint">Zaznacz tę opcję, a na dole strony w formularzu opisz swoje potrzeby. Wycenimy to indywidualnie!</div>

            <div class="info-desc">
                W cenie miesięcznego pakietu: prowadzimy Twoje social media od A do Z. W tym: wykorzystujemy profesjonalny sprzęt foto/wideo, jesteśmy w stałym kontakcie ze zleceniodawcą, przygotowujemy comiesięczne raporty z wynikami, odpisujemy na komentarze i wiadomości.
            </div>
        </div>
    </details>

    <details>
        <summary>Projektowanie Graficzne</summary>
        <div class="content">
            <label>Rodzaj projektu:</label>
            <select id="gfx_type" onchange="toggleGfxHint()">
                <option value="0">-- Wybierz --</option>
                <option value="150">Baner</option>
                <option value="150">Ulotka</option>
                <option value="100">Wizytówka</option>
                <option value="100">Grafika Social Media</option>
                <option value="0">Inne</option>
            </select>
            
            <div id="gfx-hint" class="custom-hint">Wybierz tę opcję dla nietypowych zleceń i opisz je w formularzu końcowym.</div>

            <label style="margin-top:15px">Ilość sztuk:</label>
            <input type="number" id="gfx_qty" placeholder="np. 1" min="1">

            <button class="btn-add" onclick="addItem('gfx')">+ Dodaj do wyceny</button>
            
            <div id="gfx-list" style="margin-top:15px"></div>

            <label class="checkbox-row" style="margin-top:20px; font-size:14px;">
                <input type="checkbox" id="gfx_print"> 
                <span>Zlecam również druk</span>
            </label>
        </div>
    </details>

    <details>
        <summary>Tworzenie Filmów</summary>
        <div class="content">
            <label>Rodzaj wideo:</label>
            <select id="vid_type" onchange="toggleVidHint()">
                <option value="0">-- Wybierz --</option>
                <option value="200">Rolka do 30s</option>
                <option value="350">Rolka 30s-60s</option>
                <option value="450">Film 1-2 min</option>
                <option value="550">Film > 2 min</option>
                <option value="0">Inne</option>
            </select>

            <div id="vid-hint" class="custom-hint">Opisz niestandardowe wideo w formularzu na dole.</div>

            <label style="margin-top:15px">Ilość filmów:</label>
            <input type="number" id="vid_qty" placeholder="np. 1" min="1">

            <button class="btn-add" onclick="addItem('vid')">+ Dodaj do wyceny</button>
            <div id="vid-list" style="margin-top:15px"></div>
            
            <div style="font-size: 12px; color: #666; margin-top: 15px; font-style: italic;">
                * Cena obejmuje nagranie wideo oraz profesjonalny montaż.
            </div>
        </div>
    </details>

    <div class="checkbox-group">
        <label class="checkbox-row">
            <input type="checkbox" id="drone">
            <span>Ujęcia z drona</span>
        </label>
        <label class="checkbox-row">
            <input type="checkbox" id="travel">
            <span>Dojazd do klienta (>60km od Oświęcimia)</span>
        </label>
    </div>

    <button class="btn-calc" onclick="calculate()">Oblicz szacunkowy koszt</button>

    <div id="result-section">
        <div class="price-box">
            <div class="price-label">Szacowany koszt</div>
            <span class="price-val" id="total-display">0 zł</span>
        </div>

        <div class="form-box">
            <div style="text-align:center; margin-bottom:15px; font-size:13px; font-style:italic; color:#555;">
                Jesteśmy elastyczni, dopasujemy usługę pod Twoje potrzeby!
            </div>

            <div style="text-align:center; margin-bottom:20px; font-weight:600; line-height:1.4;">
                Wyślij zapytanie, a odezwiemy się do Ciebie jak najszybciej SMS-em oraz mailem.
            </div>
            
            <div class="auto-attach-info">
                <span>✅</span>
                <span>Twoje wybory z kalkulatora zostaną automatycznie dołączone do zgłoszenia. Nie musisz ich przepisywać!</span>
            </div>

            <form id="contactForm" action="https://formsubmit.co/eb22f98293c64af2624298419c9477ac" method="POST" target="_blank">
                <input type="hidden" name="_subject" value="Leads: Born to Brand">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="_template" value="table">
                
                <input type="hidden" name="Szczegóły" id="hidden-details">
                <input type="hidden" name="Kwota" id="hidden-total">

                <div style="margin-bottom:12px">
                    <input type="text" name="Klient" placeholder="Imię / Firma" required>
                </div>
                
                <div style="margin-bottom:12px">
                    <input type="tel" id="contact-phone" name="Telefon" placeholder="Telefon (tylko cyfry)" oninput="this.value = this.value.replace(/[^0-9]/g, '');">
                </div>
                
                <div style="margin-bottom:12px">
                    <input type="email" id="contact-email" name="Email" placeholder="E-mail">
                </div>
                
                <div style="margin-bottom:12px">
                    <textarea name="Wiadomosc" placeholder="Dodatkowe informacje..." rows="3"></textarea>
                </div>

                <button type="submit" class="btn-send">Wyślij Zapytanie</button>
            </form>
            <div style="text-align:center; margin-top:15px; font-size:14px; font-weight:600;">
                lub zadzwoń: <a href="tel:+48515478736" style="color:var(--primary-hover); text-decoration:none;">515 478 736</a>
            </div>
        </div>
    </div>
</div>

<script>
    let cart = { gfx: [], vid: [] };

    function selectPackage(el, price, name, details) {
        let isActive = el.classList.contains('active');
        document.querySelectorAll('.btn-preset').forEach(b => b.classList.remove('active'));
        
        if (!isActive) {
            el.classList.add('active');
            document.getElementById('sm_price_val').value = price;
            document.getElementById('sm_desc').value = (name === 'INNE') ? 'Social: Wycena Indywidualna' : `Social: ${name}`;
            document.getElementById('sm-hint').style.display = (name === 'INNE') ? 'block' : 'none';
        } else {
            document.getElementById('sm_price_val').value = 0;
            document.getElementById('sm_desc').value = "";
            document.getElementById('sm-hint').style.display = 'none';
        }
    }

    function toggleGfxHint() {
        let txt = document.getElementById('gfx_type').selectedOptions[0].text;
        document.getElementById('gfx-hint').style.display = (txt === 'Inne') ? 'block' : 'none';
    }
    function toggleVidHint() {
        let txt = document.getElementById('vid_type').selectedOptions[0].text;
        document.getElementById('vid-hint').style.display = (txt === 'Inne') ? 'block' : 'none';
    }

    function addItem(type) {
        let select = document.getElementById(type + '_type');
        let qtyInput = document.getElementById(type + '_qty');
        
        let price = parseFloat(select.value);
        let name = select.selectedOptions[0].text;
        let qty = parseInt(qtyInput.value);

        if (name === '-- Wybierz --') return alert('Wybierz rodzaj usługi!');
        if (name !== 'Inne' && (!qty || qty < 1)) return alert('Podaj ilość!');
        if (name === 'Inne') qty = 1; 

        cart[type].push({ name, price, qty, isOther: (name === 'Inne') });

        select.value = "0";
        qtyInput.value = "";
        renderList(type);
        if(type === 'gfx') toggleGfxHint();
        if(type === 'vid') toggleVidHint();
    }

    function removeItem(type, index) {
        cart[type].splice(index, 1);
        renderList(type);
    }

    function renderList(type) {
        let container = document.getElementById(type + '-list');
        container.innerHTML = '';
        
        cart[type].forEach((item, idx) => {
            let div = document.createElement('div');
            div.className = 'added-item';
            div.innerHTML = `
                <span>${item.isOther ? 'Inne (do wyceny)' : item.name + ' x' + item.qty}</span>
                <span class="remove-btn" onclick="removeItem('${type}', ${idx})">&times;</span>
            `;
            container.appendChild(div);
        });
    }

    function calculate() {
        let total = 0;
        let detailsArr = [];
        let isCustom = false;

        // 1. Social Media
        let smPrice = parseFloat(document.getElementById('sm_price_val').value) || 0;
        let smDesc = document.getElementById('sm_desc').value;
        if (smPrice > 0) total += smPrice;
        if (smDesc) detailsArr.push(smDesc);
        if (smDesc.includes('Indywidualna')) isCustom = true;

        // 2. Grafika
        cart.gfx.forEach(i => {
            if (i.isOther) {
                isCustom = true;
                detailsArr.push('Grafika: INNE');
            } else {
                let cost = i.price * i.qty;
                if (i.qty > 1) cost *= 0.9; 
                total += cost;
                detailsArr.push(`Grafika: ${i.name} x${i.qty}`);
            }
        });

        // 3. Wideo
        cart.vid.forEach(i => {
            if (i.isOther) {
                isCustom = true;
                detailsArr.push('Wideo: INNE');
            } else {
                let cost = i.price * i.qty;
                if (i.qty > 1) cost *= 0.9; 
                total += cost;
                detailsArr.push(`Wideo: ${i.name} x${i.qty}`);
            }
        });

        // 4. Dodatki
        let drone = document.getElementById('drone').checked;
        let travel = document.getElementById('travel').checked;
        let print = document.getElementById('gfx_print').checked;

        if (drone) {
            let base = total; 
            let droneCost = (base <= 1000) ? base * 0.2 : 200;
            if (base > 0) total += droneCost;
            detailsArr.push('Dron: TAK');
        }

        if (travel) {
            let travelCost = total * 0.15;
            if (total > 0) total += travelCost;
            detailsArr.push('Dojazd: TAK');
        }

        if (print) detailsArr.push('Druk: TAK (do wyceny)');

        // Finalizacja
        total = Math.round(total);
        let displayTxt = total + " zł";
        
        if (isCustom) displayTxt += " + Wycena";
        if (total === 0 && isCustom) displayTxt = "Wycena Indywidualna";
        if (print) displayTxt += " + Druk";

        if (total === 0 && !isCustom && !print) displayTxt = "0 zł";

        document.getElementById('total-display').innerText = displayTxt;
        document.getElementById('hidden-total').value = displayTxt;
        document.getElementById('hidden-details').value = detailsArr.join(" | ");

        let resSec = document.getElementById('result-section');
        if (total > 0 || isCustom || print) {
            resSec.style.display = 'block';
            resSec.scrollIntoView({behavior: 'smooth'});
        }
    }

    // --- NOWA LOGIKA WALIDACJI FORMULARZA ---
    document.getElementById('contactForm').addEventListener('submit', function(e) {
        var phone = document.getElementById('contact-phone').value;
        var email = document.getElementById('contact-email').value;

        // 1. Sprawdź czy podano cokolwiek (Telefon LUB Email)
        if (!phone && !email) {
            e.preventDefault();
            alert('Podaj numer telefonu LUB adres e-mail, abyśmy mogli się z Tobą skontaktować.');
            return;
        }

        // 2. Walidacja telefonu (jeśli wpisany)
        if (phone) {
            if (phone.length < 9) {
                e.preventDefault();
                alert('Numer telefonu jest za krótki. Wpisz co najmniej 9 cyfr.');
                return;
            }
            // (Blokada liter jest już zrobiona przez oninput w HTML)
        }

        // 3. Walidacja e-maila (jeśli wpisany) - prosty regex dla pewności
        if (email) {
            var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!re.test(email)) {
                e.preventDefault();
                alert('Podany adres e-mail wygląda na nieprawidłowy.');
                return;
            }
        }
    });

</script>

</body>
</html>
"""

components.html(html_content, height=2300, scrolling=True)
