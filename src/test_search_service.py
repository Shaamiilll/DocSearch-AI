from search_service import SearchService

service = SearchService()

results = service.search("How do containers communicate?")

print("Results:")
print()

for r in results:
    print(r)