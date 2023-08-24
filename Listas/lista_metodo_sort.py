linguagens = ["Python", "JS", "C", "Java", "CSharp"]
linguagens.sort()
print(linguagens)


linguagens = ["Python", "JS", "C", "Java", "CSharp"]
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ["Python", "JS", "C", "Java", "CSharp"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens = ["Python", "JS", "C", "Java", "CSharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)