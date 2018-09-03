import jupytext
from testfixtures import compare

jupytext.file_format_version.FILE_FORMAT_VERSION = {}


def test_read_simple_file(julia='''"""
   cube(x)

Compute the cube of `x`, ``x^3``.

# Examples
```jldoctest
julia> cube(2)
8
```
"""
function cube(x)
   x^3
end

cube(x)

# And a markdown comment
'''):
    nb = jupytext.reads(julia, ext='.jl')
    assert nb.metadata == {'main_language': 'julia'}
    assert len(nb.cells) == 3
    assert nb.cells[0].cell_type == 'code'
    assert nb.cells[0].source == '''"""
   cube(x)

Compute the cube of `x`, ``x^3``.

# Examples
```jldoctest
julia> cube(2)
8
```
"""
function cube(x)
   x^3
end'''
    assert nb.cells[1].cell_type == 'code'
    assert nb.cells[1].source == 'cube(x)'
    assert nb.cells[2].cell_type == 'markdown'
    compare(nb.cells[2].source, 'And a markdown comment')

    julia2 = jupytext.writes(nb, ext='.jl')
    compare(julia, julia2)
