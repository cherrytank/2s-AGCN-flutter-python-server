import json
import os
# --------------define_file_path---------------#
input_path  = r'C:\Users\USER\Desktop\output_jsons'  # data files from openpose
output_path = r'C:\Users\USER\Desktop\data\kinetics_raw' #kinetics data files link
# --------------define_data---------------#
writefile = "testfile02"
label = "foot_up"
label_index = 1
boolen = True

def create_output_file():
    # --------------kinetics data------------------#
    data_Dict = {
        "data":[],
        "label": f"{label}",
        "label_index": label_index,
    }
    # --------------add data to Dict---------------#
    index=0
    while(take_skeleton(index)!= False):#request all files data
        skeleton_data={
            "frame_index": index+1, "skeleton": [{"pose": take_skeleton(index)[0], "score": take_skeleton(index)[1]}]
        }
        data_Dict["data"].append(skeleton_data)
        index +=1
    # --------------output_json file---------------#
    with open(output_path+f"\kinetics_train\{writefile}.json", "w+") as w:
        json.dump(data_Dict, w)
    w.close()

def take_skeleton(fileindex):
    files = os.listdir(input_path) #create array load all files
    if(fileindex>(len(files)-1)):  #check request not over quantity
        return False
    data_array = []
    pose = []
    score = []
    index = 0
    # --------------open file and take data---------------#
    with open(input_path + f"\{files[fileindex]}", 'r') as l:
        json_array = json.load(l) #load json data
    for i in range(54):  #coco format (18(joints)*2(x,y)+18(score))
        data_array.append(float(json_array["people"][0]["pose_keypoints_2d"][i]))
        #take data from pose_keypoints_2d
    while index != 54:
        pose.append(data_array[index])     # pose x
        pose.append(data_array[index + 1]) # pose y
        score.append(data_array[index + 2])# score
        index += 3
    return pose,score

def add_label():
    label_Dict = {
        f"---{writefile}": {
            "has_skeleton": boolen,
            "label": label,
            "label_index": label_index
        },
    }
    # --------------update file---------------#
    with open(output_path + f"\kinetics_train_label.json", "r") as w:
        label_array = json.load(w)
        label_array.update(label_Dict)
    with open(output_path + f"\kinetics_train_label.json", "w") as w:
        json.dump(label_array,w,indent=4)
    w.close()

if __name__ == '__main__':
    create_output_file()
    print("Transform complete")
    add_label()
    print("add label complete")
