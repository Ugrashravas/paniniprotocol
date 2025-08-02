import datetime

# === CONFIGURABLE VALUES ===
unicity_distances = [46, 339, 475]   # List of UD values (in symbols)
translated_symbols = 508                  # Number of symbols translated
total_target_symbols = 1000                # Progress bar range

# === CALCULATED VALUES ===
progress_pct = translated_symbols / total_target_symbols * 100
max_ud = max(unicity_distances)

# === BUILD MARKERS ===
marker_divs = []
for ud in unicity_distances:
    color = "red" if ud == unicity_distances[-1] else "pink"  # red, pink
    percent = ud / total_target_symbols * 100
    marker_div = f'''  <!-- Unicity Distance marker -->
  <div style="
    position: absolute;
    left: {percent:.0f}%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: {color};
    z-index: 2;">
  </div>'''
    marker_divs.append(marker_div)

unicity_markers = '\n'.join(marker_divs)

# === TIMESTAMP ===
now = datetime.datetime.now().strftime("%Y-%b-%d, %H:%M (GMT +5:30)")

# === FINAL HTML BLOCK ===
html_output = f'''

As of date, the unicity distance is **{unicity_distances[-1]}**, and **{translated_symbols}+** symbols have been translated (green bar). This may be outdated — see the [translation page](translation.md) for live numbers.

<h3>Progress in first {total_target_symbols} symbols</h3>

<div style="position: relative; width: 100%; max-width: 600px; height: 30px; background: #eee; border-radius: 6px; overflow: hidden; border: 1px solid #ccc;">

  <!-- Green progress bar -->
  <div style="width: {progress_pct:.0f}%; height: 100%; background: #4caf50;"></div>

{unicity_markers}

</div>

<p style="margin-top: 0.5rem;">Current progress: <strong>{progress_pct:.2f}%</strong>. Last updated: {now}</p>
'''

# === PRINT TO TERMINAL ===
print(html_output)
