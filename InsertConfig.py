CAN_CHOOSE_REPEAT_CHARACTER = True		#可选重复角色
CAN_CHOOSE_REPEAT_COLOR = True			#可选重复配色
CAN_RECOVER_POWER_IN_BC = True			#BC中可回收能量
EXPEND_MAX_BC = True					#BC条长度随上场人物变化
CAN_STUN_IN_BC = True					#BC中可造成晕值
FIX_PRACTICE_IBOSS_ATK_DEF = True		#修正练习模式BOSS攻防
STORM_COMING_AGAIN = True				#风云再起式回收资源

CHOOSE_REPEAT_CHARACTER = [0xA31FA, 0x31]
CHOOSE_REPEAT_COLOR1 = [0x1ECD6, 0x39, 0xDB, 0x75]
CHOOSE_REPEAT_COLOR2 = [0xA3264, 0xEB]
RECOVER_POWER_IN_BC1 = [0x7FE8A, 0x02, 0x74]
RECOVER_POWER_IN_BC2 = [0x885E9, 0x02, 0x0F, 0x84]
INIT_MAX_BC_LENGTH = [0x86088, 0xDD, 0x05, 0xE8, 0x26, 0x7A, 0x00, 0xD9, 0x98, 0xBC, 0x00, 0x00, 0x00, 0xD9, 0x05, 0x88, 0x37, 0x79, 0x00, 0x8B, 0x35, 0x0C, 0x27, 0x7E, 0x00, 0x33, 0xDB, 0xD9, 0x90, 0xC4, 0x00, 0x00, 0x00, 0x33, 0xC9, 0xD9, 0x98, 0xC0, 0x00, 0x00, 0x00, 0x89, 0x98, 0xD0, 0x00, 0x00, 0x00, 0xD9, 0x05, 0xF4, 0xBB, 0x71, 0x00, 0x88, 0x98, 0xD4, 0x00, 0x00, 0x00, 0xD9, 0x98, 0xCC, 0x00, 0x00, 0x00, 0x3B, 0xF3, 0xD9, 0xEE, 0x0F, 0x9E, 0xC1, 0xD9, 0x90, 0xC8, 0x00, 0x00, 0x00, 0xD9, 0x05, 0x2C, 0x27, 0x7E, 0x00, 0xD9, 0x98, 0xCC, 0x00, 0x00, 0x00, 0xDD, 0x90, 0xDC, 0x00, 0x00, 0x00]
STUN_IN_BC = [0x88227, 0x82]
PRACTICE_BOSS_NORMAL_ATTACK_DEFENSE = [0x89AB0, 0x55, 0x8B, 0xEC, 0x6A, 0xFF, 0x68, 0x4A, 0x23, 0x71, 0x00, 0x64, 0xA1, 0x00, 0x00, 0x00, 0x00, 0x50, 0x83, 0xEC, 0x08, 0x53, 0x56, 0xA1, 0xB0, 0xA8, 0x7D, 0x00, 0x33, 0xC5, 0x50, 0x8D, 0x45, 0xF4, 0x64, 0xA3, 0x00, 0x00, 0x00, 0x00, 0x8B, 0xF1, 0x8B, 0x96, 0x6C, 0x01, 0x00, 0x00, 0xD9, 0xE8, 0x8B, 0x86, 0x68, 0x01, 0x00, 0x00, 0xD9, 0x17, 0x8B, 0x8E, 0x60, 0x01, 0x00, 0x00, 0xD9, 0x5F, 0x04, 0x8B, 0xDA, 0x2B, 0xD8, 0xC1, 0xFB, 0x03, 0x3B, 0xCB, 0x73, 0x0B, 0xD9, 0x04, 0xC8, 0xD9, 0x1F, 0xD9, 0x44, 0xC8, 0x04, 0xEB, 0x0E, 0x3B, 0xC2, 0x74, 0x0D, 0x8B, 0xC2, 0xD9, 0x40, 0xF8, 0xD9, 0x1F, 0xD9, 0x40, 0xFC, 0xD9, 0x5F, 0x04, 0x83, 0xCB, 0xFF, 0xF6, 0x05, 0xCC, 0x1D, 0x83, 0x00, 0x01, 0x75, 0x23, 0x83, 0x0D, 0xCC, 0x1D, 0x83, 0x00, 0x01, 0xC7, 0x45, 0xFC, 0x00, 0x00, 0x00, 0x00, 0xE8, 0xF8, 0x43, 0xFA, 0xFF, 0x68, 0x00, 0x8D, 0x71, 0x00, 0xE8, 0xF5, 0x95, 0x12, 0x00, 0x83, 0xC4, 0x04, 0x89, 0x5D, 0xFC, 0x8B, 0x46, 0x28, 0x83, 0xF8, 0x19, 0x74, 0x18, 0x83, 0xF8, 0x1A, 0x74, 0x13, 0x83, 0xF8, 0x25, 0x74, 0x0E, 0x83, 0xF8, 0x1F, 0x74, 0x09, 0x83, 0xF8, 0x18, 0x0F, 0x85, 0xA8, 0x00, 0x00, 0x00, 0x80, 0xBE, 0xAA, 0x01, 0x00, 0x00, 0x00, 0x0F, 0x84, 0x9B, 0x00, 0x00, 0x00, 0xF6, 0x05, 0x5C, 0x1C, 0x83, 0x00, 0x01, 0xBE, 0x01, 0x00, 0x00, 0x00, 0x75, 0x1E, 0x09, 0x35, 0x5C, 0x1C, 0x83, 0x00, 0x89, 0x75, 0xFC, 0xE8, 0xFF, 0xC2, 0xF7, 0xFF, 0x68, 0x70, 0x8B, 0x71, 0x00, 0xE8, 0x9C, 0x95, 0x12, 0x00, 0x83, 0xC4, 0x04, 0x89, 0x5D, 0xFC, 0x80, 0x3D, 0xD5, 0xA8, 0x7E, 0x00, 0x00, 0x75, 0x66, 0xF6, 0x05, 0xCC, 0x1D, 0x83, 0x00, 0x01, 0x75, 0x22, 0x09, 0x35, 0xCC, 0x1D, 0x83, 0x00, 0xC7, 0x45, 0xFC, 0x02, 0x00, 0x00, 0x00, 0xE8, 0x6B, 0x43, 0xFA, 0xFF, 0x68, 0x00, 0x8D, 0x71, 0x00, 0xE8, 0x68, 0x95, 0x12, 0x00, 0x83, 0xC4, 0x04, 0x89, 0x5D, 0xFC, 0x83, 0x3D, 0xBC, 0x1D, 0x83, 0x00, 0x04, 0x74, 0x1C, 0xE8, 0xDD, 0x42, 0xFA, 0xFF, 0x83, 0xB8, 0x8C, 0x00, 0x00, 0x00, 0x08, 0x74, 0x0E, 0xE8, 0xCF, 0x42, 0xFA, 0xFF, 0x83, 0xB8, 0x8C, 0x00, 0x00, 0x00, 0x15, 0x75, 0x16, 0xD9, 0x07, 0xD8, 0x0D, 0xB0, 0x27, 0x7E, 0x00, 0xD9, 0x1F, 0xD9, 0x47, 0x04, 0xD8, 0x0D, 0xB4, 0x27, 0x7E, 0x00, 0xD9, 0x5F, 0x04, 0xD9, 0xEE, 0xD8, 0x5F, 0x04, 0xDF, 0xE0, 0xF6, 0xC4, 0x01, 0x74, 0x1C, 0xD9, 0x47, 0x04, 0xD9, 0xE8, 0xDE, 0xF1, 0xD9, 0x5D, 0xF0, 0xD9, 0x45, 0xF0, 0xDC, 0x15, 0xB8, 0x22, 0x7A, 0x00, 0xDF, 0xE0, 0xF6, 0xC4, 0x41, 0x75, 0x08, 0xDD, 0xD8, 0xD9, 0x05, 0x88, 0x37, 0x79, 0x00, 0xD9, 0x5D, 0xF0, 0x8B, 0xC7, 0xD9, 0x45, 0xF0, 0xD9, 0x5F, 0x04, 0x8B, 0x4D, 0xF4, 0x64, 0x89, 0x0D, 0x00, 0x00, 0x00, 0x00, 0x59, 0x5E, 0x5B, 0x8B, 0xE5, 0x5D, 0xC3, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC]
DISPLAY_MAX_BC_LENGTH = [0x92FE1, 0xD9, 0x5E, 0x04, 0xD9, 0x46, 0x04]
ADD_POWER_FUNCTION = [0x92FF0, 0x55, 0x8B, 0xEC, 0x80, 0x79, 0x18, 0x00, 0x75, 0x52, 0xD9, 0xEE, 0x80, 0x7C, 0x24, 0x04, 0x4F, 0x74, 0x06, 0x83, 0x7D, 0x08, 0x00, 0x7F, 0x05, 0xD9, 0x45, 0x08, 0xEB, 0x03, 0xD9, 0x41, 0x08, 0xD8, 0xD1, 0xDF, 0xE0, 0xF6, 0xC4, 0x41, 0x7B, 0x06, 0x83, 0x79, 0x14, 0x00, 0x75, 0x30, 0xD8, 0x41, 0x0C, 0xD9, 0xC9, 0xD8, 0xD1, 0xDF, 0xE0, 0xF6, 0xC4, 0x41, 0x75, 0x04, 0xDD, 0xD9, 0xEB, 0x02, 0xDD, 0xD8, 0xD9, 0x41, 0x08, 0xD9, 0xC9, 0xD8, 0xD1, 0xDF, 0xE0, 0xDD, 0xD9, 0xF6, 0xC4, 0x41, 0x75, 0x05, 0xDD, 0xD8, 0xD9, 0x41, 0x08, 0xD9, 0x59, 0x0C, 0x5D, 0xC2, 0x04, 0x00, 0xDE, 0xD9, 0x5D, 0xC2, 0x04, 0x00, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC,]
ADD_BC_FUNCTION = [0x931E0, 0x55, 0x8B, 0xEC, 0xDD, 0x05, 0xB8, 0x22, 0x7A, 0x00, 0xD9, 0x44, 0x24, 0x08, 0xD8, 0xD1, 0xDF, 0xE0, 0xF6, 0xC4, 0x41, 0x74, 0x04, 0xDD, 0xD8, 0xD9, 0xC0, 0xD9, 0x01, 0xDB, 0x41, 0x04, 0xD8, 0xCB, 0xD8, 0xC1, 0xDD, 0xD9, 0xD8, 0xC1, 0xDB, 0x41, 0x08, 0xD8, 0xCB, 0xD8, 0xC3, 0xD8, 0xD1, 0xDF, 0xE0, 0xF6, 0xC4, 0x41, 0x74, 0x0A, 0x8B, 0x41, 0x08, 0x89, 0x41, 0x04, 0xDE, 0xD9, 0xEB, 0x09, 0xDD, 0xD8, 0xD8, 0xE2, 0xD8, 0xF2, 0xDB, 0x59, 0x04, 0xDD, 0xD8, 0xD9, 0x19, 0x5D, 0xC2, 0x04, 0x00, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC]