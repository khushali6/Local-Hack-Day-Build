from nltk.chat.util import Chat,reflections

pairs=[
       ['my name is (.*)',['hi %1']],
       ['(hello|hi|hey|holla|hola)',['hi there','hey there','haayy ' ]],
       ['whats your name?',['my name is Chatbot. i am here to help you.' ]],
       ['can (.*) help me?',['sure, i can help you. go ahead!']],
       ['(.*) created you?',['Khushali Pariyal created me']]
]

chat=Chat(pairs,reflections)
chat.converse()