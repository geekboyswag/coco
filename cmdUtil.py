import time
import coco.internals

lib = coco.internals

class cmd_start():
        def command(self, group, user, msg, cmd, args):
                say = group.post
                commands = ["cmds", "say"]

                if cmd == 'cmds':
                   cm = list()
                   if Access().get(user)>1:
                      for x in commands:
                          if x.title() not in cm:
                            cm.append(x.title())
                      say("%s you have <b>'%s'</b> available commands: <b>%s</b>." % (user, len(commands), ", ".join(cm)))
                
                if cmd == 'say':
                   b = ' '.join(args)
                   if(len(b)) < 1:
                      say("I can't say nothing -_-\"")
	           else:
	           	say(b)
