import vk, random, time
token = 'YOUR TOKEN HERE'
session = vk.Session(token)
vk_api = vk.API(session)
print('ok')
def info(user_id):
    user = vk_api.users.get(user_ids=user_id,v='5.74')
    return user
delete_people = []
delete_chat = []
delete_group = []
people_info = []
def delete_g(group):
    i = 0
    print(len(group))
    while i < len(group)-1:
        try:
            vk_api.messages.deleteConversation(peer_id = '-'+group[i],v = '5.86')
        except:
            i - 1
        i += 1
def delete_per_chat(chat):
    i = 0
    print(len(chat))
    while i < len(chat) - 1:
        try:
            vk_api.messages.deleteConversation(peer_id= chat[i], v='5.86')
        except:
            i - 1
        i += 1
l = 0
conversations = vk_api.messages.getConversations(count=200, v='5.85')
print(conversations)
for s in range(300):
    print(s)
    try:
        conversations = vk_api.messages.getConversations(count=200, v='5.85')
    except:
        time.sleep(1)
        s-= 1
        continue
    delete_people = []
    delete_chat = []
    delete_group = []
    print(conversations)
    for conv in conversations['items']:
        if conv['conversation']['peer']['type'] == 'user':
            delete_people.append(conv['conversation']['peer']['id'])
            #people_info.append(info(conv['conversation']['peer']['id']))
        if conv['conversation']['peer']['type'] == 'chat':
            delete_chat.append(conv['conversation']['peer']['id'])
        if conv['conversation']['peer']['type'] == 'group':
            delete_group.append(conv['conversation']['peer']['id'])
    delete_g(delete_group)
    delete_per_chat(delete_people)
    delete_per_chat(delete_chat)
    l += 200
