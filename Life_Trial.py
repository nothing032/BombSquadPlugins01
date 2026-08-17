D=Exception
try:import os,re,urllib.request,babase as A,baenv
except:pass
I='https://raw.githubusercontent.com/nothing032/BombSquadPlugins01/refs/heads/main/Life_api8.py'
J='https://raw.githubusercontent.com/nothing032/BombSquadPlugins01/refs/heads/main/Life_api9.py'
def B():
	H='error'
	try:
		K=baenv.TARGET_BALLISTICA_VERSION;L=re.sub('[a-zA-Z].*','',K);E=[int(A)for A in L.split('.')]
		if[1,7,20]<=E<=[1,7,36]:F=I
		elif E>=[1,7,37]:F=J
		else:A.screenmessage('Your version is not supported!',color=(1,0,0));A.getsimplesound(H).play();return
		B=A.app.env.get('python_directory_user')
		if not B:raise D('Mods folder not found!')
		C='Life.py';G=[A for A in os.listdir(B)if re.match('^Life(\\s*\\(\\d+\\))?\\.py$',A,re.I)]
		if G:C=min(G,key=len)
		M=os.path.join(B,C);A.screenmessage('Downloading mod...',color=(1,1,0))
		with urllib.request.urlopen(F,timeout=15)as N:O=N.read()
		with open(M,'wb')as P:P.write(O)
		A.screenmessage(f"Installed: {C} (Restart the game.)",color=(0,1,0));A.getsimplesound('ding').play()
	except D as Q:A.screenmessage(f"Installation error: {Q}",color=(1,0,0));A.getsimplesound(H).play()
B()
