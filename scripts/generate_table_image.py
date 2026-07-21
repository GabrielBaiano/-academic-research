import matplotlib.pyplot as plt
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(ROOT_DIR, "graficos")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "tabela_analise_ia.png")

# Data
columns = ['Indicador', 'QSS (Periódico)', 'EBBC (Conferência)', 'Total Geral']
data = [
    ['Artigos Analisados', '391', '315', '706'],
    ['Artigos Candidatos (Termo IA)', '81', '11', '92'],
    ['Artigos com Uso Efetivo', '80', '11', '91'],
    ['Taxa de Incorporação (%)', '20.46%', '3.49%', '12.89%']
]

# Set up figure (widened to accommodate column widths)
fig, ax = plt.subplots(figsize=(11, 4.5), dpi=300)
ax.axis('off')
ax.axis('tight')

# Create table with custom column widths
# Total width of columns is 1.0 (relative to plot area)
col_widths = [0.38, 0.20, 0.22, 0.20]

table = ax.table(
    cellText=data,
    colLabels=columns,
    colWidths=col_widths,
    loc='center',
    cellLoc='center'
)

# Style table
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.0, 2.2)  # scale height of cells (x-scale = 1.0 since we set colWidths explicitly)

# Colors (Hex)
header_bg = {
    0: '#334155',  # Indicador (Slate)
    1: '#1E3A8A',  # QSS (Navy Blue)
    2: '#047857',  # EBBC (Emerald Green)
    3: '#1E293B'   # Total Geral (Dark Slate)
}

# Apply styling to cells
for (row, col), cell in table.get_celld().items():
    cell.set_linewidth(0.8)
    cell.set_edgecolor('#CBD5E1')  # Light gray borders
    
    if row == 0:
        # Header formatting
        cell.set_text_props(weight='bold', color='white', size=11)
        cell.set_facecolor(header_bg.get(col, '#1E293B'))
    else:
        # Data formatting
        if col == 0:
            cell.set_text_props(weight='bold', color='#1E293B', ha='left')
        else:
            cell.set_text_props(color='#333333')
            
        # Zebra striping and highlights
        if row == 4:
            # Highlight row (Taxa)
            cell.set_facecolor('#EFF6FF')
            cell.set_text_props(weight='bold')
        elif row % 2 == 0:
            cell.set_facecolor('#F8FAFC')
        else:
            cell.set_facecolor('#FFFFFF')

# Add Title
plt.title(
    "A Incorporação da Inteligência Artificial na Cienciometria: QSS vs. EBBC",
    fontsize=14,
    weight='bold',
    color='#1E3A8A',
    pad=25
)

# Adjust layout and save
plt.tight_layout()
plt.savefig(output_path, bbox_inches='tight', transparent=True)
print(f"Table image successfully generated and saved to: {output_path}")
