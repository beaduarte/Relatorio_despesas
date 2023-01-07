from PyQt5 import uic,QtWidgets
import sqlite3
import locale
import datetime
import pandas as pd

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def salvar():
    despesa = incluir.lineEdit.text()
    valor = (incluir.lineEdit_2.text().replace(",", "."))
    data = datetime.datetime.strptime(incluir.dateEdit.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    vl = (locale.currency((float(valor)), grouping=True))

    if incluir.radioButton.isChecked():
        banco = sqlite3.connect('DB/admin.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (despesa text, vl text, data date, valor text )")
        cursor.execute("INSERT INTO dados VALUES ('" + despesa + "','" + vl + "','" + data + "','" + valor + "')")
        banco.commit()
        banco.close()

    elif incluir.radioButton_2.isChecked():
        banco = sqlite3.connect('DB/oficina.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (despesa text, vl text, data date, valor text )")
        cursor.execute("INSERT INTO dados VALUES ('" + despesa + "','" + vl + "','" + data + "','" + valor + "')")
        banco.commit()
        banco.close()

    elif incluir.radioButton_3.isChecked():
        banco = sqlite3.connect('DB/sn.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (despesa text, vl text, data date, valor text )")
        cursor.execute("INSERT INTO dados VALUES ('" + despesa + "','" + vl + "','" + data + "','" + valor + "')")
        banco.commit()
        banco.close()

    elif incluir.radioButton_4.isChecked():
        banco = sqlite3.connect('DB/vn.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (despesa text, vl text, data date, valor text )")
        cursor.execute("INSERT INTO dados VALUES ('" + despesa + "','" + vl + "','" + data + "','" + valor + "')")
        banco.commit()
        banco.close()

    else:
        incluir.label_3.setText("DEPARTAMENTO *")

    incluir.lineEdit.setText("")
    incluir.lineEdit_2.setText("")

def listar_tabelas():

        relatorio.show()
        relatorio.dateEdit_2.setDate(datetime.date.today())
        banco = sqlite3.connect('DB/admin.db')
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM dados")
        dados_lidos = cursor.fetchall()
        relatorio.tableWidget_4.setRowCount(len(dados_lidos))
        relatorio.tableWidget_4.setColumnWidth(0, 213)
        for i in range(0, len(dados_lidos)):
            for j in range(0, 3):
                relatorio.tableWidget_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


        banco2 = sqlite3.connect('DB/oficina.db')
        cursor2 = banco2.cursor()
        cursor2.execute("SELECT * FROM dados")
        dados_lidos2 = cursor2.fetchall()
        relatorio.tableWidget_3.setRowCount(len(dados_lidos2))
        relatorio.tableWidget_3.setColumnWidth(0, 213)
        for i in range(0, len(dados_lidos2)):
            for j in range(0, 2):
                relatorio.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos2[i][j])))

        banco3 = sqlite3.connect('DB/vn.db')
        cursor3 = banco3.cursor()
        cursor3.execute("SELECT * FROM dados")
        dados_lidos3 = cursor3.fetchall()
        relatorio.tableWidget_2.setRowCount(len(dados_lidos3))
        relatorio.tableWidget_2.setColumnWidth(0, 213)
        for i in range(0, len(dados_lidos3)):
            for j in range(0, 2):
                relatorio.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos3[i][j])))

        banco4 = sqlite3.connect('DB/sn.db')
        cursor4 = banco4.cursor()
        cursor4.execute("SELECT * FROM dados")
        dados_lidos4 = cursor4.fetchall()
        relatorio.tableWidget.setRowCount(len(dados_lidos4))
        relatorio.tableWidget.setColumnWidth(0, 213)
        for i in range(0, len(dados_lidos4)):
            for j in range(0, 2):
                relatorio.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos4[i][j])))
   


