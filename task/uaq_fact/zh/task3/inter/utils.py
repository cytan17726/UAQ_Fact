
def arr_doc_to_target_base(doc):
    return [i['label'] for i in doc["answer"]]

def arr_doc_to_text(doc):
    doc_to_text_dict = {
    "zh": "问题: {question}\n答案: 该问句可被拆分为2个子问题，记为q1和q2。q1是\"{que1}\"。q2是\"{que2}\"。q1的答案是\"{ans1}\"。q2的答案是\"{ans2}\"。结合q1和q2的答案进行判断。如果子问题答案有交集，则该问句的答案为此交集。如果子问题答案没有交集，则该问句没有答案。综上，我的答案是: ",
    "en": "Q: {question}\nA: The question can be split into 2 sub-questions, denoted as q1 and q2. q1 is \"{que1}\". q2 is \"{que2}\". The answer to q1 is \"{ans1}\". The answer to q2 is \"{ans2}\". Combine the answers to q1 and q2 to make a judgement. If there is an intersection of the answers to the sub-questions, then the answer to the question is this intersection. If there is no intersection of the answers to the sub-questions, then there is no answer to the question. In summary, my answer is: "
}
    '''Answer the given question in no more than one sentence.\nPlease keep your answer short and concise. Return ##None## if there is no suitable answer.\nQuestion: {{question}}\nAnswer:'''

    lan = doc["lan"]
    template = doc_to_text_dict[lan]
    question = doc["question"]
    que1, que2 = doc["sup_questions"]
    ans1, ans2 = doc["sup_que_ans"]
    # import pdb;pdb.set_trace()
    return template.format(question=question, que1=que1, que2=que2, ans1=ans1, ans2=ans2)
