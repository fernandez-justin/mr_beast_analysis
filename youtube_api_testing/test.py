import csv

with open('..\\all_100_video_ids.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile)

    part = ''
    for id_list in csvReader:
        for id in id_list:
            part = str(f"{part},{id}")
    part = part[1:]
    print(part)
