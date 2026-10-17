import json,pathlib,datetime,urllib.parse
root=pathlib.Path(__file__).resolve().parents[1]
t=json.loads((root/'data/translations.json').read_text(encoding='utf-8'))
n=json.loads((root/'data/updates.json').read_text(encoding='utf-8'))
assert set(t)==set('en de pl it sk fr es cs'.split())
assert all(len(v)==16 for v in t.values())
for x in n:
 datetime.date.fromisoformat(x['date'])
 assert urllib.parse.urlparse(x['url']).scheme=='https'
 assert x['publisher'] and x['en']
print('Validated',len(n),'source records and',len(t),'languages. Manual editorial verification is still required.')
