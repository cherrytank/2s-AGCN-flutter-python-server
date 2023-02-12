# 2s-AGCN
Two-Stream Adaptive Graph Convolutional Networks for Skeleton-Based Action Recognition in CVPR19

# Data Preparation

        -data\  
          -kinetics_raw\  
            -kinetics_train\
              ...
            -kinetics_val\
              ...
            -kinetics_train_label.json
            -keintics_val_label.json
          -nturgbd_raw\  
            -nturgb+d_skeletons\
              ...
            -samples_with_missing_skeletons.txt
            


 - Preprocess the data with
  
    
    `python data_gen/kinetics_gendata.py`

 - Generate the bone data with: 
    
    `python data_gen/gen_bone_data.py`
     
# Training & Testing

Change the config file depending on what you want.


    `python main.py --config ./config/kinetics/train_joint.yaml`

    `python main.py --config ./config/kinetics/train_bone.yaml`
To ensemble the results of joints and bones, run test firstly to generate the scores of the softmax layer. 

    `python main.py --config ./config/kinetics/test_joint.yaml`

    `python main.py --config ./config/kinetics/test_bone.yaml`

Then combine the generated scores with: 

    `python ensemble.py --datasets kinetics`
     
# Citation
Please cite the following paper if you use this repository in your reseach.

    @inproceedings{2sagcn2019cvpr,  
          title     = {Two-Stream Adaptive Graph Convolutional Networks for Skeleton-Based Action Recognition},  
          author    = {Lei Shi and Yifan Zhang and Jian Cheng and Hanqing Lu},  
          booktitle = {CVPR},  
          year      = {2019},  
    }
    
    @article{shi_skeleton-based_2019,
        title = {Skeleton-{Based} {Action} {Recognition} with {Multi}-{Stream} {Adaptive} {Graph} {Convolutional} {Networks}},
        journal = {arXiv:1912.06971 [cs]},
        author = {Shi, Lei and Zhang, Yifan and Cheng, Jian and LU, Hanqing},
        month = dec,
        year = {2019},
	}
