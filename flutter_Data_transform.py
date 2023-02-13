import json
import os
# --------------define_file_path---------------#
output_path = r'C:\Users\USER\Desktop\2s-agcn-flutter-python-server\data\kinetics_raw' #kinetics data files link
# --------------define_data---------------#
writefile = "data_test"
label = "data"
label_index = 1
boolen = True
# ----------------------------------------#


def create_output_file(data):
    # --------------kinetics data------------------#
    data_Dict = {
        "data":[],
        "label": f"{label}",
        "label_index": label_index,
    }
    # --------------add data to Dict---------------#
    index=0
    frame=len(data)/54
    while(index < frame):#request all files data
        skeleton_data={
            "frame_index": index+1, "skeleton": [{"pose": take_skeleton(index,data)[0], "score": take_skeleton(index,data)[1]}]
        }
        data_Dict["data"].append(skeleton_data)
        index +=1
    # --------------output_json file---------------#
    with open(output_path+f"\kinetics_data\{writefile}.json", "w+") as w:
        json.dump(data_Dict, w)
    w.close()
    return "success output data file"

def take_skeleton(data_index,data):
    data_array = []
    pose = []
    score = []
    index = 0
    data_frame_index=data_index*54

    for i in range(data_frame_index,data_frame_index+54):#coco format (18(joints)*2(x,y)+18(score))
        print(i)
        print("------------------------")
        data_array.append(float(data[i]))
        print(data_array)
        #take data from pose_keypoints_2d
    while index != 54:
        pose.append(data_array[index])     # pose x
        pose.append(data_array[index + 1]) # pose y
        score.append(data_array[index + 2])# score
        index += 3
    return pose,score

