# coding=utf-8
import argparse
import textwrap
import time
import os, sys
sys.path.append(os.path.dirname(__file__))
from utils.config import process_config, check_config_dict
from utils.logger import ExampleLogger
from trainers.example_model import ExampleModel
from trainers.example_trainer import ExampleTrainer
from data_loader.dataset import get_data_loader
import argparse


config = process_config(os.path.join(os.path.dirname(__file__), 'configs', 'config.json'))

class ImageClassificationPytorch:
    def __init__(self, config):
        gpu_id = config['gpu_id']
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = gpu_id
        # check_config_dict(config)
        self.config = config
        self.time = now
 
        self.init()


    def init(self):
        # create net 
        self.model = ExampleModel(self.config)
        # load
        self.model.load()
        
        # create your data generator
        self.test_loader = get_data_loader(self.config)
        
        # create logger
        self.logger = ExampleLogger(self.config)

        # create trainer and path all previous components to it
        self.trainer = ExampleTrainer(self.model, self.test_loader , self.config, self.logger)
     

    def run(self):
        # here you test your model
        self.trainer.test()

    # def close(self):
    #     # close
    #     self.logger.close()


def main(now):
    config = process_config(os.path.join("/image_classification_pytorch/submission", 'configs', 'config.json'))
    imageClassificationPytorch = ImageClassificationPytorch(config)
    imageClassificationPytorch.run()
    # imageClassificationPytorch.close()


if __name__ == '__main__':

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--config', type=str)
    # parser.add_argument('--suffix', type=str)
    # args = parser.parse_args()
    

    now = time.strftime('%Y-%m-%d | %H:%M:%S', time.localtime(time.time()))

    print('----------------------------------------------------------------------')
    print('Time: ' + now)
    print('----------------------------------------------------------------------')
    print('                    Now start ...')
    print('----------------------------------------------------------------------')




    main(now)

    print('----------------------------------------------------------------------')
    print('                      All Done!')
    print('----------------------------------------------------------------------')
    print('Start time: ' + now)
    print('Now time: ' + time.strftime('%Y-%m-%d | %H:%M:%S', time.localtime(time.time())))
    print('----------------------------------------------------------------------')

