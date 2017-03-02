# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:21:45 2017


This is an example about how to draw picture for papers.
@author: cil
"""
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('text.latex',preamble=r'\usepackage{mathptmx}')
matplotlib.rcParams['text.usetex'] = True
font = {'family' : 'times new roman',
        'weight' : 'normal',
        'size'   : 10}
plt.style.use('seaborn')   #use style
matplotlib.rc('font', **font)
plt.figure(figsize=(3.45, 2.45), dpi=600)   # for one column
#plt.ploths_re_acc_list(re_acc_list, label='Random pruning')
#plt.plot(x_before,1-dx_1, color='#555555', linewidth=0.7)
plt.plot(range(-700,15625),1-np.ones(16325)*0.9815, color='#555555', linewidth=0.7, linestyle= '--', label='Before Pruning')
plt.plot((1-hs_re_acc_list).tolist(), label='LWC', color='#007500', linewidth=0.7)

#plt.plot(hu, label='Hu et al.')
plt.plot((1-re_acc_list[0:650]).tolist(),label='L-OBS', color='#AE0000', linewidth=0.6)
plt.yscale('log')
plt.ylim([0.01,1])
plt.xlim([-700,12000])
plt.xticks([-700, 0, 2500,5000,7500,10000],['','0','7.5','15','22.5','30'])

plt.xlabel('Retraining Iterations ($10^3$)')
plt.ylabel('Error')
plt.yticks([0.01,0.0184,0.1,1],['0.01','0.0127','0.1','1'])
#plt.xticks(np.array(range(0,2352,235)),['0','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.legend(loc=1)
plt.tight_layout()
plt.show()
plt.savefig('acc_retrain.pdf',format='pdf')

#np.save('hs_re_acc_list',hs_re_acc_list)
#np.save('re_acc_list',re_acc_list)
#np.save('x_before',x_before)
#np.save('dx_1',dx_1)
