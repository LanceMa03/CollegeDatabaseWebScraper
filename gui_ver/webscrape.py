import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd

"""
* College Database
*
* This program allows users to enter a name of a college, and the program will display stats of that specific college/university based on CollegeVine's website.
*
* @author Lance Ma
*
* @version September 19th, 2021
*
* Web Scraped from ("https://www.collegevine.com/")
"""


def webscrape(collegeName):
    input1 = collegeName

    input1 = input1.replace(' ', '-').lower()

    url = ("https://www.collegevine.com/schools/" + input1)
    url2 = ("https://www.collegevine.com/schools/" + input1 + "/admission-requirements")
    url3 = ("https://www.collegevine.com/schools/" + input1 + "/finances")

    response = requests.get(url)

    if (response.status_code == 404):
        return -1
    else:

        list1 = []
        for i in range(24):
            list1.append(i)

        response2 = requests.get(url2)
        response3 = requests.get(url3)

        soup2 = BeautifulSoup(response2.text, "html.parser")
        soup = BeautifulSoup(response.text, "html.parser")
        soup3 = BeautifulSoup(response3.text, "html.parser")

        name = soup.find_all('h1', class_="header-title", )

        y = soup.find_all('h1')

        location = soup.find_all('h6', class_="header-pretitle")

        a = soup.find('h6')

        acceptanceRate = soup.find_all('div', class_="large font-weight-bold fw-bold mr-1")

        Diversity = soup.find_all('div', class_="ml-2")

        sat = soup2.find_all('div', class_="large font-weight-bold fw-bold")

        act = soup2.find_all('div', class_="large font-weight-bold fw-bold")

        inStateCost = soup3.find_all('div', class_="large font-weight-bold fw-bold")

        publicOrPrivate = soup.find_all('strong', class_="")

        undergrad = soup.find_all('strong', class_='')

        for name in y:
            print("")
            #print(name.text)
            #print("--------------------------------------")

        # Displays name of college
        #print("Name: " + name.text)
        c_name = name.text
        list1[0] = "Name: " + c_name

        # Prints location of college
        #print("Location: " + a.text)
        list1[1] = "Location: " + a.text

        # Prints whether it's a public or private school
        #print("Public or Private: " + publicOrPrivate[0].text)
        list1[2] = "Public or Private: " + publicOrPrivate[0].text

        # Prints undergraduate population
        #print("Undergraduate Population: " + undergrad[2].text)
        list1[3] = "Undergraduate Population: " + undergrad[2].text

        # Prints number of applicants
        #print("Number of Applicants: " + acceptanceRate[1].text)
        list1[4] = "Number of Applicants: " + acceptanceRate[1].text

        # Prints acceptance rate
        #print("Acceptance Rate: " + acceptanceRate[0].text)
        list1[5] = "Acceptance Rate: " + acceptanceRate[0].text

        # Prints the yield rate of the university
        #print("Yield Rate: " + acceptanceRate[2].text)
        list1[6] = "Yield Rate: " + acceptanceRate[2].text

        # Prints the retention rate of the university
        #print("Retention Rate: " + acceptanceRate[3].text)
        list1[7] = "Retention Rate: " + acceptanceRate[3].text

        # Prints the student to faculty ratio of the university
        #print("Student to faculty ratio: " + acceptanceRate[5].text)
        list1[8] = "Student to faculty ratio: " + acceptanceRate[5].text

        #print("--------------------------------------")

        # Prints asian population
        #print(Diversity[0].text)
        list1[8] = Diversity[0].text

        # Prints black population
        #print(Diversity[1].text)
        list1[9] = Diversity[1].text

        # Prints hispanic population
        #print(Diversity[2].text)
        list1[10] = Diversity[2].text

        # Prints native american population
        #print(Diversity[3].text)
        list1[11] = Diversity[3].text

        # Prints white population
        #print(Diversity[5].text)
        list1[12] = Diversity[5].text

        # Prints "other" population
        #print(Diversity[4].text)
        list1[13] = Diversity[4].text

        #print("--------------------------------------")
        #print("SAT")

        # Prints SAT/ACT stats
        #print("Average SAT: " + sat[1].text)
        list1[14] = "Average SAT: " + sat[1].text

        #print("SAT 25-75%: " + sat[2].text)
        list1[15] = "SAT 25-75%: " + sat[2].text

        #print("Average Math SAT: " + sat[4].text)
        list1[16] = "Average Math SAT: " + sat[4].text

        #print("Average English SAT: " + sat[5].text)
        list1[17] = "Average English SAT: " + sat[5].text

        #print("--------------------------------------")
        #print("ACT")

        #print("Average ACT: " + act[6].text)
        list1[18] = "Average ACT: " + act[6].text

        #print("ACT 25-75%: " + act[7].text)
        list1[19] = "ACT 25-75%: " + act[7].text

        #print("Average Math ACT: " + act[9].text)
        list1[20] = "Average Math ACT: " + act[9].text

        #print("Average English ACT: " + act[10].text)
        list1[21] = "Average English ACT: " + act[10].text

        #print("--------------------------------------")
        #print("In state cost: " + inStateCost[0].text)
        list1[22] = "In state cost: " + inStateCost[0].text

        #print("Out of state cost: " + inStateCost[1].text)
        list1[23] = "Out of state cost: " + inStateCost[1].text

        return list1




