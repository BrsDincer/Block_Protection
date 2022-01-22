class ST_HTML():
    def CREATOR_ART():
        return """
                  .----.
      .---------. | == |  --> BLOCKCHAIN KNOWLEDGE PROTECTION
      |.-     -.| |1111|  --> KNOWLEDGE SHOULD BE PUBLIC AND ACCESSIBLE
      ||       || | == |  --> IIPV
      ||       || |0000|  
      |'-.....-'| |::::|
      `"")---(""` |___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\
        
        """
    def RUN_HEAD(head_str=str):
        return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta name="viewport" content="width=device-width">
    <style>
    h1 {
    background-color: white;
    text-align: center;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    color: #005073;
    font-size: 22px;
    }
    </style>
    <title>IIPV</title>
    </head>
    <body>
    <h1>%s</h1>
    <p style="text-align: center; font-size:13px; color:#00B7FF; background-color: black">CREATED FOR OPEN-KNOWLEDGE PROTECTION</p>
    </body>
    </html>""" % (head_str)
    
    def RUN_TXT(body_str=str,body_block=str,user_id=str):
        return """
    <style>
    .gen {
    background-color: black;
    font-size: 12px;
    color: white;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    font-weight: bold;
    }
    </style>
    <body>
    <p style="color:#00B7FF; background-color: black; font-size: 12px; padding: 12px 12px 12px">PUBLIC CHAIN --> %s </p>
    <p class="gen">KNOWLEDGE: %s </p>
    <p class="gen">USER: #%s </p>
    </body>""" % (body_block,body_str,user_id)
    
    def RUN_SIMPLE(body_str=str):
        return """
    <style>
    .genfirst {
    background-color: black;
    font-size: 13px;
    color: white;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    font-weight: bold;
    }
    </style>
    <body>
    <p class="genfirst">KNOWLEDGE: %s </p>
    </body>""" % (body_str)
    
    def RUN_CONNECTED(body_str=str):
        return """
    <style>
    .gensecond {
    background-color: black;
    font-size: 13px;
    color: #FFF700;
    padding: 12px 12px 12px;
    letter-spacing: 0.3px;
    }
    </style>
    <body>
    <p class="gensecond">PRE BLOCK --> %s </p>
    </body>""" % (body_str)