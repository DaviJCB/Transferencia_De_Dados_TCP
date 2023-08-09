NOME_ARQUIVO = "Grafo.txt"
import pandas as pd
import numpy as np  
import networkx as nx
import matplotlib.pyplot as plt

class grafo:
    def __init__(self, nome_arquivo):
        self.nos = []
        self.arestas = []
        self.arquivo = nome_arquivo
        self.encontra_Nos(self.arquivo, self.nos)
        self.Encontra_Arestas(self.arestas, self.arquivo)
    
    def encontra_Nos(self, arc, nos):
        try:
            with open(arc, "r") as arquivo:
                conteudo = arquivo.readlines()
                for linha in conteudo:
                    if linha.strip():
                        nos.append(linha[0])
                return nos
        except FileNotFoundError:
                print("Arquivo não encontrado")
        except Exception as e:
                print("Excessão do tipo e")

    def Encontra_Arestas(self, arestas, arc):
        try:
            with open(arc, "r") as arquivo:
                conteudo = arquivo.readlines()
                for linha in conteudo:
                    arestas.append(linha[4:].strip())
                return arestas
        except FileNotFoundError:
                print("Arquivo não encontrado")
        except Exception as e:
                print("Excessão do tipo e")

    def liga_nos(self, nos, arestas):
        #aplicar recursividade para ele ver de indice em indice. Visto que na teoria ele não saberia nem quantos são os nos nem sues nomes.
        for i in nos:
            if "A" in arestas[i]:
                 print()
            elif "B" in arestas[i]:
                 print()
            elif "C" in arestas[i]:
                 print()
            elif "D" in arestas[i]:    
                 print()
            elif "E" in arestas[i]:    
                 print()
            elif "F" in arestas[i]:    

         

grafo = grafo(NOME_ARQUIVO)



"""
    def le_linhas(self, arc):
        try:
            with open(arc, "r") as arquivo:
                conteudo = arquivo.readlines()
                return conteudo
        except FileNotFoundError:
                print("Arquivo não encontrado")
        except Exception as e:
                print("Excessão do tipo e")
    
    def encontra_Nos(self, conteudo, nos):
        for linha in conteudo:
            if linha.strip():
                nos.append(linha[0])
                return nos


    def Encontra_Arestas(self, arestas, conteudo):
        for linha in conteudo:
            arestas.append(linha[4:].strip())
            return arestas
"""