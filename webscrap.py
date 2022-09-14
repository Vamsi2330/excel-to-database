from logging import exception
from os import stat
from pydoc import text
from re import S
from tkinter import END
from turtle import title
from bs4 import BeautifulSoup
import requests
import openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title="Covid 19 Report"
sheet.append(["State Name","Confirmed cases","Cuired cases","Died cases","State Code"])
try :
    url = "https://www.mygov.in/corona-data/covid19-statewise-status/"
    get = requests.get(url)
    soup = BeautifulSoup(get.text,"html.parser")
    sources = soup.find("div",class_= "content").find_all_next("div",class_="field field-name-field-select-state field-type-list-text field-label-above")
    for s  in sources:
        statename = s.text[12:]
        conf = s.find_next("div",class_="field field-name-field-total-confirmed-indians field-type-number-integer field-label-above").find_next("div",class_="field-item even").text
        
        cur = s.find_next("div",class_="field field-name-field-cured field-type-number-integer field-label-above").find_next("div",class_="field-item even").text
        die = s.find_next("div",class_="field field-name-field-deaths field-type-number-integer field-label-above").find_next("div",class_="field-item even").text
        statecode = s.find_next("div",class_="field field-name-field-state-code field-type-number-integer field-label-above").find_next("div",class_="field-item even").text
        sheet.append([statename,conf,cur,die,statecode])
    excel.save("Coid19.xls")
except exception as e :
    print(e)
