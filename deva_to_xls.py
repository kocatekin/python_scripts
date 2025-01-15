import xlwt
import pandas as pd
import datetime
from openpyxl import Workbook

def main():
   data = []
   filename = input("\ndosya adını tam girin (deva.xls): \n >> ")
   df = pd.read_excel(filename)

   #drop some rows
   df = df.iloc[3:]

   #select the necessary columns - cant use column names due to merge rows
   df = df.iloc[:, [0,1,2,4,5,6,17]]
   
   #satirlarda da sorunlar var - deger olmayan satirlar var bunlari almamak gerekiyor
   #yani bi satir eger tarih ile baslamiyorsa onu discard edebiliriz

   for idx, row in df.iterrows():
      if row[4] not in ["plakalar listeli sekilde burada olacak"] #bu plakalar gelmesin
         continue

      if isinstance(row[0], datetime.datetime): #bos satirlar var gereksiz
         mytxt = f"{str(row[0])[0:10]}-{row[1]}-{row[2]}-{row[3]} LISTE-{row[4]}-{row[6]}"
         data.append(mytxt)

   writeToExcel(data)

def writeToExcel(data: list) -> None:      
   # here we are going to divide the list into months. 
   # first we need to understand how many months we have, later we will create excel files for each.
   # we have the list, we need to parse every item; we need to create a dict for them

   outs = {}
   aylar = []
   for line in data:
      ay = line[0:10].split("-")[1]
      #print(ay)
      if ay in aylar:
         outs[str(ay)].append(line)
      else:
         outs[str(ay)] = []
         outs[str(ay)].append(line)

         aylar.append(ay)
   
   for key in outs:
      #create a new excel here
      toExcel(outs[key], key)
   print("done?")

def toExcel(listdata, name):
   import xlsxwriter as xl
   workbook = xl.Workbook(f"{name}.xlsx")
   worksheet = workbook.add_worksheet()

   worksheet.write(0,0,"HESAPKODU")
   worksheet.write(0,1,"EVRAKNO")
   worksheet.write(0,2,"AÇIKLAMA")
   worksheet.write(0,3,"BORÇ")
   worksheet.write(0,4,"ALACAK")

   x = 1
   for data in listdata:
      worksheet.write(x,2,data)
      x += 1
   
   workbook.close()
   print("closed workbook", name)  

main()
