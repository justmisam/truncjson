from .truncjson cimport get_expects, get_completion


cdef class Stream:
    cdef public list _objs
    cdef public list _expects
    cdef public int _last_ch
    cdef public str _trunc

    def __cinit__(self):
        self._objs = []
        self._expects = []
        self._last_ch = 0
        self._trunc = ''
    
    cpdef list extract(self, str chunk):
        if len(chunk) > 0:
            self._expects = get_expects(chunk, self._expects, self._last_ch)
            self._last_ch = ord(chunk[-1])
            if len(self._expects) > 0:
                while self._expects[0] <= 0:
                    separator = -self._expects.pop(0)
                    if chunk[separator] in ['}', ']']:
                        self._objs.append(self._trunc + chunk[:separator + 1])
                        chunk = chunk[separator + 1:]
                    else:
                        chunk = chunk[separator:]
                    self._trunc = ''
                    if len(self._expects) == 0:
                        break
                if len(self._expects) > 0:
                    self._trunc += chunk
                    return self._objs + [self._trunc + get_completion(self._expects)]
        return self._objs
