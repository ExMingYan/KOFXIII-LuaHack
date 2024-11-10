#/usr/bin/env python3

from InsertConfig import *

def WriteBytes(AddrValue:list)->None:
	with open('kofxiii.exe', 'r+b') as wf:
		wf.seek(AddrValue[0], 0)
		wf.write(bytes(AddrValue[1:]))

if __name__ == "__main__":
	if CAN_CHOOSE_REPEAT_CHARACTER:
		WriteBytes(CHOOSE_REPEAT_CHARACTER)
	if CAN_CHOOSE_REPEAT_COLOR:
		WriteBytes(CHOOSE_REPEAT_COLOR1)
		WriteBytes(CHOOSE_REPEAT_COLOR2)
	if CAN_RECOVER_POWER_IN_BC:
		WriteBytes(RECOVER_POWER_IN_BC1)
		WriteBytes(RECOVER_POWER_IN_BC2)
	if EXPEND_MAX_BC:
		WriteBytes(INIT_MAX_BC_LENGTH)
		WriteBytes(DISPLAY_MAX_BC_LENGTH)
	if CAN_STUN_IN_BC:
		WriteBytes(STUN_IN_BC)
	if FIX_PRACTICE_IBOSS_ATK_DEF:
		WriteBytes(PRACTICE_BOSS_NORMAL_ATTACK_DEFENSE)
	if STORM_COMING_AGAIN:
		WriteBytes(ADD_POWER_FUNCTION)
		WriteBytes(ADD_BC_FUNCTION)
