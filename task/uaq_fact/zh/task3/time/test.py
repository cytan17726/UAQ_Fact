import json
import re
filename='/data/cytan/myeval/data/final_sup_que/logic/time/complete/time_sup_logic_en_ua.json'

json_files=json.load(open(filename,'r',encoding='utf8'))
for line in json_files:
    flag=line['flag']
    question=line['question']
    time_sign=[' from ',' between ',' during ',' in ']
    inde=-1
    for sign in time_sign:
        index=question.rfind(sign)
        if index!=-1:
            break
    if index==-1:
        raise ValueError('time sign not exist')
    Q=question[:index]+"?"
    time_temp=question[index:]
    matches=re.findall(r"\d+",time_temp)
    if len(matches)==1:
        T=int(matches[0])
    elif len(matches)>1:
        if flag=='True':
            T=int(matches[0])
        else:
            T=int(matches[1])
    else:
        raise ValueError("the len of matches is zero")
    print(Q)
    print(time_temp)
    print(T)
    break