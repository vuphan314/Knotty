"""
Copyright (c) 2014, Evgenii Balai
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY EVGENII BALAI "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL EVGENII BALAI OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the FreeBSD Project.
"""


class AST:
    """The class is used to represent a non-empty abstract syntax trees
    as defined in section 3.5 of the document
    """

    def __init__(self, root_label, children=None):
        """Construct a tree  given  root label and list of trees representing
        the children
        """
        self.root_label = root_label
        self.children = children

    def repr(self):
        """Get the representation of the tree as defined in section 3.5
        of the documentation
        """

        if self.children is None:
            # if T consists of only one node labeled by l, it is represented
            # by the label l
            return self.root_label
        else:
            # if a tree consists of more then one node, it is represented
            # by the list [r, t 1 , . . . , t n ], where r is a label of the
            # root of T and t i is the representation of the subtree of T
            # rooted at i th child of T
            return [self.root_label] + self.children

    def children_list(self):
        """ Return the list of children of the root of the tree.
        If the tree has no children, an empty list is returned
        """
        if self.children is None:
            return []
        else:
            return self.children

    def __repr__(self):
        return str(self.repr())

    def __str__(self):
        return self.__repr__()

    def __getitem__(self,index):
         return ([self.root_label] + self.children)[index]

    def __len__(self):
        return 1 + len(self.children)
