def convertor(usd_val):
    inr_val = usd_val*83
    print(usd_val,"USD = ",inr_val,"INR")

usd_val = int(input("Enter the number :- "))
convertor(usd_val)