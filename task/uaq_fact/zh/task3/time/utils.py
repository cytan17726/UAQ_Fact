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
    "zh": "问题: {question}\n答案:该问句可被拆分为主问句{Q}和时间{T},通过辅助问句'{que}'得到主问句{Q}的{real_time}，这个辅助问句的答案是{real_time},判断T是否与{real_time}有交集，如果有交集则有答案，则回复对应的答案，如果没有交集，则该问句没有答案。综上，我的答案是: ",
    # "en": "Q: {question}\nA: This can be split into the main question '{Q}' and time {T}. Through the auxiliary question, '{que}', we obtain the {real_time} of the main question. Determine whether {T} {compare} {real_time}. If the comparison condition is meet, there is an answer, then the corresponding answer will be replied. If the comparison condition is not meet, there is no answer in the question. In summary, my answer is: "
    "en": "Q: {question}\nA: This can be split into the main question {Q} and time {T}. Through the auxiliary question, '{que}', we obtain the {real_time} of the main question. Determine whether {T} {compare} {real_time}. If the comparison condition is meet, there is an answer, then the corresponding answer will be replied. If the comparison condition is not meet, there is no answer in the question. In summary, my answer is: "
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
        
    lan = doc["lan"]
    template = doc_to_text_dict[lan]
    question = doc["question"]
    answer=int(doc['sup_que_ans'][0]['label'])
    # Match time pattern like "2019-2024年"
    one_year_pattern = r'在\d{2,4}年|\d{2,4}年期间|\d{2,4}年时|自\d{2,4}年以后|于\d{2,4}年|\d{2,4}年时间段'
    time_patterns = [r'(\d{2,4}[-~]\d{2,4}年)', r'(\d{2,4}年至\d{2,4}年)', r'\d{2,4}年到\d{2,4}年']
    time_pattern = "|".join(time_patterns)
    time_match = re.search(time_pattern, question)
    if time_match:
        T = time_match.group(0)
        # Remove the time part to get the main question
        Q = question.replace(T, 'XX').strip()
        if Q.endswith('？'):
            Q = Q[:-1]
    elif re.findall(one_year_pattern, question):
        tmp = re.findall(one_year_pattern, question)
        if len(tmp) == 1:
            T = re.search(r'\d{2,4}', tmp[0]).group(0)
            Q = question.replace(T, 'XX').strip()
            if Q.endswith('？'):
                Q = Q[:-1]
        else:
            import pdb;pdb.set_trace()
            raise ValueError(f"No time pattern found in the question: {question}")
    else:
        print(question)
        import pdb;pdb.set_trace()
        raise ValueError(f"No time pattern found in the question: {question}")
    que1 = doc["sup_questions"][0]

    return template.format(question=question, que=que1,real_time=real_time,answer=answer,T=T,Q=Q,compare=compare)