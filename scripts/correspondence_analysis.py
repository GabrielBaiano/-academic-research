import os
import json
import glob
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Definir caminhos
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS_PATH = os.path.join(ROOT_DIR, "datasets", "*_data.json")

# Diretório dos artefatos
ART_DIR = "/home/gabrielgama/.gemini/antigravity/brain/32df1f7d-817b-4130-b656-b7cd7fcabf46"

def map_tool(clean_text):
    text = clean_text.lower()
    if 'vosviewer' in text or 'vos viewer' in text or 'vos-viewer' in text:
        return 'VOSviewer'
    if 'gephi' in text:
        return 'Gephi'
    if 'iramuteq' in text:
        return 'IRaMuTeQ'
    if 'scriptlattes' in text:
        return 'ScriptLattes'
    if 'citespace' in text:
        return 'CiteSpace'
    if 'scival' in text:
        return 'SciVal'
    if 'pajek' in text:
        return 'Pajek'
    if 'ucinet' in text:
        return 'UCINET'
    if 'spss' in text:
        return 'SPSS'
    if 'stata' in text:
        return 'Stata'
    if 'bibliometrix' in text or 'biblioshiny' in text:
        return 'Bibliometrix (R)'
    if re.search(r'\bpython\b', text):
        return 'Python'
    if re.search(r'\br\b|r-based|r packages|r package|r programming', text):
        return 'R'
    if 'excel' in text:
        return 'Excel'
    if 'altmetric' in text:
        return 'Altmetric'
    if 'crossref' in text:
        return 'Crossref'
    if 'dimensions' in text:
        return 'Dimensions'
    if 'openalex' in text:
        return 'OpenAlex'
    return None

def map_source(clean_text):
    text = clean_text.lower()
    if 'web of science' in text or 'wos' in text:
        return 'Web of Science'
    if 'scopus' in text:
        return 'Scopus'
    if 'lattes' in text:
        return 'Plataforma Lattes'
    if 'dimensions' in text:
        return 'Dimensions'
    if 'brapci' in text:
        return 'Brapci'
    if 'openalex' in text:
        return 'OpenAlex'
    if 'crossref' in text:
        return 'Crossref'
    if 'pubmed' in text or 'pmc' in text or 'medline' in text or 'pubmed central' in text:
        return 'PubMed'
    if 'scielo' in text:
        return 'SciELO'
    if 'google scholar' in text or 'google academico' in text or 'google acadêmico' in text:
        return 'Google Scholar'
    if 'microsoft academic' in text or 'mag' in text:
        return 'Microsoft Academic'
    if 'cnpq' in text:
        return 'CNPq'
    if 'orcid' in text:
        return 'ORCID'
    if 'overton' in text:
        return 'Overton'
    if 'arxiv' in text:
        return 'arXiv'
    if 'twitter' in text:
        return 'Twitter'
    return None

def clean_and_split(text):
    if not text or text == "N/A" or text == "Não":
        return []
    parts = []
    for part in text.split(","):
        clean = part.strip().lower()
        if clean and clean not in ["n/a", "não", "unspecified"]:
            parts.append(clean)
    return parts

def extract_pairs(papers):
    co_occurrences = []
    for paper in papers:
        tools_raw = paper.get("Ferramenta utilizada", "N/A")
        sources_raw = paper.get("Fonte de coleta de dados (da onde o pesquisador tirou a informação?)", "N/A")
        
        tools_list = clean_and_split(tools_raw)
        sources_list = clean_and_split(sources_raw)
        
        mapped_tools = []
        for t in tools_list:
            mapped_t = map_tool(t)
            if mapped_t:
                mapped_tools.append(mapped_t)
                
        mapped_sources = []
        for s in sources_list:
            mapped_s = map_source(s)
            if mapped_s:
                mapped_sources.append(mapped_s)
                
        mapped_tools = list(set(mapped_tools))
        mapped_sources = list(set(mapped_sources))
        
        for t in mapped_tools:
            for s in mapped_sources:
                co_occurrences.append((t, s))
    return co_occurrences

