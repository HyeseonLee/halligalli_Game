from show_two_cards import *

def print_board(rd_keep, rp_keep, d_keep, p_keep,username):
    dealer="딜러"
    deal_dkeep_num=len(d_keep)
    myname=username
    my_pkeep_num=len(p_keep)

    print("   ")
    print("┏==============================================================┓")
    print("                                                   ")
    print("      【  " + dealer + "  】", "                            【  " + myname + "  】")
    print("      카드 수:", deal_dkeep_num, "장", "                         카드 수:", my_pkeep_num, "장")
    print("                                                   ")
    show_two_cards(rd_keep, rp_keep)
    print("                                                   ")
    print("                                                   ")
    print("┗==============================================================┛")