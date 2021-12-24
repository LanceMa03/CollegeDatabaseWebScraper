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


def webscrape():
    input1 = input("Enter the full name of the university: ")
    print("--------------------------------------")

    input1 = input1.replace(' ', '-').lower()

    url = ("https://www.collegevine.com/schools/" + input1)
    url2 = ("https://www.collegevine.com/schools/" + input1 + "/admission-requirements")
    url3 = ("https://www.collegevine.com/schools/" + input1 + "/finances")

    response = requests.get(url)
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
        name = print("Name: " + name.text)  # Displays name of college

    location = print("Location: " + a.text)  # Displays the location of the college
    publicOrPrivate = print(
        "Public or Private: " + publicOrPrivate[0].text)  # Displays whether it's a public or private school
    population = print("Undergraduate Population: " + undergrad[2].text)  # Displays undergraduate population
    applicationnumbers = print(
        "Number of Applicants: " + acceptanceRate[1].text)  # Displays the amount of applicants the college recieved
    acceptancerate = print(
        "Acceptance Rate: " + acceptanceRate[0].text)  # Displays the acceptance rate of the university
    yieldrate = print("Yield Rate: " + acceptanceRate[2].text)  # Displays the yield rate of the university
    retentionrate = print("Retention Rate: " + acceptanceRate[3].text)  # Displays the retention rate of the university
    studenttofacultyratio = print("Student to faculty ratio: " + acceptanceRate[
        5].text)  # Displays the student to faculty ratio of the university
    print("--------------------------------------")
    asianDiversity = print(Diversity[0].text)  # Displays the asian population
    blackDiversity = print(Diversity[1].text)  # Displays the black population
    hispanicDiversity = print(Diversity[2].text)  # Displays the hispanic population
    nativeAmericanDiversity = print(Diversity[3].text)  # Displays the native american population
    whiteDiversity = print(Diversity[5].text)  # Displays the white population
    otherDiversity = print(Diversity[4].text)  # Displays the "other" population
    print("--------------------------------------")
    print("SAT")
    averageSAT = print("Average SAT: " + sat[1].text)  # Displays the average SAT of the college
    sat25to75 = print("SAT 25-75%: " + sat[2].text)  # Displays the 25th to 75th percentile of SAT scores
    averageMathSAT = print("Average Math SAT: " + sat[4].text)  # Displays the average math SAT of the college
    averageEnglishSAT = print(
        "Average English SAT: " + sat[5].text)  # Displays the average reading and writing of the college
    print("--------------------------------------")
    print("ACT")
    averageACT = print("Average ACT: " + act[6].text)  # Displays the average ACT score of the college
    act25to75 = print("ACT 25-75%: " + act[7].text)  # Displays the average 25th to 75th percentile of ACT scores
    averageMathACT = print("Average Math ACT: " + act[9].text)  # Displays the average math ACT of the college
    averageEnglishACT = print(
        "Average English ACT: " + act[10].text)  # Displays the average reading and writing ACt of the college
    print("--------------------------------------")
    inStateCOA = print("In state cost: " + inStateCost[0].text)  # Displays the cost-of-attendance for in-state students
    outOfStateCOA = print(
        "Out of state cost: " + inStateCost[1].text)  # Displays the cost-of-attendance for out-of-state students
    print("--------------------------------------")
    again = input("Do you want to enter another college/university? ")

    if again.lower() == "y":
        webscrape()
    else:
        print("Thank you for using the college database webscraper.")


