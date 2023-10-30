from .truncjson cimport get_expects, get_completion


cdef class Stream:
    cdef public list expects
    cdef public int last_ch
    cdef public str trunc

    def __cinit__(self):
        self.expects = []
        self.last_ch = 0
        self.trunc = ''
    
    cpdef str complete(self, str chunk):
        self.expects = get_expects(chunk, self.expects, self.last_ch)
        self.last_ch = ord(chunk[-1])
        cdef str completion = get_completion(self.expects)
        self.trunc += chunk
        return self.trunc + completion
