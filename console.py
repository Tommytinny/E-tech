#!/usr/bin/python3


import cmd

class StudenPortal(cmd.Cmd):
    """ implementation of Student Portal class """
    prompt = "(Student portal) "

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        """ when you enter an empty line """
        pass

    def tokenize_arg(self, arg):
        """ tokenize argument string """
        try: 
            return shlex.split(arg)
        except ValueError as e:
            print(f"Argument parsing error: {e}")
            return []

    def do_create(self, arg):
        """ Create a new instance of BaseModel"""
        args = self.tokenize(arg)



if __name__ == '__main__':
    StudentPortal().cmdloop()
