#import openpyxl and methods
from openpyxl import Workbook

#Create new workbook
my_excel_file = Workbook()

#Create New Worksheet
my_excel_sheet = my_excel_file.create_sheet("Inventories")

#Create Column Headings for the Worksheet
my_excel_sheet["A1"] = "Product No."

my_excel_sheet["B1"] = "Inventory"

my_excel_sheet["C1"] = "Price"

my_excel_sheet["D1"] = "Supplier"

#Save the Workbook
my_excel_file.save("Products.xls")