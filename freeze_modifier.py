import c4d
from c4d import gui

def copy_object(obj,suffix,doc):

	clone = obj.GetClone()
	clone[c4d.ID_BASELIST_NAME] = '%s_%s'%(clone[c4d.ID_BASELIST_NAME],suffix)
	clone[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
	clone[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1

	doc.InsertObject(clone)
	doc.SetActiveObject(obj)
	return clone

def ctrl_hold():

	state = c4d.BaseContainer()
	gui.GetInputEvent(c4d.BFM_INPUT_KEYBOARD,state)
	res = state.GetData(c4d.BFM_INPUT_QUALIFIER) == c4d.QCTRL
	return res

def main():

	obj = doc.GetActiveObject()
	child = obj.GetChildren()
	orig_Points = obj.GetAllPoints()

	if obj and child :

		doc.StartUndo()
		doc.AddUndo(c4d.UNDOTYPE_CHANGE,obj)

		if ctrl_hold() :
			clone = copy_object(obj,'BACKUP',doc)
			doc.AddUndo(c4d.UNDOTYPE_NEW,clone)
		
		modif=obj.GetDeformCache()
		modif_Points = modif.GetAllPoints()
		obj.SetAllPoints(modif_Points)
		obj.Message(c4d.MSG_UPDATE)
		modif.Message(c4d.MSG_UPDATE)
		
		doc.EndUndo()

	else : print "Select object please"



if __name__=='__main__':
    main()
    c4d.EventAdd()
