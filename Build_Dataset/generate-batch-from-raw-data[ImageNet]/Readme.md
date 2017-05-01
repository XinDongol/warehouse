# A Parallel Batch Provider

  This batch-provider can be easily deployed for different dataset. The only thing users have to do is to generate 'yourdataset.txt' and feed it to the provider. Format of .txt file is like 'val.txt' in this dir.

Please note that this provider was implemented on Tensorflow r1.0.
If you come up with any problem on other verison of Tensorflow, please check function of **`process()`** in `dataset.py`. Note that if fucntion of `process` does not work well, `processed_queue` will be closed accidentally.

  Simon X Dong
  simonxdong@gmail.com
