'''with open("imdb_250.txt", "r") as f:
    lines= f.readlines()
    # print(lines)
with open("imdb_250.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "Pulp Fiction":
            f.write(line)'''
#yada

with open("imdb_250.txt", "r+") as f:
    filmListesi= f.readlines()
    # print(filmListesi)
    if "Pulp Fiction\n" in filmListesi:
        indexFilm = filmListesi.index("Pulp Fiction\n")
        filmListesi.pop(indexFilm)
        f.seek(0)
        f.writelines(filmListesi)