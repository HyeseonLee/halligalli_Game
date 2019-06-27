def check_answer(d_open, p_open):
    if d_open[-1]['suit'] == 'joker1' or d_open[-1]['suit'] == 'joker2' or p_open[-1]['suit'] == 'joker1' or p_open[-1]['suit'] == 'joker2':
        return True
    elif d_open[-1]['suit'] == p_open[-1]['suit']:
        if d_open[-1]['rank'] + p_open[-1]['rank'] == 5:
            return True
        else:
            return False
    else:
        if d_open[-1]['rank'] == 5 or p_open[-1]['rank'] == 5:
            return True
        else:
            return False