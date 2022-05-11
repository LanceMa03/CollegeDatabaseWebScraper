import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd

"""
* College Database
*
* This program allows users to enter a name of a college, and the program will display stats of that specific 
* college/university based on CollegeVine's website.
*
* @author Lance Ma
*
* @version September 19th, 2021
*
* Web Scraped from ("https://www.collegevine.com/")
"""


def webscrape():
    input1 = input("Enter the full name of the college/university: ")

    input1 = input1.replace(' ', '-').lower()

    url = ("https://www.collegevine.com/schools/" + input1)
    url2 = ("https://www.collegevine.com/schools/" + input1 + "/admission-requirements")
    url3 = ("https://www.collegevine.com/schools/" + input1 + "/finances")

    response = requests.get(url)

    if (response.status_code == 404):
        print("--------------------------------------")
        print("College not found")
    else:
        print("--------------------------------------")
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
            print(name.text)
            print("--------------------------------------")

        # Displays name of college
        print("Name: " + name.text)

        # Prints location of college
        print("Location: " + a.text)

        # Prints whether it's a public or private school
        print("Public or Private: " + publicOrPrivate[0].text)

        # Prints undergraduate population
        population = print("Undergraduate Population: " + undergrad[2].text)

        # Prints number of applicants
        print("Number of Applicants: " + acceptanceRate[1].text)

        # Prints acceptance rate

        print("Acceptance Rate: " + acceptanceRate[0].text)

        # Prints the yield rate of the university
        print("Yield Rate: " + acceptanceRate[2].text)

        # Prints the retention rate of the university
        retentionrate = print("Retention Rate: " + acceptanceRate[3].text)

        # Prints the student to faculty ratio of the university
        print("Student to faculty ratio: " + acceptanceRate[5].text)

        print("--------------------------------------")

        # Prints asian population
        print(Diversity[0].text)

        # Prints black population
        print(Diversity[1].text)

        # Prints hispanic population
        print(Diversity[2].text)

        # Prints native american population
        print(Diversity[3].text)

        # Prints white population
        print(Diversity[5].text)

        # Prints "other" population
        print(Diversity[4].text)

        print("--------------------------------------")
        print("SAT")

        # Prints SAT/ACT stats
        print("Average SAT: " + sat[1].text)
        print("SAT 25-75%: " + sat[2].text)
        print("Average Math SAT: " + sat[4].text)
        print("Average English SAT: " + sat[5].text)
        print("--------------------------------------")
        print("ACT")
        print("Average ACT: " + act[6].text)
        print("ACT 25-75%: " + act[7].text)
        print("Average Math ACT: " + act[9].text)
        print("Average English ACT: " + act[10].text)
        print("--------------------------------------")
        print("In state cost: " + inStateCost[0].text)
        print("Out of state cost: " + inStateCost[1].text)


print("--------------------------------------")

again = input("Do you want to enter another college/university? ")

if again.lower() == "y":
    webscrape()
else:
    print("Thank you for using the college database webscraper.")


