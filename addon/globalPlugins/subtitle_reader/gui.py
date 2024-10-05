#encoding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

import addonHandler
addonHandler.initTranslation()

import wx
import gui

tray = gui.mainFrame.sysTrayIcon
toolsMenu = tray.toolsMenu

class Menu(wx.Menu):
	def __init__(self, main):
		super(Menu, self).__init__()
		self.main = main
		# Translators: Subtitle Reader menu on the NVDA tools menu
		self.menuItem = toolsMenu.AppendSubMenu(self, _(u'字幕閱讀器 (&R)'))
		# Translators: Reader toggle switch on the Subtitle Reader menu
		self.switch = self.AppendCheckItem(wx.ID_ANY, _(u'閱讀器開關 (&S)'))
		self.switch.Check(True)
		
		# Translators: toggle reading when video window not in foreground on the Subtitle Reader menu
		self.backgroundReading = self.AppendCheckItem(wx.ID_ANY, _(u'背景閱讀 (&B)'))
		self.backgroundReading.Check(True)
		
		self.youtube = wx.Menu()
		self.youtubeMenuItem = self.AppendSubMenu(self.youtube, _('Youtube 相關設定'))
		
		# Translators: toggle Youtube menu item whether to read the chat message when the new chat message already appeared
		self.readChat = self.youtube.AppendCheckItem(wx.ID_ANY, _(u'閱讀聊天室(&R)'))
		self.readChat.Check(True)
		
		# Translators: toggle Youtube menu item whether to read the chat message sender. 
		self.readChatSender = self.youtube.AppendCheckItem(wx.ID_ANY, _(u'閱讀聊天室訊息發送者(&A)'))
		self.readChatSender.Check(True)
		
		# Translators: toggle Youtube menu item whether to read the manager's chat message only.
		self.onlyReadManagersChat = self.youtube.AppendCheckItem(wx.ID_ANY, _(u'僅閱讀管理員訊息(&M)'))
		self.onlyReadManagersChat.Check(False)
		
		# Translators: toggle Youtube menu item whether to read the chat gift sponser message. 
		self.readChatGiftSponser = self.youtube.AppendCheckItem(wx.ID_ANY, _(u'閱讀會籍贈送(&G)'))
		self.readChatGiftSponser.Check(True)
		
		# Translators: toggle Youtube menu item whether to omit graphic when reading the chats
		self.omitChatGraphic = self.youtube.AppendCheckItem(wx.ID_ANY, _(u'閱讀聊天室時掠過圖片名稱(&G)'))
		self.omitChatGraphic.Check(True)
		
		# Translators: toggle menu item whether to prompt wher Youtube info card is already appear
		self.infoCardPrompt = self.youtube.AppendCheckItem(wx.ID_ANY, _(u'資訊卡提示(&I)'))
		self.infoCardPrompt.Check(True)
		
		# Translators: This menu item performs a check for updates to the reader
		self.checkForUpdate = self.Append(wx.ID_ANY, _(u'立即檢查更新(&C)'))
		# Translators: This is menu item that open the changelog
		self.openChangeLog = self.Append(wx.ID_ANY, _(u'開啟更新日誌(&O)'))
		# Translators: This menu item that can toggle automatic check for update when Subtitle Reader is start
		self.checkUpdateAutomatic = self.AppendCheckItem(wx.ID_ANY, _(u'自動檢查更新(&A)'))
		self.checkUpdateAutomatic.Check(True)
		
		self.contactDeveloper = wx.Menu()
		self.contactDeveloperMenuItem = self.AppendSubMenu(self.contactDeveloper, _('聯絡開發者 (&C)'))
		
		self.contactUseSkype = self.contactDeveloper.Append(wx.ID_ANY, 'Skype, id:p15937a')
		self.contactUseFacebook = self.contactDeveloper.Append(wx.ID_ANY, _('Facebook 個人檔案'))
		self.contactUseQq = self.contactDeveloper.Append(wx.ID_ANY, _('QQ, id:2231691423'))
		self.contactUseLine = self.contactDeveloper.Append(wx.ID_ANY, 'Line, id:Maxe0310 ' + _('點此複製到剪貼簿'))
		self.contactUseDiscord = self.contactDeveloper.Append(wx.ID_ANY, 'Discord, ID:maxe0310 ' + _('點此複製到剪貼簿'))
		
		self.contactUseX = self.contactDeveloper.Append(wx.ID_ANY, _('X, ID:Maxe0310'))
	

class UpdateDialog(wx.Dialog):
	def __init__(self, version):
		super(UpdateDialog, self).__init__(gui.mainFrame, wx.ID_ANY, title=_(u'字幕閱讀器 V') + str(version) + _(u' 新版資訊'))
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		# Translators: This label means the edit box content is changelog
		self.changelogLabel = wx.StaticText(self, label=_(u'更新日誌'))
		self.sizer.Add(self.changelogLabel)
		self.changelogText = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2 | wx.HSCROLL, size=(1024, 768))
		self.sizer.Add(self.changelogText, wx.SizerFlags(1).Expand())
		
		self.subtitleLabel = Label(self, label=_(u'字幕'))
		self.sizer.Add(self.subtitleLabel, wx.SizerFlags(0).Center())
		
		self.progress = wx.Gauge(self, style=wx.GA_VERTICAL + wx.ST_NO_AUTORESIZE)
		self.sizer.Add(self.progress)
		self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.sizer.Add(self.buttonSizer, wx.SizerFlags(0).Center())
		# Translators: This button means now run the update process
		self.updateNow = wx.Button(self, label=_(u'現在更新(&U)'))
		self.buttonSizer.Add(self.updateNow, wx.SizerFlags(1).Bottom())
		self.buttonSizer.AddStretchSpacer(1)
		# Translators: This button means that the automatic check for updates will skip this version
		self.skipVersion = wx.Button(self, label=_(u'跳過此版本(&S)'))
		self.buttonSizer.Add(self.skipVersion, wx.SizerFlags(1).Bottom())
		self.buttonSizer.AddStretchSpacer(1)
		# Translators: This button means close window until next automatic or manual check for update
		self.later = wx.Button(self, label=_(u'晚點再說(&L)'))
		self.buttonSizer.Add(self.later, wx.SizerFlags(1).Bottom())
		
		self.SetSizerAndFit(self.sizer)
		self.CenterOnScreen()
	

class Label(wx.StaticText):
	def AcceptsFocus(self):
		return True
	
	def AcceptsFocusFromKeyboard(self):
		return True
	
