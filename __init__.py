import googlesearch as gs
import webbrowser as wb

def playonyt(title):
    try:
	    	query=gs.search(title,num_results=15)
	    	for links in query:
	        	link = links.split('/')
	        	if link[2]=='www.youtube.com':
	            		wb.open(links)
	            		print(f'opening {title}')
    except:
		   print('An Error Occured\nTry Searching Something else\nNetwork Conmection Error(')

if __name__ =='__main__':
	playonyt('Play date')