import torch
from Data_preprocessing import input_preprocessing_predict
#from datasets import synchronized_data


video_audio_path="./raw_data_video/happy_wrong_without_audio.mp4"


def predict(opt, model):
    model.eval()
    
    #load best state, there are two file pth for separating if the machine hase cuda or not
    if(opt.device=="cuda"):
        best_state = torch.load('%s/%s_best' % (opt.result_path, opt.store_name)+'.pth')
    else:
        best_state = torch.load('%s/%s_best' % (opt.result_path, opt.store_name)+'_cpu_.pth', map_location="cpu")
        
    #Load the weigths on the model
    model.load_state_dict(best_state['state_dict'])
    audio_var, video_var = input_preprocessing_predict.preprocessing_audio_video(video_audio_path,video_norm_value=opt.video_norm_value, batch_size=1)
    
    

    with torch.no_grad():
        output = model(x_audio=audio_var, x_visual=video_var)

    

    print("[LOGITS] Output: ", output)
    
    
    
    