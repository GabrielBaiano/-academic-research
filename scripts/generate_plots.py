import matplotlib.pyplot as plt
import numpy as np
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(ROOT_DIR, "graficos")
os.makedirs(output_dir, exist_ok=True)

# 1. GENERATE TABLE 1: METRICAS GERAIS
def generate_table_metrics():
    output_path = os.path.join(output_dir, "tabela_metricas_gerais.png")
    columns = ['Indicador', 'QSS (Periódico)', 'EBBC (Conferência)', 'Total Geral']
    data = [
        ['Artigos Analisados', '391', '315', '706'],
        ['Artigos Candidatos (Termo IA)', '81', '11', '92'],
        ['Artigos com Uso Efetivo', '80', '11', '91'],
        ['Taxa de Incorporação (%)', '20.46%', '3.49%', '12.89%']
    ]

    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    ax.axis('off')
    ax.axis('tight')

    col_widths = [0.38, 0.20, 0.22, 0.20]
    table = ax.table(
        cellText=data,
        colLabels=columns,
        colWidths=col_widths,
        loc='center',
        cellLoc='center'
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.0, 2.2)

    header_bg = {
        0: '#334155',  # Indicador (Slate)
        1: '#1E3A8A',  # QSS (Navy Blue)
        2: '#047857',  # EBBC (Emerald Green)
        3: '#1E293B'   # Total Geral (Dark Slate)
    }

    for (row, col), cell in table.get_celld().items():
        cell.set_linewidth(0.8)
        cell.set_edgecolor('#CBD5E1')
        
        if row == 0:
            cell.set_text_props(weight='bold', color='white', size=11)
            cell.set_facecolor(header_bg.get(col, '#1E293B'))
        else:
            if col == 0:
                cell.set_text_props(weight='bold', color='#1E293B', ha='left')
            else:
                cell.set_text_props(color='#333333')
                
            if row == 4:
                cell.set_facecolor('#EFF6FF')
                cell.set_text_props(weight='bold')
            elif row % 2 == 0:
                cell.set_facecolor('#F8FAFC')
            else:
                cell.set_facecolor('#FFFFFF')

    # Draw canvas to calculate positions
    fig.canvas.draw()
    # Get bounding box of the table grid in pixels and convert to inches
    bbox = table.get_window_extent(fig.canvas.get_renderer())
    bbox_inches = bbox.transformed(fig.dpi_scale_trans.inverted())
    
    # Save cropped exactly to the table boundary with a tiny padding
    plt.savefig(output_path, bbox_inches=bbox_inches, transparent=True, pad_inches=0.01)
    plt.close()
    print(f"Table 1 saved to: {output_path}")

