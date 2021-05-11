"""
created by Nagaj at 11/05/2021
"""


class Country:
    REGION = "NOTHING"

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"<{self.name}><{self.code}>"

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Code: {self.code}")

    @classmethod
    def show_region(cls):
        print(cls.REGION)


class NorthAfricaCountry(Country):
    REGION = "NA"


class AsiaCountry(Country):
    REGION = "ASIA"


class NorthAmericaCountry(Country):
    REGION = "NORTH AMERICA"


country = Country("SOMETHING", "00")

print(country)

eg = NorthAfricaCountry("EGYPT", "+20")
tunis = NorthAfricaCountry("TUNIS", "+216")
china = AsiaCountry("CHINA", "+86")
america = NorthAmericaCountry("US", "+1")

countries = [eg, china, america, tunis]

for country in countries:
    print("Region for '{}' is '{}'".format(country, country.REGION))
