def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

plt.plot(smooth(oriloss,5*50), color='r', label='ori' )
plt.plot(smooth(dxloss,5*50), color='g', label='dx' )
plt.ylim([0,1])
#plt.plot(m2_history['val_loss'], color='b', label='m2' )
#plt.plot(m0_history['acc'], color='c', label='m0')
#plt.plot(m3_025_history['val_loss'], color='m', label='m3-025' )
plt.legend()

plt.show()
