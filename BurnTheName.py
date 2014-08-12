import urllib2
from bs4 import BeautifulSoup

def NameBurn(sigil_path, sigil_time, sigil_name, house, no_vertices)
#an unproven method may provide a path to immanentizing sigils to the printed world.
#https://www.dropcam.com/live-demos/more/little-printer

#collate libraries
import os

#get key
soup = BeautifulSoup(urllib2.urlopen('http://littleprinter.com/').read())

#when no new sigil is drawn, but the method invoked, record my name
if sigil_path.eq."" then:
  sigil_path="http://33.media.tumblr.com/f74e85659b553bef271f499a2f78a59b/tumblr_na72kjm6TU1qzfbjco1_500.jpg"
  sigil_time=""
  sigil_name=""
  house=""
  no_vertices=""

#join words 
simple_sigil_log=sigil_time+' : '+sigil_name+' : '+house+' : '+no_vertices

#sigil transfer
os.system(soup.code)