def averagegrade(records):
    totalgrade=sum(record[2] for record in records)
    return totalgrade/len(records)
students=(
    ('James',20,98),
    ('Hamid',19,56),
    ('Kashif',32,78)
)
def main():
    avggrade=averagegrade(students)
    print("Average:", avggrade)
main()        