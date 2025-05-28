# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

# Français | Peharge: Ce code source est publié sous la licence MIT.
#
# Droits d'utilisation:
# Le code source peut être copié, édité et adapté aux besoins individuels.
# Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
# Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
# car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
#
# Dépendances et frameworks supplémentaires:
# Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
# Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
# Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
# pour éviter d'éventuels conflits avec les installations de logiciels existantes.
#
# Clause de non-responsabilité:
# L'utilisation du code est entièrement à vos propres risques.
# Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
# pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
#
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

import sys
import readline
from datetime import datetime, timedelta
import requests

# Weather icons (Open-Meteo codes)
weather_icons = {
    0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️",
    45: "🌫️", 48: "🌁",
    51: "🌦️", 53: "🌦️", 55: "🌧️",
    61: "🌧️", 63: "🌧️", 65: "🌧️🌧️",
    71: "❄️", 73: "❄️", 75: "❄️❄️",
    95: "⛈️", 99: "⛈️❄️"
}

# Data icons
icons = {
    'temp': "🌡️",
    'humidity': "💧",
    'wind': "🌬️",
    'precip': "🌧️",
    'uv': "🔆"
}

blue = "\033[94m"
reset = "\033[0m"

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_weather():
    readline.parse_and_bind('tab: complete')
    location = input('Enter location (e.g., Berlin, New York): ').strip()
    if not location:
        print(f"[{timestamp()}] [ERROR] Location cannot be empty.")
        sys.exit(1)

    try:
        geo = requests.get(
            'https://nominatim.openstreetmap.org/search',
            params={'q': location, 'format': 'json', 'limit': 1},
            headers={'User-Agent': 'weather-cli'}
        )
        geo.raise_for_status()
        loc = geo.json()[0]
        lat, lon = float(loc['lat']), float(loc['lon'])
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Geocoding failed: {e}")
        sys.exit(1)

    now = datetime.now()
    labels = ['4h ago', 'Now', 'In 4h'] + [f"+{i}d" for i in range(1, 11)]
    times_req = [now - timedelta(hours=4), now, now + timedelta(hours=4)] + [now + timedelta(days=i) for i in range(1, 11)]

    start = (now - timedelta(hours=4)).date().isoformat()
    end = (now + timedelta(days=10)).date().isoformat()

    try:
        params = {
            'latitude': lat,
            'longitude': lon,
            'hourly': 'temperature_2m,relativehumidity_2m,windspeed_10m,precipitation,weathercode,uv_index',
            'daily': 'sunrise,sunset',
            'start_date': start,
            'end_date': end,
            'timezone': 'auto'
        }
        r = requests.get('https://api.open-meteo.com/v1/forecast', params=params)
        r.raise_for_status()
        wf = r.json()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Fetch failed: {e}")
        sys.exit(1)

    times = [datetime.fromisoformat(t) for t in wf['hourly']['time']]
    temps = wf['hourly']['temperature_2m']
    hums = wf['hourly']['relativehumidity_2m']
    winds = wf['hourly']['windspeed_10m']
    precs = wf['hourly']['precipitation']
    codes = wf['hourly']['weathercode']
    uvs = wf['hourly']['uv_index']

    print(f"\n[{timestamp()}] [INFO] Weather for {location} ({lat:.4f}, {lon:.4f})")

    def row(metric_key, metric_vals, icon):
        line = f"{icon:<10}"
        for dt in times_req:
            idx = min(range(len(times)), key=lambda i: abs(times[i] - dt))
            val = metric_vals[idx]
            if metric_key == 'temp':
                cell = f"{val:.1f}°C"
            elif metric_key == 'humidity':
                cell = f"{val:.0f}%"
            elif metric_key == 'wind':
                cell = f"{val:.1f}km/h"
            elif metric_key == 'uv':
                cell = f"{val:.1f}"
            else:
                cell = f"{val:.1f}mm"
            line += f"{cell:^12}"
        print(line)

    print(f"\n[{timestamp()}] [INFO] Weather details:")
    for i, dt in enumerate(times_req):
        idx = min(range(len(times)), key=lambda j: abs(times[j] - dt))
        dt_label = labels[i]
        dt_time = times[idx].strftime("%A, %d %b %Y %H:%M")
        print(f"\n{dt_label} ({dt_time})")
        print(f"{icons['temp']} {blue}Temperature{reset}: {temps[idx]:.1f}°C")
        print(f"{icons['humidity']} {blue}Humidity{reset}: {hums[idx]:.0f}%")
        print(f"{icons['wind']} {blue}Wind{reset}: {winds[idx]:.1f} km/h")
        print(f"{icons['precip']} {blue}Precipitation{reset}: {precs[idx]:.1f} mm")
        print(f"{icons['uv']} {blue}UV Index{reset}: {uvs[idx]:.1f}")
        print(f"🌦️ {blue}Weather{reset}: {weather_icons.get(codes[idx], 'N/A')}")

    # Sunrise/Sunset info (first few days)
    print(f"\nSunrise / Sunset:")
    for i, (sr, ss) in enumerate(zip(wf['daily']['sunrise'], wf['daily']['sunset'])):
        print(f"  {wf['daily']['time'][i]}: 🌅 {sr[-5:]} | 🌇 {ss[-5:]}")

    print()

if __name__ == '__main__':
    get_weather()
