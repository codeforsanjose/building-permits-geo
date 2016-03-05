import os
from tasks import convert_to_dict

def run_pipeline():
    pipeline = [
        convert_to_dict
    ]
    
    for task in pipeline:
        result = task.run()
        
    print(result)
        
run_pipeline()
