import collections
import re
import sys
import unicodedata

from lm_eval.filters.extraction import Filter, RegexFilter

def arr_doc_to_target_base(doc):
    # tmp = [i['label'] for i in doc["answer"]]
    # if tmp == [None]:
    #     import pdb;pdb.set_trace()
    return [i['label'] for i in doc["answer"]]

def arr_doc_to_target_cls(doc):
    return doc["cls_target"]

def arr_doc_to_text(doc):
    doc_to_text_dict = {
"zh": "问题: {question}\n答案:该问句可被拆分为主问句{Q}和时间{T},通过辅助问句'{que}'得到主问句{Q}的{real_time}，这个辅助问句的答案是{answer},判断{T}是否与{real_time} {answer}有交集，如果有交集则有答案，则回复对应的答案，如果没有交集，则该问句没有答案。综上，我的答案是: ",
    # "en": "Q: {question}\nA: This question can be split into the main question {Q} and time {T}. Through the auxiliary question,'{que}',we obtain the {real_time} of the main question sentence {Q}, the answer of the auxiliary question is {answer}. Determined whether {T} has an intersection is with {real_time}. If there is an intersection, there is an answer, and the corresponding answer will be replied. If there is no intersection, there is no answer in the question. In summary, my answer is: "
    "en": "Q: {question}\nA: This question can be split into the main question {Q} and time {T}. Through the auxiliary question,'{que}',we obtain the {real_time} of the main question sentence {Q}, the answer of the auxiliary question is {answer}. Determined whether {T} {compare} {real_time} {answer}. If the comparison condition is meet, there is an answer, then the corresponding answer will be replied. If the comparison condition is not meet, there is no answer in the question. In summary, my answer is: "
}
    # ,and two options are \"{options}\"
    '''Answer the given question in no more than one sentence.\nPlease keep your answer short and concise. Return ##None## if there is no suitable answer.\nQuestion: {{question}}\nAnswer:'''
    
    flag=doc['flag']
    if flag=='True':
        real_time="END_TIME"
        compare='<'
    else:
        real_time="START_TIME" 
        compare='>'
    #需要提取主问句，要不直接加一个主问句字段。 目前先只考虑en
    lan = doc["lan"]
    template = doc_to_text_dict[lan]
    question = doc["question"]
    que1 = doc["sup_questions"][0]
    answer=int(doc['sup_que_ans'][0]['label'])
    time_sign=[' from ',' between ',' during ',' in ']
    for sign in time_sign:
        index=question.rfind(sign)
        if index!=-1:
            break
        
    Q=question[:index]+"?"
    time_temp=question[index:]
    T=time_temp
    # matches=re.findall(r"\d+",time_temp)
    # if len(matches)==1:
    #     T=int(matches[0])
    # elif len(matches)>1:
    #     if flag=='True':
    #         T=int(matches[0])
    #     else:
    #         T=int(matches[1])
    # else:
    #     raise ValueError("the len of matches is zero")
    
    # if lan=="en":
    #     from pdb import set_trace;set_trace()
    # return template.format(question=question, que=que1,real_time=real_time,answer=answer,T=T,Q=Q)
    return template.format(question=question, que=que1,real_time=real_time,answer=answer,T=T,Q=Q,compare=compare)