#!/usr/bin/env python
'''Validates a converted ImageNet model against the ILSVRC12 validation set.'''

import argparse
import numpy as np
import tensorflow as tf
import os.path as osp

import models
import dataset
import os
def save_batch(batch_output, name, ith_batch, dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    real_name = dir_name+'/'+name+'-'+str(ith_batch)
    np.save(real_name, batch_output)
    return 0

# note that this function is used to get data-information for specific network.
# you can also change parameters in 'data_spec' manually

def get_spec():
    net = load_model('AlexNet')
    if net is None:
        exit(-1)
    # Load the dataset
    data_spec = models.get_data_spec(model_instance=net)
    return data_spec
    
# Arguements:
#val_path: the advantage of this dataset provider is that if want to select a part of the whole
#          dataset or you have a dataset which is not named normally like ImageNet, you can generate 
#          your own your_dateset.txt reading:
#          file_path    label
#          n01440764/n01440764_10026.JPEG 0
#when you have a new dataset, you don't have to modify codes of this dataset_provider. The only thing
#you need to do is that generate your own your_dateset.txt 

image_producer = dataset.ImageNetProducer(val_path='./train.txt',
                                          data_path='/home/simon/imagenet-data/raw-data/train',
                                          data_spec=get_spec())

# Evaluate its performance on the ILSVRC12 validation set
total = len(image_producer)

# Start a session
sesh = tf.Session()
coordinator = tf.train.Coordinator()
sesh.run(init)
threads = image_producer.start(session=sesh, coordinator=coordinator)
# Iterate over and classify mini-batches
for (labels, images) in image_producer.batches(sesh):
    sesh.run(your_train, feed_dict={
    	x: images,
    	y: labels
    	})
# Stop the worker threads
coordinator.request_stop()
coordinator.join(threads, stop_grace_period_secs=2)
    

