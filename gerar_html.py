import pandas as pd

# 1. Ler o arquivo Excel (ajuste o nome se a sua planilha tiver outro nome)
df = pd.read_excel('dados.xlsx')

# 2. Converter a planilha em uma tabela HTML
tabela_html = df.to_html(classes='tabela-excel', index=False, na_rep='')

# 3. Estruturar a página HTML com estilo
html_completo = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel de Dados</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 30px;
            background-color: #f8f9fa;
            color: #333;
        }}
        h1 {{
            color: #1a252f;
            text-align: center;
            margin-bottom: 20px;
        }}
        .container {{
            max-width: 90%;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
        }}
        .tabela-excel {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        .tabela-excel th {{
            background-color: #2c3e50;
            color: white;
            padding: 12px;
            text-align: left;
        }}
        .tabela-excel td {{
            padding: 10px;
            border-bottom: 1px solid #e0e0e0;
        }}
        .tabela-excel tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .tabela-excel tr:hover {{
            background-color: #f1f1f1;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Painel Atualizado</h1>
        {tabela_html}
    </div>
</body>
</html>
"""

# 4. Salvar como index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_completo)

print("Arquivo index.html gerado com sucesso!")
