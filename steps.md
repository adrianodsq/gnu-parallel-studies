## Para rodar serial
```
python3 generate_input.py -t 1000
```

## Para encadear serial
```
python3 generate_input.py -t 1000 | xargs -L1 python3 reverse.py -s
```

## Para rodar em paralelo para os mesmo 1000 elementos (final inclusivo no parallel)
```
parallel python3 generate_input.py -i ::: {0..9}
```

## para encadear em paralelo
```
parallel python3 generate_input.py -i ::: {0..9} | parallel --pipe -N1 python3 reverse.py 
parallel python3 generate_input.py -i ::: {0..9} | xargs -P 4 -L1 python3 process2.py -s
```

## Estatisticas

### P1 Serial P2 Serial
```
python3 generate_input.py -t 1000 | xargs -L1 python3 process2.py -s > serial.out
real	0m54.549s
user	0m16.629s
sys	0m4.986s
```

# P1 Serial P2 Parallel
```
real	0m34.309s
user	0m23.362s
sys	0m11.848s
```

# P1 Serial P2 Xargs Paralelo
```
python3 generate_input.py -t 1000 | xargs -P 4 -L1 python3 process2.py -s > serial.out
real	0m24.831s
user	0m16.695s
sys	0m4.730s
```
# P1 parallel P2 serial
```
real	0m46.594s
user	0m17.482s
sys	0m5.081s
```

# P1 parallel P2 Parallel
```
time parallel python3 generate_input.py -i ::: {0..9} | parallel --pipe -N1 python3 process2.py > s4.out
real	0m15.075s
user	0m23.177s
sys	0m12.218s
```

# P1 parallel P2 Xargs paralelo
```
time parallel python3 generate_input.py -i ::: {0..9} | xargs -P 4 -L1 python3 process2.py -s >> y.out
real	0m13.081s
user	0m17.709s
sys	0m5.026s
```

