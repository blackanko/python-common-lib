# -*- coding: <utf-8> -*-
import maya.cmds as cmds

def renameNamespace(oldName, newName):
	nslist = cmds.namespaceInfo( listNamespace=True )
	for ns in nslist:
	    if ns.find(oldName) < 0:
	        continue
	    newNs = ns.replace(oldName,newName)
	    try:
	        cmds.namespace(rename=[ns,newNs])
	    except:
	        pass


def renameNode(oldName, newName):
	for n in cmds.ls("%s*"%oldName):
	    t = n.split("|")[-1]
	    tt = cmds.ls(t)
	    for ts in tt:
	        ns = ts.replace(oldName, newName)
	        cmds.rename(ts, ns)