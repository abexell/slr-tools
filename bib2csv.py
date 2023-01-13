import bibtexparser
import sys
from collections import defaultdict

source = bibtexparser.load(open(sys.argv[1]))

EXCLUDE_REASONS = {r for e in source.entries for r in e.get('exclude_reason', '').split(';') if e.get('exclude_reason')}

SIMPLE_FIELDS = ['ID', 'author', 'title', 'year', 'journal', 'doi', 'abstract', 'include', 'downloaded']

def pages(e):
    a = e.get('pages')
    if not a: return 'N/A'
    a = a.split('-')
    if len(a) < 2: return a[0]
    return str(int(a[1])-int(a[0]))

def field_getter(f):
    def get(e):
        return e.get(f, '').replace('\n', '').replace('|', '')
    return get

def exclude_getter(r):
    def get(e):
        return 'x' if r in e.get('exclude_reason', '').split(';') else ''
    return get

FIELDS = [field_getter(f) for f in SIMPLE_FIELDS] + \
         [pages] + \
         [exclude_getter(r) for r in EXCLUDE_REASONS]

print('|'.join(SIMPLE_FIELDS + ['pages'] + list(EXCLUDE_REASONS)))

for e in source.entries:
    print('|'.join(f(e) for f in FIELDS))

