from telegram.ext.filters import BaseFilter

class UserJoinedGroupFilter(BaseFilter):
	def filter(self, message):
		if len(message.new_chat_members)!=0:
			return True
		return False
