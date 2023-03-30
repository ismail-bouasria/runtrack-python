#job 29 
import math

notes = [37,43,82,73,66]

def score_math(notes):
    for note in notes:
        if note > 40: 
            if math.ceil(note/5)*5 - note < 3:
                note = math.ceil(note/5)*5
        print(note)
                
score_math(notes)