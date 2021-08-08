import os, sys, time, discord

def help_cmd(msg):
    help_list = ""
    help_list += "     Wocky TermUIX Bot\n"
    help_list += "____________________________\n"
    help_list += "► img2txt\n"
    help_list += "  ╚► img2txt <URL>\n"
    help_list += "► gif2txt\n"
    help_list += "  ╚► gif2txt <URL>\n"
    help_list += "► gradient\n"
    help_list += "  ╚► grandient <color1> <color2> <text>\n"
    help_list += "► gradient-fade (symbols not supported!)\n"
    help_list += "  ╚► gradient-fade <color1> <color2> <text>\n"
    help_list += "► Table Generator\n"
    help_list += "  ╚► table help"
    return help_list