def listar_label():

        banco = sqlite3.connect('DB/admin.db')
        cursor = banco.cursor()
        sql = f"SELECT SUM(valor) FROM dados"
        cursor.execute(sql)
        sum = cursor.fetchall()
        if str(sum) == "[(None,)]":
            sum = 0
            relatorio.label_5.setText((locale.currency(sum, grouping=True)))

        else:
            sum = float(sum[0][0])
            relatorio.label_5.setText((locale.currency(sum, grouping=True)))


        banco = sqlite3.connect('DB/oficina.db')
        cursor = banco.cursor()
        sql = f"SELECT SUM(valor) FROM dados"
        cursor.execute(sql)
        sum1 = cursor.fetchall()
        if str(sum1) == "[(None,)]":
            sum1 = 0
            relatorio.label_6.setText((locale.currency(sum1, grouping=True)))

        else:
            sum1 = float(sum1[0][0])
            relatorio.label_6.setText((locale.currency(sum1, grouping=True)))

        banco = sqlite3.connect('DB/vn.db')
        cursor = banco.cursor()
        sql = f"SELECT SUM(valor) FROM dados"
        cursor.execute(sql)
        sum2 = cursor.fetchall()
        if str(sum2) == "[(None,)]":
            sum2 = 0
            relatorio.label_7.setText((locale.currency(sum2, grouping=True)))

        else:
            sum2 = float(sum2[0][0])
            relatorio.label_7.setText((locale.currency(sum2, grouping=True)))

        banco = sqlite3.connect('DB/sn.db')
        cursor = banco.cursor()
        sql = f"SELECT SUM(valor) FROM dados"
        cursor.execute(sql)
        sum3 = cursor.fetchall()
        if str(sum3) == "[(None,)]":
            sum3 = 0
            relatorio.label_8.setText((locale.currency(sum3, grouping=True)))

        else:
            sum3 = float(sum3[0][0])
            relatorio.label_8.setText((locale.currency(sum3, grouping=True)))

        total = (locale.currency(sum+sum1+sum2+sum3, grouping=True))
        relatorio.label_9.setText(total)

def filtro():

    # seminovos tabela
    if relatorio.tableWidget.rowCount()>0:
        relatorio.tableWidget.clearContents()

    relatorio.show()
    datainicio = datetime.datetime.strptime(relatorio.dateEdit.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    datafinal = datetime.datetime.strptime(relatorio.dateEdit_2.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    banco = sqlite3.connect('DB/sn.db')
    cursor = banco.cursor()
    sql = f"SELECT * FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()

    for i in range(0, len(dados_lidos)):
        for j in range(0, 2):
            relatorio.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    banco = sqlite3.connect('DB/sn.db')
    cursor = banco.cursor()
    sql = f"SELECT SUM(valor) FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    cursor.execute(sql)
    sum = cursor.fetchall()
    if str(sum)=="[(None,)]":
        sum = 0
        relatorio.label_8.setText((locale.currency(sum, grouping=True)))

    else:
        sum = float(sum[0][0])
        relatorio.label_8.setText((locale.currency(sum, grouping=True)))


    #novos tabela
    if relatorio.tableWidget_2.rowCount()>0:
        relatorio.tableWidget_2.clearContents()

    relatorio.show()
    datainicio = datetime.datetime.strptime(relatorio.dateEdit.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    datafinal = datetime.datetime.strptime(relatorio.dateEdit_2.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    banco2 = sqlite3.connect('DB/vn.db')
    cursor2 = banco2.cursor()
    sql = f"SELECT * FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    cursor2.execute(sql)
    dados_lidos2 = cursor2.fetchall()

    for i in range(0, len(dados_lidos2)):
        for j in range(0, 2):
            relatorio.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos2[i][j])))

    banco2 = sqlite3.connect('DB/vn.db')
    cursor2 = banco2.cursor()
    sql = f"SELECT SUM(valor) FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    cursor2.execute(sql)
    sum2 = cursor2.fetchall()
    if str(sum2) == "[(None,)]":
        sum2 = 0
        relatorio.label_7.setText((locale.currency(sum2, grouping=True)))

    else:
        sum2 = float(sum2[0][0])
        relatorio.label_7.setText((locale.currency(sum2, grouping=True)))


    #oficina tabela
    if relatorio.tableWidget_3.rowCount()>0:
        relatorio.tableWidget_3.clearContents()

    relatorio.show()
    datainicio = datetime.datetime.strptime(relatorio.dateEdit.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    datafinal = datetime.datetime.strptime(relatorio.dateEdit_2.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    banco3 = sqlite3.connect('DB/oficina.db')
    cursor3 = banco3.cursor()
    sql = f"SELECT * FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    cursor3.execute(sql)
    dados_lidos3 = cursor3.fetchall()

    for i in range(0, len(dados_lidos3)):
        for j in range(0, 2):
            relatorio.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos3[i][j])))

    banco3 = sqlite3.connect('DB/oficina.db')
    cursor3 = banco3.cursor()
    sql = f"SELECT SUM(valor) FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    cursor3.execute(sql)
    sum3 = cursor3.fetchall()
    if str(sum3) == "[(None,)]":
        sum3 = 0
        relatorio.label_6.setText((locale.currency(sum3, grouping=True)))

    else:
        sum3 = float(sum3[0][0])
        relatorio.label_6.setText((locale.currency(sum3, grouping=True)))

    # admin tabela
    if relatorio.tableWidget_4.rowCount() > 0:
        relatorio.tableWidget_4.clearContents()

    relatorio.show()
    datainicio = datetime.datetime.strptime(relatorio.dateEdit.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    datafinal = datetime.datetime.strptime(relatorio.dateEdit_2.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    banco4 = sqlite3.connect('DB/admin.db')
    cursor4 = banco4.cursor()
    sql = f"SELECT * FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    cursor4.execute(sql)
    dados_lidos4 = cursor4.fetchall()

    for i in range(0, len(dados_lidos4)):
        for j in range(0, 2):
            relatorio.tableWidget_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos4[i][j])))

    banco4 = sqlite3.connect('DB/admin.db')
    cursor4 = banco4.cursor()
    sql = f"SELECT SUM(valor) FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    cursor4.execute(sql)
    sum4 = cursor4.fetchall()

    if str(sum4) == "[(None,)]":
        sum4 = 0
        relatorio.label_5.setText((locale.currency(sum4, grouping=True)))

    else:
        sum4 = float(sum4[0][0])
        relatorio.label_5.setText((locale.currency(sum4, grouping=True)))

    total = sum+sum2+sum3+sum4
    relatorio.label_9.setText((locale.currency(total, grouping=True)))

