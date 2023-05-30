import random as r

total_circulating_money = 100


class Consumers:
    def __init__(self, economic_percentage):
        self.total_money = total_circulating_money * economic_percentage
        self.new_total_money = self.total_money
        self.targetted_econmoic_percentage = economic_percentage
        self.total_consumers = 1000
        self.population_employed = self.total_consumers * 0.8
        self.buying_attitude = 0.9
        self.working_attitude = 0.7
        self.saving_rate = 0.1
        self.trading_attitude = 0.2

    def income(self, producers_class):
        self.new_total_money += self.population_employed * producers_class.salary
        producers_class.new_total_money -= (
            self.population_employed * producers_class.salary
        )

    def consumption_expenditure(self, producers_class):
        self.new_total_money -= (self.total_consumers * self.buying_attitude) * 10
        producers_class.new_total_money += (
            self.total_consumers * self.buying_attitude
        ) * 10

    def savings(self, financial_sector_class):
        self.new_total_money -= self.total_money * self.saving_rate
        financial_sector_class.new_total_money += self.total_money * self.saving_rate

    def update_values(self):
        # Update offical total money simultaneously
        self.total_money = self.new_total_money
        # If households have too much money, they will consume more, work less, and save less
        if (
            self.new_total_money
            > total_circulating_money * self.targetted_econmoic_percentage
        ):
            self.buying_attitude += 0.01
            self.working_attitude -= 0.01
            self.saving_rate -= 0.01
        # If households do not have enough money, they will consume less, work more, and save more
        else:
            self.buying_attitude -= 0.01
            self.working_attitude += 0.01
            self.saving_rate += 0.01


class Producers:
    def __init__(self, economic_percentage):
        self.total_money = total_circulating_money * economic_percentage
        self.new_total_money = self.total_money
        self.targetted_econmoic_percentage = economic_percentage
        self.hiring_attitude = 0.8
        self.salary = 20
        self.trading_attitude = 0.1

    def hire(self, consumers_class):
        if self.hiring_attitude > consumers_class.working_attitude:
            consumers_class.population_employed += r.randint(
                0, round((self.hiring_attitude - consumers_class.working_attitude) * 10)
            )
        elif self.hiring_attitude == consumers_class.working_attitude:
            consumers_class.population_employed += round(r.uniform(-1, 1) * 10)
        else:
            consumers_class.population_employed -= r.randint(
                0, (consumers_class.working_attitude - self.hiring_attitude) * 10
            )

    def interest(self, financial_sector_class):
        self.new_total_money -= (
            financial_sector_class.money_invested * financial_sector_class.interest_rate
        )
        financial_sector_class.new_total_money += (
            financial_sector_class.money_invested * financial_sector_class.interest_rate
        )

    def update_values(self):
        # Update offical total money simultaneously
        self.total_money = self.new_total_money
        # If producers have too much money, they will hire more employees, and pay them more
        if (
            self.total_money
            > total_circulating_money * self.targetted_econmoic_percentage
        ):
            self.salary += 0.01
            self.hiring_attitude += 0.01
        # If producers do not have enough money, they will hire less employees, and pay them less
        else:
            self.salary -= 0.01
            self.hiring_attitude -= 0.01


class Government:
    def __init__(self, economic_percentage):
        self.total_money = total_circulating_money * economic_percentage
        self.new_total_money = self.total_money
        self.targetted_econmoic_percentage = economic_percentage
        self.printing_rate = 0.5
        self.corruption = 0
        self.government_spending_rate = 0.1
        self.tax_rate = 0.3

    def government_spendings(self, producers_class):
        self.new_total_money -= round(self.total_money * self.government_spending_rate)
        producers_class.new_total_money += round(self.total_money * self.government_spending_rate)

    def taxes_and_rates(self, consumers_class):
        self.new_total_money += round(consumers_class.total_money * self.tax_rate)

    def print_money(self):
        self.new_total_money += self.total_money * (
            self.printing_rate + self.corruption
        )

    def update_values(self):
        # Update offical total money simultaneously
        self.total_money = self.new_total_money
        # If the government has too much money, it will print less, tax less, and spend more
        if (
            self.total_money
            > total_circulating_money * self.targetted_econmoic_percentage
        ):
            self.printing_rate -= 0.07
            self.tax_rate -= 0.07
            self.government_spending_rate += 0.07
        # If the government does not have enough money, it will print more, tax more, and spend less
        else:
            self.printing_rate += 0.01
            self.tax_rate += 0.01
            self.government_spending_rate -= 0.01


