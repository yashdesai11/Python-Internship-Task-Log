#import panda
import pandas as pd


#Read Excel File
df = pd.read_excel("IPL.xls")
len_rows = len(df)
r_df = df.head(len_rows)


#Storing Data from Data Frames to Common List
year_list = r_df.values.tolist()

# To avoid traceback error transferred values in another list
final_list = []
final_list = final_list  + year_list


def easy_task_one(year):
    year_total_match = 0
    match_win_team_first = 0
    match_chase_win = 0
    match_tied = 0
    for val in final_list:
        if val[3]==int(year):
            year_total_match += 1
            if val[16]=="FirstBatting":
                match_win_team_first += 1
            elif val[16] == "Chasing":
                match_chase_win += 1
            elif val[16] == "Match Tied":
                match_tied += 1        
    print("Year : ",year)
    print("Total Number of Matches: ",(year_total_match))
    print("Number of matches Team Batting First Won: ",match_win_team_first)    
    print("Number of matches team Chasing Won: ",match_chase_win)
    print("Number of times Match Tied: ",match_tied)
    print("---------------------")
    
    
def easy_task_three():
    max_runrate=df['Bat_First_Run_Rate'].max()
    for valv in final_list:
        if valv[19]==13.25:
            print("Match Number: ",valv[0])
            print("Team Batting First: ",valv[5])
            print("Runs Scored: ",valv[7])
            print("Number of Overs: ",valv[9])
    print("Maximum Run Rate was: ",max_runrate)


def medium_task_one(year):
    close_count=0
    for valvv in final_list:
        if valvv[3]==int(year):
            if valvv[16] == "Match Tied" or valvv[21] == 3 or (valvv[16]=="Chasing" and valvv[17]==1 and valvv[18]=="wicket") or (valvv[16]=="FirstBatting" and valvv[17]==5 and valvv[18]=="run"):
                close_count += 1
    print("Number of Close Matches: ",close_count)



def medium_task_two(team):
    win_count=0
    win_bat_count=0
    for vaal in final_list:
        if vaal[15]==team:
            win_count += 1
    for vul in final_list:
        if vul[15]==team and vul[16]=="FirstBatting":
            win_bat_count += 1
    perc = (win_bat_count/win_count)*100
    print("Percent won batting first for {}: {}".format(team,perc))
    
    
def complex_task_one():
    for vl in final_list:
        #6 wickets reamining means 4 wickets are taken
        # 33 runs means 32 for tie and 1 to win
        # And for 33 runs in last 5 overs : Total Score - 15 over score
            if vl[16]=="FirstBatting" and vl[37]==4 and (vl[7]-vl[36])== 32:
                print("Match Number: ",vl[0])
                print("Team Batting Second: ",vl[6])
                print("Team Batting First: ",vl[5])
                print("Date: ",vl[2])

def complex_task_two():
    for vll in final_list:
        if vll[27]==2 and (vll[7]-vll[26])<25:
            print("Match Number: ",vll[0])
            print("Team Batting Second: ",vll[6])
            print("Team Batting First: ",vll[5])
            print("Date: ",vll[2])
            print("-----")
            print("")



    
    
print("-- Easy Task One -- ") 
print("--")
easy_task_one(2008) 
easy_task_one(2009)
easy_task_one(2010)
easy_task_one(2011)
easy_task_one(2012)
easy_task_one(2013)
easy_task_one(2014)
easy_task_one(2015)
print("--")
print("-----------------------------------------------------------------------")
print("")
print("")
print("-- Easy Task Two-- ")
print("--")
print("Venue: Mumbai")
print("Maximum Number of Matches: ",df['Venue'].value_counts().max())
print("--")
print("-----------------------------------------------------------------------")
print("")
print("")
print("-- Easy Task Three-- ")
print("--")
easy_task_three()
print("--")
print("-----------------------------------------------------------------------")
print("")
print("")
print("")
print("")
print("-- Medium Task One-- ")
print("--")
medium_task_one(2008)
medium_task_one(2009)
medium_task_one(2010)
medium_task_one(2011)
medium_task_one(2012)
medium_task_one(2013)
medium_task_one(2014)
medium_task_one(2015)
print("--")
print("-----------------------------------------------------------------------")
print("")
print("")
print("-- Medium Task Two-- ")
print("--")
medium_task_two("Chennai")
medium_task_two("Hyderabad")
medium_task_two("Mumbai")
medium_task_two("Kolkata")
print("--")
print("-----------------------------------------------------------------------")
print("")
print("")
print("")
print("")
print("-- Complex Task One-- ")
print("--")
complex_task_one()
print("--")
print("-----------------------------------------------------------------------")
print("")
print("")
print("-- Complex Task Two-- ")
print("--")
complex_task_two()
print("--")
print("-----------------------------------------------------------------------")