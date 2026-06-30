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
OUTPUT_IMAGE = os.path.join(ROOT_DIR, "ca_biplot.png")
ARTIFACTS_IMAGE = "/home/gabrielgama/.gemini/antigravity/brain/32df1f7d-817b-4130-b656-b7cd7fcabf46/ca_biplot.png"

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

def main():
    print("[Análise] Carregando datasets...")
    all_papers = []
    
    for filepath in glob.glob(DATASETS_PATH):
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                all_papers.extend(data)
            except Exception as e:
                print(f"[Aviso] Falha ao ler {os.path.basename(filepath)}: {e}")
                
    print(f"[Análise] Total de artigos carregados: {len(all_papers)}")
    
    # Coletar pares co-ocorrentes
    co_occurrences = []
    
    for paper in all_papers:
        tools_raw = paper.get("Ferramenta utilizada", "N/A")
        sources_raw = paper.get("Fonte de coleta de dados (da onde o pesquisador tirou a informação?)", "N/A")
        
        tools_list = clean_and_split(tools_raw)
        sources_list = clean_and_split(sources_raw)
        
        # Mapear e filtrar termos conhecidos de forma flexível/robusta
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
                
        # Garantir unicidade dentro do mesmo artigo
        mapped_tools = list(set(mapped_tools))
        mapped_sources = list(set(mapped_sources))
        
        # Gerar pares
        for t in mapped_tools:
            for s in mapped_sources:
                co_occurrences.append((t, s))
                
    print(f"[Análise] Total de pares (Ferramenta, Fonte) extraídos: {len(co_occurrences)}")
    
    if not co_occurrences:
        print("[Erro] Nenhum par de (Ferramenta, Fonte) encontrado para a análise!")
        return
        
    df_pairs = pd.DataFrame(co_occurrences, columns=["Ferramenta", "Fonte"])
    
    # Montar tabela de contingência
    contingency_table = pd.crosstab(df_pairs["Ferramenta"], df_pairs["Fonte"])
    
    # Filtrar para manter apenas o componente principal conectado e evitar distorções de outliers perfeitamente isolados
    tools_to_keep = ['VOSviewer', 'Python', 'ScriptLattes', 'IRaMuTeQ', 'UCINET', 'SciVal', 'Excel', 'Bibliometrix (R)', 'Pajek', 'Altmetric']
    sources_to_keep = ['Scopus', 'Web of Science', 'Plataforma Lattes', 'CNPq', 'Brapci', 'SciELO', 'OpenAlex']
    
    tools_to_keep = [t for t in tools_to_keep if t in contingency_table.index]
    sources_to_keep = [s for s in sources_to_keep if s in contingency_table.columns]
    
    contingency_table = contingency_table.loc[tools_to_keep, sources_to_keep]
    
    print(f"[Análise] Tabela de contingência filtrada (tamanho {contingency_table.shape}):")
    print(contingency_table)
    
    # --- Algoritmo de Análise de Correspondência (CA) ---
    N = contingency_table.values
    grand_total = N.sum()
    P = N / grand_total
    
    r = P.sum(axis=1)
    c = P.sum(axis=0)
    
    # Impedir divisões por zero em colunas/linhas vazias
    r[r == 0] = 1e-10
    c[c == 0] = 1e-10
    
    Dr_inv_sqrt = np.diag(1.0 / np.sqrt(r))
    Dc_inv_sqrt = np.diag(1.0 / np.sqrt(c))
    
    # Matriz de resíduos padronizados
    S = Dr_inv_sqrt @ (P - np.outer(r, c)) @ Dc_inv_sqrt
    
    # Decomposição em Valores Singulares (SVD)
    U, S_vals, Vt = np.linalg.svd(S, full_matrices=False)
    
    # Cálculo das inércias (autovalores) e variância explicada
    inertias = S_vals ** 2
    total_inertia = inertias.sum()
    var_explained = (inertias / total_inertia) * 100
    
    print(f"\n[Análise] Inércia Total: {total_inertia:.4f}")
    for idx, var in enumerate(var_explained):
        if idx < len(var_explained):
            print(f"  Dimensão {idx+1}: {var:.2f}% de inércia explicada")
        
    # Coordenadas principais das linhas (Ferramentas) e colunas (Fontes)
    row_coords = Dr_inv_sqrt @ U @ np.diag(S_vals)
    col_coords = Dc_inv_sqrt @ Vt.T @ np.diag(S_vals)
    
    # Obter os nomes das categorias
    row_labels = contingency_table.index.tolist()
    col_labels = contingency_table.columns.tolist()
    
    # --- Plotagem Gráfica (Biplot Simétrico) ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
    
    # Eixos de referência (linhas tracejadas em x=0 e y=0)
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    
    # Plotar Ferramentas (Linhas) - Azul Royal
    ax.scatter(row_coords[:, 0], row_coords[:, 1], color='#1f77b4', marker='o', s=120, label='Ferramentas', edgecolors='black', linewidth=0.8, zorder=3)
    # Plotar Fontes de Dados (Colunas) - Laranja Coral
    ax.scatter(col_coords[:, 0], col_coords[:, 1], color='#ff7f0e', marker='s', s=120, label='Fontes de Dados', edgecolors='black', linewidth=0.8, zorder=3)
    
    # Adicionar rótulos de texto
    texts = []
    for i, label in enumerate(row_labels):
        texts.append(ax.text(row_coords[i, 0], row_coords[i, 1], label, fontsize=10, weight='bold', color='#0f3a5f'))
        
    for j, label in enumerate(col_labels):
        texts.append(ax.text(col_coords[j, 0], col_coords[j, 1], label, fontsize=10, weight='bold', color='#8c3d00'))
        
    # Ajustar as posições para evitar sobreposição de texto
    print("[Análise] Ajustando posições dos rótulos de texto...")
    adjust_text(texts, arrowprops=dict(arrowstyle="-", color='gray', lw=0.5, alpha=0.6))
    
    # Estilização Premium do Gráfico
    ax.set_title("Mapa de Associação: Ferramentas vs. Fontes de Dados\n(Análise de Correspondência - CA)", fontsize=14, weight='bold', pad=15, color='#2c3e50')
    ax.set_xlabel(f"Dimensão 1 ({var_explained[0]:.1f}%)", fontsize=11, labelpad=10, color='#2c3e50')
    ax.set_ylabel(f"Dimensão 2 ({var_explained[1]:.1f}%)", fontsize=11, labelpad=10, color='#2c3e50')
    
    # Configurar legenda bonita no canto inferior esquerdo (onde não há dados para evitar sobreposição)
    ax.legend(frameon=True, facecolor='white', edgecolor='#e2e8f0', fontsize=10, loc='lower left')
    
    # Margens e layout
    plt.tight_layout()
    
    # Salvar nos destinos
    plt.savefig(OUTPUT_IMAGE, bbox_inches='tight')
    plt.savefig(ARTIFACTS_IMAGE, bbox_inches='tight')
    plt.close()
    
    print(f"[Análise] Mapa gerado com sucesso!")
    print(f"  -> Salvo localmente em: {OUTPUT_IMAGE}")
    print(f"  -> Salvo nos artefatos em: {ARTIFACTS_IMAGE}")

if __name__ == "__main__":
    main()
