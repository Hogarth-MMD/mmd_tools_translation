# License: Don't worry, it's a free gift to the world. 
# This Blender python script is for the purpose of mass renaming bones from MikuMikDance Japanese bone names to DAZ/Poser bone names. The armature animation with renamed bones can then be exported as a VMD animation using the mmd_tools Blender add-on (powroupi fork). Run this script from the Blender text editor. The armature object of the imported DAZ BVH animation must be the active object.


DAZ_bvh_bones_dict = {0: 'hip', 1: 'abdomen', 2: 'chest', 3: 'neck', 4: 'head', 5: 'leftEye', 6: 'rightEye', 7: 'rCollar', 8: 'rShldr', 9: 'rForeArm', 10: 'rHand', 11: 'rThumb1', 12: 'rThumb2', 13: 'rIndex1', 14: 'rIndex2', 15: 'rMid1', 16: 'rMid2', 17: 'rRing1', 18: 'rRing2', 19: 'rPinky1', 20: 'rPinky2', 21: 'lCollar', 22: 'lShldr', 23: 'lForeArm', 24: 'lHand', 25: 'lThumb1', 26: 'lThumb2', 27: 'lIndex1', 28: 'lIndex2', 29: 'lMid1', 30: 'lMid2', 31: 'lRing1', 32: 'lRing2', 33: 'lPinky1', 34: 'lPinky2', 35: 'rButtock', 36: 'rThigh', 37: 'rShin', 38: 'rFoot', 39: 'lButtock', 40: 'lThigh', 41: 'lShin', 42: 'lFoot', 43: 'root', 44: 'lower body', 45: "leg IK_L", 46: "leg IK_R", 47: "toe IK_L", 48: "toe IK_R", 49: "lToe", 50: "rToe"}

DAZ_bvh_MMD_bones_English = {0: 'center', 1: 'upper body', 2: 'upper body 2', 3: 'neck', 4: 'head', 5: 'eye_L', 6: 'eye_R', 7: 'shoulder_R', 8: 'arm_R', 9: 'elbow_R', 10: 'wrist_R', 11: 'thumb1_R', 12: 'thumb2_R', 13: 'fore2_R', 14: 'fore3_R', 15: 'middle2_R', 16: 'middle3_R', 17: 'third2_R', 18: 'third3_R', 19: 'little2_R', 20: 'little3_R', 21: 'shoulder_L', 22: 'arm_L', 23: 'elbow_L', 24: 'wrist_L', 25: 'thumb1_L', 26: 'thumb2_L', 27: 'fore2_L', 28: 'fore3_L', 29: 'middle2_L', 30: 'middle3_L', 31: 'third2_L', 32: 'third3_L', 33: 'little2_L', 34: 'little3_L', 35: 'rButtock', 36: 'leg_R', 37: 'knee_R', 38: 'ankle_R', 39: 'lButtock', 40: 'leg_L', 41: 'knee_L', 42: 'ankle_L', 43: 'root', 44: 'lower body', 45: "leg IK_L", 46: "leg IK_R", 47: "toe IK_L", 48: "toe IK_R", 49: "toe_L", 50: "toe_R"}

DAZ_bvh_MMD_bones_Japanese = {0: 'センター', 1: '上半身', 2: '上半身2', 3: '首', 4: '頭', 5: '左目', 6: '右目', 7: '右肩', 8: '右腕', 9: '右ひじ', 10: '右手首', 11: '右親指１', 12: '右親指２', 13: '右人指２', 14: '右人指３', 15: '右中指２', 16: '右中指３', 17: '右薬指２', 18: '右薬指３', 19: '右小指２', 20: '右小指３', 21: '左肩', 22: '左腕', 23: '左ひじ', 24: '左手首', 25: '左親指１', 26: '左親指２', 27: '左人指２', 28: '左人指３', 29: '左中指２', 30: '左中指３', 31: '左薬指２', 32: '左薬指３', 33: '左小指２', 34: '左小指３', 35: 'rButtock', 36: '右足', 37: '右ひざ', 38: '右足首', 39: 'lButtock', 40: '左足', 41: '左ひざ', 42: '左足首', 43: '全ての親', 44: '下半身', 45: "左足ＩＫ", 46: "右足ＩＫ", 47: "左つま先ＩＫ", 48: "右つま先ＩＫ", 49: "左つま先", 50: "右つま先"}

original_bone_names = DAZ_bvh_MMD_bones_Japanese
renamed_bones_names = DAZ_bvh_bones_dict

import bpy

#use international fonts and display the names of the bones
def use_international_fonts_display_names_bones():
	bpy.context.user_preferences.system.use_international_fonts = True
	bpy.context.object.data.show_names = True


#rename all bones from DAZ DAZ bone names to MMD Japanese bone names
def rename_bones():
	bpy.ops.object.mode_set(mode='OBJECT')
	for i in original_bone_names.keys():
		if original_bone_names[i] in bpy.context.active_object.data.bones.keys():
			bpy.context.active_object.data.bones[original_bone_names[i]].name = renamed_bones_names[i]

use_international_fonts_display_names_bones()
rename_bones()
bpy.ops.object.mode_set(mode='POSE')
bpy.ops.pose.select_all(action='SELECT')

