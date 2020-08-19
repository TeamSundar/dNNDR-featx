#!E:\Projects\202004_MultiLabelClass python
# -*- coding: utf-8 -*-

# Import essential libraries
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error 
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from keras.utils import plot_model
import keras
from tqdm import tqdm
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

class process_mlc:
    def __init__(self):
        pass
    
    # Prepare protein descriptors
    def prep(self, type, protein):
        x=pd.read_csv('data/fset_' + protein + '_'+ type +'.csv')
        x=x.drop(['Unnamed: 0'], axis=1)
        try:
            x=x.drop(['Descriptor calculation failed.'], axis=1)
        except:
            pass
        x.index=x['#'].values
        x=x.drop(['#'], axis=1)
        try:
            x= x.drop(['hsa:390956', 'hsa:94009'])
            print("Empty Dropped for: ", type)
        except:
            print("Nothing Dropped for: ", type) 
        return x

    def build_model(self, features, test):
        model = Sequential()

        # The Input Layer :
        model.add(Dense(512, kernel_initializer='normal',input_dim = features.shape[1], activation='relu'))
        model.add(Dropout(0.5))

        # The Hidden Layers :
        model.add(Dense(512, kernel_initializer='normal',activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(256, kernel_initializer='normal',activation='relu'))
        model.add(Dense(256, kernel_initializer='normal',activation='relu'))
        model.add(Dense(256, kernel_initializer='normal',activation='relu'))
        model.add(Dense(128, kernel_initializer='normal',activation='relu'))
        model.add(Dense(128, kernel_initializer='normal',activation='relu'))
        model.add(Dropout(0.5))

        # The Output Layer :
        model.add(Dense(5, kernel_initializer='normal',activation='linear'))

        # Compile the network :
        model.compile(loss='mse', optimizer=keras.optimizers.RMSprop(lr=1e-3), metrics=['mae', 'mse'])

        # Write model summary to file
        with open('logs/models/summary' + str(test) + '.txt','w') as fh:
            # Pass the file handle in as a lambda function to make it callable
            model.summary(print_fn=lambda x: fh.write(x + '\n'))
        return model

    #Calculate r2
    def r2(self,y,x):
        score=[]
        for i in range(0,y.shape[1]):
            correlation_matrix = np.corrcoef(y[:,i],x[:,1])
            correlation_xy = correlation_matrix[0,1]
            r_squared = correlation_xy**2
            score=np.append(score, r_squared)
        return score

    #Replace x with the choice of protein feature set
    def mean(self, feat, y, ref):
        stdev_all=np.empty((0,y.shape[1]), float)
        mean_all=np.empty((0,y.shape[1]), float)

        for row in tqdm(feat.index.values):
            sum= np.empty((0,y.shape[1]), float)
            for i in range(len(ref)):      
                if row==ref[0][i]:
                    drug=y.loc['drug/'+ref[1][i]+'.mol', :]
                    sum=np.append(sum, [drug.values], axis=0)

            # Calculate stdev for all the drugs for a single ptotein
            stdev = np.std(sum, axis = 0)
            # Calculate mean of all drugs for a single protein
            mean = np.mean(sum, axis=0)

            stdev_all=np.append(stdev_all, [stdev], axis=0)
            mean_all = np.append(mean_all, [mean], axis=0)
        return mean_all, stdev_all
    
    def boxdict(self, train, test):
        box_data = {}
        #box_data['MolLogP'] = {}
        box_data['NOCount'] = {}
        box_data['NHOHCount'] = {}
        box_data['MolWt'] = {}
        box_data['NumRotatableBonds'] = {}
        box_data['TPSA'] = {}

        for key, value in box_data.items():
            # if key == 'MolLogP':
            #     value['Train'] = [i[0] for i in train]
            #     value['Test'] = [i[0] for i in test]
            if key == 'NOCount':
                value['Train'] = [i[0] for i in train]
                value['Test'] = [i[0] for i in test]
            if key == 'NHOHCount':
                value['Train'] = [i[1] for i in train]
                value['Test'] = [i[1] for i in test]
            if key == 'MolWt':
                value['Train'] = [i[2] for i in train]
                value['Test'] = [i[2] for i in test]
            if key == 'NumRotatableBonds':
                value['Train'] = [i[3] for i in train]
                value['Test'] = [i[3] for i in test]
            if key == 'TPSA':
                value['Train'] = [i[4] for i in train]
                value['Test'] = [i[4] for i in test]
        return box_data
    
    def plot_r2(self, target, pred, r2, save):
        descriptors=['NOCount', 'NHOHCount', 'MolWt', 'NumRotatableBonds', 'TPSA']
        color=['orange', 'r', 'b', 'm', 'y', 'g']
        fig, axs = plt.subplots(2,3, figsize=(12,8))
        for ax, i, descriptor, col in zip(axs.flatten(), range(0,target.shape[1]), descriptors, color):
            ax.scatter(target[:,i], pred[:,i], c=col)
            ax.text(0.035, 0.935, 'r2:'+str(round(np.mean(r2, axis=0)[i],3)), transform=ax.transAxes, size=10, backgroundcolor='deeppink', alpha =0.8)
            ax.grid()
            #ax.plot(inv_test_target[:,i], popt0[i]*inv_test_target[:,i] + popt+i+[1])
            ax.set_title(descriptor)
            
        if type(save)==str:
            plt.savefig('analysis/figures/'+save+'.png', dpi=800, bbox_inches='tight')
            print('Plot Saved!')
        elif save==False:
            print('Plot displayed, not saved')
        plt.show()
        return None
