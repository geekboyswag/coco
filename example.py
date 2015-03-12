import coco.internals
import conf
import cmdUtil

class Bot(coco.internals.Manager):
	def _p_ok(self, group):
		group.setNameColor("ff0")
		group.setFontColor("3bf")
		print("Successfully connected to %s" % (group.name))
		
	def _init(self):
		self.run()

	def _on_Message(self, group, user, msg):
		post = msg.post
		ret = "%s: %s: %s" % (group.name, user, post)
		print(ret)
		
		prefix = conf.prefix
		if user == group.username: return              
	
                if msg.post == group.username:
                      group.post('<b>%s</b> >_> {how can I help you}? (The current prefix is %s )' % (user, prefix))
                
                reload_command = '%s reload' % (group.username.lower())
                if msg.post == reload_command:
                  try:
                   imp.reload(conf)
                   imp.reload(coco.internals)
                   imp.reload(cmdUtil)
                   group.post('Reloaded All Modules.')
                  except Exception as e:
                     group.post(str(e))

                if len(prefix)>1:  
                 if post.split()[0][:6] == prefix:
                    cmd = post.split()[1][:6].lower()
                    args = post.split()[2][:6] #### need to fix -.-
                    bot = self
                    self._callEvent("Command", bot, group, user, msg, cmd, args)
                else:
                 if post[0] == prefix:
                    bot = self
                    data = post[1:].split(" ", 1)
                    if len(data) > 1:
			cmd, args = data[0], data[1]
		    else:
			cmd, args = data[0], ""
                    self._callEvent("Command", bot, group, user, msg, cmd, args)
                    
        def _p_Command(self, bot, group, user, msg, cmd, args):
            cmdUtil.cmd_start().command(bot, group, user, msg, cmd, args)

bot = Bot(conf.groups, conf.name, conf.password)._init()
