# 📊 CSV para Excel Converter

> 🛠️ **Ferramenta simples para limpeza e conversão de arquivos CSV para Excel (.xlsx).**

Este script em Python realiza a leitura de arquivos `.csv`, limpa caracteres inválidos que podem causar erros no Excel, e salva o resultado em formato `.xlsx`. Ideal para tratar extrações de sistemas antes da análise no Excel.

---

## ⚙️ Funcionamento

- Lê um arquivo `.csv` da pasta `entrada/`;
- Remove caracteres ASCII de controle que podem gerar erros no Excel;
- Salva o resultado na pasta `saida/` com o mesmo nome e extensão `.xlsx`.

---

## 📁 Estrutura do Projeto

```
csv-to-excel-cleaner/
├── entrada/                  → Pasta onde o arquivo CSV deve ser colocado
│   └── vw_consultas_pep.csv → Nome esperado do arquivo de entrada
├── saida/                    → Pasta onde será salvo o arquivo Excel gerado
├── script.py                 → Script principal de conversão e limpeza
```

---

## 🚀 Como Executar

1. **Certifique-se de ter o Python instalado.**

2. **Instale as dependências necessárias:**

```bash
    pip install pandas openpyxl
```

3. **Coloque o arquivo CSV na pasta `entrada/` com o nome `vw_consultas_pep.csv`.**

4. **Execute o script:**

```bash
    python script.py
```

5. **Saída esperada:**

```bash
    ✅ Conversão concluída com sucesso!
    📥 Entrada: entrada/vw_consultas_pep.csv
    📤 Saída: saida/vw_consultas_pep.xlsx
```

---

## 🧼 Sobre a Limpeza

A função `limpar_caracteres_invalidos()` remove caracteres ASCII de controle (como `\x00` a `\x1F`, exceto tabulação e nova linha), que são comuns em extrações de sistemas e podem causar falhas ao abrir arquivos no Excel.

---

## 📦 Requisitos

- Python 3.6+
- pandas
- openpyxl

---

## 📫 Contato

Sugestões, correções ou melhorias?  
Fique à vontade para abrir uma issue ou enviar um PR! 🚀

---

## ⚠️ Aviso

Esta ferramenta foi criada para uso em ambientes controlados e arquivos confiáveis.  
Sempre revise os dados antes de compartilhar planilhas geradas!

