import time
import coco.internals

lib = coco.internals

class cmd_start:
        def commands(self, bot, group, user, msg, cmd, args):
                self = bot()
                say = group.post
                commands = ["cmds", "say"]

                if cmd == 'cmds':
                   cm = list()
                   for x in commands:
                       if x.title() not in cm:
                          cm.append(x.title())
                   say("%s you have <b>'%s'</b> available commands: <b>%s</b>." % (user, len(commands), ", ".join(cm)))
                
                if cmd == 'say':
                   if(len(args)) < 1:
                      say("I can't say nothing -_-\"")
                   else:
                        say(args)
