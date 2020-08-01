class Invoice:

    def init(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    #private or procteted make sure to add underscores to it..Child classes given access to data (private attr uses 2 )

    @property                 #  use the @ symbol (decorator) wraps property to work with, 
    def client(self):         # create a function called client pass in self
        return self._client   # now just return self underscore self
                              # basically tells us how we should treat it/most likely will want to access this point(call on client)
                              # if you don't see the @property decorator but you see it in the init__ it means it's private and probably shouldn't use
    @client.setter              # give ability to override client using @(then name of what you want to override) then setter
    def client(self, client):   # then create the function
        self._client = client   # now override 

    @property
    def total(self):
        return self._total

google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'   #overriding the name of the client from the setter function

print(google.client)