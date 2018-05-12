
if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]
                                    contact = cl.getContact(sender)
                                    sendMessageWithMention(to, contact.mid)
                                    cl.sendMessage(to, "安安你好,我是防翻機器人Yukino,有事請找主人")
                                    time.sleep(0.5)
                                    cl.sendContact(op.param1, "u85ee80cfb293599510d0c17ab25a5c98")
                                break
