from libs import survey

table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies', len(table.records))

alive1 = 0
alive_other = 0
for r in table.records:
    if r.nbrnaliv == 1:
        if r.birthord == 1:
            alive1 += 1
        else:
            alive_other += 1

print(alive1)
print(alive_other)