def webscrape2():
    input1 = input("Enter the full name of the first university: ")  # stores the name of college 1 in input1
    input2 = input("Enter the full name of the second university: ")  # stores the name of college2 in input2

    input1 = input1.replace(' ', '-').lower()  # Makes the input of the user lowercase and replaces spaces with dashes
    input2 = input2.replace(' ', '-').lower()  # Makes the input of the user lowercase and replaces spaces with dashes

    url = ("https://www.collegevine.com/schools/" + input1)
    url2 = ("https://www.collegevine.com/schools/" + input1 + "/admission-requirements")
    url3 = ("https://www.collegevine.com/schools/" + input1 + "/finances")
    url4 = ("https://www.collegevine.com/schools/" + input2)
    url5 = ("https://www.collegevine.com/schools/" + input2 + "/admission-requirements")
    url6 = ("https://www.collegevine.com/schools/" + input2 + "/finances")

    response = requests.get(url)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)
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
        name = print("Name: " + name.text)  # Displays name of college

    location = print("Location: " + a.text)  # Displays location of college
    publicOrPrivate = print("Public or Private: " + publicOrPrivate[
        0].text)  # Displays whether the college is a public or private university
    population = print("Undergraduate Population: " + undergrad[2].text)  # Displays undergraduate population
    applicationnumbers = print(
        "Number of Applicants: " + acceptanceRate[1].text)  # Displays the number of applications the college recieved
    acceptancerate = print(
        "Acceptance Rate: " + acceptanceRate[0].text)  # Displays the acceptance rate of the university
    yieldrate = print("Yield Rate: " + acceptanceRate[2].text)  # Displays yield rate
    retentionrate = print("Retention Rate: " + acceptanceRate[3].text)  # Displays retention rate
    studenttofacultyratio = print(
        "Student to faculty ratio: " + acceptanceRate[5].text)  # Displays the student to faculty ratio
    print("--------------------------------------")
    asianDiversity = print(Diversity[0].text)  # Displays the asian population
    blackDiversity = print(Diversity[1].text)  # Displays the black population
    hispanicDiversity = print(Diversity[2].text)  # Displays the hispanic population
    nativeAmericanDiversity = print(Diversity[3].text)  # Displays the native american population
    whiteDiversity = print(Diversity[5].text)  # Displays the white population
    otherDiversity = print(Diversity[4].text)  # Displays "other" population
    print("--------------------------------------")
    print("SAT")
    averageSAT = print("Average SAT: " + sat[1].text)  # Displays the average SAT of the university
    sat25to75 = print("SAT 25-75%: " + sat[2].text)  # Displays the 25th to 75th percentile SAT scores
    averageMathSAT = print("Average Math SAT: " + sat[4].text)  # Displays the average math SAT of the university
    averageEnglishSAT = print(
        "Average English SAT: " + sat[5].text)  # Displays the average reading and writing SAT of the university
    print("--------------------------------------")
    print("ACT")
    averageACT = print("Average ACT: " + act[6].text)  # Displays the average ACT of the university
    act25to75 = print("ACT 25-75%: " + act[7].text)  # Displays tht 25th to 75th percentile ACT scores
    averageMathACT = print("Average Math ACT: " + act[9].text)  # Displays the average math ACT of the university
    averageEnglishACT = print(
        "Average English ACT: " + act[10].text)  # Displays the average reading and writing ACT score
    print("--------------------------------------")
    inStateCOA = print("In state cost: " + inStateCost[0].text)  # Displays the cost of attendance for in-state students
    outOfStateCOA = print(
        "Out of state cost: " + inStateCost[1].text)  # Displays the cost of attendance for out-of-state students

    for name2 in z:
        print("--------------------------------------")
        print(name2.text)
        print("--------------------------------------")
        name2 = print("Name: " + name2.text)  # Displays name of college 2

    location2 = print("Location: " + b.text)  # Displays location of college 2
    publicOrPrivate2 = print("Public or Private: " + publicOrPrivate2[
        0].text)  # Displays whether the college 2 is a public or private university
    population2 = print(
        "Undergraduate Population: " + undergrad2[2].text)  # Displays undergraduate population of college 2
    applicationnumbers2 = print(
        "Number of Applicants: " + acceptanceRate2[1].text)  # Displays the number of applications college 2 recieved
    acceptancerate2 = print("Acceptance Rate: " + acceptanceRate2[0].text)  # Displays the acceptance rate of college 2
    yieldrate2 = print("Yield Rate: " + acceptanceRate2[2].text)  # Displays yield rate of college 2
    retentionrate2 = print("Retention Rate: " + acceptanceRate2[3].text)  # Displays retention rate of college 2
    studenttofacultyratio2 = print(
        "Student to faculty ratio: " + acceptanceRate2[5].text)  # Displays the student to faculty ratio of college 2
    print("--------------------------------------")
    asianDiversity2 = print(Diversity2[0].text)  # Displays the asian population
    blackDiversity2 = print(Diversity2[1].text)  # Displays the black population
    hispanicDiversity2 = print(Diversity2[2].text)  # Displays the hispanic population
    nativeAmericanDiversity2 = print(Diversity2[3].text)  # Displays the native american population
    whiteDiversity2 = print(Diversity2[5].text)  # Displays the white population
    otherDiversity2 = print(Diversity2[4].text)  # Displays "other" population
    print("--------------------------------------")
    print("SAT")
    averageSAT2 = print("Average SAT: " + sat2[1].text)  # Displays average SAT of college 2
    sat25to752 = print("SAT 25-75%: " + sat2[2].text)  # Displays 25th to 75th percentile of SAT scores
    averageMathSAT2 = print("Average Math SAT: " + sat2[4].text)  # Displays average math SAT of college 2
    averageEnglishSAT2 = print(
        "Average English SAT: " + sat2[5].text)  # Displays average reading and writing of college 2
    print("--------------------------------------")
    print("ACT")
    averageACT2 = print("Average ACT: " + act2[6].text)  # Displays average ACT of college 2
    act25to752 = print("ACT 25-75%: " + act2[7].text)  # Displays 25th to 75th percentile of ACT scores
    averageMathACT2 = print("Average Math ACT: " + act2[9].text)  # Displays average math SAT of college 2
    averageEnglishACT2 = print(
        "Average English ACT: " + act2[10].text)  # Displays average reading and writing of college 2
    print("--------------------------------------")
    inStateCOA2 = print(
        "In state cost: " + inStateCost2[0].text)  # Displays the cost-of-attendance for in-state students
    outOfStateCOA2 = print(
        "Out of state cost: " + inStateCost2[1].text)  # Displays the cost-of-attendance for in-state students

    menuChoice = input("1: Compare Two College\n2: Compare a college\n3: Exit")

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
