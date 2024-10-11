import pandas as pd

def clean_field(text):
    if isinstance(text, str):
        return f'"{text}"' if ',' in text or '\n' in text else f'"{text}"'
    return text

df = pd.read_csv('resolved_tickets.csv', delimiter=',', on_bad_lines='skip')

df['Ticket Number'] = df['Ticket Number'].apply(clean_field)
df['Subject'] = df['Subject'].apply(clean_field)
df['Resolution'] = df['Resolution'].apply(clean_field)

df.to_csv('formatted_restickets.csv', index=False, header=False)
