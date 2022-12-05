from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("billing software")
        bg_color="#074463"
        title=Label(self.root,text="Billing software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #-----variable-----#
        #------item-------#
        self.chilly=IntVar()
        self.curry=IntVar()
        self.dragon=IntVar()
        self.hydrabd=IntVar()
        self.btrmasla=IntVar()
        self.mughlai=IntVar()
        self.kassa=IntVar()
        #-------item1-----#
        self.vchowmin=IntVar()
        self.pchowmin=IntVar()
        self.vroll=IntVar()
        self.proll=IntVar()
        self.troti=IntVar()
        self.btrnan=IntVar()
        self.garnan=IntVar()
        #------item2------#
        self.tumbsup=IntVar()
        self.icrm=IntVar()
        self.sprite=IntVar()
        self.cocal=IntVar()
        self.vgmojito=IntVar()
        self.mstumbsup=IntVar()
        self.mazza=IntVar()
        #-------total price------#
        self.item_price=StringVar()
        self.item1_price=StringVar()
        self.item2_price=StringVar()
        #--------tax----------#
        self.item_tax=StringVar()
        self.item1_tax=StringVar()
        self.item2_tax=StringVar()
        #-------customer-------#
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        F1=LabelFrame(self.root,bd=10,text="customer details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer name",bg=bg_color,fg="white",font=("times new roman",15,"bold"),pady=2).grid(row=0,column=0,padx=20,pady=5)
        cname_lbl=Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphon_lbl=Label(F1,text="Phone No",bg=bg_color,fg="white",font=("times new roman",15,"bold"),pady=2).grid(row=0,column=2,padx=20,pady=5)
        cphon_lbl=Entry(F1,width=20,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        

        cbill_lbl=Label(F1,text="Bill No",bg=bg_color,fg="white",font=("times new roman",15,"bold"),pady=2).grid(row=0,column=4,padx=20,pady=5)
        cbill_lbl=Entry(F1,width=20,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(F1,text="search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6)
        
        
        #=========items===========
         
        F2=LabelFrame(self.root,bd=10,text="Items",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=325,height=380)
        
        chl_ckn_lbl=Label(F2,text="Chilly Chicken /90",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,sticky="w")
        chl_ckn_txt=Entry(F2,width=8,textvariable=self.chilly,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        ckn_cur_lbl=Label(F2,text="Chicken Curry /90",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,sticky="w")
        ckn_cur_txt=Entry(F2,width=8,textvariable=self.curry,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        ckn_drg_lbl=Label(F2,text="Chicken dragon /90",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,sticky="w")
        ckn_drg_txt=Entry(F2,width=8,textvariable=self.dragon,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        ckn_hyd_lbl=Label(F2,text="Chicken Hydrabadi /90",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,sticky="w")
        ckn_hyd_txt=Entry(F2,width=8,textvariable=self.hydrabd,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        ckn_btr_lbl=Label(F2,text="Chicken btr masala /90",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,sticky="w")
        ckn_btr_txt=Entry(F2,width=8,textvariable=self.btrmasla,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        ckn_mgh_lbl=Label(F2,text="Chicken mughlai /90",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,sticky="w")
        ckn_mgh_txt=Entry(F2,width=8,textvariable=self.mughlai,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        ckn_kas_lbl=Label(F2,text="Chicken kassa /90",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=6,column=0,padx=10,sticky="w")
        ckn_kas_txt=Entry(F2,width=8,textvariable=self.kassa,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
        
        
       
        
        
        F3=LabelFrame(self.root,bd=10,text="Items1",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=170,width=325,height=380)
        
        veg_chaw_lbl=Label(F3,text="Veg chowmin /50",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,sticky="w")
        veg_chaw_txt=Entry(F3,width=8,textvariable=self.vchowmin,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        pan_chaw_lbl=Label(F3,text="Paneer Chowmin /60",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,sticky="w")
        pan_chaw_txt=Entry(F3,width=8,textvariable=self.pchowmin,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        veg_roll_lbl=Label(F3,text="Veg Roll /50",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,sticky="w")
        veg_roll_txt=Entry(F3,width=8,textvariable=self.vroll,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        pan_roll_lbl=Label(F3,text="Paneer Roll /60",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,sticky="w")
        pan_roll_txt=Entry(F3,width=8,textvariable=self.proll,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        taw_roti_lbl=Label(F3,text="Tawa Roti /5",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,sticky="w")
        taw_roti_txt=Entry(F3,width=8,textvariable=self.troti,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        btr_naan_lbl=Label(F3,text="Butter naan /20",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,sticky="w")
        btr_naan_txt=Entry(F3,width=8,textvariable=self.btrnan,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        gar_naan_lbl=Label(F3,text="Garlic Naan /20",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=6,column=0,padx=10,sticky="w")
        gar_naan_txt=Entry(F3,width=8,textvariable=self.garnan,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
        
        
        
        
        F4=LabelFrame(self.root,bd=10,text="items2",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=675,y=170,width=325,height=380)
        
        
        tumbsup_lbl=Label(F4,text="Thumbsup /30",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,sticky="w")
        tumbsup_txt=Entry(F4,width=8,textvariable=self.tumbsup,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        ice_cream_lbl=Label(F4,text="ice cream /60",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,sticky="w")
        ice_cream_txt=Entry(F4,width=8,textvariable=self.icrm,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        sprite_lbl=Label(F4,text="sprite /30",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,sticky="w")
        sprite_txt=Entry(F4,width=8,textvariable=self.sprite,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        coca_cola_lbl=Label(F4,text="coca cola /30",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,sticky="w")
        coca_cola_txt=Entry(F4,width=8,textvariable=self.cocal,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        vergin_mojito_lbl=Label(F4,text="virgin mojito /50",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,sticky="w")
        vergin_mojito_txt=Entry(F4,width=8,textvariable=self.vgmojito,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        masala_tumbsup_lbl=Label(F4,text="masala tumbsup /20",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,sticky="w")
        masala_tumbsup_txt=Entry(F4,width=8,textvariable=self.mstumbsup,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        mazza_lbl=Label(F4,text="mazza /20",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=6,column=0,padx=10,sticky="w")
        mazza_txt=Entry(F4,width=8,textvariable=self.mazza,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
        
        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=170,width=325,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack()
        
        
        
        F6=LabelFrame(self.root,bd=10,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=135)
        
        m1_lbl=Label(F6,text="item price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.item_price,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(F6,text="item1 price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.item1_price,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
       
        m3_lbl=Label(F6,text="item2 price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.item2_price,bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        c1_lbl=Label(F6,text="item tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.item_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(F6,text="item1 tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.item1_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
       
        c2_lbl=Label(F6,text="item2 tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=15,font="arial 10 bold",textvariable=self.item2_tax,bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)
        
        total_btn=Button(btn_f,command=self.total,text="total",font="arial 10 bold",bg="cadet blue",fg="white",pady=15,width=15).grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,text="Gbill",command=self.bill_area,font="arial 10 bold",bg="cadet blue",fg="white",pady=15,width=15).grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="clear",font="arial 10 bold",bg="cadet blue",fg="white",pady=15,width=15).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="exit",font="arial 10 bold",bg="cadet blue",fg="white",pady=15,width=15).grid(row=0,column=3,padx=5,pady=5)
        self.wellcome_bill()
        
    def total(self):
      
      self.ch_ck=self.chilly.get()*90
      self.ch_cu=self.curry.get()*90
      self.ch_drg=self.dragon.get()*90
      self.ch_hd=self.hydrabd.get()*90
      self.ch_btrms=self.btrmasla.get()*90
      self.ch_mgh=self.mughlai.get()*90
      self.ch_kas=self.kassa.get()*90
      
      self.total_item_price=float(
                                self.ch_ck+
                                self.ch_cu+
                                self.ch_drg+
                                self.ch_hd+
                                self.ch_btrms+
                                self.ch_mgh+
                                self.ch_kas
     )
      
      self.item_price.set("Rs "+ str(self.total_item_price))
      self.item_tax.set("Rs "+str(self.total_item_price*0.025))
      
      self.v_ch=self.vchowmin.get()*50
      self.p_ch=self.pchowmin.get()*60
      self.v_rl=self.vroll.get()*50
      self.p_rl=self.proll.get()*60
      self.t_rt=self.troti.get()*5
      self.bt_n=self.btrnan.get()*20
      self.gr_nn=self.garnan.get()*20
      
      self.total_item1_price=float( 
                                   self.v_ch+
                                   self.p_ch+
                                   self.v_rl+
                                   self.p_rl+
                                   self.t_rt+
                                   self.bt_n+
                                   self.gr_nn                   
      )
      self.item1_price.set("Rs "+ str(self.total_item1_price))
      self.item1_tax.set("Rs "+str(self.total_item1_price*0.025))
      
      
      self.th_up=self.tumbsup.get()*30
      self.ic_rm=self.icrm.get()*60
      self.sp_it=self.sprite.get()*30
      self.co_co=self.cocal.get()*30
      self.vg_mg=self.vgmojito.get()*50
      self.ms_tm=self.mstumbsup.get()*20
      self.mz_mz=self.mazza.get()*20
      
      self.total_item2_price=float(
                                 self.th_up+
                                 self.ic_rm+
                                 self.sp_it+
                                 self.co_co+
                                 self.vg_mg+
                                 self.ms_tm+
                                 self.mz_mz
      )
      
      self.item2_price.set("Rs "+ str(self.total_item2_price))
      self.item2_tax.set("Rs "+str(self.total_item2_price*0.025))
      
      self.Total_bill=float(
                          self.total_item_price+
                          self.total_item1_price+
                          self.total_item2_price
                              )
      
    def wellcome_bill(self):
      self.txtarea.delete("1.0",END)
      self.txtarea.insert(END,"\tWelcome to ABC hotel")
      self.txtarea.insert(END,f"\nBill no :{(self.bill_no.get())} ")
      self.txtarea.insert(END,f"\nCustomer Name :{(self.c_name.get())}")
      self.txtarea.insert(END,f"\nPhone No :{(self.c_phon.get())}")
      self.txtarea.insert(END,f"\n=================================== ") 
      self.txtarea.insert(END,f"\nItems\t\tQTY\t Price")
      self.txtarea.insert(END,f"\n=================================== ")
    def bill_area(self):
      self.wellcome_bill()
      #------items-------#
      if self.chilly.get()!=0:
        self.txtarea.insert(END,f"\nchilly chicken\t\t{self.chilly.get()}\t\t{self.ch_ck}")
      if self.curry.get()!=0:
         self.txtarea.insert(END,f"\nchicken curry\t\t{self.curry.get()}\t\t{self.ch_cu}") 
      if self.dragon.get()!=0:
        self.txtarea.insert(END,f"\ndragon chicken\t\t{self.dragon.get()}\t\t{self.ch_drg}")
      if self.hydrabd.get()!=0:
        self.txtarea.insert(END,f"\nchicken hydrabadi\t\t{self.hydrabd.get()}\t\t{self.ch_hd}")
      if self.btrmasla.get()!=0:
        self.txtarea.insert(END,f"\nchicken btrmasala\t\t{self.btrmasla.get()}\t\t{self.ch_btrms}")
      if self.mughlai.get()!=0:
        self.txtarea.insert(END,f"\nchiken mughlai\t\t{self.mughlai.get()}\t\t{self.ch_mgh}")
      if self.kassa.get()!=0:
        self.txtarea.insert(END,f"\nchicken kassa\t\t{self.kassa.get()}\t\t{self.ch_kas}")  
      #-------items1--------#
      if self.vchowmin.get()!=0:
        self.txtarea.insert(END,f"\nveg chowmin\t\t{self.vchowmin.get()}\t\t{self.v_ch}")
      if self.pchowmin.get()!=0:
         self.txtarea.insert(END,f"\npaneer chowmin\t\t{self.pchowmin.get()}\t\t{self.p_ch}") 
      if self.vroll.get()!=0:
        self.txtarea.insert(END,f"\nveg roll\t\t{self.vroll.get()}\t\t{self.v_rl}")
      if self.proll.get()!=0:
        self.txtarea.insert(END,f"\npaneer roll\t\t{self.proll.get()}\t\t{self.p_rl}")
      if self.troti.get()!=0:
        self.txtarea.insert(END,f"\ntawa roti\t\t{self.troti.get()}\t\t{self.t_rt}")
      if self.btrnan.get()!=0:
        self.txtarea.insert(END,f"\nbutter naan\t\t{self.btrnan.get()}\t\t{self.bt_n}")
      if self.garnan.get()!=0:
        self.txtarea.insert(END,f"\ngarlic naan\t\t{self.garnan.get()}\t\t{self.gr_nn}")  
      #---------items2--------#
      if self.tumbsup.get()!=0:
        self.txtarea.insert(END,f"\nthumbsup\t\t{self.tumbsup.get()}\t\t{self.th_up}")
      if self.icrm.get()!=0:
         self.txtarea.insert(END,f"\nice cream\t\t{self.icrm.get()}\t\t{self.ic_rm}") 
      if self.sprite.get()!=0:
        self.txtarea.insert(END,f"\nsprite\t\t{self.sprite.get()}\t\t{self.sp_it}")
      if self.cocal.get()!=0:
        self.txtarea.insert(END,f"\ncoca cola\t\t{self.cocal.get()}\t\t{self.co_co}")
      if self.vgmojito.get()!=0:
        self.txtarea.insert(END,f"\nvirgin mojito\t\t{self.vgmojito.get()}\t\t{self.vg_mg}")
      if self.mstumbsup.get()!=0:
        self.txtarea.insert(END,f"\nmasala thumbsup\t\t{self.mstumbsup.get()}\t\t{self.ms_tm}")
      if self.mazza.get()!=0:
        self.txtarea.insert(END,f"\nmazza\t\t{self.mazza.get()}\t\t{self.mz_mz}")  
      
      self.txtarea.insert(END,f"\n=================================== ")
      self.txtarea.insert(END,f"\nTotal Bill :\t\t\tRs.  {self.Total_bill}") 
      self.txtarea.insert(END,f"\n=================================== ")
      self.save_bill()
    def save_bill(self):
      op=messagebox.askyesno("save bill","do yo want to save the bill")
      if op>0:
        self.bill_data=self.txtarea.get("1.0",END)
        f1=open("bills/"+str(self.bill_no.get()))+".txt","w"
        f1.write(self.bill_data)
        f1.close()
        messagebox.showinfo("saved",f"bill no.:{self.bill_no.get()} saved successfully")
      else:
        return      
      
      
      
root=Tk()
obj=Bill_App(root)
root.mainloop()