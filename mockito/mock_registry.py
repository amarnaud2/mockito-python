# Copyright (c) 2008-2016 Szczepan Faber, Serhiy Oplakanets, Herr Kaste
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


class MockRegistry:
    """Registry for mocks

    Registers mock()s, ensures that we only have one mock() per mocked_obj, and
    iterates over them to unstub each stubbed method.
    """

    def __init__(self):
        self.mocks = {}

    def register(self, obj, mock):
        self.mocks[obj] = mock

    def mock_for(self, obj):
        return self.mocks.get(obj, None)

    def unstub(self, obj):
        mock = self.mocks.pop(obj)
        if mock:
            mock.unstub()

    def unstub_all(self):
        for mock in self.mocks.itervalues():
            mock.unstub()
        self.mocks.clear()


mock_registry = MockRegistry()
