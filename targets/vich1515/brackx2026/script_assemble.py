# assemble.py: puts the renotated bodies (work/reading_body_v2.txt, work/english_body_v2.txt, written by renotate.py)
# into the code blocks of reading_original.md and translation_en.md, leaving their headers and notes as they are.
# Run from the vich1515 folder after renotate.py.
def put(md, body):
    t = open(md).read(); a = t.index('```') + 3; a = t.index('\n', a) + 1; b = t.index('```', a)
    new = open(body).read()
    if not new.endswith('\n'): new += '\n'
    open(md, 'w').write(t[:a] + new + t[b:])
put('reading_original.md', 'work/reading_body_v2.txt')
put('translation_en.md', 'work/english_body_v2.txt')
print('assembled')
