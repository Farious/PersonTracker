# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

MainTimer = 1000
statsTimer = 1001
checkListTimer = 1002
rocTimer = 1003

###########################################################################
## Class TrackerMainFrame
###########################################################################

class TrackerMainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 605,456 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.notebookPanel = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_TAB_SPLIT )
		self.notebookPanel.SetMinSize( wx.Size( 640,480 ) )
		
		self.trackerTab = wx.Panel( self.notebookPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_splitter2 = wx.SplitterWindow( self.trackerTab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_BORDER )
		self.m_splitter2.SetSashSize( 2 )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		self.m_splitter2.SetMinimumPaneSize( 100 )
		
		self.m_panel14 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		playerBox = wx.BoxSizer( wx.VERTICAL )
		
		self.glPanel = wx.Panel( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		playerBox.Add( self.glPanel, 8, wx.ALL|wx.EXPAND, 5 )
		
		playerBtnBox = wx.BoxSizer( wx.HORIZONTAL )
		
		self.rewBtn = wx.Button( self.m_panel14, wx.ID_ANY, u"Rewind", wx.DefaultPosition, wx.DefaultSize, 0 )
		playerBtnBox.Add( self.rewBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.prevFrameBtn = wx.Button( self.m_panel14, wx.ID_ANY, u"Previous", wx.DefaultPosition, wx.DefaultSize, 0 )
		playerBtnBox.Add( self.prevFrameBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.stopBtn = wx.Button( self.m_panel14, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		playerBtnBox.Add( self.stopBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.playBtn = wx.Button( self.m_panel14, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		playerBtnBox.Add( self.playBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.pauseBtn = wx.Button( self.m_panel14, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		playerBtnBox.Add( self.pauseBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.nextFrameBtn = wx.Button( self.m_panel14, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		playerBtnBox.Add( self.nextFrameBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.forwardBtn = wx.Button( self.m_panel14, wx.ID_ANY, u"Forward", wx.DefaultPosition, wx.DefaultSize, 0 )
		playerBtnBox.Add( self.forwardBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		playerBox.Add( playerBtnBox, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel14.SetSizer( playerBox )
		self.m_panel14.Layout()
		playerBox.Fit( self.m_panel14 )
		self.m_panel11 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetMinSize( wx.Size( 100,50 ) )
		
		expansionBox = wx.BoxSizer( wx.VERTICAL )
		
		expansionBox.SetMinSize( wx.Size( 100,50 ) ) 
		personSelBox = wx.StaticBoxSizer( wx.StaticBox( self.m_panel11, wx.ID_ANY, u"Person Selection" ), wx.VERTICAL )
		
		personCheckListChoices = []
		self.personCheckList = wx.CheckListBox( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, personCheckListChoices, wx.LB_ALWAYS_SB )
		self.personCheckList.SetMinSize( wx.Size( 100,50 ) )
		
		personSelBox.Add( self.personCheckList, 2, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		expansionBox.Add( personSelBox, 2, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		videoSelBox = wx.StaticBoxSizer( wx.StaticBox( self.m_panel11, wx.ID_ANY, u"Video Selection" ), wx.VERTICAL )
		
		videoChkListChoices = []
		self.videoChkList = wx.Choice( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, videoChkListChoices, 0 )
		self.videoChkList.SetSelection( 0 )
		self.videoChkList.SetMinSize( wx.Size( 100,25 ) )
		
		videoSelBox.Add( self.videoChkList, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		expansionBox.Add( videoSelBox, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		propertiesSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel11, wx.ID_ANY, u"Properties" ), wx.VERTICAL )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chkbox_show_det = wx.CheckBox( self.m_panel11, wx.ID_ANY, u"Show detections", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkbox_show_det.SetValue(True) 
		bSizer71.Add( self.chkbox_show_det, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.thrshValue = wx.TextCtrl( self.m_panel11, wx.ID_ANY, u"Threshold Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.thrshValue, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		propertiesSizer.Add( bSizer71, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chkbox_show_reid = wx.CheckBox( self.m_panel11, wx.ID_ANY, u"Show re-identifications", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkbox_show_reid.SetValue(True) 
		bSizer81.Add( self.chkbox_show_reid, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer81.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.rank_slider = wx.Slider( self.m_panel11, wx.ID_ANY, 10, 1, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer81.Add( self.rank_slider, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer81.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.actual_rank = wx.StaticText( self.m_panel11, wx.ID_ANY, u"[1]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.actual_rank.Wrap( -1 )
		bSizer81.Add( self.actual_rank, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		propertiesSizer.Add( bSizer81, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.chkbox_show_selected = wx.CheckBox( self.m_panel11, wx.ID_ANY, u"Show frames with selected detections", wx.DefaultPosition, wx.DefaultSize, 0 )
		propertiesSizer.Add( self.chkbox_show_selected, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		expansionBox.Add( propertiesSizer, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel11, wx.ID_ANY, u"Frames per second" ), wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		sbSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fps_slider = wx.Slider( self.m_panel11, wx.ID_ANY, 1, 1, 120, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sbSizer4.Add( self.fps_slider, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"120", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		sbSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.actual_fps = wx.StaticText( self.m_panel11, wx.ID_ANY, u"[1]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.actual_fps.Wrap( -1 )
		sbSizer4.Add( self.actual_fps, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		expansionBox.Add( sbSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, 5 )
		
		
		self.m_panel11.SetSizer( expansionBox )
		self.m_panel11.Layout()
		expansionBox.Fit( self.m_panel11 )
		self.m_splitter2.SplitVertically( self.m_panel14, self.m_panel11, 500 )
		bSizer8.Add( self.m_splitter2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.trackerTab.SetSizer( bSizer8 )
		self.trackerTab.Layout()
		bSizer8.Fit( self.trackerTab )
		self.notebookPanel.AddPage( self.trackerTab, u"Tracker", True, 0 )
		self.rocTab = wx.Panel( self.notebookPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.notebookPanel.AddPage( self.rocTab, u"ROC", False, 0 )
		self.statTab = wx.Panel( self.notebookPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.notebookPanel.AddPage( self.statTab, u"Stats", False, 0 )
		
		bSizer7.Add( self.notebookPanel, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		self.glTimer = wx.Timer()
		self.glTimer.SetOwner( self, MainTimer )
		self.glTimer.Start( 1000 )
		
		self.updateStatTimer = wx.Timer()
		self.updateStatTimer.SetOwner( self, statsTimer )
		self.updateStatTimer.Start( 300 )
		
		self.updateCheckLTimer = wx.Timer()
		self.updateCheckLTimer.SetOwner( self, checkListTimer )
		self.updateCheckLTimer.Start( 2000 )
		
		self.updateROCTimer = wx.Timer()
		self.updateROCTimer.SetOwner( self, rocTimer )
		self.updateROCTimer.Start( 300 )
		
		self.glCanvasUpdateTimer = wx.Timer()
		self.glCanvasUpdateTimer.SetOwner( self, wx.ID_ANY )
		self.glCanvasUpdateTimer.Start( 500 )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.fileMenu = wx.Menu()
		self.fileMenu.AppendSeparator()
		
		self.exitMenuItem = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"E&xit", wx.EmptyString, wx.ITEM_NORMAL )
		self.exitMenuItem.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_MENU ) )
		self.fileMenu.AppendItem( self.exitMenuItem )
		
		self.m_menubar1.Append( self.fileMenu, u"File" ) 
		
		self.editMenu = wx.Menu()
		self.m_menubar1.Append( self.editMenu, u"Edit" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_PAINT, self.reDraw )
		self.Bind( wx.EVT_SIZE, self.reDraw )
		self.Bind( wx.EVT_UPDATE_UI, self.update_ui )
		self.rewBtn.Bind( wx.EVT_BUTTON, self.rewindBtnClick )
		self.prevFrameBtn.Bind( wx.EVT_BUTTON, self.prevFrameBtnClick )
		self.stopBtn.Bind( wx.EVT_BUTTON, self.stopBtnClick )
		self.playBtn.Bind( wx.EVT_BUTTON, self.playBtnClick )
		self.pauseBtn.Bind( wx.EVT_BUTTON, self.pauseBtnClick )
		self.nextFrameBtn.Bind( wx.EVT_BUTTON, self.nextFrameBtnClick )
		self.forwardBtn.Bind( wx.EVT_BUTTON, self.forwardBtnClick )
		self.personCheckList.Bind( wx.EVT_CHECKLISTBOX, self.personSelectionUpdate )
		self.personCheckList.Bind( wx.EVT_KEY_DOWN, self.chkListKeyDown )
		self.personCheckList.Bind( wx.EVT_KEY_UP, self.chkListKeyUp )
		self.videoChkList.Bind( wx.EVT_CHOICE, self.videoSelectionUpdate )
		self.chkbox_show_det.Bind( wx.EVT_CHECKBOX, self.deactivate_reid )
		self.rank_slider.Bind( wx.EVT_SCROLL_CHANGED, self.update_rank )
		self.rank_slider.Bind( wx.EVT_SCROLL_THUMBTRACK, self.update_rank )
		self.fps_slider.Bind( wx.EVT_SCROLL_CHANGED, self.update_fps )
		self.fps_slider.Bind( wx.EVT_SCROLL_THUMBTRACK, self.update_fps )
		self.Bind( wx.EVT_TIMER, self.updateStreamImage, id=MainTimer )
		self.Bind( wx.EVT_TIMER, self.updateStatPanel, id=statsTimer )
		self.Bind( wx.EVT_TIMER, self.updateCheckList, id=checkListTimer )
		self.Bind( wx.EVT_TIMER, self.updateROC, id=rocTimer )
		self.Bind( wx.EVT_TIMER, self.updateGLCanvas, id=wx.ID_ANY )
		self.Bind( wx.EVT_MENU, self.exit_form, id = self.exitMenuItem.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def reDraw( self, event ):
		event.Skip()
	
	
	def update_ui( self, event ):
		event.Skip()
	
	def rewindBtnClick( self, event ):
		event.Skip()
	
	def prevFrameBtnClick( self, event ):
		event.Skip()
	
	def stopBtnClick( self, event ):
		event.Skip()
	
	def playBtnClick( self, event ):
		event.Skip()
	
	def pauseBtnClick( self, event ):
		event.Skip()
	
	def nextFrameBtnClick( self, event ):
		event.Skip()
	
	def forwardBtnClick( self, event ):
		event.Skip()
	
	def personSelectionUpdate( self, event ):
		event.Skip()
	
	def chkListKeyDown( self, event ):
		event.Skip()
	
	def chkListKeyUp( self, event ):
		event.Skip()
	
	def videoSelectionUpdate( self, event ):
		event.Skip()
	
	def deactivate_reid( self, event ):
		event.Skip()
	
	def update_rank( self, event ):
		event.Skip()
	
	
	def update_fps( self, event ):
		event.Skip()
	
	
	def updateStreamImage( self, event ):
		event.Skip()
	
	def updateStatPanel( self, event ):
		event.Skip()
	
	def updateCheckList( self, event ):
		event.Skip()
	
	def updateROC( self, event ):
		event.Skip()
	
	def updateGLCanvas( self, event ):
		event.Skip()
	
	def exit_form( self, event ):
		event.Skip()
	
	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 500 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )
	

