from scholarly import scholarly
import json, os

SCHOLAR_ID = "Ab5ge18AAAAJ"

def main():
    print("Fetching Google Scholar data...")

    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    pubs = []

    for pub in author["publications"]:
        filled = scholarly.fill(pub)

        pubs.append({
            "title": filled.get("bib", {}).get("title", ""),
            "authors": filled.get("bib", {}).get("author", ""),
            "venue": filled.get("bib", {}).get("venue", ""),
            "year": filled.get("bib", {}).get("pub_year", ""),
            "cited_by": filled.get("num_citations", 0)
        })

    os.makedirs("_data", exist_ok=True)
    with open("_data/scholar_publications.json", "w") as f:
        json.dump(pubs, f, indent=2)

    print("Saved _data/scholar_publications.json")

if __name__ == "__main__":
    main()