def webscrape2():
    input1 = input("Enter the full name of the first college/university: ")  # stores the name of college 1 in input1
    input2 = input("Enter the full name of the second college/university: ")  # stores the name of college2 in input2

    input1 = input1.replace(' ', '-').lower()  # Makes the input of the user lowercase and replaces spaces with dashes
    input2 = input2.replace(' ', '-').lower()  # Makes the input of the user lowercase and replaces spaces with dashes

    url = ("https://www.collegevine.com/schools/" + input1)
    url2 = ("https://www.collegevine.com/schools/" + input1 + "/admission-requirements")
    url3 = ("https://www.collegevine.com/schools/" + input1 + "/finances")
    url4 = ("https://www.collegevine.com/schools/" + input2)
    url5 = ("https://www.collegevine.com/schools/" + input2 + "/admission-requirements")
    url6 = ("https://www.collegevine.com/schools/" + input2 + "/finances")

    response = requests.get(url)
    response4 = requests.get(url4)

    if ((response.status_code == 404) or (response4.status_code == 404)):
        print("--------------------------------------")
        print("College not found")
        print("--------------------------------------")
    else:
        response2 = requests.get(url2)
        response3 = requests.get(url3)
        response5 = requests.get(url5)
        response6 = requests.get(url6)

        soup2 = BeautifulSoup(response2.text, "html.parser")
        soup = BeautifulSoup(response.text, "html.parser")
        soup3 = BeautifulSoup(response3.text, "html.parser")
        soup4 = BeautifulSoup(response4.text, "html.parser")
        soup5 = BeautifulSoup(response5.text, "html.parser")
        soup6 = BeautifulSoup(response6.text, "html.parser")

        name = soup.find_all('h1', class_="header-title", )
        name2 = soup4.find_all('h1', class_="header-title", )

        y = soup.find_all('h1')
        z = soup4.find_all('h1')

        location = soup.find_all('h6', class_="header-pretitle")
        location2 = soup5.find_all('h6', class_="header-pretitle")

        a = soup.find('h6')
        b = soup5.find('h6')

        acceptanceRate = soup.find_all('div', class_="large font-weight-bold fw-bold mr-1")
        acceptanceRate2 = soup4.find_all('div', class_="large font-weight-bold fw-bold mr-1")

        Diversity = soup.find_all('div', class_="ml-2")  # Finds Diversity stats for college 1
        Diversity2 = soup4.find_all('div', class_="ml-2")  # Finds Diversity stats for college 2

        sat = soup2.find_all('div', class_="large font-weight-bold fw-bold")  # Finds SAT stats for college 1
        sat2 = soup5.find_all('div', class_="large font-weight-bold fw-bold")  # Finds SAT stats for college 2

        act = soup2.find_all('div', class_="large font-weight-bold fw-bold")  # Finds ACT stats for college 1
        act2 = soup5.find_all('div', class_="large font-weight-bold fw-bold")  # Finds ACT stats for college 2

        inStateCost = soup3.find_all('div',
                                     class_="large font-weight-bold fw-bold")  # Finds instate/out of state cost of attendence for college 1
        inStateCost2 = soup6.find_all('div',
                                      class_="large font-weight-bold fw-bold")  # Finds instate/out of state cost of attendence for college 2

        publicOrPrivate = soup.find_all('strong', class_="")  # Finds whether the school is public or private
        publicOrPrivate2 = soup4.find_all('strong', class_="")  # Finds whether the school is public or private

        undergrad = soup.find_all('strong', class_='')  # Finds the undergrad population
        undergrad2 = soup4.find_all('strong', class_='')  # Finds the undergrad population of college 2
        undergradpop = print(undergrad[2].text)

        for name in y:
            print("--------------------------------------")
            print(name.text)
            print("--------------------------------------")
            # Prints name of college
            print("Name: " + name.text)

            # Prints location
        print("Location: " + a.text)  # Displays location of college
        print("Public or Private: " + publicOrPrivate[0].text)
        print("Undergraduate Population: " + undergrad[2].text)  # Displays undergraduate population
        print("Number of Applicants: " + acceptanceRate[1].text)  # Displays the number of applications
        print("Acceptance Rate: " + acceptanceRate[0].text)  # Displays the acceptance rate of the university
        print("Yield Rate: " + acceptanceRate[2].text)  # Displays yield rate
        print("Retention Rate: " + acceptanceRate[3].text)  # Displays retention rate
        print("Student to faculty ratio: " + acceptanceRate[5].text)  # Displays the student to faculty ratio
        print("--------------------------------------")
        print(Diversity[0].text)  # Displays the asian population
        print(Diversity[1].text)  # Displays the black population
        print(Diversity[2].text)  # Displays the hispanic population
        print(Diversity[3].text)  # Displays the native american population
        print(Diversity[5].text)  # Displays the white population
        print(Diversity[4].text)  # Displays "other" population
        print("--------------------------------------")
        print("SAT")
        print("Average SAT: " + sat[1].text)  # Displays the average SAT of the university
        print("SAT 25-75%: " + sat[2].text)  # Displays the 25th to 75th percentile SAT scores
        print("Average Math SAT: " + sat[4].text)  # Displays the average math SAT of the university
        print("Average English SAT: " + sat[5].text)  # Displays the average reading and writing SAT of the university
        print("--------------------------------------")
        print("ACT")
        print("Average ACT: " + act[6].text)  # Displays the average ACT of the university
        print("ACT 25-75%: " + act[7].text)  # Displays tht 25th to 75th percentile ACT scores
        print("Average Math ACT: " + act[9].text)  # Displays the average math ACT of the university
        print("Average English ACT: " + act[10].text)  # Displays the average reading and writing ACT score
        print("--------------------------------------")
        print("In state cost: " + inStateCost[0].text)  # Displays the cost of attendance for in-state students
        print("Out of state cost: " + inStateCost[1].text)  # Displays the cost of attendance for out-of-state students

        for name2 in z:
            print("--------------------------------------")
            print(name2.text)
            print("--------------------------------------")
            print("Name: " + name2.text)  # Displays name of college 2

        print("Location: " + b.text)  # Displays location of college 2
        print("Public or Private: " + publicOrPrivate2[0].text)  # Displays whether the college is a public or private
        print("Undergraduate Population: " + undergrad2[2].text)  # Displays undergraduate population of college 2
        print("Number of Applicants: " + acceptanceRate2[1].text)  # Displays the number of applications received
        print("Acceptance Rate: " + acceptanceRate2[0].text)  # Displays the acceptance rate of college 2
        print("Yield Rate: " + acceptanceRate2[2].text)  # Displays yield rate of college 2
        print("Retention Rate: " + acceptanceRate2[3].text)  # Displays retention rate of college 2
        print("Student to faculty ratio: " + acceptanceRate2[5].text)  # Displays the student to faculty ratio
        print("--------------------------------------")
        print(Diversity2[0].text)  # Displays the asian population
        print(Diversity2[1].text)  # Displays the black population
        print(Diversity2[2].text)  # Displays the hispanic population
        print(Diversity2[3].text)  # Displays the native american population
        print(Diversity2[5].text)  # Displays the white population
        print(Diversity2[4].text)  # Displays "other" population
        print("--------------------------------------")
        print("SAT")
        print("Average SAT: " + sat2[1].text)  # Displays average SAT of college 2
        print("SAT 25-75%: " + sat2[2].text)  # Displays 25th to 75th percentile of SAT scores
        print("Average Math SAT: " + sat2[4].text)  # Displays average math SAT of college 2
        print("Average English SAT: " + sat2[5].text)  # Displays average reading and writing of college 2
        print("--------------------------------------")
        print("ACT")
        print("Average ACT: " + act2[6].text)  # Displays average ACT of college 2
        print("ACT 25-75%: " + act2[7].text)  # Displays 25th to 75th percentile of ACT scores
        print("Average Math ACT: " + act2[9].text)  # Displays average math SAT of college 2
        print("Average English ACT: " + act2[10].text)  # Displays average reading and writing of college 2
        print("--------------------------------------")
        print(
            "In state cost: " + inStateCost2[0].text)  # Displays the cost-of-attendance for in-state students
        print(
            "Out of state cost: " + inStateCost2[1].text)  # Displays the cost-of-attendance for in-state students
        print("--------------------------------------")


menuChoice = input("1: Compare two colleges/universities\n2: Compare a college/university\n3: Exit\n")

if (menuChoice == "1"):
    webscrape2()
elif (menuChoice == "2"):
    webscrape()
else:
    print("Thank you for using the college database webscraper")

print("Welcome to the college database!")
askCompare = input("Do you want to compare two universities/colleges? (Y or N) ")
askCompare = askCompare.upper()

if askCompare == "Y":  # If statements asking user if they want to compare two colleges.
    webscrape2()
elif (askCompare == "N"):  # If user doesn't want to compare colleges
    webscrape()
else:
    print("That's not a valid input. Thank you for using the college database.")
