# "L", para girar a la izquierda.
# 
# "R", para girar a la derecha.
# 
# "H", para dar media vuelta.
# 
# ".", para mantener la orientación actual.  


# LLL: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# LRR: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# LH.: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# RRL: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# L.H: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# RLR: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# RHH: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# R..: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# HL.: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# HHR: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# ..R: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# HRH: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# H.L: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# .LH: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# .HL: si(N)->E; si(S)->W; si(E)->S; si(W)->N
# .R.: si(N)->E; si(S)->W; si(E)->S; si(W)->N

# LLR: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# LRL: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# L..: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# RLL: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# .HR: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# RH.: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# LHH: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# HLH: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# RRR: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# R.H: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# HHL: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# HR.: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# H.R: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# .L.: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# .RH: si(N)->W; si(S)->E; si(E)->N; si(W)->S
# ..L: si(N)->W; si(S)->E; si(E)->N; si(W)->S

# LL.: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# LRH: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# LHR: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# L.L: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# RLH: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# HLR: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# RR.: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# HRL: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# HHH: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# H..: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# .RR: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# .H.: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# .LL: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# ..H: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# R.R: si(N)->S; si(S)->N; si(E)->W; si(W)->E
# RHL: si(N)->S; si(S)->N; si(E)->W; si(W)->E

# LLH: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# LR.: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# L.R: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# LHL: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# RL.: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# RRH: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# RHR: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# R.L: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# HLL: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# HRR: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# HH.: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# H.H: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# .LR: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# .RL: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# .HH: si(N)->N; si(S)->S; si(E)->E; si(W)->W
# ...: si(N)->N; si(S)->S; si(E)->E; si(W)->W








