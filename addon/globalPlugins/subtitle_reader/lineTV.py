#coding=utf-8

from .subtitle_alg import SubtitleAlg, SupportStatus
from .object_finder import find
from .compatible import role

class LineTV(SubtitleAlg):
	info = {
		'name': 'LINE TV',
		'url': 'https://www.linetv.tw/',
		'status': SupportStatus.supported,
	}
	def getVideoPlayer(self):
		obj = self.main.focusObject
		videoPlayer = find(obj, 'parent', 'id', 'player')
		return videoPlayer
	
	def getSubtitleContainer(self):
		videoPlayer = self.main.videoPlayer
		subtitleContainer = videoPlayer.firstChild.next
		return subtitleContainer
	
	def getSubtitle(self):
		return super(LineTV, self).getSubtitle()
	
