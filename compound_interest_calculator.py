initial_investment = int(input("Initial Investment: "))
initial_investment_display = initial_investment

initial_investment_year = int(input("Year: "))
initial_investment_year_display = initial_investment_year

interest_rate_1 = int(input("Interest rate: "))
interest_rate_2 = interest_rate_1 / 100
interest_rate_3 = interest_rate_2 + 1

year = 1

while initial_investment_year > 0:
    initial_investment = initial_investment * interest_rate_3
    print("--------------")
    print(f"{year}. Year(s): {round(initial_investment)}")
    year += 1
    initial_investment_year -= 1
    
print("--------------")

input(f"For {initial_investment_display} initial investment in {initial_investment_year_display} year(s), and with {interest_rate_1}% interest rate, you gathered~{round(initial_investment)}.")
