import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
import queries
import time
import math

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.crearcuent.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()

        if email == '' or password == '':
            QMessageBox.information(self, "Información", "Llenar todos los campos", QMessageBox.Ok)
            return

        empleado = queries.login(email, password)
        
        if empleado:
            self.go_to_boletos(empleado)
        else:
            QMessageBox.information(self, "Información", "Acceso incorrecto", QMessageBox.Ok)
            self.limpiar()

    def limpiar(self):
        self.email.setText('')
        self.password.setText('')

    def gotocreate(self):
        nuevo_empleado=Nuevo_Empleado()
        widget.addWidget(nuevo_empleado)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_boletos(self, id_empleado):
        boletos = Boletos(id_empleado)
        widget.addWidget(boletos)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Nuevo_Empleado(QDialog):
    def __init__(self):
        super(Nuevo_Empleado, self).__init__()
        loadUi("nuevo_empleado.ui",self)
        
        self.crearbutton.clicked.connect(self.nuevo_empleadofunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pbLogin.clicked.connect(self.go_to_login)

    def nuevo_empleadofunction(self):
        ## To Do: Get atributos para insertar empleado
        nombre = self.nombre.text()
        apellido_p = self.ap_pat.text()
        apellido_m = self.ap_mat.text()
        email = self.email.text()
        password = self.password.text()
        password2 = self.confirpass.text()

        if nombre == '' or apellido_p == '' or apellido_m == '' or email == '' or password == '' or password2 == '':
            QMessageBox.information(self, "Información", "Debe llenar todos los campos", QMessageBox.Ok)
            return

        if password == password2:

            meses = {'ene.':'01', 'feb.':'02','mar.':'03','abr.':'04','may.':'05','jun.':'06','jul.':'07','ago.':'08','sep.':'09','oct.':'10','nov.':'11','dic.':'12'}
            f = self.calendar.selectedDate().toString()
            fsplit = f.split()[1:]
            dia = f"0{fsplit[1]}" if int(fsplit[1]) < 10 else fsplit[1]
            fecha_nac_empleado = dia + '/' + meses[fsplit[0]] + '/' + fsplit[2]
            empleado = {'nombre_empleado':nombre, 'apellido_p_empleado':apellido_p, 'apellido_m_empleado':apellido_m, 'fecha_nac_empleado':fecha_nac_empleado, 'correo_elec_empleado':email, 'password_empleado':password}

            insertado = queries.insertar_empleado(empleado)

            if insertado:
                self.go_to_login()
            else:
                QMessageBox.information(self, "Información", "Hubo un error al ingresar sus datos", QMessageBox.Ok)
            
            self.limpiar()
        else:
            QMessageBox.information(self, "Información", "Las contraseñas deben coincidir", QMessageBox.Ok)

    def go_to_login(self):
        login=Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)     

    def limpiar(self):
        self.nombre.setText('')
        self.ap_pat.setText('')
        self.ap_mat.setText('')
        self.email.setText('')
        self.password.setText('')
        self.confirpass.setText('')

        hoy = time.strftime("%x").split('/')
        hoy[0] = hoy[0][1] if int(hoy[0]) < 10 else hoy[0]
        hoy[1] = hoy[1][1] if int(hoy[1]) < 10 else hoy[1]
        hoy[2] = f'20{hoy[2]}'

        mes, dia, anio = hoy
        self.calendar.setSelectedDate(QDate(int(anio), int(mes), int(dia)))

