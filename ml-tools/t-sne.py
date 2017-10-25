#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:49:45 2017

@author: xdong
"""

import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from matplotlib import offsetbox



def plot_embedding(X, Y, title=None):
    
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    Y = np.argmax(Y,axis=1)
    plt.figure()
    
    #ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(Y[i]),
                 color=plt.cm.Set1(Y[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
    '''
    if hasattr(offsetbox, 'AnnotationBbox'):
        # only print thumbnails with matplotlib > 1.0
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(digits.data.shape[0]):
            dist = np.sum((X[i] - shown_images) ** 2, 1)
            if np.min(dist) < 4e-3:
                # don't show points that are too close
                continue
            shown_images = np.r_[shown_images, [X[i]]]
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r),
                X[i])
            ax.add_artist(imagebox)
    '''
    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)




def vis_anchor_vector(X, Y):
    '''
    X=[n_samples, sample_dims]
    Y=[n_samples, one_hot_label]
    '''
    tsne = TSNE(n_components=2, init='pca', random_state=0)

    X_tsne = tsne.fit_transform(X)
    plot_embedding(X_tsne, Y,
               "t-SNE embedding of the digits")

    plt.show()
    