def excel():
    datainicio = datetime.datetime.strptime(relatorio.dateEdit.text(), "%d/%m/%Y").strftime("%Y-%m-%d")
    datafinal = datetime.datetime.strptime(relatorio.dateEdit_2.text(), "%d/%m/%Y").strftime("%Y-%m-%d")

    con = sqlite3.connect('DB/admin.db')
    sql = f"SELECT * FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    df = pd.read_sql_query(sql, con)
    df.to_excel('RELATORIO/admin.xlsx')

    con2 = sqlite3.connect('DB/oficina.db')
    sql2 = f"SELECT * FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    df2 = pd.read_sql_query(sql2, con2)
    df2.to_excel('RELATORIO/oficina.xlsx')

    con3 = sqlite3.connect('DB/vn.db')
    sql3 = f"SELECT * FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    df3 = pd.read_sql_query(sql3, con3)
    df3.to_excel('RELATORIO/vn.xlsx')

    con4 = sqlite3.connect('DB/sn.db')
    sql4 = f"SELECT * FROM dados WHERE data between '{datainicio}' and '{datafinal}'"
    df4 = pd.read_sql_query(sql4, con4)
    df4.to_excel('RELATORIO/seminovos.xlsx')

#converter QT em python
app=QtWidgets.QApplication([])
incluir = uic.loadUi("QT/incluir.ui")
relatorio = uic.loadUi("QT/relatorio.ui")


incluir.pushButton.clicked.connect(salvar)
incluir.pushButton_2.clicked.connect(listar_tabelas)
incluir.pushButton_2.clicked.connect(listar_label)
relatorio.filtro_2.clicked.connect(filtro)
relatorio.limpar.clicked.connect(listar_tabelas)
relatorio.limpar.clicked.connect(listar_label)
relatorio.pushButton.clicked.connect(excel)

incluir.show()
app.exec()
