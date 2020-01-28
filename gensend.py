def gen(n):
    import random
    inp = n
    while inp != 4:
        rnum = random.randint(0, 100)
        out = inp + rnum
        print(f'*** {inp=}, {rnum=}:  gen about to send {out=}...')
        inp = (yield out)
        print(f'gen received {inp=}')
    print('Got 4!')
    return 'DONE'

# 15:12: python-utils $ p38 gensend.py 
# Start value?  28
# *** inp=28, rnum=93:  gen about to send out=121...
# >>> got val=121 from g, sending seed=1
# gen received inp=1
# *** inp=1, rnum=45:  gen about to send out=46...
# >>> got val=46 from g, sending seed=6
# gen received inp=6
# *** inp=6, rnum=5:  gen about to send out=11...
# >>> got val=11 from g, sending seed=1
# gen received inp=1
# *** inp=1, rnum=97:  gen about to send out=98...
# >>> got val=98 from g, sending seed=8
# gen received inp=8
# *** inp=8, rnum=10:  gen about to send out=18...
# >>> got val=18 from g, sending seed=8
# gen received inp=8
# *** inp=8, rnum=84:  gen about to send out=92...
# >>> got val=92 from g, sending seed=2
# gen received inp=2
# *** inp=2, rnum=59:  gen about to send out=61...
# >>> got val=61 from g, sending seed=1
# gen received inp=1
# *** inp=1, rnum=74:  gen about to send out=75...
# >>> got val=75 from g, sending seed=5
# gen received inp=5
# *** inp=5, rnum=65:  gen about to send out=70...
# >>> got val=70 from g, sending seed=0
# gen received inp=0
# *** inp=0, rnum=11:  gen about to send out=11...
# >>> got val=11 from g, sending seed=1
# gen received inp=1
# *** inp=1, rnum=34:  gen about to send out=35...
# >>> got val=35 from g, sending seed=5
# gen received inp=5
# *** inp=5, rnum=68:  gen about to send out=73...
# >>> got val=73 from g, sending seed=3
# gen received inp=3
# *** inp=3, rnum=71:  gen about to send out=74...
# >>> got val=74 from g, sending seed=4
# gen received inp=4
# Got 4!
# Traceback (most recent call last):
#   File "gensend.py", line 18, in <module>
#     val = g.send(seed)
# StopIteration: DONE

# So let's handle the exception:

def genx(n):
    import random
    inp = n
    while inp != 4:
        rnum = random.randint(0, 100)
        out = inp + rnum
        print(f'*** {inp=}, {rnum=}:  gen about to send {out=}...')
        inp = (yield out)
        print(f'gen received {inp=}')
    print('Got 4!')
    return 'DONER'

# MAIN CODE:

g = gen(int(input('Start value?  ')))
val = next(g)
while val and val != 'HALT':
    seed = val % 10
    print(f'>>> got {val=} from g, sending {seed=}')
    try:
        val = g.send(seed)
    except StopIteration as si:
        print(f'** Machine stopped.')
        break
print(f'** Received "HALT" from gen or StopIteration thrown.  [{val=}.]   Done. :)\n\n')

