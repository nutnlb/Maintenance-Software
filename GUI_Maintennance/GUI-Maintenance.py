from tkinter import * # import * คือดึง function ทั้งหมดใน libralies
from tkinter import messagebox # function นี้แยกออกจาก tkinterปกติ เพื่อแจ้ง pop-up
#from songline import Sendline
import csv
from datetime import datetime
from tkinter import ttk # theme

#token = 'sWZfZ6BzXaJ1KqwLAxKPgCPLKd8GEOy8AT3tk7yDl0X'
#messenger = Sendline(token)

#database
from db_maintenance import *



'''def writecsv(record_list):
    with open('data.CSV','a',newline='',encoding ='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)
'''
GUI = Tk()
GUI.title('Maintenance program by Nut')
GUI.geometry('850x450+50+50')#+50+50 คือระยะจากขอบซ้ายกับขอบบน
#if need to comment code multi line >>> ''' dsdsdsds '''
#*********FONT********
FONT1 = ('Angsana New', 20) # font type and font size
FONT2 = ('Angsana New', 15) 
######## TAB #############
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1, text='ใบแจ้งซ่อม')
Tab.add(T2, text='ดูใบแจ้งซ่อม')
Tab.add(T3, text='สรุป')
Tab.pack(fill=BOTH, expand=1)
##########################
L = Label(T1, text='ใบแจ้งซ่อม', font=FONT1) #นำ label ไปใส่ใน gui แค่ assign in backside
L.place(x=80,y=10) # เอาจาก backside ขึ้น show แต่จะอยู๋ center เสมอ

L = Label(T1, text='ชื่อผู้แจ้ง', font=FONT2)
L.place(x=30,y=50)
v_name = StringVar()#ตัวแปรพิเศษใช้กับ GUI 
E1 = ttk.Entry(T1, textvariable=v_name ,font=FONT2) # จะเอค่าที่กรอกไปไว้ใน V_name
E1.place(x=150,y=50)
#########
L = Label(T1, text='แผนก', font=FONT2)
L.place(x=30,y=100)
v_department = StringVar()
E2 = ttk.Entry(T1,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#########
L = Label(T1, text='เครื่อง', font=FONT2)
L.place(x=30,y=150)
v_machine = StringVar()
E3 = ttk.Entry(T1,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#########
L = Label(T1, text='อาการเสีย', font=FONT2)
L.place(x=30,y=200)
v_problem = StringVar()
E4 = ttk.Entry(T1,textvariable=v_problem,font=FONT2)
E4.place(x=150,y=200)
#########
L = Label(T1, text='หมายเลข', font=FONT2)
L.place(x=30,y=250)
v_number = StringVar()
E5 = ttk.Entry(T1,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#########
L = Label(T1, text='โทร', font=FONT2)
L.place(x=30,y=300)
v_tel = StringVar()
E6 = ttk.Entry(T1,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)


####Button#####
def save():
    name = v_name.get() #คือการดึงค่าจาก StringVar()
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = 'ชื่อผู้แจ้ง:' + name + '\n'
    text = text + 'แผนก:' + department + '\n'
    text = text + 'เครื่อง:' + machine + '\n'
    text = text + 'อาการเสีย:' + problem + '\n'
    text = text + 'หมายเลข:' + number + '\n'
    text = text + 'โทร:' + tel + '\n'
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #generate tsid (transaction)
    tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S')) + 114152147165)
    insert_mtworkorder(tsid,name,department,machine,problem,number,tel)
    v_name.set('')
    v_department.set('')
    v_machine.set('')
    v_problem.set('')
    v_number.set('')
    v_tel.set('')
    update_table()
    
    #datalist = [dt,name,department,machine,problem,number,tel]
    # writecsv(datalist)
    # messenger.sendtext(text)
    #messagebox.showinfo('กำลังบันทึกข้อมูล...',text)
    
B = ttk.Button(T1, text= 'บันทึกใบแจ้งซ่อม', command = save )
B.place(x=200,y=350)

'''L.place(x=20, y=140)# similar pack but it can fix position from pixel
L.grid(row=0,column=0) # position similar excel table

L = Label(GUI, text = ' By NUT')
L.grid(row=0,column=1)
'''
############# TAB2 ###########################
header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทรผู้แจ้ง']
headerw = [100,100,100,150,200,100,100]
mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=10)
mtworkorderlist.pack()
for h,W in zip(header,headerw):
    # h= 'TSID', w= 50 ----> h= 'ชื่อ' w=100
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=W)

mtworkorderlist.column('TSID',anchor='w')

def update_table():
    #clear old data
    mtworkorderlist.delete(*mtworkorderlist.get_children())
    data = view_mmtworkorder()
    for d in data:
        d = list(d) #แปลง tuple to list
        del d[0] #ลบ index 0
        mtworkorderlist.insert('','end',values=d) # ('','end', > is feature threeview of tkinter 

####Start#####
update_table()


GUI.mainloop()
