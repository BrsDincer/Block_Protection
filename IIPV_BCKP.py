import hashlib,json
from sqllite_exam import DB_PROCESS
from streamlit_s import DEFINE_ST_PARAMETERS
from knowledge_chain import CHAIN_INFO
from knowledge_chain import KNOWLEDGE_CHAIN
from html_type import ST_HTML


class MAIN_RUN():
    def ST_SESSION():
        DEFINE_ST_PARAMETERS.ST_CONF_DEFINE()
    def ST_HEAD():
        s_t = DEFINE_ST_PARAMETERS.ST_API()
        s_t.c(ST_HTML.CREATOR_ART())
        
class START_PROCESS():
        def LAUNCHED_FUNCTION():
            try:
                s_t = DEFINE_ST_PARAMETERS.ST_API()
                c_list,k_list,u_list,p_list,m_list = KNOWLEDGE_CHAIN.DEFINE_PER_INPUT()
                data_base_define = CHAIN_INFO.MAIN_BASE()
                mother_base = KNOWLEDGE_CHAIN.CREATE_MOTHER()
                DB_PROCESS.CREATE_DB("blockchain.db")
                main_chain = data_base_define.main_chain
                chain_spec = {"chain":c_list}
                chain_all = {"main_chain":{}}
                mother_chain = {"chain_class":{f"{mother_base}":{}}}
                side_select = s_t.sdb.selectbox("SELECT PROCESS",
                                      ("JOIN THE FEED",
                                       "KNOWLEDGE TREE",
                                       "CHAIN-BASE TRANSFER",
                                       "KNOWLEDGE BURNING PROCESS"))
                if side_select == "JOIN THE FEED":
                    s_t.md(ST_HTML.RUN_HEAD("KNOWLEDGE FEED"),
                               unsafe_allow_html=True)
                    try: 
                        pub_token_ask = s_t.ta("WRITE THE PUBLIC TOKEN TO READ",
                                   help="WRITE THE PUBLIC TOKEN YOU WANT TO READ THE KNOWLEDGE").replace(" ","")
                        pub_button = s_t.b("READ")
                        if pub_button:
                            user_ask_read = DB_PROCESS.REACH_DB(pub_token_ask,"blockchain.db")
                            s_t.md(ST_HTML.RUN_SIMPLE(str(user_ask_read)),
                                       unsafe_allow_html=True)
                    except:
                        pass
                    
                    user_ask = s_t.ta("WRITE YOUR KNOWLEDGE TO JOIN THE BLOCK",
                                                      help="WRITE THE KNOWLEDGE YOU WANT TO ADD").replace("\n"," ")
                    run_button = s_t.b("ADD")
                    try:
                        if run_button:
                            Message_In,knowledge_chain,message_proof = KNOWLEDGE_CHAIN.CREATE_KNOWLEDGE(c_list,k_list,u_list,p_list,m_list,
                                                                                  user_ask)
                            s_t.i("This is the secret token for your knowledge, save it before exit")
                            s_t.c(message_proof)
                            s_t.tx("YOUR USER ID")
                            s_t.c(chain_spec['chain'][0]['user_id'])
                            chain_all["main_chain"][f"{knowledge_chain}"] = k_list[-1]
                            main_chain.append(knowledge_chain)
                            mother_chain["chain_class"][f"{mother_base}"] = chain_all
                            DB_PROCESS.ADD_DB(f"{user_ask}",
                                                  f"{chain_spec['chain'][0]['proof_message']}",
                                                  u_list[-1],
                                                  "blockchain.db")
                            read_all = DB_PROCESS.READ_DB("blockchain.db")
                            for x_count,_ in enumerate(read_all):
                                s_t.tx("---"*7)
                                s_t.md(ST_HTML.RUN_CONNECTED(str(read_all[x_count-1][1])),
                                           unsafe_allow_html=True)
                                s_t.md(ST_HTML.RUN_TXT(str(read_all[x_count][0]),
                                                           str(read_all[x_count][1]),
                                                           str(read_all[x_count][2])),
                                           unsafe_allow_html=True)
                        else:
                            pass
                    except Exception as err:
                        s_t.tx(str(err))
                elif side_select == "KNOWLEDGE TREE":
                    try:
                        s_t.md(ST_HTML.RUN_HEAD("KNOWLEDGE TREE"),
                               unsafe_allow_html=True)
                        read_all = DB_PROCESS.READ_DB("blockchain.db")
                        json_data = json.dumps(read_all)
                        s_t.j(json_data)
                    except:
                        pass
                elif side_select == "CHAIN-BASE TRANSFER":
                    try:
                        s_t.md(ST_HTML.RUN_HEAD("KNOWLEDGE TRANSFER"),
                               unsafe_allow_html=True)
                        s_t.w("IF SECRET TOKEN MATCHES A KNOWLEDGE, THE TRANSFER IS COMPLETED")
                        user_ask = s_t.ta("WRITE THE TOKEN YOU WANT TO TRANSFER TO YOURSELF",
                                                      help="WRITE THE TOKEN TRANSFERRED TO YOU BY THE PRINCIPAL OWNER OF TOKEN").replace(" ","")
                        
                        run_button = s_t.b("LAUNCH")
                    except:
                        pass
                    if run_button:
                        try:
                            hash_check = hashlib.sha256(user_ask.encode()).hexdigest()
                            user_ask = DB_PROCESS.REACH_DB(str(hash_check),"blockchain.db")
                            if user_ask != None:
                                s_t.md(ST_HTML.RUN_SIMPLE(str(user_ask)),
                                       unsafe_allow_html=True)
                                pass_proof = hashlib.sha256(hash_check.encode()).hexdigest()
                                s_t.s("[ SAVE IT ] NEW SECRET KEY: "+hash_check)
                                DB_PROCESS.EXC_DB(str(hash_check),str(pass_proof),"blockchain.db")
                                s_t.i("NEW PUBLIC KEY: "+pass_proof)
                                s_t.i("KNOWLEDGE HAS BEEN TRANSFERED TO YOU")
                            else:
                                s_t.e("TOKEN IS NOT VALID")
                        except:
                            pass
                elif side_select == "KNOWLEDGE BURNING PROCESS":
                    try:
                        s_t.md(ST_HTML.RUN_HEAD("KNOWLEDGE BURNING"),
                               unsafe_allow_html=True)
                        s_t.w("IF SECRET TOKEN MATCHES A KNOWLEDGE, THE BURNING IS COMPLETED")
                        s_t.w("THIS PROCESS IS IRREVERSIBLE")
                        user_ask = s_t.ta("WRITE THE TOKEN YOU WANT TO DELETE",
                                                      help="WRITE THE SECRET TOKEN TO DELETE").replace(" ","")
                        
                        run_button = s_t.b("DELETE")
                    except:
                        pass
                    try:
                        if run_button:
                            hash_check = hashlib.sha256(user_ask.encode()).hexdigest()
                            user_ask = DB_PROCESS.REACH_DB(str(hash_check),"blockchain.db")
                            if user_ask != None:
                                s_t.md(ST_HTML.RUN_SIMPLE(str(user_ask)),
                                           unsafe_allow_html=True)
                                DB_PROCESS.DELETE_DB(str(hash_check),"blockchain.db")
                                s_t.s("PERMANENTLY DELETED")
                            else:
                                s_t.e("TOKEN IS NOT VALID")
                        else:
                            pass
                    except:
                        pass
            except:
                pass
                

class RUN_ST_ALL():
    def RUNNING_PROCESS():
        MAIN_RUN.ST_SESSION()
        MAIN_RUN.ST_HEAD()
        START_PROCESS.LAUNCHED_FUNCTION()
    
RUN_ST_ALL.RUNNING_PROCESS()

if __name__ == "__main__":
    try:
        RUN_ST_ALL.RUNNING_PROCESS()
    except:
        pass