# 2. GENERATE TABLE 2: SUBGRUPOS IA
def generate_table_subgroups():
    output_path = os.path.join(output_dir, "tabela_subgrupos_ia.png")
    columns = ['Subgrupo de IA', 'QSS (N)', 'QSS (%)', 'EBBC (N)', 'EBBC (%)', 'Total Geral (N)']
    data = [
        ['Processamento de Linguagem Natural (PLN)', '23', '28.7%', '10', '90.9%', '33'],
        ['Modelagem de Tópicos', '16', '20.0%', '1', '9.1%', '17'],
        ['Modelagem Preditiva', '5', '6.2%', '0', '0.0%', '5'],
        ['Curadoria/Extração de Dados', '3', '3.8%', '0', '0.0%', '3'],
        ['Análise de Redes/Grafos', '33', '41.2%', '0', '0.0%', '33'],
        ['Outros', '0', '0.0%', '0', '0.0%', '0']
    ]

    fig, ax = plt.subplots(figsize=(13.5, 4.5), dpi=300)
    ax.axis('off')
    ax.axis('tight')

    col_widths = [0.38, 0.11, 0.11, 0.11, 0.11, 0.18]
    table = ax.table(
        cellText=data,
        colLabels=columns,
        colWidths=col_widths,
        loc='center',
        cellLoc='center'
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.0, 2.2)

    header_bg = {
        0: '#334155',  # Subgrupo (Slate)
        1: '#1E3A8A',  # QSS N (Navy)
        2: '#1E3A8A',  # QSS %
        3: '#047857',  # EBBC N (Green)
        4: '#047857',  # EBBC %
        5: '#1E293B'   # Total Geral N (Dark Slate)
    }

    for (row, col), cell in table.get_celld().items():
        cell.set_linewidth(0.8)
        cell.set_edgecolor('#CBD5E1')
        
        if row == 0:
            cell.set_text_props(weight='bold', color='white', size=10)
            cell.set_facecolor(header_bg.get(col, '#1E293B'))
        else:
            if col == 0:
                cell.set_text_props(weight='bold', color='#1E293B', ha='left')
            else:
                cell.set_text_props(color='#333333')
                
            if row % 2 == 0:
                cell.set_facecolor('#F8FAFC')
            else:
                cell.set_facecolor('#FFFFFF')

    # Draw canvas to calculate positions
    fig.canvas.draw()
    # Get bounding box of the table grid in pixels and convert to inches
    bbox = table.get_window_extent(fig.canvas.get_renderer())
    bbox_inches = bbox.transformed(fig.dpi_scale_trans.inverted())
    
    # Save cropped exactly to the table boundary with a tiny padding
    plt.savefig(output_path, bbox_inches=bbox_inches, transparent=True, pad_inches=0.01)
    plt.close()
    print(f"Table 2 saved to: {output_path}")

# 3. GENERATE SIDE-BY-SIDE EVOLUTION BAR CHART
def generate_evolution_chart():
    output_path = os.path.join(output_dir, "evolucao_ia_comparada.png")
    
    # Shared years: 2020, 2022, 2024
    years = ['2020', '2022', '2024']
    qss_rates = [16.48, 22.41, 18.18]
    ebbc_rates = [2.22, 2.30, 5.07]
    
    x = np.arange(len(years))
    width = 0.35  # width of bars
    
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    
    # Draw bars
    rects1 = ax.bar(x - width/2, qss_rates, width, label='QSS (Periódico Internacional)', color='#1E3A8A', edgecolor='#172554', linewidth=0.8)
    rects2 = ax.bar(x + width/2, ebbc_rates, width, label='EBBC (Conferência Nacional)', color='#047857', edgecolor='#064e3b', linewidth=0.8)
    
    # Custom styling
    ax.set_ylabel('Taxa de Incorporação de IA (%)', fontsize=11, weight='bold', color='#334155', labelpad=15)
    ax.set_title('Evolução Temporal do Uso Metodológico de IA: QSS vs. EBBC (Lado a Lado)', fontsize=13, weight='bold', color='#1E3A8A', pad=25)
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=11, weight='bold', color='#334155')
    
    # Legend
    ax.legend(frameon=True, facecolor='#FFFFFF', edgecolor='#E2E8F0', fontsize=10, loc='upper left')
    
    # Gridlines
    ax.grid(axis='y', linestyle='--', alpha=0.5, color='#CBD5E1')
    ax.set_axisbelow(True)
    
    # Despine
    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)
    ax.spines['bottom'].set_color('#94A3B8')
    ax.spines['bottom'].set_linewidth(1.2)
    
    # Label bars with their values
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(
                f'{height:.2f}%',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 5),  # 5 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10, weight='bold',
                color='#1E293B'
            )
            
    autolabel(rects1)
    autolabel(rects2)
    
    # Limit y axis to give some headroom
    ax.set_ylim(0, 30)
    
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', transparent=True)
    plt.close()
    print(f"Evolution chart saved to: {output_path}")

def main():
    generate_table_metrics()
    generate_table_subgroups()
    generate_evolution_chart()

if __name__ == "__main__":
    main()
