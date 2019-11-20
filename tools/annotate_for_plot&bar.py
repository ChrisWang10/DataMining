for a, b in zip(x, y):
	plt.annotate('%.7s' % b, xy=(a, b), xytext=(-20, 10), textcoords='offset points')
	

for a,b in zip(x,y):
    plt.text(a, b+0.001, '%.4f' % b, ha='center', va= 'bottom',fontsize=9)