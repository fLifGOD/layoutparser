from label_studio_ml.model import LabelStudioMLBase
import layoutparser as lp
from PIL import Image
import numpy as np

class DocumentLayout(LabelStudioMLBase):
    def __init__(self, **kwargs):


#         super(DocumentLayout, self).__init__(**kwargs)
        from_name, schema = list(self.parsed_label_config.items())[0]
        self.from_name = from_name
        self.to_name = schema['to_name'][0]
        self.labels = schema['labels']
        
        custom_label_map = {0: "column",1:"details",2:"heading" ,3:"image",4:"para"}
#         self.model = lp.Detectron2LayoutModel("/content/drive/MyDrive/lp_model_24_04/lp_model_24_04/config.yaml",
#                                   "/content/drive/MyDrive/lp_model_24_04/lp_model_24_04/model_final 24_04.pth",
#                                   extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.60],
#                                 label_map=custom_label_map)
        # self.model = ImageClassifier(resources['num_classes'])
        # self.model.load(resources['model_path'])
        # self.labels = resources['labels']
        
    def predict(self, tasks, **kwargs):
        img = Image.open(img_path).convert("RGB")
        layout = model.detect(np.array(img))
        predictions = []
        for task in tasks:
            print(task)
        #     predictions.append({
        #         'score': 0.987,  # prediction overall score, visible in the data manager columns
        #         'model_version': 'delorean-20151021',  # all predictions will be differentiated by model version
        #         'result': [{
        #             'from_name': self.from_name,
        #             'to_name': self.to_name,
        #             'type': 'choices',
        #             # 'score': 0.5,  # per-region score, visible in the editor 
        #             'value': {
        #                 'choices': [self.labels[0]]
        #             }
        #         }]
        #     })
        # return predictions
        

        


    def fit(self, completions, **kwargs):
        pass
