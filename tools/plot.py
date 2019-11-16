import matplotlib.pyplot as plt                                                                                          
import numpy as np                                                                                                       
import pandas as pd                                                                                                      

#
def example1():                                                                                                                        
	df1 = pd.DataFrame(np.random.rand(25), index=np.arange(25), columns=['test1'])                                           
	df2 = pd.DataFrame(np.random.rand(25), index=np.arange(25), columns=['test2'])                                           
	df3 = pd.DataFrame(np.random.rand(25), index=np.arange(25), columns=['test3'])                                           
	df4 = pd.DataFrame(np.random.rand(25), index=np.arange(25), columns=['test4'])                                           

	# 生成4个子图                                                                                                                 
	fig = plt.figure(1)                                                                                                      
	ax1 = fig.add_subplot(2,2,1)                                                                                             
	ax2 = fig.add_subplot(2,2,2)                                                                                             
	ax3 = fig.add_subplot(2,2,3)                                                                                             
	ax4 = fig.add_subplot(2,2,4)                                                                                             
																			   #------ df.plot参数 ---------#                  
	df1.plot(ax = ax1, style = 'b*-', kind = 'line', rot = 360, grid = 'on')   # style设置线型(ko--)                             
	ax1.set_xticks(range(0,26,5))                                              # alpha设置不透明度                                 
	ax1.set_xticklabels(range(0,26,5))                                         # kind可以是'line','bar','barh','kde'            
																			   # logy　在y轴使用对数标尺                              
	df2.plot(ax = ax2, kind = 'line', logy = True, title = 'test2', rot = 270) # xlim x轴的界限                                  
	ax2.set_xticks(range(0,26,5))                                              # ylim y轴的界限                                  
	ax2.set_xticklabels(range(0,26,5))                                         # grid 网格线                                    
																			   # rot旋转坐标刻度标签                                 
	df3.plot(ax = ax3, kind = 'line', title = 'test3', rot = 180, sharex = True)# title 图像标题                                 
	ax3.set_xticks(range(0,26,5))                                              # figsiez 图像大小                                
	ax3.set_xticklabels(range(0,26,5))                                         # sharex/sharex 共用x轴/y轴                       

	df4.plot(ax = ax4, style = 'ko--', kind = 'line', title = 'test4', rot = 90, figsize = (8,10))                           
	ax4.set_xticks(range(0,26,5))                                                                                            
	ax4.set_xticklabels(range(0,26,5))                                                                                       

	plt.show() 

def example12():
	array1 = np.random.rand(100)                                                                                                         
	array2 = np.random.rand(100)                                                                                                         


	fig1 = plt.figure(1)                                           # 创建一个Figure                                                          
	ax1 = fig1.add_subplot(1,1,1)                                  # add_subplot()创建一个子图或多个子图                                            
	ax1.plot(array1, 'o-', color = 'blue', label = 'array1')       # label设置标签,'o-'代表线型                                                           
	ax1.plot(array2, '>-', color = 'red', label = 'array1')                                                                              
	ax1.set_xscale('log')                                          # 设置x轴为对数坐标                                                           
	ax1.set_yscale('log')                                          # 设置y轴为对数坐标                                                           
	ax1.set_xlabel('x',fontsize = 15)                              # 设置x轴的标签, fontsize设置字体大小                                             
	ax1.set_ylabel('y', fontsize = 15)                             # 设置y轴的标签, fontsize设置字体大小                                             
	ax1.set_xlim(0,100)                                            #　设置x轴范围                                                              
	ax1.set_ylim(0,1)                                              #　设置y轴范围                                                              
	ax1.set_xticks([1,2,3,4,5,6,7,8,9,10,20,30,40,50,100])         # 设置x轴要显示的刻度                                                          
	ax1.set_xticklabels(['a','b','c','d',5,6,7,8,9,10,20,30,40,50,100]) # 设置该刻度上的标签                                                      
	ax1.grid(True, which='major', axis='both')                      # 设置网格                                                               
	ax1.legend(loc = 'best', numpoints = 1)                         # 图例, loc='best',即图例放在最不碍事的位置,numpoint图例上自由一个点                       
	plt.show()

def main():
	pass

	
if __name__ == '__main__':
    main()