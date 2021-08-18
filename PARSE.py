from bs4 import BeautifulSoup
import requests
import os
import PyPDF2
from collections import Counter
import math
import numpy as np


class Query:

    def __init__(self, query, results):
        self.l = []
        self.query = query
        self.results = results

    def links_to_txt(self):
        file = 'links.txt'    
        doc_read = open(file, 'r').read()
        doc_read = doc_read.split()
        for link in self.l:
            if link not in doc_read:
                doc_append = open(file, 'a+')
                doc_append.write(link)
                doc_append.close()

    def parse(self):
        while self.results >= 0:
            url_a = 'https://scholar.google.com.br/scholar?start=' + str(self.results) + '&q=' + self.query + '&hl=pt-BR&oe=ASCII&as_sdt=0,5'
            url_b = 'https://search.scielo.org/?q=' + self.query + '&lang=pt&count=10&from=' + str(self.results - 9) + '&output=site&sort=&format=summary&fb=&page=1'

            page_a = requests.get(url_a)
            soup_a = BeautifulSoup(page_a.content, 'html.parser')

            a_find = soup_a.find_all('a', href=True)
            links_a = []

            for link in a_find:
                if str(link) not in links_a:
                    if 'data-clk' in str(link):
                        links_a.append(link['href'])
            
            for link in links_a:
                if link not in self.l:
                    self.l.append(link)


            page_b = requests.get(url_b)
            soup_b = BeautifulSoup(page_b.content, 'html.parser')

            b_find = soup_b.find_all('a', href=True)
            links_b = []

            for link in b_find:
                if str(link) not in links_b:
                    if 'ePDF' not in str(link):
                        if 'PDF' in str(link):
                            links_b.append(link['href'])

            for link in links_b:
                if link not in self.l:
                    self.l.append(link)

                    
            for link in self.l:
                print(link)
                print()
            self.results -= 10  

        self.links_to_txt()          

class PdfText:
    
    def __init__(self):
        self.d = {}
        self.sub_dir = []
        self.files = []
        self.PTS = {}
        self.pageObj = ''
        self.fim = {}


    def prep(self, dir):
        for sub in os.listdir(dir):
            if sub.endswith('.pdf'):
                self.files.append(dir + sub)
            
            elif not sub.endswith('.pdf'):
                if sub != '.DS_Store':
                    for file in os.listdir(dir + '/' + sub + '/'):
                        self.files.append(dir + '/' + sub + '/' + file)

        for file in self.files:
            try:
                self.pdf_txt(file)
                print(file + " __________ "  + 'OK')               
            except PyPDF2.utils.PdfReadError:
                pass
            except TypeError:
                pass
            except FileNotFoundError:
                pass
            except KeyError:
                pass
    

    def pdf_txt(self, file):
        pdfFileObj = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        self.pageObj = ''
        for page in range(pdfReader.numPages):
            self.pageObj += pdfReader.getPage(page).extractText()
        
        data = self.pageObj.split()
        count = Counter(data)
        self.d.update(count)

    def cont(self, dir):
        self.prep(dir)
        
        for i in list(self.d):
            if len(i) < 4:
                self.d.pop(i)

        for file in self.files:
            try:
                pdfFileObj = open(file, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                pages = ''
                for page in range(pdfReader.numPages):
                    pages += pdfReader.getPage(page).extractText()
                
                data = pages.split()
                x = 0 
                while x < len(data):
                    for i in data[x]:
                        if ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z') or 192 <= ord(i) <= 252:
                            pass
                        else:
                            data[x] = data[x].replace(i, '')
                    x += 1
                
                for i in data:
                    if len(i) < 4:
                        del data[data.index(i)]
                
                count = Counter(data)
                n = 0
                for i in list(self.d):
                    if i in list(count):
                        n += 1
                
                a = math.log(len(self.d) / n)
                b = len(count) / sum(count.values())
                c = a * b
                self.PTS[file] = c
                print(file + ' __________ ' + 'OK')

            except PyPDF2.utils.PdfReadError:
                pass
            except TypeError:
                pass
            except FileNotFoundError:
                pass
            except KeyError:
                pass

    def pts_files(self, dir):

        self.cont(dir)
        sorted_value = dict(sorted(self.PTS.items(), key=lambda kv: kv[1]))
        mean_value = np.mean(list(sorted_value.values()))
        for i in sorted_value.keys():
            x = 100 * ((sorted_value[i] / mean_value) - 1)
            self.fim[i] = x
            print(i + ' __________ ' + str(self.PTS[i]) + ' __________ ' + str(x) + '%')
            
        with open('Artigos_pontos.csv', 'w') as f:
            for i in sorted_value.keys():
                f.write('%s,%s\n'%(i, self.PTS[i]))
