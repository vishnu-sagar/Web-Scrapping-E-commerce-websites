import csv
from flip import settings

def write_to_csv(item):
       writer = csv.writer(open(settings.csv_file_path, 'a',encoding="utf-8"), lineterminator='\n')
       #print(settings.product)
       #print(item.keys())
       writer.writerow([item[key] for key in item.keys()])
       
class WriteToCsv(object):
    def process_item(self, item, spider):
            write_to_csv(item)
            return item
