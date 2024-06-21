import csv
import os

livros = [
    ["Demian", "Hermann Hesse", 1919, 176],
    ["O Morro dos Ventos Uivantes", "Emily Brontë", 1847, 416],
    ["O Apanhador no Campo de Centeio", "J.D. Salinger", 1951, 277],
    ["O Retrato de Dorian Gray", "Oscar Wilde", 1890, 254],
    ["A Morta Apaixonada", "Théophile Gautier", 1836, 68],
    ["Drácula", "Bram Stoker", 1897, 418],
    ["Pessoas Normais", "Sally Rooney", 2018, 266],
    ["Hamlet", "William Shakespeare", 1603, 342],
    ["A Paixão Segundo G.H.", "Clarice Lispector", 1964, 176],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 279]
]

arquivo_csv = "meus_livros.csv"

with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    escritor_csv.writerows(livros)

print(f"Arquivo salvo em: {os.path.abspath(arquivo_csv)}")
