import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def company_revenue(data):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    driver.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")

    revenue = driver.find_element(By.XPATH,
                                  '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[' + str(data) + ']/td[4]').text

    revenue = revenue.replace(",", "")
    return int(revenue)


if __name__ == '__main__':
    print("Game initializing, please wait...")
    tax_percent = random.randrange(1, 30)
    company_index = random.randrange(1, 99)
    company_earned = company_revenue(company_index)
    tax_paid = company_earned * tax_percent / 100
    #print(tax_paid)
    #print(tax_percent)
    answer = "no"

    counter = 1

    while counter < 8:
        guess = input("Enter a number\n")
        try:
            guess = int(guess)
            if guess > tax_paid + 200:
                print("Accountant: We did not pay that many tax.")
            elif guess < tax_paid - 200:
                print("Accountant: We paid more than that.")
            elif guess == tax_paid + 100 or guess == tax_paid - 100:
                print("Accountant: You almost have it.")
            elif guess == tax_paid:
                print("Accountant: No way! how do you get this extra number ")
            else:
                print("Accountant: That is very close")
        except:
            print("Invalid input")

        counter += 1
        print("You have", 8 - counter, "more guess left")

    if tax_percent >= 15:
        answer = "yes"

    decision = input("Determine whether this company had paid at least 15% tax on its revenue. Enter yes or no\n")
    if decision.lower() == answer:
        print("Great job, IRS tax officer.")
    else:
        print("Company boss: Great job, IRS tax officer, thank you for saving my money.")

    print("statistics: company revenue", company_earned, "\n tax paid:", tax_paid, "\n tax percentage:", tax_percent,
          "%\n Thank you for playing, exiting...")
