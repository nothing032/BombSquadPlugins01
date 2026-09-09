try:import os,re,urllib.request,babase as A,baenv
except:pass
H='https://raw.githubusercontent.com/nothing032/BombSquadPlugins01/main/Life_api8.py'
I='https://raw.githubusercontent.com/nothing032/BombSquadPlugins01/main/Life_api9.py'
def B():
	G='error'
	try:
		J=baenv.TARGET_BALLISTICA_VERSION;K=re.sub('[a-zA-Z].*','',J);C=[int(O)for O in K.split('.')]
		if[1,7,20]<=C<=[1,7,36]:D=H
		elif C>=[1,7,37]:D=I
		else:A.screenmessage('Your game version is not supported.',color=(1,0,0));A.getsimplesound(G).play();return
		E=A.env()['python_directory_user'];B='Life.py';F=[O for O in os.listdir(E)if re.match('^Life(\\s*\\(\\d+\\))?\\.py$',O,re.I)]
		if F:B=min(F,key=len)
		L=os.path.join(E,B)
		with urllib.request.urlopen(D,timeout=15)as M:N=M.read()
		with open(L,'wb')as O:O.write(N)
		A.screenmessage(f"Installed successfully: {B}. Please restart the game.",color=(0,1,0));A.getsimplesound('ding').play()
	except Exception as P:A.screenmessage(f"Installation failed: {P}",color=(1,0,0));A.getsimplesound(G).play()
B()
