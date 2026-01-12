import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="Kalkulator Born to Brand", layout="centered")

# Kod HTML/JS Kalkulatora
calc_html = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f8f9fa; color: #333; padding: 10px; }
        .calc-container { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); max-width: 480px; margin: auto; }
        h1 { text-align: center; color: #000; font-size: 24px; text-transform: uppercase; border-bottom: 4px solid #e67e22; padding-bottom: 10px; margin-bottom: 25px; }
        h2 { font-size: 15px; margin-top: 20px; color: #555; text-transform: uppercase; letter-spacing: 1px; border-left: 4px solid #e67e22; padding-left: 10px; }
        label { display: block; margin: 12px 0 5px; font-weight: bold; font-size: 14px; }
        select, input[type="number"] { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 8px; box-sizing: border-box; background: #fff; }
        
        /* Panel Opcji Dodatkowych */
        .extra-panel { background: #fdf2e9; padding: 15px; border-radius: 10px; margin-top: 20px; border: 1px solid #fad7bc; }
        .checkbox-row { display: flex; align-items: center; gap: 12px; margin: 10px 0; cursor: pointer; font-size: 14px; }
        .checkbox-row input { width: 18px; height: 18px; accent-color: #e67e22; }

        .btn-calc { width: 100%; background: #e67e22; color: white; border: none; padding: 16px; font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer; margin-top: 25px; transition: 0.3s; text-transform: uppercase; }
        .btn-calc:hover { background: #d35400; }
        
        .result-box { background: #000; color: #fff; text-align: center; padding: 20px; border-radius: 12px; margin-top: 25px; }
        .total-label { font-size: 14px; color: #bbb; text-transform: uppercase; }
        .total-price { font-size: 32px; color: #e67e22; font-weight: bold; display: block; }
    </style>
</head>
<body>

<div class="calc-container">
    <h1>Born to Brand</h1>

    <h2>1. Obsługa Social Media</h2>
    <label>Zakres współpracy:</label>
    <select id="sm">
        <option value="0">Brak obsługi miesięcznej</option>
        <option value="600">Pakiet Basic (do 4 treści/mies.)</option>
        <option value="1500">Pakiet Standard (4-6 rolek + grafiki)</option>
        <option value="2000">Pakiet Premium (6-10 rolek + grafiki)</option>
    </select>

    <h2>2. Projekty Graficzne</h2>
    <label>Rodzaj grafiki:</label>
    <select id="gfx_type">
        <option value="0">Brak projektów</option>
        <option value="150">Baner lub Ulotka</option>
        <option value="100">Projekt wizytówki</option>
        <option value="100">Grafika do Social Media</option>
    </select>
    <label>Ilość projektów:</label>
    <input type="number" id="gfx_qty" value="0" min="0">

    <h2>3. Produkcja Filmowa</h2>
    <label>Długość i format:</label>
    <select id="vid">
        <option value="0">Brak realizacji wideo</option>
        <option value="200">Rolka/Short (do 30s)</option>
        <option value="350">Rolka/Short (30s - 60s)</option>
        <option value="450">Film promocyjny (1 - 2 min)</option>
        <option value="550">Film długi (powyżej 2 min)</option>
    </select>

    <div class="extra-panel">
        <h2>Opcje dodatkowe i logistyka</h2>
        
        <label class="checkbox-row">
            <input type="checkbox" id="drone">
            Czy wykorzystać ujęcia z drona?
        </label>
        
        <label class="checkbox-row">
            <input type="checkbox" id="location">
            Realizacja powyżej 60km od Oświęcimia
        </label>
    </div>

    <button class="btn-calc" onclick="calculate()">Oblicz wartość zlecenia</button>

    <div class="result-box">
        <span class="total-label">Szacunkowy koszt usług:</span>
        <span class="total-price" id="total">0 zł</span>
    </div>
</div>

<script>
function calculate() {
    // 1. Social Media
    let sm = parseFloat(document.getElementById('sm').value);
    
    // 2. Grafika (Rabat 10% przy pakiecie powyżej 1 szt)
    let gBase = parseFloat(document.getElementById('gfx_type').value);
    let gQty = parseInt(document.getElementById('gfx_qty').value) || 0;
    let gTotal = gBase * gQty;
    if(gQty > 1) {
        gTotal *= 0.9; 
    }

    // 3. Wideo + Ukryte mnożniki
    let vBase = parseFloat(document.getElementById('vid').value);
    let vTotal = vBase;
    
    if(vBase > 0) {
        // Dodatek za drona (ukryte +20%)
        if(document.getElementById('drone').checked) {
            vTotal *= 1.20;
        }
        // Dodatek za dojazd (ukryte +15%)
        if(document.getElementById('location').checked) {
            vTotal *= 1.15;
        }
    }

    // Suma końcowa
    let finalResult = sm + gTotal + vTotal;

    // Zabezpieczenie przed wynikiem ujemnym
    if (finalResult < 0) {
        finalResult = 0;
    }

    document.getElementById('total').innerText = Math.round(finalResult) + " zł";
}
</script>

</body>
</html>
"""

# Renderowanie w PyCharm/Streamlit
components.html(calc_html, height=950, scrolling=True)
