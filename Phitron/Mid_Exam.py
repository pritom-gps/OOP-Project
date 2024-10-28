class Star_Cinema:
    _hall_list=[]
    def __init__(self,hall_info):
        self.hall_info=hall_info

    def entry_hall(self):
        self._hall_list.append(self.hall_info)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.seats={}
        self.show_list=[]
        self.hall_info=(rows,cols,hall_no)
        super().__init__(self.hall_info)
    
    def entry_show(self,id,movie_name,time):
        self.show_list.append((id,movie_name,time))
        self.seats[id]=[['0'] * self.cols for _ in range(self.rows)]
    
    def book_seats(self,id,seat):
        self.seats[id][seat[0]][seat[1]]='1'
          
    def view_show_list(self):
        print(f'\nShow_ID\t\tMovie_Name\t\tTime\n--------\t----------\t\t----\n')
        for x,y,z in self.show_list:
             print(f'{x}\t\t{y}\t\t{z}\n')
            
    def view_available_seats(self,id):
        for x in  self.seats[id]:
            for y in x:
                print(y,end=('   '))
            print('\n')
        
Hall_Name=[]
Hall_1=Hall(10,10,1)
Hall_1.entry_hall()
Hall_1.entry_show('101','Jurassic Park',9)
Hall_1.entry_show('102','Captain America',12)
Hall_Name.append(Hall_1)

Hall_2=Hall(8,8,2)
Hall_2.entry_hall()
Hall_2.entry_show('201','Wrong Turn',9)
Hall_2.entry_show('202','Evil Dead',12)
Hall_Name.append(Hall_2)

run_p=True
while run_p:
    print('\n\nWelcome To Star Cinema')
    print('----------------------\nHere The Hall List:\n')
    def hall_func():
        print('Hall_Serial\tHall_Name\tHall_Capacity\n')
        for hl_serial,hl_list in enumerate(Star_Cinema._hall_list):
            print(f'{hl_serial}\t\tHall_{hl_serial}\t\t{hl_list[0]}*{hl_list[1]}','\n')
        
        hl_sl=int(input('Please Select A Hall SeriaL Number: '))
        if hl_sl>=len(Star_Cinema._hall_list):
            print('\nInvaid Hall Number!\nPlease Select A Correct Hall Number.\n')
            hall_func()
        else:
            for sl,hl in enumerate(Star_Cinema._hall_list):
                if sl==hl_sl:
                    def main_menu():
                        print('\n\t1. View Show List\n\t2. Book Seat\n\t3. View Available Seats\n\t4. Home\n\t5. Exit\n')
                        op=int(input('Please Select An Option: '))

                        if op==5:
                            # 5. Exit
                            print('\nThanks For Visiting Star Cinema\nHave A Great Day !')
                            return
                        else:
                            if op>=1 and op<=3:
                                def check_show_id(show_id):
                                    valid=False
                                    for item in Hall_Name[sl].show_list:
                                        if item[0]==show_id:
                                            valid=True
                                            break
                                    return valid
                                if op==1:
                                    # 1. View Show List
                                    Hall_Name[sl].view_show_list()
                                elif op==2:
                                    def book_movie():
                                        Hall_Name[sl].view_show_list()
                                        show_id=input('Please Enter Show ID: ')
                                        if check_show_id(show_id)==False:
                                            print('\nWrong Show ID !\nPlease Enter Correct Show ID.')
                                            book_movie()
                                        else:
                                            # 2. Book Seat
                                            seat_qnt=int(input('Please Enter How Many Seats You Want: '))
                                            print(f'To Book {seat_qnt} Seat/Seats Please Enter Row & Column For Every Seat.')
                                            i=1
                                            selected_seat=[]
                                            while i<=seat_qnt:
                                                def Is_valid():
                                                    global s_row
                                                    global s_col
                                                    s_row=int(input(f'Enter Row For Seat {i}: '))
                                                    s_col=int(input(f'Enter Col For Seat {i}: '))
                                                    if s_row>=Star_Cinema._hall_list[sl][0] or s_col>=Star_Cinema._hall_list[sl][1]:
                                                        print('\nInvalid Seat !\nPlease Enter A Valid Seat Info.\n')
                                                        print(f'Valid Row: {0}-{Star_Cinema._hall_list[sl][0]-1}')
                                                        print(f'Valid Col: {0}-{Star_Cinema._hall_list[sl][1]-1}\n')
                                                        Is_valid()
                                                    elif Hall_Name[sl].seats[show_id][s_row][s_col]=='1':
                                                        print(f'\nSeat - ({s_row},{s_col}) Is Already Booked !\nPlease Select A Empty One.\n')
                                                        Hall_Name[sl].view_available_seats(show_id)
                                                        Is_valid()
                                                    else:
                                                        selected_seat.append((s_row,s_col))
                                                        return

                                                Is_valid()
                                                i+=1
                                            print(f'\n{seat_qnt} Seat/Seats Booked Successfully.\nHere The Seat/Seats: ')
                                            for p,pos in enumerate(selected_seat):
                                                Hall_Name[sl].book_seats(show_id,pos)
                                                print(f'Seat {p+1} - {pos}')
                                            
                                    book_movie()
                                else:
                                    # 3. View Available Seats
                                    def view_seats():   
                                        Hall_Name[sl].view_show_list()
                                        show_id=input('Please Enter Show ID: ')
                                        print('\n')
                                        Is_present=check_show_id(show_id)
                                        if Is_present==True:
                                            Hall_Name[sl].view_available_seats(show_id)
                                        else:
                                            print('Wrong Show ID !\nPlease Enter Correct Show ID.')
                                            view_seats()
                                    view_seats()
                                main_menu()
                            elif op==4:
                                # 4. Home
                                hall_func()
                            else:
                                print('\nPlease Select An Valid Option !')
                                main_menu()
                    main_menu()
                    break
    hall_func()
    run_p=False
#end


#Project Name: A ticket booking system of a Cinema Hall
#Purpose: Mid Exam- Python (Phitron-SDT)

#Owner: Pritom Das 
#Batch: 4
#Email: pritom.gps@gmail.com
#Finished Date: 28/10/2024

#Note: First time I made a project like this. I enjoyed so much & will add additional functionalities in future. Thanks Phitron. Happy Coding!