class Financial_Sector:
    def __init__(self, economic_percentage):
        self.total_money = total_circulating_money * economic_percentage
        self.new_total_money = self.total_money
        self.targetted_econmoic_percentage = economic_percentage
        self.interest_rate = 0.1
        self.investment_rate = 0.1
        self.money_invested = 0

    def investment(self, producers_class):
        self.new_total_money -= self.total_money * self.investment_rate
        producers_class.new_total_money += self.total_money * self.investment_rate
        self.money_invested = self.total_money * self.investment_rate

    def update_values(self):
        # Update offical total money simultaneously
        self.total_money = self.new_total_money

        # Update the money invested amount
        self.money_invested = round(self.money_invested*0.4)

        # If the financial sector has too much money, it will charge less and invest more
        if (
            self.total_money
            > total_circulating_money * self.targetted_econmoic_percentage
        ):
            self.interest_rate -= 0.01
            self.investment_rate += 0.01
        # If the financial sector needs more money, it will charge more and invest less
        else:
            self.interest_rate += 0.01
            self.investment_rate -= 0.01


class Foreign_Sector:
    def __init__(self, starting_general_trading_attitude):
        self.general_trading_attitude = starting_general_trading_attitude
        self.balance_of_trade = 0

    def clear_balance_of_trade(self):
        self.balance_of_trade = 0
    
    def import_payments(self, consumers_class):
        consumers_class.total_money -= (self.general_trading_attitude + consumers_class.trading_attitude) * consumers_class.total_money
        self.balance_of_trade += (self.general_trading_attitude + consumers_class.trading_attitude) * consumers_class.total_money
        print(f"import payments: {(self.general_trading_attitude + consumers_class.trading_attitude) * consumers_class.total_money}")
        
    def export_payments(self, producers_class):
        producers_class.total_money += (self.general_trading_attitude + producers_class.trading_attitude) * producers_class.total_money
        self.balance_of_trade -= (self.general_trading_attitude + producers_class.trading_attitude) * producers_class.total_money
        print(f"export_payements: -${(self.general_trading_attitude + producers_class.trading_attitude) * producers_class.total_money}")
    
    def update_values(self, consumers_class, producers_class):
        # If the foreign sector is exporting more to this economy than the imports it receives from the country, it will increase the amount of imports and decrease the amount of exports
        if self.balance_of_trade <= 0:
            consumers_class.trading_attitude += 0.1
            producers_class.trading_attitude -= 0.3
        # If the foreign secotr is exporting less to this economy than it recieves in imports from this economy, then it will be exporting more and slightly decrease importing
        elif self.balance_of_trade > 0:
            consumers_class.trading_attitude -= 0.05
            producers_class.trading_attitude += 0.1        

class Simulation:
    def __init__(self):
        self.consumer_sector = Consumers(0.25)
        self.producer_sector = Producers(0.4)
        self.government_sector = Government(0.15)
        self.financial_sector = Financial_Sector(0.2)
        self.foreign_sector = Foreign_Sector(0.3)
        self.round_number = 0

    def calculate_statistics(self):
        pass

    def run_round(self):
        # Update the round number
        self.round_number += 1

        # Update the total money in circulation
        total_circulating_money = (
            self.consumer_sector.total_money
            + self.producer_sector.total_money
            + self.government_sector.total_money
            + self.financial_sector.total_money
        )

        # Print important information
        print()
        print()
        print()
        print(f"Round: {str(self.round_number)}")
        print(f"Total circulating money in EEMS is: ${str(int(total_circulating_money))}!")
        print(f"Consumers have ${str(int(self.consumer_sector.total_money))}!")
        print(f"Producers have ${str(int(self.producer_sector.total_money))}!")
        print(f"The government has ${str(int(self.government_sector.total_money))}!")
        print(f"The financial sector has ${str(int(self.financial_sector.total_money))}!")
        print(f"The foreign sector has a balance of trade of {str(int(self.foreign_sector.balance_of_trade))}!")

        # Run all the functions for consumers
        self.consumer_sector.income(self.producer_sector)
        self.consumer_sector.consumption_expenditure(self.producer_sector)
        self.consumer_sector.savings(self.financial_sector)

        # Run all the functions for producers
        self.producer_sector.hire(self.consumer_sector)
        self.producer_sector.interest(self.financial_sector)

        # Run all the functions for the government
        self.government_sector.government_spendings(self.producer_sector)
        self.government_sector.taxes_and_rates(self.consumer_sector)
        self.government_sector.print_money()

        # Run all the functions for the financial sector
        self.financial_sector.investment(self.producer_sector)

        # Run all the functions for the foreign sector
        self.foreign_sector.clear_balance_of_trade()
        self.foreign_sector.import_payments(self.consumer_sector)
        self.foreign_sector.export_payments(self.producer_sector)

        # Update all the variables of each sector class
        self.consumer_sector.update_values()
        self.producer_sector.update_values()
        self.government_sector.update_values()
        self.financial_sector.update_values()
        self.foreign_sector.update_values(self.consumer_sector, self.producer_sector)

    def run_multiple_rounds(self, num_rounds):
        for round in range(0, num_rounds):
            self.run_round()


circular_flow_of_income_simulation = Simulation()
circular_flow_of_income_simulation.run_multiple_rounds(100)
