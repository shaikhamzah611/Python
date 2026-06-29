student_data= {
    "Id1":{'name':'Sara','Grade':"V",'Subjects':'English,Math,Science'},
    "Id2":{'name':'Joe','Grade':"V",'Subjects':'English,Math,Science'},
    "Id3":{'name':'David','Grade':"V",'Subjects':'English,Math,Science'},
    "Id4":{'name':'Sara','Grade':"V",'Subjects':'English,Math,Science'},
    }

result={}
seen_keys=[]

for student_id,details in student_data.items():
    unique_key = (details['name'],details['Grade'],details['Subjects'])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]= details
for k,v in result.items():
    print(k,":",v)