def movimiento_robot(orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str) -> str:
    c = f"{giro_1}{giro_2}{giro_3}"

    if orientacion_actual == "N":
        if c == "LLL" or c == "LRR" or c == "LH." or c == "RRL" or c == "L.H" or c == "RLR" or c == "RHH" or c == "R.." or c == "HL." or c == "HHR" or c == "..R" or c == "HRH" or c == "H.L" or c == ".LH" or c == ".HL" or c == ".R.":
            res = "E"
    if orientacion_actual == "S":
        if c == "LLL" or c == "LRR" or c == "LH." or c == "RRL" or c == "L.H" or c == "RLR" or c == "RHH" or c == "R.." or c == "HL." or c == "HHR" or c == "..R" or c == "HRH" or c == "H.L" or c == ".LH" or c == ".HL" or c == ".R.":
            res = "W"
    if orientacion_actual == "E":
        if c == "LLL" or c == "LRR" or c == "LH." or c == "RRL" or c == "L.H" or c == "RLR" or c == "RHH" or c == "R.." or c == "HL." or c == "HHR" or c == "..R" or c == "HRH" or c == "H.L" or c == ".LH" or c == ".HL" or c == ".R.":
            res = "S"
    if orientacion_actual == "W":
        if c == "LLL" or c == "LRR" or c == "LH." or c == "RRL" or c == "L.H" or c == "RLR" or c == "RHH" or c == "R.." or c == "HL." or c == "HHR" or c == "..R" or c == "HRH" or c == "H.L" or c == ".LH" or c == ".HL" or c == ".R.":
            res = "N"

    if orientacion_actual == "N":
        if c == "LLR" or c == "LRL" or c == "L.." or c == "RLL" or c == ".HR" or c == "RH." or c == "LHH" or c == "HLH" or c == "RRR" or c == "R.H" or c == "HHL" or c == "HR." or c == "H.R" or c == ".L." or c == ".RH" or c == "..L":
            res = "W"
    if orientacion_actual == "S":
        if c == "LLR" or c == "LRL" or c == "L.." or c == "RLL" or c == ".HR" or c == "RH." or c == "LHH" or c == "HLH" or c == "RRR" or c == "R.H" or c == "HHL" or c == "HR." or c == "H.R" or c == ".L." or c == ".RH" or c == "..L":
            res = "E"
    if orientacion_actual == "E":
        if c == "LLR" or c == "LRL" or c == "L.." or c == "RLL" or c == ".HR" or c == "RH." or c == "LHH" or c == "HLH" or c == "RRR" or c == "R.H" or c == "HHL" or c == "HR." or c == "H.R" or c == ".L." or c == ".RH" or c == "..L":
            res = "N"
    if orientacion_actual == "W":
        if c == "LLR" or c == "LRL" or c == "L.." or c == "RLL" or c == ".HR" or c == "RH." or c == "LHH" or c == "HLH" or c == "RRR" or c == "R.H" or c == "HHL" or c == "HR." or c == "H.R" or c == ".L." or c == ".RH" or c == "..L":
            res = "S"
    
    if orientacion_actual == "N":
        if c == "LL." or c == "LRH" or c == "LHR" or c == "L.L" or c == "RLH" or c == "HLR" or c == "RR." or c == "HRL" or c == "HHH" or c == "H.." or c == ".RR" or c == ".H." or c == ".LL" or c == "..H" or c == "R.R" or c == "RHL":
            res = "S"
    if orientacion_actual == "S":
        if c == "LL." or c == "LRH" or c == "LHR" or c == "L.L" or c == "RLH" or c == "HLR" or c == "RR." or c == "HRL" or c == "HHH" or c == "H.." or c == ".RR" or c == ".H." or c == ".LL" or c == "..H" or c == "R.R" or c == "RHL":
            res = "N"
    if orientacion_actual == "E":
        if c == "LL." or c == "LRH" or c == "LHR" or c == "L.L" or c == "RLH" or c == "HLR" or c == "RR." or c == "HRL" or c == "HHH" or c == "H.." or c == ".RR" or c == ".H." or c == ".LL" or c == "..H" or c == "R.R" or c == "RHL":
            res = "W"
    if orientacion_actual == "W":
        if c == "LL." or c == "LRH" or c == "LHR" or c == "L.L" or c == "RLH" or c == "HLR" or c == "RR." or c == "HRL" or c == "HHH" or c == "H.." or c == ".RR" or c == ".H." or c == ".LL" or c == "..H" or c == "R.R" or c == "RHL":
            res = "E"
    
    if orientacion_actual == "N":
        if c == "LLH" or c == "LR." or c == "L.R" or c == "LHL" or c == "RL." or c == "RRH" or c == "RHR" or c == "R.L" or c == "HLL" or c == "HRR" or c == "HH." or c == "H.H" or c == ".LR" or c == ".RL" or c == ".HH" or c == "...":
           res = "N"
    if orientacion_actual == "S":
        if c == "LLH" or c == "LR." or c == "L.R" or c == "LHL" or c == "RL." or c == "RRH" or c == "RHR" or c == "R.L" or c == "HLL" or c == "HRR" or c == "HH." or c == "H.H" or c == ".LR" or c == ".RL" or c == ".HH" or c == "...":
           res = "S"
    if orientacion_actual == "E":
        if c == "LLH" or c == "LR." or c == "L.R" or c == "LHL" or c == "RL." or c == "RRH" or c == "RHR" or c == "R.L" or c == "HLL" or c == "HRR" or c == "HH." or c == "H.H" or c == ".LR" or c == ".RL" or c == ".HH" or c == "...":
           res = "E"
    if orientacion_actual == "W":
        if c == "LLH" or c == "LR." or c == "L.R" or c == "LHL" or c == "RL." or c == "RRH" or c == "RHR" or c == "R.L" or c == "HLL" or c == "HRR" or c == "HH." or c == "H.H" or c == ".LR" or c == ".RL" or c == ".HH" or c == "...":
           res = "W"

    return res

print(movimiento_robot("W", "L", "H", "."))