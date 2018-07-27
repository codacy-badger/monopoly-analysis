def announce(text):
    """
    This function is used to format the program.
    It requires the DEBUG = True on global configuration file.

    Parameter:
        text: (String) the text that will be shown.
    """
    try:
        text = str(text)
        text = "Service: %s" %(text)
        print(text)
    except Exception:
        return
    return


def user_prompt(player, prompt_type = None):

    if type(prompt_type) != type("String"):
        return

    if prompt_type == 'turn':
        action_prompt()

    if prompt_type == 'confirm':
        confirm_prompt()

    def action_prompt(player):
        print("{} > Please choose action(s)".format(player))
        print("{}\t{}\t{}]\t{}".format(
            '[buy] Buy Property at full',
            '[auction] Auction Property',
            '[trade] Trade money or Property',
            '[done] Finished your turn'))
        pass

    def confirm_prompt():
        pass

    pass
