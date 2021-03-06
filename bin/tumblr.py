#!/usr/local/bin/python

import sys
import basics
import pytumblr

class tumblr(object):
    '''Class for throwing stuff onto Tumblr.
    We only care about writing so that's all I've implemented here.'''

    def __init__(self, pif, name='bamca'):
	pif.secure.set_config('tumblr')
	self.name = name
	self.client = pytumblr.TumblrRestClient(pif.secure.oauth, pif.secure.secret, pif.secure.key, pif.secure.value)

    # All of these have: state tags tweet date format slug, plus...

    def create_photo(self, **kwargs):
        # caption link source data
	return self.client.create_photo(self.name, **kwargs)

    def create_text(self, **kwargs):
        # title body
	return self.client.create_text(self.name, **kwargs)

    def create_quote(self, **kwargs):
        # quote source
	return self.client.create_quote(self.name, **kwargs)

    def create_link(self, **kwargs):
        # title url description
	return self.client.create_link(self.name, **kwargs)

    def create_chat(self, **kwargs):
        # title conversation
	return self.client.create_chat(self.name, **kwargs)

    def create_audio(self, **kwargs):
        # caption external_url data
	return self.client.create_audio(self.name, **kwargs)

    def create_video(self, **kwargs):
        # caption embed data
	return self.client.create_video(self.name, **kwargs)