def run_ca_and_plot(df_pairs, tools_to_keep, sources_to_keep, output_path, artifacts_path, title):
    if df_pairs.empty:
        print(f"[Erro] Sem dados para gerar CA para {title}!")
        return

    # Montar tabela de contingência
    contingency_table = pd.crosstab(df_pairs["Ferramenta"], df_pairs["Fonte"])
    
    # Filtrar
    valid_tools = [t for t in tools_to_keep if t in contingency_table.index]
    valid_sources = [s for s in sources_to_keep if s in contingency_table.columns]
    
    contingency_table = contingency_table.loc[valid_tools, valid_sources]
    
    # Se a tabela for muito pequena ou vazia, avisar e pular
    if contingency_table.empty or contingency_table.shape[0] < 2 or contingency_table.shape[1] < 2:
        print(f"[Aviso] Tabela de contingência para {title} é muito pequena ({contingency_table.shape}) para análise de correspondência!")
        return
        
    print(f"\n[Análise] Tabela de contingência para {title} (tamanho {contingency_table.shape}):")
    print(contingency_table)
    
    # Algoritmo CA
    N = contingency_table.values
    grand_total = N.sum()
    P = N / grand_total
    
    r = P.sum(axis=1)
    c = P.sum(axis=0)
    
    r[r == 0] = 1e-10
    c[c == 0] = 1e-10
    
    Dr_inv_sqrt = np.diag(1.0 / np.sqrt(r))
    Dc_inv_sqrt = np.diag(1.0 / np.sqrt(c))
    
    S = Dr_inv_sqrt @ (P - np.outer(r, c)) @ Dc_inv_sqrt
    U, S_vals, Vt = np.linalg.svd(S, full_matrices=False)
    
    inertias = S_vals ** 2
    total_inertia = inertias.sum()
    var_explained = (inertias / total_inertia) * 100
    
    print(f"  Inércia Total: {total_inertia:.4f}")
    if len(var_explained) > 0:
        print(f"  Dimensão 1: {var_explained[0]:.2f}% de inércia explicada")
    if len(var_explained) > 1:
        print(f"  Dimensão 2: {var_explained[1]:.2f}% de inércia explicada")
        
    row_coords = Dr_inv_sqrt @ U @ np.diag(S_vals)
    col_coords = Dc_inv_sqrt @ Vt.T @ np.diag(S_vals)
    
    row_labels = contingency_table.index.tolist()
    col_labels = contingency_table.columns.tolist()
    
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
    
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    
    # Plotar
    ax.scatter(row_coords[:, 0], row_coords[:, 1], color='#1f77b4', marker='o', s=120, label='Ferramentas', edgecolors='black', linewidth=0.8, zorder=3)
    ax.scatter(col_coords[:, 0], col_coords[:, 1], color='#ff7f0e', marker='s', s=120, label='Fontes de Dados', edgecolors='black', linewidth=0.8, zorder=3)
    
    texts = []
    for i, label in enumerate(row_labels):
        texts.append(ax.text(row_coords[i, 0], row_coords[i, 1], label, fontsize=10, weight='bold', color='#0f3a5f'))
    for j, label in enumerate(col_labels):
        texts.append(ax.text(col_coords[j, 0], col_coords[j, 1], label, fontsize=10, weight='bold', color='#8c3d00'))
        
    adjust_text(texts, arrowprops=dict(arrowstyle="-", color='gray', lw=0.5, alpha=0.6))
    
    ax.set_title(f"Mapa de Associação ({title}): Ferramentas vs. Fontes de Dados\n(Análise de Correspondência - CA)", fontsize=13, weight='bold', pad=15, color='#2c3e50')
    
    dim1_lbl = f"Dimensão 1 ({var_explained[0]:.1f}%)" if len(var_explained) > 0 else "Dimensão 1"
    dim2_lbl = f"Dimensão 2 ({var_explained[1]:.1f}%)" if len(var_explained) > 1 else "Dimensão 2"
    ax.set_xlabel(dim1_lbl, fontsize=11, labelpad=10, color='#2c3e50')
    ax.set_ylabel(dim2_lbl, fontsize=11, labelpad=10, color='#2c3e50')
    
    # Configurar legenda no canto inferior esquerdo para evitar sobreposição
    ax.legend(frameon=True, facecolor='white', edgecolor='#e2e8f0', fontsize=10, loc='lower left')
    
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.savefig(artifacts_path, bbox_inches='tight')
    plt.close()
    
    print(f"  -> Mapa gerado com sucesso!")
    print(f"     Salvo em: {output_path}")
    print(f"     Salvo nos artefatos em: {artifacts_path}")

