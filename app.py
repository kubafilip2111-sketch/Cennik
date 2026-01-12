import streamlit as st
import streamlit.components.v1 as components

# Tytuł aplikacji
st.set_page_config(page_title="Kalkulator Born to Brand", layout="centered")

# Kod HTML/JS Kalkulatora
calc_html = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <style>
        body { font-family: sans-serif; background: #f4f4f4; padding: 10px; }
        .calc-card { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 500px; margin: auto; }
        h2 { color: #000; text-transform: uppercase; font-size: 1.2em; border-bottom: 2px solid #e67e22; padding-bottom: 5px; }
        label { display: block; margin: 12px 0 5px; font-weight: bold; font-size: 0.9em; }
        select, input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; }
        .checkbox-row { display: flex; align-items: center; gap: 10px; margin: 15px 0; }
        .checkbox-row input { width: auto; }
        .btn-calc { width: 100%; background: #e67e22; color: white; border: none; padding: 15px; font-weight: bold; border-radius: 5px; cursor: pointer; margin-top: 20px; }
        .result { background: #000; color: #fff; text-align: center; padding: 15px; border-radius: 8px; margin-top: 20px; }
        .price { font-size: 2em; color: #e67e22; display: block; }
    </style>
</head>
<body>
    <div class="calc-card">
        <h2>1. Social Media</h2>
        <label>Pakiet:</label>
        <select id="sm">
            <option value="0">Brak</option>
            <option value="600">Basic (do 4 rolek/postów) - ok. 600zł</option>
            <option value="1500">Standard (4-6 rolek) - 1500zł</option>
            <option value="2000">Premium (6-10 rolek) - 2000zł</option>
        </select>

        <h2>2. Grafika</h2>
        <label>Rodzaj:</label>
        <select id="gfx_type">
            <option value="0">Brak</option>
            <option value="150">Baner/Ulotka (150zł)</option>
            <option value="100">Wizytówka (100zł)</option>
            <option value="100">Grafika SM (100zł)</option>
        </select>
        <label>Ilość:</label>
        <input type="number" id="gfx_qty" value="0" min="0">

        <h2>3. Wideo</h2>
        <label>Długość:</label>
        <select id="vid">
            <option value="0">Brak</option>
            <option value="200">Rolka do 30s (200zł)</option>
            <option value="350">Rolka 30-60s (350zł)</option>
            <option value="450">Film 1-2 min (450zł)</option>
            <option value="550">Film 2min+ (550zł)</option>
        </select>
        <div class="checkbox-row">
            <input type="checkbox" id="drone"> <label>Użycie drona (+20%)</label>
        </div>
        <div class="checkbox-row">
            <input type="checkbox" id="dist"> <label>Dojazd powyżej 60km (+15% wideo)</label>
        </div>

        <button class="btn-calc" onclick="calculate()">OBLICZ WYCENĘ</button>

        <div class="result">
            Suma zamówienia:
            <span class="price" id="total">0 zł</span>
        </div>
    </div>

    <script>
        function calculate() {
            let sm = parseFloat(document.getElementById('sm').value);
            
            let gfxBase = parseFloat(document.getElementById('gfx_type').value);
            let gfxQty = parseInt(document.getElementById('gfx_qty').value) || 0;
            let gfxTotal = gfxBase * gfxQty;
            if(gfxQty > 1) gfxTotal *= 0.9;

            let vidBase = parseFloat(document.getElementById('vid').value);
            if(document.getElementById('drone').checked) vidBase *= 1.2;
            if(document.getElementById('dist').checked) vidBase *= 1.15;

            document.getElementById('total').innerText = Math.round(sm + gfxTotal + vidBase) + " zł";
        }
    </script>
</body>
</html>
"""

# Renderowanie kalkulatora w Streamlit
components.html(calc_html, height=850, scrolling=True)
