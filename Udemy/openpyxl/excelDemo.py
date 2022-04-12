import openpyxl
book = openpyxl.load_workbook("C:\\Users\\citri\\OneDrive\\Documents\\Automation\\Udemy\\openpyxl\\PythonDemo.xlsx")
sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)