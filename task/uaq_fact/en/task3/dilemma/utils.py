
def arr_doc_to_target_base(doc):
    return [i['label'] for i in doc["answer"]]

def arr_doc_to_text(doc):
#     doc_to_text_dict = {
#     "zh": "问题: {question}\n答案: 该问句可被拆分为2个子问题，记为q1和q2。q1是\"{que1}\"。q2是\"{que2}\"。q1的答案是\"{ans1}\"。q2的答案是\"{ans2}\"。结合q1和q2的答案进行判断。如果子问题答案有交集，则该问句的答案为此交集。如果子问题答案没有交集，则该问句没有答案。综上，我的答案是: ",
#     "en": "Q: {question}\nA: The question can be split into 2 sub-questions, denoted as q1 and q2. q1 is \"{que1}\". q2 is \"{que2}\". The answer to q1 is \"{ans1}\". The answer to q2 is \"{ans2}\". Combine the answers to q1 and q2 to make a judgement. If there is an intersection of the answers to the sub-questions, then the answer to the question is this intersection. If there is no intersection of the answers to the sub-questions, then there is no answer to the question. In summary, my answer is: "
# }
    
    
    #v1_prompt "en": "Q: {question}\nA: This question is a dilemma. First we ignore the next two options, then the problem becomes: \"{que}\" , and two options are \"{options}\". The answer to the previous question is \"{ans}\" , do the answer appear in the two options? If it does, then that is the answer. If it does not, then there is no answer to the question.In summary, my answer is: "

    doc_to_text_dict = {
    "zh": "问题: {question}\n答案: 该问句是一个假两难问题。首先我们忽略候选选项，那么问题变为了：\"{que}\"，问句中的两个选项是\"{options}\"。这个问题的答案是\"{ans}\"，这些答案是否出现在了后续的选项中？如果出现了那么出现的便是答案，若没有出现则该问句没有答案。综上，我的答案是: ",
    "en": "Q: {question}\nA: This question is a dilemma. First we focuse on the main problem, then the problem becomes: \"{que}\", and the following options are \"{options}\". The answer to the previous question is \"{ans}\". If the answer appear in the two options, this is the answer, otherwise, there is no answer to the question. In all my answer is: "
}
    '''Answer the given question in no more than one sentence.\nPlease keep your answer short and concise. Return ##None## if there is no suitable answer.\nQuestion: {{question}}\nAnswer:'''

    lan = doc["lan"]
    template = doc_to_text_dict[lan]
    question = doc["question"]
    que1= doc["sup_questions"]
    ans_ls = [i['label'] for i in doc['sup_que_ans']][:10]
    ans1 = " , ".join(ans_ls)
    tmp_que = que1[:-1].strip()
    options =  question.replace(tmp_que,"")
    options = options.replace(",","").replace("?","").strip()
    options = options.replace("，","").replace("？","").strip()
    # options = options.replace("or",)
    # if "en" in lan:
    #     import pdb;pdb.set_trace()
    return template.format(question=question, que=que1, ans=ans1,options=options)
