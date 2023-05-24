from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import mysql.connector


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1910x1100+0+0")

        # ==============addMed Variable===========

        self.ref_var = StringVar()
        self.cmpName_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.Price_var = StringVar()
        self.ProductQt_var = StringVar()

        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg='darkgreen', fg="white",
                         font=("times new roman", 50, "bold"), padx=3, pady=2)
        lbltitle.pack(side=TOP, fill=X)

        img1 = Image.open(
            "F:/Study/Tslas-DESKTOP-G14D31O/Year 3/Semester 4/DBMS/Pharmacy_Management_system/Pharmacy Managemnt System Project/p_m_s/Pics/GANESH Company.png")
        img1 = img1.resize((110, 80), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=200, y=15)

        # ==============DataFrame==================

        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=10, y=120, width=1900, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine information", fg="darkgreen",
                                   font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=1300, height=350)

        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=10, y=520, width=1900, height=65)

        btnAddData = Button(ButtonFrame, text="ADD MEDICINE", command=self.add_var, font=("arial", 12, "bold"),
                            width=17, bg="darkgreen",
                            fg="white")
        btnAddData.grid(row=0, column=0)

        btnUpdateMed = Button(ButtonFrame, text="UPDATE", command=self.Update, font=("arial", 13, "bold"), width=17,
                              bg="darkgreen",
                              fg="white")
        btnUpdateMed.grid(row=0, column=1)

        btnDeleteMed = Button(ButtonFrame, text="DELETE", command=self.Delete, font=("arial", 13, "bold"), width=17,
                              bg="red", fg="white")
        btnDeleteMed.grid(row=0, column=2)

        btnRestMed = Button(ButtonFrame, text="RESET", command=self.reset, font=("arial", 13, "bold"), width=17,
                            bg="darkgreen", fg="white")
        btnRestMed.grid(row=0, column=3)

        btnExitMed = Button(ButtonFrame, text="EXIT", font=("arial", 12, "bold"), width=17, bg="darkgreen", fg="white")
        btnExitMed.grid(row=0, column=4)

        # ============SEARCH BY============
        lblSearch = Label(ButtonFrame, text="SEARCH BY", font=("arial", 17, "bold"), padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        self.search_Var = StringVar()
        search_combo = ttk.Combobox(ButtonFrame, width=16, textvariable=self.search_Var, font=("arial", 17, "bold"),
                                    state="readonly",
                                    foreground="red")
        search_combo['values'] = ("Ref_no", "Medname", "LotNo")
        search_combo.grid(row=0, column=6)
        search_combo.current(0)

        self.searchTxt_var = StringVar()
        txtSearch = Entry(ButtonFrame, bd=3, relief=RIDGE, textvariable=self.searchTxt_var, width=16,
                          font=("arial", 17, "bold"))
        txtSearch.grid(row=0, column=7)

        searchbtn = Button(ButtonFrame, text="SEARCH", command=self.Search, font=("arial", 12, "bold"), width=16,
                           bg="darkgreen", fg="white")
        searchbtn.grid(row=0, column=8)

        showAll = Button(ButtonFrame, command=self.fetch_data, text="SHOW ALL", font=("arial", 13, "bold"), width=16,
                         bg="darkgreen", fg="white")
        showAll.grid(row=0, column=9)

        # =========================Label and entry============================
        lblrefno = Label(DataFrameLeft, padx=2, text="Reference No",
                         font=("arial", 12, "bold"))
        lblrefno.grid(row=0, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                       database="p_m_s")

        my_cursor = conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row = my_cursor.fetchall()

        search_combo = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 12, "bold"), textvariable=self.ref_var,
                                    state="readonly")
        search_combo['values'] = row
        search_combo.grid(row=0, column=1, sticky=W)
        search_combo.current(0)

        # =========================CompanyName============================

        lblCompanyName = Label(DataFrameLeft, text="Company Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblCompanyName.grid(row=1, column=0, sticky=W)
        txtSearch = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.cmpName_var, relief=RIDGE, width=29,
                          font=("arial", 12, "bold"))
        txtSearch.grid(row=1, column=1)

        # ==========================AddMedicine============================

        lblMedType = Label(DataFrameLeft, text="Medicine Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMedType.grid(row=2, column=0, sticky=W)

        comTypeofMedicine = ttk.Combobox(DataFrameLeft, width=27, textvariable=self.typeMed_var,
                                         font=("arial", 12, "bold"), state="readonly")
        comTypeofMedicine['values'] = (
            " Tablet", "Liquid", "Capsules", "Topical Medicines", "Drops", "Inhales", "Injection")
        comTypeofMedicine.grid(row=2, column=1)
        comTypeofMedicine.current(0)

        lblMedName = Label(DataFrameLeft, text="Medicine Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMedName.grid(row=3, column=0, sticky=W)
        conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                       database="p_m_s")

        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med = my_cursor.fetchall()

        comMedicineName = ttk.Combobox(DataFrameLeft, width=27, textvariable=self.medName_var,
                                       font=("arial", 12, "bold"), state="readonly")
        comMedicineName['values'] = med
        comMedicineName.grid(row=3, column=1)
        comMedicineName.current(0)

        lblLotNo = Label(DataFrameLeft, text="Lot No:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtSearchLot = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.lot_var, relief=RIDGE, width=29,
                             font=("arial", 13, "bold"))
        txtSearchLot.grid(row=4, column=1)

        lblIssue = Label(DataFrameLeft, text="Issue Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIssue.grid(row=5, column=0, sticky=W)
        txtSearchIssue = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.issuedate_var, relief=RIDGE, width=29,
                               font=("arial", 13, "bold"))
        txtSearchIssue.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, text="Expiry Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtSearchExpiry = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.expdate_var, relief=RIDGE, width=29,
                                font=("arial", 13, "bold"))
        txtSearchExpiry.grid(row=6, column=1)

        lblUses = Label(DataFrameLeft, text="Uses:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblUses.grid(row=7, column=0, sticky=W)
        txtSearchUses = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.uses_var, relief=RIDGE, width=29,
                              font=("arial", 13, "bold"))
        txtSearchUses.grid(row=7, column=1)

        lblSideEffects = Label(DataFrameLeft, text="Side Effects:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSideEffects.grid(row=8, column=0, sticky=W)
        txtSearchSideEffects = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.sideeffect_var, relief=RIDGE,
                                     width=29,
                                     font=("arial", 13, "bold"))
        txtSearchSideEffects.grid(row=8, column=1)

        lblPreWarning = Label(DataFrameLeft, text="Prec&Warning:", font=("arial", 12, "bold"), padx=15)
        lblPreWarning.grid(row=0, column=2, sticky=W)
        txtSearchPreWarninglblPreWarning = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.warning_var,
                                                 relief=RIDGE, width=29,
                                                 font=("arial", 13, "bold"))
        txtSearchPreWarninglblPreWarning.grid(row=0, column=3)

        lblDosage = Label(DataFrameLeft, text="Dosage:", font=("arial", 12, "bold"), padx=15)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtSearchDosage = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.dosage_var, relief=RIDGE, width=29,
                                font=("arial", 13, "bold"))
        txtSearchDosage.grid(row=1, column=3)

        lblTabletPrice = Label(DataFrameLeft, text="Tablet Price:", font=("arial", 12, "bold"), padx=30)
        lblTabletPrice.grid(row=0, column=4, sticky=W)
        txtSearchTabletPrice = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.Price_var, relief=RIDGE,
                                     width=29,
                                     font=("arial", 13, "bold"))
        txtSearchTabletPrice.grid(row=0, column=5)

        lblProduct_Qt = Label(DataFrameLeft, text="Product Qt.:", font=("arial", 12, "bold"), padx=30)
        lblProduct_Qt.grid(row=1, column=4, sticky=W)
        txtSearchProduct_Qt = Entry(DataFrameLeft, bd=2, bg="white", textvariable=self.ProductQt_var, relief=RIDGE,
                                    width=29, font=("arial", 13, "bold"))
        txtSearchProduct_Qt.grid(row=1, column=5)

        # ====================Adding Images=====================

        lblquote = Label(DataFrameLeft, text="Pharmacy: science + compassion = better health",
                         font=("arial", 18, "bold"), padx=15, bg="red", fg="white")
        lblquote.place(x=485, y=60)

        img2 = Image.open(
            "F:/Study/Tslas-DESKTOP-G14D31O/Year 3/Semester 4/DBMS/Pharmacy_Management_system/Pharmacy Managemnt System Project/p_m_s/Pics/pharmacy-3087599_1920.jpg")
        img2 = img2.resize((250, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image=self.photoimg2, borderwidth=0)
        b1.place(x=485, y=260)

        img3 = Image.open(
            "F:/Study/Tslas-DESKTOP-G14D31O/Year 3/Semester 4/DBMS/Pharmacy_Management_system/Pharmacy Managemnt System Project/p_m_s/Pics/scientist-2141259_1920.jpg")
        img3 = img3.resize((300, 200), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.photoimg3, borderwidth=0)
        b1.place(x=735, y=260)

        img4 = Image.open(
            "F:/Study/Tslas-DESKTOP-G14D31O/Year 3/Semester 4/DBMS/Pharmacy_Management_system/Pharmacy Managemnt System Project/p_m_s/Pics/thermometer-1539191_1920.jpg")
        img4 = img4.resize((290, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image=self.photoimg4, borderwidth=0)
        b1.place(x=1025, y=260)

        # ====================dataframeRight ===================

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department",
                                    fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameRight.place(x=1330, y=5, width=500, height=350)

        img5 = Image.open(
            "F:/Study/Tslas-DESKTOP-G14D31O/Year 3/Semester 4/DBMS/Pharmacy_Management_system/Pharmacy Managemnt System Project/p_m_s/Pics/syringe-417786_1920.jpg")
        img5 = img5.resize((300, 115), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image=self.photoimg5, borderwidth=0)
        b1.place(x=1390, y=160)

        img6 = Image.open(
            "F:/Study/Tslas-DESKTOP-G14D31O/Year 3/Semester 4/DBMS/Pharmacy_Management_system/Pharmacy Managemnt System Project/p_m_s/Pics/herbs-906140_1920.jpg")
        img6 = img6.resize((170, 180), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root, image=self.photoimg6, borderwidth=0)
        b1.place(x=1690, y=160)

        lblrefno = Label(DataFrameRight, text="Reference No:", font=("arial", 12, "bold"))
        lblrefno.place(x=-15, y=125)

        self.ref_add_var = StringVar()

        self.txtSearchrefno = Entry(DataFrameRight, textvariable=self.ref_add_var, bd=2, bg="white", relief=RIDGE,
                                    width=19, font=("arial", 13, "bold"))
        self.txtSearchrefno.place(x=105, y=125)

        lblmedname = Label(DataFrameRight, text="Med Name:", font=("arial", 12, "bold"))
        lblmedname.place(x=-15, y=155)

        self.medicine_add_var = StringVar()

        self.txtSearchmedname = Entry(DataFrameRight, textvariable=self.medicine_add_var, bd=2, bg="white",
                                      relief=RIDGE, width=19, font=("arial", 13, "bold"))
        self.txtSearchmedname.place(x=105, y=155)

        # ======================side Frame=====================
        side_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=-10, y=185, width=290, height=130)

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)

        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(side_frame, columns=("ref", "medname"), xscrollcommand=sc_x.set,
                                           yscrollcommand=sc_y.set)  # Treeview helps to present hierarchical structure so that user can use mmouse to hide or reveal any part needed.

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease>", self.Medget_cursor)

        # ====================Medicine Add Buttons==================

        Rightside_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="darkgreen")
        Rightside_frame.place(x=300, y=180, width=143, height=135)

        btnAddMed = Button(Rightside_frame, text="ADD", command=self.add_medicine, font=("arial", 11, "bold"), width=14,
                           bg="lightblue", fg="white")
        btnAddMed.grid(row=0, column=0)

        btnUpdate = Button(Rightside_frame, text="UPDATE", font=("arial", 11, "bold"), width=14, bg="lightblue",
                           fg="white", command=self.UpdateMed)
        btnUpdate.grid(row=1, column=0)

        btnDelete = Button(Rightside_frame, text="DELETE", font=("arial", 11, "bold"), width=14, bg="lightblue",
                           fg="white", command=self.DeleteMed)
        btnDelete.grid(row=2, column=0)

        btnClear = Button(Rightside_frame, text="CLEAR", font=("arial", 11, "bold"), width=14, bg="lightblue",
                          fg="white", command=self.ClearMed)
        btnClear.grid(row=3, column=0)

        # ======================Frame Details==========================

        Framedetails = Frame(self.root, bd=15, relief=RIDGE)
        Framedetails.place(x=10, y=585, width=1900, height=410)

        # ======================Main Table & scrollbar=================

        main_Frame = Frame(Framedetails, bd=15, relief=RIDGE, padx=20)
        main_Frame.place(x=0, y=1, width=1875, height=380)

        scroll_x = ttk.Scrollbar(main_Frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y = ttk.Scrollbar(main_Frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table = ttk.Treeview(main_Frame, columns=(
            "ref", "company_name", "type", "tabletname", "lotno", "issuedate", "expdate", "uses", "sideffects", "warning",
            "dosage", "price", "productqty"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("ref", text="Reference No")
        self.pharmacy_table.heading("company_name", text="Company Name")
        self.pharmacy_table.heading("type", text="Medicine Type")
        self.pharmacy_table.heading("tabletname", text="Tablet Name")
        self.pharmacy_table.heading("lotno", text="Lot No")
        self.pharmacy_table.heading("issuedate", text="Issue Date")
        self.pharmacy_table.heading("expdate", text="Exp Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideffects", text="Side Effects")
        self.pharmacy_table.heading("warning", text="Prec&Warning")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("productqty", text="Product Qty")
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.pharmacy_table.column("ref", width=100)
        self.pharmacy_table.column("company_name", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("tabletname", width=100)
        self.pharmacy_table.column("lotno", width=100)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideffects", width=100)
        self.pharmacy_table.column("warning", width=100)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("productqty", width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease>", self.get_cursor)

        # ======================Add Medicine Functionality Declaration=====================

    def add_medicine(self):
        User = self.ref_add_var.get()
        pas = self.medicine_add_var.get()
        if (User == '') or (pas == ''):
            messagebox.showinfo("Error", "You have entered nothing")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                           database="p_m_s")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)", (User, pas))
            conn.commit()
            messagebox.showinfo("Success", "Medicine Added!!")
            self.fetch_dataMed()
            self.Medget_cursor()
            conn.close()

    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                       database="p_m_s")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from pharma')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def Medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.ref_add_var.set(row[0])
        self.medicine_add_var.set(row[1])

    def UpdateMed(self):
        if self.ref_add_var.get() == "" or self.medicine_add_var.get() == "":
            messagebox.showerror("Warning", "All fields are Required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                           database="p_m_s")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",
                              (self.medicine_add_var.get(), self.ref_add_var.get(),))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success", "Medicine has been updated")

    def DeleteMed(self):
        mDelete = messagebox.askyesno("Pharmacy Management System", "Do you delete this Medicine")
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                           database="p_m_s")
            my_cursor = conn.cursor()
            my_cursor.execute("delete from pharma where Ref=%s", (self.ref_add_var.get(),))
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_dataMed()
        conn.close()

    def ClearMed(self):
        self.ref_add_var.set("")
        self.medicine_add_var.set("")

    # ===============================Main Table=====================
    def add_var(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                           database="p_m_s")
            my_cursor = conn.cursor()
            my_cursor.execute("select ref_no from pharmacy;")
            row = list(my_cursor.fetchall())
            print(row)
            I: int = 0
            for i in row:
                if self.ref_var.get() == i:
                    messagebox.showinfo("Failure", "Data-Duplicacy")
                    break
                else:
                    I: int = I + 1
                    n = len(row)
                    if n != I:
                        continue
                    else:
                        my_cursor.execute(
                            "insert into pharmacy(ref_no, company_name, medType, medname, lot_no, issuedate, expdate, uses, sideeffect, warning, dosage, product_price, Med_qty) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (
                                self.ref_var.get(), self.cmpName_var.get(), self.typeMed_var.get(),
                                self.medName_var.get(),
                                self.lot_var.get(), self.issuedate_var.get(),
                                self.expdate_var.get(), self.uses_var.get(), self.sideeffect_var.get(),
                                self.warning_var.get(),
                                self.dosage_var.get(),
                                self.Price_var.get(), self.ProductQt_var.get()
                            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "data has been inserted")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                        database="p_m_s")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from pharmacy')
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, ev=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]

        self.ref_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])
        self.issuedate_var.set(row[5])
        self.expdate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideeffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.Price_var.set(row[11])
        self.ProductQt_var.set(row[12])

    def Update(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All fields are Required/ ")
        else:
            conn  = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                         database="p_m_s")
            my_cursor = conn.cursor()
            my_cursor .execute(
                "update pharmacy set company_name=%s, medType=%s, medname=%s, lot_no=%s, issuedate=%s, expdate=%s, uses=%s, sideeffect=%s, warning=%s, dosage=%s, product_price=%s, Med_qty=%s where Ref_no= %s",
                (self.cmpName_var.get(), self.typeMed_var.get(), self.medName_var.get(),
                 self.lot_var.get(), self.issuedate_var.get(),
                 self.expdate_var.get(), self.uses_var.get(), self.sideeffect_var.get(), self.warning_var.get(),
                 self.dosage_var.get(),
                 self.Price_var.get(), self.ProductQt_var.get(), self.ref_var.get()))
            conn.commit()
        self.fetch_data ()
        conn.close()
        messagebox.showinfo("UPDATED", "Record has been updated successfully")

    def Delete(self):
        mDelete = messagebox.askyesno("Pharmacy Management System", "Do you delete this Medicine")
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                           database="p_m_s")
            my_cursor = conn.cursor()
            my_cursor.execute("delete from pharmacy where Ref_no= %s", (self.ref_var.get(),))
            messagebox.showinfo("Delete", "Information deleted")
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
         # self.ref_var.set("")
        self.cmpName_var.set("")
        # self.typeMed_var.set("")
        # self.medName_var.set(""),
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideeffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.Price_var.set("")
        self.ProductQt_var.set("")

    def Search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hello123jb@", port='3306',
                                       database="p_m_s")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacy where " + str(self.search_Var.get()) + " LIKE '%" + str(self.searchTxt_var.get()) + "%'")
        rows = my_cursor.fetchall()
        if  len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                 self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
