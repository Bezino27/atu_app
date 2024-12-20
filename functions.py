from pandas.core.computation.common import result_type_many

FILEPATH = "data.txt"
actual_year = 2024
def get_file(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        data_local = file_local.readlines()
    return data_local

def write_to_file(new_data, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(new_data)

def get_players_by_year(year):
    data=get_file()
    result=[]
    for row in data:
        words=row.split()
        if len(words)==5:
            if words[3]==str(year):
                result.append(row)
    return result


def add_players(number,name,year,email):
    if number.isnumeric():
        row=number
    else:
        return False
    if " " in name:
        row=row +" "+ name.title()
        print(row)
    else:
        return False

    if year > 1950:
        row=row+" "+str(year)
    else:
        return False
    if "@" in email:
        row=row+" "+email
    else:
        return False

    data=get_file()
    row_check = row.split()
    for x in data:
        words=x.split()
        if len(words)==5:
            if words[0] == row_check[0]:
                if words[1]==row_check[1]:
                    if words[2]==row_check[2]:
                        if words[3]==row_check[3]:
                            if words[4] == row_check[4]:
                                return 1

    data.append(row+'\n')
    write_to_file(data)


def view_by_category(category,year):
    result=[]
    if category=="Mladšia prípravka":
        for i in range(8):
            result+=get_players_by_year(year-(i+1))

    elif category=="Staršia prípravka":
        result1=get_players_by_year(year-9)
        result2=get_players_by_year(year-10)
        result=result1+result2

    elif category=="Mladší žiaci":
        result1=get_players_by_year(year-11)
        result2=get_players_by_year(year-12)
        result = result1 + result2
    elif category=="Starší žiaci":
        result1=get_players_by_year(year-13)
        result2=get_players_by_year(year-14)
        result = result1 + result2

    elif category=="Dorastenci":
        result1=get_players_by_year(year-15)
        result2=get_players_by_year(year-16)
        result = result1 + result2
    elif category=="Juniori":
        result1=get_players_by_year(year-17)
        result2=get_players_by_year(year-18)
        result = result1 + result2
    elif category=="Muži":
        for i in range(19):
            result1=get_players_by_year(year-(19+i))
            result = result + result1
    return result

def delete_player(name,year):
    data=get_file()
    if " " not in name:
        return False
    name=name.title()
    check_name = name.split()
    print(check_name)
    for index,row in enumerate(data):
        words=row.split()
        if len(words)==5:
            if words[3]==str(year):
                if words[1] in check_name[0]:
                    if words[2]==check_name[1]:
                        data.pop(index)
                    else:
                        return False

    write_to_file(data)
    return True

def edit_player(name,year):
    data=get_file()
    check_name = name.split()
    for index,row in enumerate(data):
        words=row.split()
        if len(words)==4:
            if words[0]==check_name[0]:
                if words[1] in check_name[1]:
                    if words[2]==str(year):
                        print("player can be edited")
                        print(row)
                        delete_player(name,year)
                        new_name=input("Enter player name: ")
                        new_year=int(input("Enter year: "))
                        new_mail=input("Enter email: ")
                        add_players(new_name,new_year,new_mail)

                    else:
                        print("Player is not in our database")
                        return False

def get_player_index(name,year,mail):
    data=get_file()
    row=name+" "+str(year)+" "+mail
    row_check = row.split()
    for index,array in enumerate(data):
        words=array.split()
        if len(words)==4:
            if words[0]==row_check[0]:
                if words[1]==row_check[1]:
                    if words[2]==row_check[2]:
                        if words[3]==row_check[3]:
                            return index


def is_player_exists(name,year):
    data=get_file()
    row=name.title()+" "+str(year)
    row_edit = row.split()
    for array in data:
        words=array.split()
        if len(words)==5:
            if words[1]==row_edit[0]:
                if words[2]==row_edit[1]:
                    if words[3]==row_edit[2]:
                            return True


