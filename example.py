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
                      group.post('<b>%s</b> >_> {how can I help you}? (The current prefix is %s )' % (user, prefix)
              
                if msg.post == '%s reload' % (group.username.lower()):
                  try:
                   imp.reload(conf)
                   imp.reload(coco.internals)
                   imp.reload(cmdUtil)
                   group.post('Reloaded All Saved Modules.')
                  except Exception as e:
                     group.post(str(e))

                if len(prefix)>1:
                 if msg.post.split()[0][:6] == prefix:
                    cmd = msg.post.split()[1][:6].lower()
                    args = msg.post.split()[2][:6]
                    self._callEvent("Command", group, user, msg, cmd, args)
                else:
                 if msg.post[0] == prefix:
                    cmd = msg.post.split()[0][1:].lower()
                    args = msg.post.split()[1:]
                    self._callEvent("Command", group, user, msg, cmd, args)
                    
        def _p_Command(self, group, user, msg, cmd, args):
            cmdUtil.cmd_start().command(group, user, msg, cmd, args)

bot = Bot(conf.groups, conf.name, conf.password)._init()
