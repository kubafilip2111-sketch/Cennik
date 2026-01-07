<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator Born to Brand</title>
    <style>
        :root {
            --primary: #000000;
            --accent: #e67e22;
            --bg: #f8f9fa;
            --card: #ffffff;
        }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: var(--bg); color: #333; padding: 20px; }
        .calc-container { max-width: 800px; margin: 0 auto; background: var(--card); padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        h1, h2 { text-align: center; color: var(--primary); text-transform: uppercase; }
        .section { margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px solid #eee; }
        label { display: block; margin: 10px 0 5px; font-weight: bold; }
        select, input[type="number"] { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; margin-bottom: 10px; }
        .checkbox-group { display: flex; align-items: center; gap: 10px; margin: 10px 0; cursor: pointer; }
        .checkbox-group input { width: 20px; height: 20px; }
        .result-box { background: var(--primary); color: white; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; }
        .total-price { font-size: 2.5em; font-weight: bold; color: var(--accent); display: block; }
        .btn-calc { width: 100%; background: var(--accent); color: white; border: none; padding: 15px; font-size: 1.2em; font-weight: bold; border-radius: 5px; cursor: pointer; transition: 0.3s; margin-top: 10px; }
        .btn-calc:hover { background: #d35400; }
        .info-text { font-size: 0.85em; color: #666; margin-top: 5px; }
    </style>
</head>
<body>

<div class="calc-container">
    <h1>Born to Brand</h1>
    <p style="text-align: center;">Skonfiguruj swoje zlecenie i sprawdź szacunkowy koszt</p>

    <div class="section">
        <h2>1. Social Media</h2>
        <label>Wybierz pakiet obsługi:</label>
        <select id="sm-package">
            <option value="0">Brak obsługi stałej</option>
            <option value="600">Basic (do 4 rolek/postów/relacji) - ok. 600 zł</option>
            <option value="1500">Standard (4-6 rolek, 4 posty, 4 relacje) - 1500 zł</option>
            <option value="2000">Premium (6-10 rolek, 4-8 postów/relacji) - 2000 zł</option>
            <option value="2500">Custom (Powyżej 10 rolek / 8 postów) - od 2500 zł</option>
        </select>
        <p class="info-text">*Obsługa sprzętem: Nikon Z6III, Mavic 4 Pro, DJI RS4 Pro. Dojazd do 60km od Oświęcimia w cenie.</p>
    </div>

    <div class="section">
        <h2>2. Grafika Komputerowa</h2>
        <label>Rodzaj grafiki:</label>
        <select id="gfx-type">
            <option value="0">Brak</option>
            <option value="150">Baner (150 zł)</option>
            <option value="150">Ulotka (150 zł)</option>
            <option value="100">Wizytówka (100 zł)</option>
            <option value="100">Grafika Social Media (średnio 100 zł)</option>
        </select>
        <label>Liczba sztuk:</label>
        <input type="number" id="gfx-qty" value="0" min="0">
        <label>Poziom skomplikowania:</label>
        <select id="gfx-level">
            <option value="0.9">Prosta (-10%)</option>
            <option value="1" selected>Standardowa</option>
            <option value="1.15">Zaawansowana (+15%)</option>
        </select>
    </div>

    <div class="section">
        <h2>3. Produkcja Wideo</h2>
        <label>Długość filmu:</label>
        <select id="vid-type">
            <option value="0">Brak</option>
            <option value="200">Rolka do 30s (200 zł)</option>
            <option value="350">Rolka 30s - 60s (350 zł)</option>
            <option value="450">Film 60s - 2min (450 zł)</option>
            <option value="550">Film powyżej 2min (550 zł)</option>
        </select>
        <label class="checkbox-group">
            <input type="checkbox" id="vid-drone"> Użycie drona DJI Mavic 4 Pro (+20%)
        </label>
        <label>Poziom montażu:</label>
        <select id="vid-level">
            <option value="0.9">Prosty (-10%)</option>
            <option value="1" selected>Standardowy</option>
            <option value="1.15">Zaawansowany (+15%)</option>
        </select>
    </div>

    <div class="section">
        <label class="checkbox-group">
            <input type="checkbox" id="geo-60"> Dojazd powyżej 60 km od Oświęcimia
        </label>
    </div>

    <button class="btn-calc" onclick="calculateTotal()">OBLICZ WYCENĘ</button>

    <div class="result-box">
        Szacunkowy koszt Twojego zlecenia:
        <span class="total-price" id="total-display">0 zł</span>
        <p id="geo-warning" style="color: #e67e22; font-size: 0.8em; display: none;">*Dla Social Media powyżej 60km cena ustalana indywidualnie.</p>
    </div>
</div>

<script>
function calculateTotal() {
    // 1. Social Media
    let smPrice = parseFloat(document.getElementById('sm-package').value);
    
    // 2. Grafika
    let gfxBase = parseFloat(document.getElementById('gfx-type').value);
    let gfxQty = parseInt(document.getElementById('gfx-qty').value) || 0;
    let gfxLevel = parseFloat(document.getElementById('gfx-level').value);
    let gfxTotal = gfxBase * gfxQty * gfxLevel;
    if (gfxQty > 1) gfxTotal *= 0.9; // Pakiet grafik -10%

    // 3. Wideo
    let vidBase = parseFloat(document.getElementById('vid-type').value);
    let vidDrone = document.getElementById('vid-drone').checked ? 1.2 : 1.0;
    let vidLevel = parseFloat(document.getElementById('vid-level').value);
    let vidTotal = vidBase * vidDrone * vidLevel;

    // Logistyka
    let isFar = document.getElementById('geo-60').checked;
    if (isFar && vidBase > 0) {
        vidTotal *= 1.15; // +15% dla wideo
    }
    
    let finalTotal = smPrice + gfxTotal + vidTotal;

    // Wyświetlanie
    document.getElementById('total-display').innerText = Math.round(finalTotal) + " zł";
    document.getElementById('geo-warning').style.display = isFar ? "block" : "none";
}
</script>

</body>
</html>