def main():
    print("[Análise] Carregando datasets...")
    qss_papers = []
    ebbc_papers = []
    
    for filepath in glob.glob(DATASETS_PATH):
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if "qss" in filename.lower():
                    qss_papers.extend(data)
                elif "ebbc" in filename.lower():
                    ebbc_papers.extend(data)
            except Exception as e:
                print(f"[Aviso] Falha ao ler {filename}: {e}")
                
    print(f"[Análise] Total de artigos carregados:")
    print(f"  QSS: {len(qss_papers)}")
    print(f"  EBBC: {len(ebbc_papers)}")
    print(f"  Total: {len(qss_papers) + len(ebbc_papers)}")
    
    # Extrair pares
    qss_pairs = extract_pairs(qss_papers)
    ebbc_pairs = extract_pairs(ebbc_papers)
    combined_pairs = qss_pairs + ebbc_pairs
    
    df_qss = pd.DataFrame(qss_pairs, columns=["Ferramenta", "Fonte"])
    df_ebbc = pd.DataFrame(ebbc_pairs, columns=["Ferramenta", "Fonte"])
    df_combined = pd.DataFrame(combined_pairs, columns=["Ferramenta", "Fonte"])
    
    # Listas de categorias a incluir em cada tipo de gráfico
    # 1. COMBINADO
    tools_combined = ['VOSviewer', 'Python', 'ScriptLattes', 'IRaMuTeQ', 'UCINET', 'SciVal', 'Excel', 'Bibliometrix (R)', 'Pajek', 'Altmetric']
    sources_combined = ['Scopus', 'Web of Science', 'Plataforma Lattes', 'CNPq', 'Brapci', 'SciELO', 'OpenAlex']
    
    # 2. EBBC (focando no componente conectado principal para evitar distorção por outliers como Gephi/Twitter)
    tools_ebbc = ['VOSviewer', 'Python', 'ScriptLattes', 'IRaMuTeQ', 'UCINET', 'SciVal', 'Excel', 'Bibliometrix (R)', 'Pajek', 'Altmetric']
    sources_ebbc = ['Scopus', 'Web of Science', 'Plataforma Lattes', 'CNPq', 'Brapci', 'SciELO', 'OpenAlex']
    
    # 3. QSS (como tem poucos pares, mantemos todos os disponíveis que co-ocorrem pelo menos 1 vez)
    tools_qss = ['Altmetric', 'Crossref', 'Dimensions', 'Excel', 'OpenAlex']
    sources_qss = ['Crossref', 'Dimensions', 'Scopus', 'Web of Science']
    
    # --- Executar Análises ---
    
    # A. Combined (Salva em ca_biplot_combined.png e também no ca_biplot.png para compatibilidade)
    print("\n--- PROCESSANDO DATASET COMBINADO ---")
    run_ca_and_plot(df_combined, tools_combined, sources_combined, 
                    os.path.join(ROOT_DIR, "ca_biplot_combined.png"), 
                    os.path.join(ART_DIR, "ca_biplot_combined.png"), 
                    "Combinado QSS + EBBC")
    # Copiar para ca_biplot.png original
    run_ca_and_plot(df_combined, tools_combined, sources_combined, 
                    os.path.join(ROOT_DIR, "ca_biplot.png"), 
                    os.path.join(ART_DIR, "ca_biplot.png"), 
                    "Combinado")

    # B. EBBC Only
    print("\n--- PROCESSANDO DATASET EBBC (NACIONAL) ---")
    run_ca_and_plot(df_ebbc, tools_ebbc, sources_ebbc, 
                    os.path.join(ROOT_DIR, "ca_biplot_ebbc.png"), 
                    os.path.join(ART_DIR, "ca_biplot_ebbc.png"), 
                    "EBBC Nacional")

    # C. QSS Only
    print("\n--- PROCESSANDO DATASET QSS (INTERNACIONAL) ---")
    run_ca_and_plot(df_qss, tools_qss, sources_qss, 
                    os.path.join(ROOT_DIR, "ca_biplot_qss.png"), 
                    os.path.join(ART_DIR, "ca_biplot_qss.png"), 
                    "QSS Internacional")

if __name__ == "__main__":
    main()
