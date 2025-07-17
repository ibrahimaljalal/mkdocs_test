import markdown

text = """
# Shopping List

- Apples
- Oranges
- Bananas

| Item    | Quantity |
|---------|----------|
| Apples  | 5        |
| Oranges | 3        |
| Bananas | 7        |
"""

# Use the 'tables' extension to enable Markdown tables
html = markdown.markdown(text, extensions=['tables'])

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

