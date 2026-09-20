import shelve

Ficheiro = shelve.open("highscore/highscore", flag="c")
Ficheiro.clear()
Ficheiro.close()

print("Highscores resetados com sucesso!")
