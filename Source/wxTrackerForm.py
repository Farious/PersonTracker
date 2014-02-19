# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class TrackerMainFrame
###########################################################################

class TrackerMainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.notebookPanel = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.trackerTab = wx.Panel( self.notebookPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		trackerSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		trackerSizer.AddGrowableCol( 0 )
		trackerSizer.AddGrowableCol( 1 )
		trackerSizer.AddGrowableRow( 0 )
		trackerSizer.SetFlexibleDirection( wx.BOTH )
		trackerSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		playerBox = wx.BoxSizer( wx.VERTICAL )
		
		self.glPanel = wx.Panel( self.trackerTab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		playerBox.Add( self.glPanel, 10, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		playerBtnBox = wx.BoxSizer( wx.HORIZONTAL )
		
		self.rewBtn = wx.BitmapButton( self.trackerTab, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.rewBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.prevFrameBtn = wx.BitmapButton( self.trackerTab, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.prevFrameBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.stopBtn = wx.BitmapButton( self.trackerTab, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.stopBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.playBtn = wx.BitmapButton( self.trackerTab, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.playBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.pauseBtn = wx.BitmapButton( self.trackerTab, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.pauseBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.nextFrameBtn = wx.BitmapButton( self.trackerTab, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.nextFrameBtn, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.forwardBtn = wx.BitmapButton( self.trackerTab, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		playerBtnBox.Add( self.forwardBtn, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		playerBox.Add( playerBtnBox, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		trackerSizer.Add( playerBox, 5, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		expansionBox = wx.BoxSizer( wx.VERTICAL )
		
		personSelBox = wx.StaticBoxSizer( wx.StaticBox( self.trackerTab, wx.ID_ANY, u"Person Selection" ), wx.VERTICAL )
		
		personCheckListChoices = []
		self.personCheckList = wx.CheckListBox( self.trackerTab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, personCheckListChoices, wx.LB_ALWAYS_SB )
		personSelBox.Add( self.personCheckList, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		expansionBox.Add( personSelBox, 2, wx.ALL|wx.EXPAND, 5 )
		
		videoSelBox = wx.StaticBoxSizer( wx.StaticBox( self.trackerTab, wx.ID_ANY, u"Video Selection" ), wx.VERTICAL )
		
		videoChkListChoices = []
		self.videoChkList = wx.CheckListBox( self.trackerTab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, videoChkListChoices, wx.LB_ALWAYS_SB )
		videoSelBox.Add( self.videoChkList, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		expansionBox.Add( videoSelBox, 2, wx.ALL|wx.EXPAND, 5 )
		
		statBox = wx.StaticBoxSizer( wx.StaticBox( self.trackerTab, wx.ID_ANY, u"Statistics" ), wx.HORIZONTAL )
		
		self.statsPanel = wx.Panel( self.trackerTab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.statsPanel.SetSizer( bSizer5 )
		self.statsPanel.Layout()
		bSizer5.Fit( self.statsPanel )
		statBox.Add( self.statsPanel, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		expansionBox.Add( statBox, 8, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		trackerSizer.Add( expansionBox, 1, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		
		self.trackerTab.SetSizer( trackerSizer )
		self.trackerTab.Layout()
		trackerSizer.Fit( self.trackerTab )
		self.notebookPanel.AddPage( self.trackerTab, u"Tracker", True )
		self.rocTab = wx.Panel( self.notebookPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.notebookPanel.AddPage( self.rocTab, u"ROC", False )
		
		bSizer1.Add( self.notebookPanel, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.glTimer = wx.Timer()
		self.glTimer.SetOwner( self, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.fileMenu = wx.Menu()
		self.fileMenu.AppendSeparator()
		
		self.exitMenuItem = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
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
		self.Bind( wx.EVT_UPDATE_UI, self.reDraw )
		self.rewBtn.Bind( wx.EVT_BUTTON, self.rewindBtnClick )
		self.prevFrameBtn.Bind( wx.EVT_BUTTON, self.prevFrameBtnClick )
		self.stopBtn.Bind( wx.EVT_BUTTON, self.stopBtnClick )
		self.playBtn.Bind( wx.EVT_BUTTON, self.playBtnClick )
		self.pauseBtn.Bind( wx.EVT_BUTTON, self.pauseBtnClick )
		self.nextFrameBtn.Bind( wx.EVT_BUTTON, self.nextFrameBtnClick )
		self.forwardBtn.Bind( wx.EVT_BUTTON, self.forwardBtnClick )
	
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
	

