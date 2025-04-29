improvements = int(input())

improvements_per_year = int(input())

frozen_year = 2022

years_passed = (improvements + improvements_per_year - 1) // improvements_per_year

current_year = frozen_year + years_passed

print(current_year)
