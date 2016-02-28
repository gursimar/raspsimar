
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStore
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.api.client import EvernoteClient
from settings import *

class evernoteAccess:
    def __init__(self, token):
        #self.note_store = 
        self.client = self._connect_evernote(token)        
        ## Get note store
        self.note_store = self.client.get_note_store() 
        
    def __init__(c_key, c_secret, self)
        ## Invoke this if you want to get auth_token using oAuth
        auth_token = self._getAuthToken(c_key, c_secret)
        print '----new OAuthToken----'
        print auth_token
        print '----new OAuthToken----'
        #self.note_store = 
        self.client = self._connect_evernote(token)        
        ## Get note store
        self.note_store = self.client.get_note_store() 
        
    def _connect_evernote(self, auth_token):
        ##
        # Create a new EvernoteClient instance with our auth
        # token.
        ##
        client = EvernoteClient(token=auth_token, sandbox=False)

        ##
        # Test the auth token...
        ##
        userStore = client.get_user_store()
        user = userStore.getUser()
        print user.username
        return client

    def getNotebooks(self):
        # Make API calls
        notebooks = self.note_store.listNotebooks()    
        return notebooks
        
    def getNotebook(self, guid):
        return self.note_store.getNotebook(auth_token, guid)
        
    def getNotesInNotebook(self, wanted_notebook):
        filter = NoteFilter()
        updated_filter = NoteFilter(words='evernote')
        filter.notebookGuid = wanted_notebook.guid;
        offset = 0
        max_notes = 10
        result_spec = NotesMetadataResultSpec(includeTitle=True)
        #notes = note_store.findNotes(auth_token, filter, offset, max_notes);
        notes_data = self.note_store.findNotesMetadata(auth_token, filter, offset, max_notes, result_spec);
        notes = notes_data.notes
        return notes
        
    def uploadNote(self):
        note = Types.Note()
        note.title = "I'm a test note!"
        note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>Hello, world!</en-note>'
        note.notebookGuid = wanted_notebook.guid
        #note = note_store.createNote(note)
        
    def listNotebooks(self, notebooks):
        # Notebooks is a list of object notebook
        for notebook in notebooks:
            print "Notebook: ", notebook.name + " " + notebook.guid
            
    def createNotebook(self, notebook):
        return self.note_store.createNotebook(notebook)            

    def _parse_query_string(self, authorize_url):
        uargs = authorize_url.split('?')
        vals = {}
        if len(uargs) == 1:
            raise Exception('Invalid Authorization URL')
        for pair in uargs[1].split('&'):
            key, value = pair.split('=', 1)
            vals[key] = value
        return vals

    def getAuthToken(self, c_key, c_secret):
        ##
        # Create an instance of EvernoteClient using your API
        # key (consumer key and consumer secret)
        ##
        client = EvernoteClient(
            consumer_key=c_key,
            consumer_secret=c_secret,
            sandbox=False # Default: True
        )

        ##
        # Provide the URL where the Evernote Cloud API should 
        # redirect the user after the request token has been
        # generated. In this example, localhost is used; note
        # that in this example, we're copying the URLs manually
        # and that, in production, this URL will need to 
        # automatically parse the response and send the user
        # to the next step in the flow.
        ##
        request_token = client.get_request_token('http://localhost')

        ##
        # Prompt the user to open the request URL in their browser
        ##
        print "Paste this URL in your browser and login"
        print
        print '\t'+client.get_authorize_url(request_token)
        print
        print '-------'

        ##
        # Have the user paste the resulting URL so we can pull it
        # apart
        ##
        print "Paste the URL after login here:"
        authurl = raw_input()

        ##
        # Parse the URL to get the OAuth verifier
        ##
        vals = parse_query_string(authurl)

        ##
        # Use the OAuth verifier and the values from request_token
        # to built the request for our authentication token, then
        # ask for it.
        ##
        auth_token = client.get_access_token(
                    request_token['oauth_token'],
                    request_token['oauth_token_secret'],
                    vals['oauth_verifier']
                )
        return auth_token        
        
if __name__ == '__main__': 

    p = evernoteAccess(auth_token)    
    # Use this if you have a consumer key and secret and want to get oAuth token
    # p = evernoteAccess(c_key, c_secret)
    wanted_notebook = p.getNotebook("2bada46b-9157-4457-bd1e-1741c5f811e3")
    notes = p.getNotesInNotebook(wanted_notebook)
    for note in notes:
        print note.title

