import hashlib,time,random
from streamlit_s import DEFINE_ST_PARAMETERS

class CHAIN_INFO:
    def LIST_PARAMETERS():
        all_parameters = type(
            "GET PARAMETERS",
            (),
            {"chain_list":[],
             "knowledge_list":[],
             "user_list":[],
             "proof_list":[],
             "main_list":[]})
        return all_parameters
    def WORD_LIST():
        return ["A","B","C","D","E","F",
                "G","H","I","J","K","L",
                "M","N","O","P","R","S",
                "T","U","V","Y","Z"]
    def MAIN_BASE():
        base_all = type(
            "DATABASE",
            (),
            {"main_chain":[],
             "user_all":[]})
        return base_all
    
class KNOWLEDGE_CHAIN:
    def DEFINE_PER_INPUT():
        d_f = CHAIN_INFO.LIST_PARAMETERS()
        c_list = d_f.chain_list
        k_list = d_f.knowledge_list
        u_list = d_f.user_list
        p_list = d_f.proof_list
        m_list = d_f.main_list
        return c_list,k_list,u_list,p_list,m_list
    def CREATE_MOTHER():
        time_n = time.time()
        user_per_id = random.choice(CHAIN_INFO.WORD_LIST())\
            + str(random.randint(0,254123)) + str(time_n)
        m_now = {"time":time_n,
                 "main_user":user_per_id}
        mother_chain = hashlib.sha256(str(m_now).encode()).hexdigest()
        return mother_chain
    def CREATE_KNOWLEDGE(c_list,
                         k_list,
                         u_list,
                         p_list,
                         m_list,
                         message_in):
        user_id = random.choice(CHAIN_INFO.WORD_LIST())\
            + str(random.randint(0,254123))
        user_complex = user_id + message_in + str(time.time())
        message_proof = hashlib.sha256(user_complex.encode()).hexdigest()
        user_proof = hashlib.sha256(message_proof.encode()).hexdigest()
        u_list.append(user_id)
        p_list.append(user_proof)
        k_list.append(message_in)
        k_now = {"proof_message":p_list[-1],
                  "user_id":u_list[-1],
                  "user_message":k_list[-1],
                  "index":(len(c_list)+1),
                  "user_count":len(u_list),
                  "time_now":str(time.time())}
        c_list.append(k_now)
        knowledge_chain = hashlib.sha256(str(k_now).encode()).hexdigest()
        return k_now,knowledge_chain,message_proof

        
        
        
    
    
            
    
        
