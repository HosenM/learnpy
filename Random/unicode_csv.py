import csv

with open ('result.csv','w',encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.w('تست فارسی')
    # csv_headers = 'Brand,Model,Price\n'
    # f.write(csv_headers)
    # f.write(item1 + "," + item2 + "," + item3 + "\n") 
    # f.close()