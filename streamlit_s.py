import streamlit as st

class DEFINE_ST_PARAMETERS():
    def ST_API():
        api_all = type("STREAMLIT",
                       (),
                       {"tt":st.title,
                        "hd":st.header,
                        "md":st.markdown,
                        "sh":st.subheader,
                        "cl":st.columns,
                        "wt":st.write,
                        "tx":st.text,
                        "ta":st.text_area,
                        "sdb":st.sidebar,
                        "j":st.json,
                        "cp":st.caption,
                        "ms":st.multiselect,
                        "sb":st.selectbox,
                        "r":st.radio,
                        "b":st.button,
                        "c":st.code,
                        "cb":st.checkbox,
                        "i":st.info,
                        "w":st.warning,
                        "e":st.error,
                        "s":st.success})
        return api_all
    def ST_CONFIGURATION():
        configuration_st = type("CONFIGURATION",
                                (),
                                {"panel_name":"BLOCKCHAIN KNOWLEDGE PROTECTION",
                                 "layout_type":"centered",
                                 "sitebar_type":"expanded",
                                 "page_name":"IIPV"})
        return configuration_st
    def ST_CONF_DEFINE():
        st_cf = DEFINE_ST_PARAMETERS.ST_CONFIGURATION()
        st.set_page_config(st_cf.panel_name,
                           layout=st_cf.layout_type,
                           initial_sidebar_state=st_cf.sitebar_type,
                           page_icon=st_cf.page_name)
        
        
        
        
        
        
        
        
        
        
        
        
        