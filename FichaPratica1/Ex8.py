# Escreva um programa que calcule a duração (no formato hh:mm:ss) de um álbum musical com 5
# canções. A duração de cada canção é lida em minutos e segundos.

minMus1 = eval(input("Introduza minutos da musica 1: "))
segMus1 = eval(input("Introduza segundos da musica 1: "))

minMus2 = eval(input("Introduza minutos da musica 2: "))
segMus2 = eval(input("Introduza segundos da musica 2: "))

minMus3 = eval(input("Introduza minutos da musica 3: "))
segMus3 = eval(input("Introduza segundos da musica 3: "))

minMus4 = eval(input("Introduza minutos da musica 4: "))
segMus4 = eval(input("Introduza segundos da musica 4: "))

minMus5 = eval(input("Introduza minutos da musica 5: "))
segMus5 = eval(input("Introduza segundos da musica 5: "))

totalMin = minMus1 + minMus2 + minMus3 + minMus4 + minMus5
totalSeg = segMus1 + segMus2 + segMus3 + segMus4 + segMus5
totalAlbum = totalMin + totalSeg

horasAlbum = totalAlbum/3600
minutosAlbum = (totalAlbum/60) - horasAlbum
segundosAlbum = (totalAlbum/60) - minutosAlbum

print(f"Total do Album: {horasAlbum:.2f}h {minutosAlbum:.2f}m {segundosAlbum:.2f}s")



