import logging
import telegram
import consts as cv

logger = logging.getLogger(__name__)

class NewUserJoinHandler:
    def __init__(self, bot, update):
        self.bot = bot
        self.update = update
        self.new_chat_members = update.message.new_chat_members
        self.chat_id = update.message.chat_id
        self.run()
    def run(self):
        for new_chat_member in self.new_chat_members:
            new_users_name = new_chat_member.first_name if new_chat_member.first_name else ''
            new_users_name += new_chat_member.last_name if new_chat_member.last_name else ''
            new_users_name = new_users_name.replace(' ', '')
            if cv.NOT_ALLOWED in new_users_name:
                bot.delete_message(self.chat.id,self.update.message.message_id)
                self.bot.restrict_chat_member(chat_id=self.chat_id, user_id=new_chat_member.id,
                        can_send_messages=False,
                        can_send_media_messages=False,
                        can_send_other_messages=False,
                        can_add_web_page_previews=False)
                except telegram.error.BadRequest:
                    self.bot.send_message(self.update.message.chat_id,
                        'But I am not an admin :/')
