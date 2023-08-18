entry_mode = True

friends = set()
books = {}

while entry_mode:
    user_input = input("Book read: ")
    if user_input:
        book_title, person = user_input.split(":")

        if person not in friends:
            friends.add(person)

        if book_title not in books:
            books[book_title] = set()
        books[book_title].add(person)
    else:
        entry_mode = False
        break

# print("Books: ", books)

report = []

for book in books:
    not_yet_read = friends - books[book]

    not_yet_read = list(not_yet_read)
    not_yet_read.sort()

    has_everyone_read_this = ""
    if not not_yet_read:
        has_everyone_read_this = "Everyone has read this!"
    report.append(book + ": " + ", ".join(not_yet_read) + has_everyone_read_this)

report.sort()

for line in report:
    print(line)