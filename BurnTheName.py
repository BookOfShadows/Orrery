def NameBurn(sigil_path, sigil_time, sigil_name, house, no_vertices)
#an unproven method may provide a path to immanentizing sigils to the printed world.
#https://www.dropcam.com/live-demos/more/little-printer

#collate libraries
import os

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
os.system('curl -X POST --data-urlencode 'html=<html><head><meta chaet="utf-8"></head><body><img src='+sigil_path+' width=370 height=370>
><p style="font-family: Comic Sans Ms; font-size: 36px;">'+simple_sigil_log+'</p> </body></html>' http://remote.bergcloud.com/playground/direct_print/FACCWOP7HPXG')
