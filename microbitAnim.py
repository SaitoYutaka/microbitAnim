# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.Point( 0,0 ), size = wx.Size( 767,507 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_button00 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button00.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button00, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button01 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button01.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button01, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button02 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button02.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button02, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button03 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button03.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button03, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button04 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button04.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button04, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button10 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button10.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button10, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button11 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button11.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button11, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button12 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button12.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button12, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button13 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button13.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button13, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button14 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button14.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button14, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button20 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button20.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button20, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button21 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button21.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button21, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button22 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button22.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button22, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button23 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button23.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button23, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button24 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button24.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button24, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button30 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button30.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button30, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button31 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button31.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button31, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button32 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button32.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button32, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button33 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button33.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button33, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button34 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button34.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button34, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button40 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button40.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button40, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button41 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button41.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button41, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button42 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button42.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button42, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button43 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button43.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button43, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_button44 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        self.m_button44.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        gbSizer1.Add( self.m_button44, wx.GBPosition( 4, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        
        self.SetSizer( gbSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem3 )
        
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )
        
        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"quit", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem2 )
        
        self.m_menubar1.Append( self.m_menu1, u"File" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button00.Bind( wx.EVT_BUTTON, self.onButton00Click )
        self.m_button01.Bind( wx.EVT_BUTTON, self.onButton01Click )
        self.m_button02.Bind( wx.EVT_BUTTON, self.onButton02Click )
        self.m_button03.Bind( wx.EVT_BUTTON, self.onButton03Click )
        self.m_button04.Bind( wx.EVT_BUTTON, self.onButton04Click )
        self.m_button10.Bind( wx.EVT_BUTTON, self.onButton10Click )
        self.m_button11.Bind( wx.EVT_BUTTON, self.onButton11Click )
        self.m_button12.Bind( wx.EVT_BUTTON, self.onButton12Click )
        self.m_button13.Bind( wx.EVT_BUTTON, self.onButton13Click )
        self.m_button14.Bind( wx.EVT_BUTTON, self.onButton14Click )
        self.m_button20.Bind( wx.EVT_BUTTON, self.onButton20Click )
        self.m_button21.Bind( wx.EVT_BUTTON, self.onButton21Click )
        self.m_button22.Bind( wx.EVT_BUTTON, self.onButton22Click )
        self.m_button23.Bind( wx.EVT_BUTTON, self.onButton23Click )
        self.m_button24.Bind( wx.EVT_BUTTON, self.onButton24Click )
        self.m_button30.Bind( wx.EVT_BUTTON, self.onButton30Click )
        self.m_button31.Bind( wx.EVT_BUTTON, self.onButton31Click )
        self.m_button32.Bind( wx.EVT_BUTTON, self.onButton32Click )
        self.m_button33.Bind( wx.EVT_BUTTON, self.onButton33Click )
        self.m_button34.Bind( wx.EVT_BUTTON, self.onButton34Click )
        self.m_button40.Bind( wx.EVT_BUTTON, self.onButton40Click )
        self.m_button41.Bind( wx.EVT_BUTTON, self.onButton41Click )
        self.m_button42.Bind( wx.EVT_BUTTON, self.onButton42Click )
        self.m_button43.Bind( wx.EVT_BUTTON, self.onButton43Click )
        self.m_button44.Bind( wx.EVT_BUTTON, self.onButton44Click )
        self.Bind( wx.EVT_MENU, self.OnMenuOpenSelect, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.OnMenuSaveSelect, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.OnMenuQuitSelect, id = self.m_menuItem2.GetId() )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def onButton00Click( self, event ):
        event.Skip()
    
    def onButton01Click( self, event ):
        event.Skip()
    
    def onButton02Click( self, event ):
        event.Skip()
    
    def onButton03Click( self, event ):
        event.Skip()
    
    def onButton04Click( self, event ):
        event.Skip()
    
    def onButton10Click( self, event ):
        event.Skip()
    
    def onButton11Click( self, event ):
        event.Skip()
    
    def onButton12Click( self, event ):
        event.Skip()
    
    def onButton13Click( self, event ):
        event.Skip()
    
    def onButton14Click( self, event ):
        event.Skip()
    
    def onButton20Click( self, event ):
        event.Skip()
    
    def onButton21Click( self, event ):
        event.Skip()
    
    def onButton22Click( self, event ):
        event.Skip()
    
    def onButton23Click( self, event ):
        event.Skip()
    
    def onButton24Click( self, event ):
        event.Skip()
    
    def onButton30Click( self, event ):
        event.Skip()
    
    def onButton31Click( self, event ):
        event.Skip()
    
    def onButton32Click( self, event ):
        event.Skip()
    
    def onButton33Click( self, event ):
        event.Skip()
    
    def onButton34Click( self, event ):
        event.Skip()
    
    def onButton40Click( self, event ):
        event.Skip()
    
    def onButton41Click( self, event ):
        event.Skip()
    
    def onButton42Click( self, event ):
        event.Skip()
    
    def onButton43Click( self, event ):
        event.Skip()
    
    def onButton44Click( self, event ):
        event.Skip()
    
    def OnMenuOpenSelect( self, event ):
        event.Skip()
    
    def OnMenuSaveSelect( self, event ):
        event.Skip()
    
    def OnMenuQuitSelect( self, event ):
        event.Skip()
    

