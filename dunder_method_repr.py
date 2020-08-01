class Invoice:
    def init(self, client, total):
      self.client = client
      self.total = total

    def str(self):                                 # use str for a prettier output
      return f"Invoice from {self.client} for {self.total}"

    def repr(self):                                # dunder repr similar to str but used for raw output not formatted nice example error logs
      return f"Invoice({self.client}, {self.total})"   # return and format the invoice

    # def repr(self):
    #     return f"Invoice <value: client: {self.client}, total: {self.total}>'


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))