###NO.1

# def calculate_years(principal,interest,tax,desired):
#     principal_tax = 0
#     years = 0
#     while principal < desired :   
#         principal_tax = ((principal + (principal * interest)) - (principal * interest * tax))
#         years += 1
#         principal = principal_tax
#         if years == 1 :
#             print("After {}st year --->  P = {}".format(years,principal))
#         elif years == 2 :
#             print("After {}nd year --->  P = {}".format(years,principal))
#         elif years == 3 :
#             print("After {}rd year --->  P = {}".format(years,principal))

#     print("Thus Mr. Scoorage has to wait for {} for the intial principal for the ammount to the desired sum".format(years))

# calculate_years(1000,0.05,0.18,1100)

###NO.2
def expanded_form(num):
    while num > 0 :
        if num >= 1000 :
            a = num // 1000
            ribuan = 1000 * a
            sisa = num - ribuan
            num = sisa
            
        elif num >= 100 :
            b = num // 100
            ratusan = 100 * b
            sisa = num - ratusan
            num = sisa
            
        elif num >= 10 :
            c = num // 10
            puluhan = 10 * c
            sisa = num - puluhan
            num = sisa
            
        elif num < 10 :
            satuan = num
            num = sisa

    print("{} + {} + {} + {}".format(ribuan,ratusan,puluhan,satuan))
expanded_form(70304)

###NO.3
# def tower_builder(n_floors, block_size):
#     z = ''
#     w,h = block_size
#     for i in range(n_floors):
#         for j in range(h):
#             for k in range(w):
                
#                 z += '*'
#             z *= 2
#             z += '\n'
#     print(z)
# tower_builder(6,(2,1))