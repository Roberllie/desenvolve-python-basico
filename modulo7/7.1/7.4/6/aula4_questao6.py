import csv

arquivo_spotify = "spotify-2023.csv"

def processar_spotify(arquivo):
    musicas_por_ano = {}
    
    with open(arquivo, mode='r', encoding='latin-1') as csvfile:
        leitor_csv = csv.reader(csvfile)
        next(leitor_csv)
        
        for linha in leitor_csv:
            track_name = linha[0]
            artist_name = linha[1]
            artist_count = int(linha[2])
            released_year = int(linha[3])
            streams = int(linha[8])
            
            if 2012 <= released_year <= 2022:
                if released_year not in musicas_por_ano or streams > musicas_por_ano[released_year][3]:
                    musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

    lista_musicas = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano)]
    return lista_musicas

musicas_populares = processar_spotify(arquivo_spotify)
print(musicas_populares)
