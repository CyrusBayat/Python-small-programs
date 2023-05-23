

# student_score = {
#     "Harry": 81, 
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grade = {}

# for i in student_score:
    
#     if student_score[i] >= 91:
#         student_grade [i] = "Outstanding"
#     elif student_score[i] >= 81:
#         student_grade [i] = "Exceeds Expectations"
#     elif student_score[i] >= 71:
#         student_grade [i] = "Acceptable"
#     else:
#         student_grade [i] = "Fail"


# print(student_grade)


# capitals = {
#     "Iran": "Tehran",
#     "USA": "Washington DC",
#     "Franch": "Paris",
# }

# Travel_log =[
#     {
#         "Cuntry":"Iran",
#         "Cites":["Tehran","Babol Sar", "Lahijan"],
#         "visit": 12, 
#     },
#     {
#     "Cuntry":"Franch",
#     "cites" :["Paris","Lion"],
#     "visit": 1, 
#     }
# ]

# def add_new_cuntry(cuntry, visit, cites):

#     new_dic = {}
#     new_dic["cuntry"]=cuntry
#     new_dic["Cites"]=cites
#     new_dic["visit"]=visit


#     Travel_log.append(new_dic)



# add_new_cuntry("Russia", 2, ["Mosco", "Saint Peterzborg"])
# print(Travel_log)

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program.")

bit_list = []

def dic(name, bid):
    new_dic = {}
    new_dic["Names"]=name
    new_dic["bids"]=bid

    if len(bit_list) == 0:
        length = 1
    else:
        length = 0


    for i in range(len(bit_list) +length):
        bit_list.append(new_dic)


# winer
def winer_function():

    bit =0
    name =""
    for i in bit_list:

        if i ["bids"] > bit:
            bit = i["bids"] 
            name = i["Names"]
    print(f"The winner is {name} with a bid of {bit}")
    


kepp_running = True
while kepp_running == True:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $ "))
    
    ask_continue = input( "\nAre there any other bidders? Type 'yes' or 'no'.\n").lower()
    dic(name,bid)
    
    if ask_continue == "no":
        winer_function()
        kepp_running = False
    






