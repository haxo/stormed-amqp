from stormed.util import add_method
from stormed.method.codegen.queue import *

@add_method(DeclareOk)
def handle(self, ch):
    if ch.callback:
        ch.invoke_callback(self.queue, self.message_count, self.consumer_count)