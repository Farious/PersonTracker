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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 743,525 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.notebookPanel = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_TAB_SPLIT )
		self.trackerTab = wx.Panel( self.notebookPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_splitter2 = wx.SplitterWindow( self.trackerTab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_BORDER )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		
		self.m_panel14 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		playerBox = wx.BoxSizer( wx.VERTICAL )
		
		self.glPanel = wx.Panel( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		playerBox.Add( self.glPanel, 8, wx.EXPAND |wx.ALL, 5 )
		
		playerBtnBox = wx.BoxSizer( wx.HORIZONTAL )
		
		self.rewBtn = wx.BitmapButton( self.m_panel14, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.rewBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.prevFrameBtn = wx.BitmapButton( self.m_panel14, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.prevFrameBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.stopBtn = wx.BitmapButton( self.m_panel14, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.stopBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.playBtn = wx.BitmapButton( self.m_panel14, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.playBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.pauseBtn = wx.BitmapButton( self.m_panel14, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.pauseBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.nextFrameBtn = wx.BitmapButton( self.m_panel14, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.nextFrameBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.forwardBtn = wx.BitmapButton( self.m_panel14, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.forwardBtn, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		playerBox.Add( playerBtnBox, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel14.SetSizer( playerBox )
		self.m_panel14.Layout()
		playerBox.Fit( self.m_panel14 )
		self.m_panel11 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		expansionBox = wx.BoxSizer( wx.VERTICAL )
		
		personSelBox = wx.StaticBoxSizer( wx.StaticBox( self.m_panel11, wx.ID_ANY, u"Person Selection" ), wx.VERTICAL )
		
		personCheckListChoices = []
		self.personCheckList = wx.CheckListBox( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, personCheckListChoices, wx.LB_ALWAYS_SB )
		personSelBox.Add( self.personCheckList, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		expansionBox.Add( personSelBox, 2, wx.ALL|wx.EXPAND, 5 )
		
		videoSelBox = wx.StaticBoxSizer( wx.StaticBox( self.m_panel11, wx.ID_ANY, u"Video Selection" ), wx.VERTICAL )
		
		videoChkListChoices = []
		self.videoChkList = wx.CheckListBox( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, videoChkListChoices, wx.LB_ALWAYS_SB )
		videoSelBox.Add( self.videoChkList, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		expansionBox.Add( videoSelBox, 2, wx.ALL|wx.EXPAND, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self.m_panel11, wx.ID_ANY, u"Show frames with selected detections", wx.DefaultPosition, wx.DefaultSize, 0 )
		expansionBox.Add( self.m_checkBox2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel11.SetSizer( expansionBox )
		self.m_panel11.Layout()
		expansionBox.Fit( self.m_panel11 )
		self.m_splitter2.SplitVertically( self.m_panel14, self.m_panel11, 0 )
		bSizer8.Add( self.m_splitter2, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )
		
		
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
		self.glTimer.Start( 50 )
		
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
		self.videoChkList.Bind( wx.EVT_CHECKLISTBOX, self.videoSelectionUpdate )
		self.videoChkList.Bind( wx.EVT_KEY_DOWN, self.chkListKeyDown )
		self.videoChkList.Bind( wx.EVT_KEY_UP, self.chkListKeyUp )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.show_det_only )
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
	
	
	
	def show_det_only( self, event ):
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
		self.m_splitter2.SetSashPosition( 0 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )
	