class Boletos(QDialog):
    def __init__(self, id_empleado):
        super(Boletos, self).__init__()
        loadUi("boletos.ui",self)
        self.id_empleado = id_empleado
        self.puerta1 = 0
        self.puerta2 = 0
        self.puerta3 = 0
        self.personas_totales = 0
        self.personas_rechazadas = 0
        self.boletos_duplicados = 0
        self.lcdNPuerta1.display(0)
        self.lcdNPuerta1.setDigitCount(2)
        self.lcdNPuerta2.display(0)
        self.lcdNPuerta2.setDigitCount(2)
        self.lcdNPuerta3.display(0)
        self.lcdNPuerta3.setDigitCount(2)
        self.lcdNTotal.display(0)
        self.lcdNTotal.setDigitCount(2)
        self.lcdNRechazados.display(0)
        self.lcdNRechazados.setDigitCount(2)
        self.lcdNDuplicados.display(0)
        self.lcdNDuplicados.setDigitCount(2)
        self.total_parcial = 0
        self.progreso = 0
        self.progressBar.setValue(self.progreso)
        self.totalAEntrar = queries.get_total_boletos_por_concierto(1)
        self.avance = (100 / self.totalAEntrar) if self.totalAEntrar != 0 else 0
        #self.crearbutton.clicked.connect(self.nuevo_empleadofunction)
        #self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.confirpass.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.lblBoleto1_P1.setText('hola')
        self.pbCerrarSesion.clicked.connect(self.logout)
        self.pbCerrarPuertas.clicked.connect(self.cerrar_puertas(self.pbCerrarPuertas))
        self.nombre_concierto = queries.get_concierto(1)
        self.nombre_empleado = queries.get_nombre_empleado(self.id_empleado)
        self.lblNombreEmpleado.setText('Empleado: ' + self.nombre_empleado)
        self.lblNombreConcierto.setText('Concierto: ' + self.nombre_concierto)

        ## PUERTA 1
        ## BOLETOS
        self.boletos = queries.get_boletos(1)
        self.lbls_boletos_P1 = [self.lblBoleto1_P1, self.lblBoleto2_P1, self.lblBoleto3_P1, self.lblBoleto4_P1, self.lblBoleto5_P1, self.lblBoleto6_P1, self.lblBoleto7_P1, self.lblBoleto8_P1, self.lblBoleto9_P1,     self.lblBoleto10_P1]
        self.id_usuarios_P1 = []
        self.id_boletos_P1 = []
    
        #Botones Rechazar
        self.btnsRechazar_P1 = [self.pbRechazar1_P1, self.pbRechazar2_P1, self.pbRechazar3_P1, self.pbRechazar4_P1, self.pbRechazar5_P1, self.pbRechazar6_P1, self.pbRechazar7_P1, self.pbRechazar8_P1, self.pbRechazar9_P1, self.pbRechazar10_P1]

        #Botones Aceptar
        self.btnsAceptar_P1 = [self.pbAceptar1_P1, self.pbAceptar2_P1, self.pbAceptar3_P1, self.pbAceptar4_P1, self.pbAceptar5_P1, self.pbAceptar6_P1, self.pbAceptar7_P1, self.pbAceptar8_P1, self.pbAceptar9_P1, self.pbAceptar10_P1]

        ##PUERTA 2
        self.boletos2 = queries.get_boletos(2)
        self.lbls_boletos_P2 = [self.lblBoleto1_P2, self.lblBoleto2_P2, self.lblBoleto3_P2, self.lblBoleto4_P2, self.lblBoleto5_P2, self.lblBoleto6_P2, self.lblBoleto7_P2, self.lblBoleto8_P2, self.lblBoleto9_P2, self.lblBoleto10_P2]
        self.id_usuarios_P2 = []
        self.id_boletos_P2 = []

        #Botones Rechazar
        self.btnsRechazar_P2 = [self.pbRechazar1_P2, self.pbRechazar2_P2, self.pbRechazar3_P2, self.pbRechazar4_P2, self.pbRechazar5_P2, self.pbRechazar6_P2, self.pbRechazar7_P2, self.pbRechazar8_P2, self.pbRechazar9_P2, self.pbRechazar10_P2]

        #Botones Aceptar
        self.btnsAceptar_P2 = [self.pbAceptar1_P2, self.pbAceptar2_P2, self.pbAceptar3_P2, self.pbAceptar4_P2, self.pbAceptar5_P2, self.pbAceptar6_P2, self.pbAceptar7_P2, self.pbAceptar8_P2, self.pbAceptar9_P2, self.pbAceptar10_P2]

        ###PUERTA 3
        self.boletos3 = queries.get_boletos(3)
        self.lbls_boletos_P3 = [self.lblBoleto1_P3, self.lblBoleto2_P3, self.lblBoleto3_P3, self.lblBoleto4_P3, self.lblBoleto5_P3, self.lblBoleto6_P3, self.lblBoleto7_P3, self.lblBoleto8_P3, self.lblBoleto9_P3, self.lblBoleto10_P3]
        self.id_usuarios_P3 = []
        self.id_boletos_P3 = []

        #Botones Rechazar
        self.btnsRechazar_P3 = [self.pbRechazar1_P3, self.pbRechazar2_P3, self.pbRechazar3_P3, self.pbRechazar4_P3, self.pbRechazar5_P3, self.pbRechazar6_P3, self.pbRechazar7_P3, self.pbRechazar8_P3, self.pbRechazar9_P3, self.pbRechazar10_P3]

        #Botones Aceptar
        self.btnsAceptar_P3 = [self.pbAceptar1_P3, self.pbAceptar2_P3, self.pbAceptar3_P3, self.pbAceptar4_P3, self.pbAceptar5_P3, self.pbAceptar6_P3, self.pbAceptar7_P3, self.pbAceptar8_P3, self.pbAceptar9_P3, self.pbAceptar10_P3]

        #Numero a verificar
        self.n_a_verificar = self.set_n_a_verificar()

        #SET BOLETOS
        self.set_boletos()

    def cargar_mas_boletos(self):
        if self.n_a_verificar == self.total_parcial and self.n_a_verificar != 0:
            self.boletos = queries.get_boletos(1)
            self.boletos2 = queries.get_boletos(2)
            self.boletos3 = queries.get_boletos(3)
            self.n_a_verificar = self.set_n_a_verificar()
            self.total_parcial = 0

            return True
        
        return False

    def set_n_a_verificar(self):
        n = 0
        if self.boletos:
            n = n + len(self.boletos)
        if self.boletos2:
            n = n + len(self.boletos2)
        if self.boletos3:
            n = n + len(self.boletos3)
        return n

    def aceptar_boleto(self, id_boleto, id_usuario, btnAceptar, btnRechazar, n_puerta):
        def ret_id_boleto():
            ingresado = queries.verificar_ingreso(id_boleto)
            if not ingresado:
                if queries.set_cliente_verificado(id_usuario):
                    if n_puerta == 1:
                        self.puerta1 = self.puerta1 + 1
                        self.lcdNPuerta1.display(self.puerta1)
                    if n_puerta == 2:
                        self.puerta2 = self.puerta2 + 1
                        self.lcdNPuerta2.display(self.puerta2)
                    if n_puerta == 3:
                        self.puerta3 = self.puerta3 + 1
                        self.lcdNPuerta3.display(self.puerta3)
                    self.personas_totales = self.personas_totales + 1
                    self.lcdNTotal.display(self.personas_totales)
                    queries.set_aceptado_boleto(id_boleto)

                self.total_parcial = self.total_parcial + 1
                self.progreso = self.progreso + self.avance
                self.progressBar.setValue(self.progreso)
            else:
                if queries.set_cliente_verificado(id_usuario):
                    self.boletos_duplicados = self.boletos_duplicados + 1
                    self.lcdNDuplicados.display(self.boletos_duplicados)
                    self.progreso = self.progreso + self.avance
                    self.progressBar.setValue(self.progreso)
                    self.total_parcial = self.total_parcial + 1

            if self.cargar_mas_boletos():
                self.set_boletos()
                return

            if self.verificar_fin():
                queries.datos_concierto(1, self.puerta1, self.puerta2, self.puerta3, self.personas_totales, self.personas_rechazadas, self.boletos_duplicados)
                return
            btnAceptar.setDisabled(True)
            btnRechazar.setDisabled(True)

        return ret_id_boleto

    def rechazar_boleto(self, btnRechazar, btnAceptar,id_usuario):
        def foo():
            if queries.set_cliente_verificado(id_usuario):
                self.personas_rechazadas = self.personas_rechazadas + 1
                self.lcdNRechazados.display(self.personas_rechazadas)
                self.progreso = self.progreso + self.avance
                self.progressBar.setValue(self.progreso)
                self.total_parcial = self.total_parcial + 1
                btnRechazar.setDisabled(True)
                btnAceptar.setDisabled(True)

                if self.cargar_mas_boletos():
                    self.set_boletos()
                    return

                if self.verificar_fin():
                    queries.datos_concierto(1, self.puerta1, self.puerta2, self.puerta3, self.personas_totales, self.personas_rechazadas, self.boletos_duplicados)
                    return
        return foo

    def verificar_fin(self):
        if self.progressBar.value() == 100:
            QMessageBox.information(self, "Información", "Empleado " + self.nombre_empleado + ' disponible', QMessageBox.Ok)
            self.personas_totales = self.puerta1 + self.puerta2 + self.puerta3
            return True
        
        return False

    def logout(self):
        disponible = queries.set_empleado_disponible(self.id_empleado)
        
        if disponible:
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def set_boletos(self):
        #PUERTA 1
        #i = 0
        if self.boletos:
            max_boletos = len(self.boletos)
            self.id_usuarios_P1 = []
            self.id_boletos_P1 = []
            self.reset(self.lbls_boletos_P1, self.btnsAceptar_P1, self.btnsRechazar_P1)
            for i in range(0,max_boletos):
                #Listas ids    
                self.id_usuarios_P1.append(self.boletos[i]['id_usuario'])
                self.id_boletos_P1.append(self.boletos[i]['id_boleto'])
                #Etiquetas
                self.lbls_boletos_P1[i].setText('Fecha de compra: ' + str(self.boletos[i]['fecha_hora_compra_boleto']) + '\nCliente: ' + self.boletos[i]['nombre_usuario'] + ' ' + self.boletos[i]['apellido_p_usuario'] + ' ' + self.boletos[i]['apellido_m_usuario'] + '\nTipo: ' + self.boletos[i]['nombre_tipo_cliente'])
                #BtnsAceptar
                self.btnsAceptar_P1[i].clicked.connect(self.aceptar_boleto(self.id_boletos_P1[i], self.id_usuarios_P1[i], self.btnsAceptar_P1[i], self.btnsRechazar_P1[i], 1))
                self.btnsAceptar_P1[i].setDisabled(False)
                #btnsRechazar
                self.btnsRechazar_P1[i].clicked.connect(self.rechazar_boleto(self.btnsRechazar_P1[i], self.btnsAceptar_P1[i], self.id_usuarios_P1[i]))
                self.btnsRechazar_P1[i].setDisabled(False)

            if max_boletos < 10:
                self.llenar_vacio(max_boletos, self.lbls_boletos_P1, self.btnsAceptar_P1 ,self.btnsRechazar_P1)
        else:
            self.llenar_vacio(0, self.lbls_boletos_P1, self.btnsAceptar_P1 ,self.btnsRechazar_P1)

        ##PUERTA 2
        if self.boletos2:
            max_boletos = len(self.boletos2)
            self.reset(self.lbls_boletos_P2,self.btnsAceptar_P2,self.btnsRechazar_P2)
            self.id_usuarios_P2 = []
            self.id_boletos_P2 = []
            for i in range(0,max_boletos):
                #Listas ids
                self.id_usuarios_P2.append(self.boletos2[i]['id_usuario'])
                self.id_boletos_P2.append(self.boletos2[i]['id_boleto'])
                #Etiquetas
                self.lbls_boletos_P2[i].setText('Fecha de compra: ' + str(self.boletos2[i]['fecha_hora_compra_boleto']) + '\nCliente: ' + self.boletos2[i]['nombre_usuario'] + ' ' + self.boletos2[i]['apellido_p_usuario'] + ' ' + self.boletos2[i]['apellido_m_usuario'] + '\nTipo: ' + self.boletos2[i]['nombre_tipo_cliente'])
                #BtnsAceptar
                self.btnsAceptar_P2[i].clicked.connect(self.aceptar_boleto(self.id_boletos_P2[i], self.id_usuarios_P2[i], self.btnsAceptar_P2[i], self.btnsRechazar_P2[i], 2))
                self.btnsAceptar_P2[i].setDisabled(False)
                #btnsRechazar
                self.btnsRechazar_P2[i].clicked.connect(self.rechazar_boleto(self.btnsRechazar_P2[i], self.btnsAceptar_P2[i], self.id_usuarios_P2[i]))
                self.btnsRechazar_P2[i].setDisabled(False)

            if max_boletos < 10:
                self.llenar_vacio(max_boletos, self.lbls_boletos_P2, self.btnsAceptar_P2 ,self.btnsRechazar_P2)
        else:
            self.llenar_vacio(0, self.lbls_boletos_P2, self.btnsAceptar_P2 ,self.btnsRechazar_P2)


        ##PUERTA 3
        if self.boletos3:
            max_boletos = len(self.boletos3)
            self.reset(self.lbls_boletos_P3,self.btnsAceptar_P3,self.btnsRechazar_P3)
            self.id_usuarios_P3 = []
            self.id_boletos_P3 = []
            for i in range(0,max_boletos):
                #Listas ids
                self.id_usuarios_P3.append(self.boletos3[i]['id_usuario'])
                self.id_boletos_P3.append(self.boletos3[i]['id_boleto'])
                #Etiquetas
                self.lbls_boletos_P3[i].setText('Fecha de compra: ' + str(self.boletos3[i]['fecha_hora_compra_boleto']) + '\nCliente: ' + self.boletos3[i]['nombre_usuario'] + ' ' + self.boletos3[i]['apellido_p_usuario'] + ' ' + self.boletos3[i]['apellido_m_usuario'] + '\nTipo: ' + self.boletos3[i]['nombre_tipo_cliente'])
                #BtnsAceptar
                self.btnsAceptar_P3[i].clicked.connect(self.aceptar_boleto(self.id_boletos_P3[i], self.id_usuarios_P3[i], self.btnsAceptar_P3[i], self.btnsRechazar_P3[i], 3))
                self.btnsAceptar_P3[i].setDisabled(False)
                #btnsRechazar
                self.btnsRechazar_P3[i].clicked.connect(self.rechazar_boleto(self.btnsRechazar_P3[i], self.btnsAceptar_P3[i], self.id_usuarios_P3[i]))
                self.btnsRechazar_P3[i].setDisabled(False)

            if max_boletos < 10:
                self.llenar_vacio(max_boletos, self.lbls_boletos_P3, self.btnsAceptar_P3 ,self.btnsRechazar_P3)
        else:
            self.llenar_vacio(0, self.lbls_boletos_P3, self.btnsAceptar_P3 ,self.btnsRechazar_P3)
        
    def llenar_vacio(self, max_boletos, labels, btnsAceptar, btnsRechazar):
        for i in range(max_boletos,10):
            #Etiquetas
            labels[i].setText('-----')
            #BtnsAceptar
            btnsAceptar[i].setDisabled(True)
            #btnsRechazar
            btnsRechazar[i].setDisabled(True)

    def reset(self, labels, btnsAceptar, btnsRechazar):
        for i in range(0, 10):
            labels[i].setText('')
            btnsAceptar[i].clicked.connect(self.x)
            btnsRechazar[i].clicked.connect(self.x)

    def cerrar_puertas(self, btnCerrarPuertas):
        def cerrar():            
            btnCerrarPuertas.setDisabled(True)
            self.label_3.setText('')
            self.lblAceptar_P1.setText('')
            self.lblRechazar_P1.setText('')
            self.label.setText('')
            self.lblAceptar_P3.setText('')
            self.lblRechazar_P3.setText('')
            self.n_a_verificar = self.set_n_a_verificar()
            self.label_2.setText('Boletos')
            self.reset(self.lbls_boletos_P1, self.btnsAceptar_P1, self.btnsRechazar_P1)
            self.reset(self.lbls_boletos_P2, self.btnsAceptar_P2, self.btnsRechazar_P2)
            self.reset(self.lbls_boletos_P3, self.btnsAceptar_P3, self.btnsRechazar_P3)
            self.boletos = []
            self.boletos3 = []
            self.boletos2 = queries.get_boletos_puerta_cerrada()
            self.set_boletos()
        return cerrar

    def x(self):
        pass

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1280)
widget.setFixedHeight(650)
widget.show()
app.exec_()