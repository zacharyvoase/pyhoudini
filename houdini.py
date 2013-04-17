import cffi


_houdini_cdef = '''
typedef struct {
    char *ptr;
    size_t asize, size;
} gh_buf;
void gh_buf_init(gh_buf *buf, size_t initial_size);
int houdini_escape_html(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_escape_html0(gh_buf *ob, const uint8_t *src, size_t size, int secure);
int houdini_unescape_html(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_escape_xml(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_escape_uri(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_escape_url(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_escape_href(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_unescape_uri(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_unescape_url(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_escape_js(gh_buf *ob, const uint8_t *src, size_t size);
int houdini_unescape_js(gh_buf *ob, const uint8_t *src, size_t size);
'''

_houdini_ffi = cffi.FFI()
_houdini_ffi.cdef(_houdini_cdef)
_libhoudini = _houdini_ffi.dlopen('houdini')


def escaper(etype):
    escaper_func = getattr(_libhoudini, 'houdini_' + etype)
    def escape(string):
        encoded = string.encode('utf-8')
        output = _houdini_ffi.new('gh_buf *')
        _libhoudini.gh_buf_init(output, 0)
        res = escaper_func(output, encoded, len(encoded))
        if not res:
            return string
        return _houdini_ffi.string(output.ptr, output.size).decode('utf-8')
    escape.__name__ = etype
    return escape


escape_html = escaper('escape_html')
unescape_html = escaper('unescape_html')
escape_xml = escaper('escape_xml')
escape_uri = escaper('escape_uri')
escape_url = escaper('escape_url')
escape_href = escaper('escape_href')
unescape_uri = escaper('unescape_uri')
unescape_url = escaper('unescape_url')
escape_js = escaper('escape_js')
unescape_js = escaper('unescape_js')
