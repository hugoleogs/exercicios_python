"""

Your task is to create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

Example

The pagination class will accept 2 parameters:

    items (default: []): A list of contents to paginate.

    pageSize (default: 10): The amount of items to show in each page.

So for example we could initialize our pagination like this:

alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)

And then use the method getVisibleItems to show the contents of the paginated list.

p.getVisibleItems() # ["a", "b", "c", "d"]

You will have to implement various methods to go through the pages such as:

    prevPage
    nextPage
    firstPage
    lastPage
    goToPage

Here's a continuation of the example above using nextPage and lastPage:

p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]

Notes

    The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
    The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
    Please remove the comments I provided before publishing your solution.

link do exercicio: https://edabit.com/challenge/yPzfgnDsPWXwH7dMq

"""


class Pagination:

    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = int(round(len(items)/pageSize+0.4999))
        self.currentPage = 1

    def getItems(self):
        return self.items
    def getPageSize(self):
        return self.pageSize
    def getCurrentPage(self):
        return self.currentPage

    def prevPage(self):
        if self.currentPage>1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, page):
        if page > self.totalPages:
            self.currentPage = self.totalPages
        elif page > 0:
            self.currentPage = int(page)
        else:
            self.currentPage = 1
        return self

    def getVisibleItems(self):
        inicio = (self.getCurrentPage()-1) * self.getPageSize()
        fim = inicio + self.getPageSize()
        if self.getCurrentPage() == self.totalPages:
            return self.getItems()[inicio:]
        return self.getItems()[inicio:fim]




defaultPagination = Pagination()
print(defaultPagination.getPageSize())
print(defaultPagination.getItems())

print("\n")

p = Pagination([None]*69, 5)
print(p.nextPage().getCurrentPage())
print(p.lastPage().getCurrentPage())
print(p.nextPage().getCurrentPage())
print(p.prevPage().getCurrentPage())
print(p.firstPage().getCurrentPage())
print(p.prevPage().getCurrentPage())
print(p.goToPage( 99).getCurrentPage())
print(p.goToPage(  4).getCurrentPage())
print(p.goToPage(6.5).getCurrentPage())
print(p.goToPage(-99).getCurrentPage())

print("\n")

ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p2 = Pagination(ids, 5)
print(p2.getVisibleItems())
print(p2.nextPage().getVisibleItems())
print(p2.nextPage().getVisibleItems())