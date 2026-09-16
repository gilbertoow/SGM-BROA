import pandas as pd

# 1. Carregar a aba principal de registros 'BROA'
# (Caso queira alterar para outra aba, mude sheet_name)
nome_arquivo = 'Resumo_BROA_2026-09-14 _2.xlsx'

try:
    df = pd.read_excel(nome_arquivo, sheet_name='BROA')
except Exception as e:
    # Caso o arquivo enviado na atualização tenha um nome padronizado
    df = pd.read_excel('dados.xlsx', sheet_name='BROA')

# Limpeza e formatação básica
df = df.dropna(how='all') # remove linhas completamente vazias

# Converter dataframe para HTML
tabela_html = df.to_html(classes='table table-striped table-hover', index=False, na_rep='')

html_completo = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal Executivo - Gestão de Ações BROA</title>

    <!-- DataTables & Bootstrap para filtros, busca e navegação interativa -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css">
    
    <style>
        body {{
            background-color: #f4f6f9;
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            padding: 25px;
        }}
        .header-box {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        .card-container {{
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }}
        table.dataTable thead {{
            background-color: #1e3c72;
            color: white;
        }}
    </style>
</head>
<body>

    <div class="container-fluid">
        <div class="header-box">
            <h2 class="m-0">Gestão de Ações — BROA</h2>
            <p class="m-0 mt-2 opacity-75">Portal executivo para acompanhamento de prazos, riscos e frentes operacionais</p>
        </div>

        <div class="card-container">
            <div class="table-responsive">
                {tabela_html}
            </div>
        </div>
    </div>

    <!-- Scripts para busca, ordenação e paginação automática -->
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>
    
    <script>
        $(document).ready(function() {{
            $('table').DataTable({{
                "language": {{
                    "url": "//cdn.datatables.net/plug-ins/1.13.6/i18n/pt-BR.json"
                }},
                "pageLength": 25,
                "responsive": true
            }});
        }});
    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_completo)

print("Painel BROA gerado com sucesso!")
